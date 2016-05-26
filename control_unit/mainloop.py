from time import sleep

import audioAPI as audio
import recognition as rec
from arduino_connection import arduinoConnection
from dbAPI import dbHandler

arConn = arduinoConnection()
db = dbHandler()


def recording_voice():
    while True:
        if rec.listen():
            audio.record()
            play_back = audio.converter()
            sleep(2)
            audio.play(play_back)
            sleep(2)
            break


def is_save():
    instruction = audio.SAVE
    audio.play(instruction)
    if rec.listen():
        return True
    else:
        db.delete_last_one()
        return False


def interface(__name__):
    _in_working = False
    _has_playlist = False

    print(1)
    while True:
        has_person = arConn.is_person()

        """
        The status: person approaching:
            check: the light is not in working pattern
                and there is no playlist now.

            1). light: change to working pattern
            2). prepare playlist
        """
        if has_person == 1:
            if not _in_working:
                arConn.ping2working()
                _in_working = True
                if not _has_playlist:
                    playlist = audio.playlist_extractor()
                    _has_playlist = True
                    continue

        """
        The status: person against:
            check: the light pattern status
                and playlist

            1). light: change to play pattern
            2). play playlist
        """
        if has_person == 0:
            if _has_playlist:
                if not _in_working:
                    arConn.ping2working()
                    _in_working = True

                audio.play_list(playlist)
                while True:
                    recording_voice()
                    if is_save():
                        break
                    else:
                        continue
            else:
                playlist = audio.playlist_extractor()
                _has_playlist = True
                audio.play_list(playlist)
                while True:
                    recording_voice()
                    if is_save():
                        break
                    else:
                        continue

            sleep(10)

        """
        The status: people leaving reset the light pattern and other value
        """
        if has_person == -1:
            arConn.ping2default()
            _in_working = False
            _has_playlist = False


#
if __name__ == "__main__":
    interface(__name__)

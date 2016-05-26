import recognition as rec
import audioAPI as audio
from arduino_connection import arduinoConnection


arConn = arduinoConnection()




def interface(__name__):
    _in_working = False
    _has_playlist = False

    print(1)
    while True:
        has_person = arConn.is_person()
        if  has_person== 1:
            if not _in_working:
                arConn.ping2working()
                _in_working = True
                if not _has_playlist:
                    playlist = audio.playlist_extractor()
                    _has_playlist = True
                    continue

        if has_person == 0:
            if _has_playlist:
                if _in_working:
                    audio.play_list(playlist)
                else:
                    arConn.ping2working()
                    _in_working = True
                    audio.play_list(playlist)
            else:
                playlist = audio.playlist_extractor()
                _has_playlist = True
                audio.play_list(playlist)

        if has_person == -1:
            arConn.ping2default()
            _in_working = False
            _has_playlist = False


#
if __name__ == "__main__":
    interface(__name__)

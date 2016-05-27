from time import sleep

import audioAPI as audio
import recognition as rec
from arduino_connection import arduinoConnection
from dbAPI import dbHandler

arConn = arduinoConnection()
db = dbHandler()





def interface(__name__):
    _in_working = False
    _in_engaging = False
    _is_standby = False
    _quit = False

    playlist = []

    instruction_hello = audio.HELLO
    instruction_ready = audio.READY
    instruction_save = audio.SAVE

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
        if has_person == 1 and not _quit:
            if not _in_engaging:
                arConn.ping2engaging()
                _in_engaging = True
                _is_standby = False
                _in_working = False
                if not playlist:
                    playlist.append(audio.playlist_extractor())
                    continue

        """
        The status: person against:
            check: the light pattern status
                and playlist

            1). light: change to play pattern
            2). play playlist
        """
        if has_person == 0 and not _quit:
            if playlist:
                if not _in_working:
                    arConn.ping2working()
                    _in_working = True
                    _is_standby = False
                    _in_engaging = False

                    # audio.play_list(playlist)
                    # while True:
                    #     if not _is_standby:
                    #         arConn.ping2standby()
                    #     recording_voice()
                    #     if is_save():
                    #         break
                    #     else:
                    #         continue
            else:
                playlist.append(audio.playlist_extractor())

            audio.play(instruction_hello)
            audio.play_list(playlist.pop())
            audio.play(instruction_ready)

            #  start recording process
            while True:
                # waiting confirm
                if not _is_standby:
                    arConn.ping2standby()
                    _is_standby = True
                    _in_working = False
                    _in_engaging = False
                #  actually, under circumstance, this while loop is useless, because the listen just has two reason,
                #  yes or no. There is no 3rd choice.
                while True:
                    # we have two choices: 1. yes for recording; 2. no for quit
                    if rec.listen():  # confirm

                        # start recording
                        # if not _in_working:
                        #     arConn.ping2working()
                        #     _in_working = True
                        #     _is_standby = False
                        #     _in_engaging = False

                        arConn.ping2record()

                        audio.record()
                        break

                        # quit
                    else:
                        _quit = True
                        break

                # because we have two layers while loop
                if _quit:
                    break

                #end quit


                # whether people could leave at here

                # saving and format converter
                # status light processing --> 2done (--> done)
                arConn.ping2processing()
                _in_working = False
                _is_standby = False
                _in_engaging = False

                play_back = audio.converter()
                sleep(2)
                arConn.ping2done()
                sleep(1)

                # playback
                # if people still there, playback
                if has_person == 0:
                    # if not _in_working:
                    arConn.ping2working()
                    # _in_working = True
                    # _is_standby = False

                    audio.play(play_back)
                    audio.play(instruction_save)

                    # two choices: 1. yes to save, actually do nothing because we already save
                    #              2. no to quit
                    arConn.ping2standby()
                    if rec.listen():
                        arConn.ping2default() # temp think people we leave
                        break

                    else:
                        db.delete_last_one()
                        _quit = True
                        break

                else:
                    break


            # sleep(10)


        """
        The status: people leaving reset the light pattern and other value
        """
        if has_person == -1:
            arConn.ping2default()
            _is_standby = False
            _in_working = False
            _in_engaging = False
            if _quit:
                _quit = False
                sleep(10)

        sleep(1)
#
if __name__ == "__main__":
    interface(__name__)

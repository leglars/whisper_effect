import wave
import os
import uuid

import pyaudio
from pydub import playback, AudioSegment

from dbAPI import dbHandler

db = dbHandler()

HELLO = "/sound/instruction/15_seconds_Mono.mp3"
READY = "/sound/instruction/Are_You_Ready_after.mp3"
SAVE = "/sound/instruction/I_Like_It_after.mp3"
THANK = "/sound/instruction/Thank_You.mp3"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

__dir__ = os.path.dirname(__file__)



def record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def filename_generator():
    return str(uuid.uuid4())


def url_extractor(path):
    temp_path = path.split('/sound')
    return "/sound"+temp_path[1]


def save2db(file_path):
    if db.insert(file_path):
        return True


def output_path():
    return __dir__ + "/sound/" + filename_generator() + ".mp3"

def louder(file, value):
    """
    :param file: int, audio_file opened by AudioSegment
    :param value: how much dB you want to
    :return: return worked file
    """
    return file + value



def converter(output_path=output_path(), source_file=WAVE_OUTPUT_FILENAME):
    audio_file = AudioSegment.from_file(source_file, format="wav")
    louder(audio_file, 3).export(output_path, format="mp3", bitrate="48k")
    remove(source_file)
    url = url_extractor(output_path)
    save2db(url)
    return url


def remove(file):
    os.remove(file)
    print(file + " has been removed")


def playlist_extractor():
    """

    :return: get a list of relative path from db
    """
    full_list = db.read()
    playlist = []
    for id, url in full_list.items():
        playlist.append(url)

    return playlist


def play(path):
    """

    :param path: path should be a relative path
    :return: None
    """
    # try:
    playback.play(AudioSegment.from_mp3(__dir__ + path))  # play mp3
    # except:
    #     playback.play(__dir__ + path )  # play wav

def play_list(playlist):
    """
    The playlist comes from func: playlist_extractor()
    :param playlist:
    :return:
    """
    for list in playlist:
        play(list)
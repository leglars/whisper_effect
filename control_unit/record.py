import pyaudio
import wave
import sys
import os


from firebase import firebase
# firebase = firebase.FirebaseApplication('whispereffect.firebaseio.com', None)


CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "/output.wav"


dir = os.path.dirname(__file__)
file = dir + WAVE_OUTPUT_FILENAME

def recording():
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
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


def wire():
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()


def play():
    wf = wave.open(file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != ' ':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


play()


# class AudioFile:
#     chunk = 1024
#
#     def __init__(self, file):
#         """ Init audio stream """
#         self.wf = wave.open(file, 'rb')
#         self.p = pyaudio.PyAudio()
#         self.stream = self.p.open(
#             format = self.p.get_format_from_width(self.wf.getsampwidth()),
#             channels = self.wf.getnchannels(),
#             rate = self.wf.getframerate(),
#             output = True
#         )
#
#     def play(self):
#         """ Play entire file """
#         data = self.wf.readframes(self.chunk)
#         while data != '':
#             self.stream.write(data)
#             data = self.wf.readframes(self.chunk)
#
#     def close(self):
#         """ Graceful shutdown """
#         self.stream.close()
#         self.p.terminate()
#
# # Usage example for pyaudio
# a = AudioFile("1.wav")
# a.play()
# a.close()




import speech_recognition as sr

m = sr.Microphone.list_microphone_names()
print(m)
# index = m.index('Logitech USB Headset')

# index = m.index('Built-in Microph')

r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.5

CONFIRM = ["yes", "ready"]


def print_phrase(audio_data):
    text = r.recognize_google(audio_data)
    print(text)


def listen():
    # 'Built-in Microph' is the name of christine's headphone in Mac mini
    with sr.Microphone(device_index=1, sample_rate=16000, chunk_size=1024) as source:
        while True:
            print("looping")

            # audio_data = r.record(source, duration=1)
            audio_data = r.listen(source)  # return an audio_data
            try:
                # transcription = r.recognize_google(audio_data)
                transcription = r.recognize_sphinx(audio_data)
                # transcription = r.recognize_wit(audio_data, "JA52V23ZT5DJTCD3FZDDUVWFXKK5EXXZ")
            except sr.UnknownValueError:
                print("no word understand")
                continue

            print(transcription)

            for word in transcription.split(' '):
                if word in CONFIRM:
                    return True
            # r.listen_in_background(source, print_phrase)

import recognition as rec
import audioAPI as audio


def interface():
    while True:

        if rec.listen():
            audio.record()
            # audio.converter()

#
# if __name__ == "main":
#     interface()

for i in range(3):
    print(i)
    while True:

        if rec.listen():
            audio.record()
            audio.play(audio.converter())
            break

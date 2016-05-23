import recognition as rec
import audioAPI as audio


def interface(__name__):
    print(1)
    while True:

        if rec.listen():
            audio.record()
            audio.converter()

#
if __name__ == "__main__":
    interface(__name__)

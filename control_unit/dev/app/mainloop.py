from time import sleep

import serial

ser = serial.Serial('COM4', 9600)  # Establish the connection on a specific port
counter = 32  # Below 32 everything in ASCII is gibberish
while True:
    counter += 1
    ser.write(b'5')  # Convert the decimal number to ASCII then send it to the Arduino
    print(ser.read())  # Read the newest output from the Arduino
    sleep(.1)  # Delay for one tenth of a second
    if counter == 255:
        counter = 32


def interface():
    while True:
        print(ser.readline())
        sleep(0.5)

# if __name__ == "main":
#     interface()

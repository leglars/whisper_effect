from time import sleep
import serial

ser = serial.Serial('COM4', 9600)  # Establish the connection on a specific port
# counter = 32  # Below 32 everything in ASCII is gibberish
while True:

    # while ser.in_waiting() == 0:
    #     pass
    text_line = "?"
    print(text_line)
    ser.write(b'L')
    print("write L")
    # text_line = ser.readline()
    sleep(5)

    ser.write(b'M')
    print("write M")
    sleep(1)
    text_line = ser.readline()
    print(text_line)

    # ser.write(b'5')  # Convert the decimal number to ASCII then send it to the Arduino
    # print(ser.read())  # Read the newest output from the Arduino
    # sleep(.1)  # Delay for one tenth of a second
    # if counter == 255:
    #     counter = 32
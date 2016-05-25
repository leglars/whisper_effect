from time import sleep
import serial


dist_port = # 'COM8' # '/dev/cu.usbmodem1461'
dist_freq = 11560

light_port = # 'COM4' # '/dev/cu.usbmodem1461'
light_freq = 9600

dist = serial.Serial(dist_port, dist_freq)
light = serial.Serial(light_port, light_freq)


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

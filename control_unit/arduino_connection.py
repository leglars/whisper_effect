from time import sleep

import serial


class arduinoConnection(object):

    def __init__(self):
        self.dist_port = 'COM8' # '/dev/cu.usbmodem1461'
        self.dist_freq = 9600

        self.light_port = 'COM4' # '/dev/cu.usbmodem1461'
        self.light_freq = 9600

        self.dist = serial.Serial(self.dist_port, self.dist_freq)
        self.light = serial.Serial(self.light_port, self.light_freq)

        self.__processing_flag = False
        self.__working_flag = False

    def read_dist(self):
        while True:
            d = self.get_dist()
            print(d)
            if 6 < d < 30:
                if not self.__working_flag:
                    self.change2working()
            elif d <= 6:
                if not self.__processing_flag:
                    self.change2processing()
            sleep(1)

    def get_dist(self):
        distance = self.dist.readline()
        # the unit of d is cm
        return int(str(distance).strip().split("\'")[1].split("\\r")[0])

    def get_dist2(self):
        return self.dist.read_all()

    def ping_dist(self):
        while True:
            self.dist.write(b'P')
            print("ping it")
            distance = self.dist.read_all()
            dist = str(distance).strip().split("\'")[1]
            print(dist)
            if dist:
                dist = dist.split("\\")[0]
                return int(dist)
            sleep(0.2)

    def ping_get_all(self):
        distance = self.dist.read_all()
        print(distance)

    def change2processing(self):
        self.light.write(b'P')
        print("write P")
        self.__processing_flag = True
        self.__working_flag = False

    def ping2processing(self):
        for i in range(4):
            self.light.write(b'P')
            print("ping it")
            # resonse = self.dist.read()
            # res = str(resonse).strip().split("\'")[1]
            # print(resonse)
            sleep(0.2)
            # if dist:
            #     dist = dist.split("\\")[0]
            #     return dist


    def change2working(self):
        self.light.write(b'W')
        print("write W")
        self.__working_flag = True
        self.__processing_flag = False

adConn = arduinoConnection()
# adConn.read_dist()
# print("the dist is " + str(adConn.ping_dist()))
adConn.ping2processing()

    # print(d)
    # if 6 < d < 30:
    #     if not adConn.__working_flag:
    #         adConn.change2working()
    # elif d <= 6:
    #     if not adConn.__processing_flag:
    #         adConn.change2processing()



# while True:
#     adConn.ping_get_all()
#     sleep(5)



# the result of following code is 9 8 173 122 184.
# but I change position for each loop,
# which means 8, 122, 184 are from buffer, but not the real-time data.

# adCoon = arduinoConnection()
# for i in range(5):
#     print(adCoon.get_dist())
#     sleep(5)


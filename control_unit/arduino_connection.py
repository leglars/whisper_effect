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

    def ping_get_all(self):
        distance = self.dist.read_all()
        print(distance)

    def change2working(self):
        self.light.write(b'W')
        print("write W")
        self.__working_flag = True
        self.__processing_flag = False


    # working functions start from here

    def ping_dist(self):
        while True:
            self.dist.write(b'P')
            print("ping ")
            distance = self.dist.read_all()
            dist = str(distance).strip().split("\'")[1]
            if dist:
                dist = dist.split("\\")[0]
                print(dist)
                try:
                    return int(dist)
                except ValueError:
                    continue
            sleep(0.2)

    def change2processing(self):
        self.light.write(b'P')
        print("write P")
        self.__processing_flag = True
        self.__working_flag = False

    def ping2processing(self):
        for i in range(4):
            self.light.write(b'P')
            print("ping process")
            # resonse = self.dist.read()
            # res = str(resonse).strip().split("\'")[1]
            # print(resonse)
            sleep(0.2)
            # if dist:
            #     dist = dist.split("\\")[0]
            #     return dist

    def ping2done(self):
        for i in range(4):
            self.light.write(b'D')
            print("ping done")
            sleep(0.2)

    def ping2working(self):
        for i in range(4):
            self.light.write(b'W')
            print("ping work")
            sleep(0.2)

    def ping2engaging(self):
        for i in range(4):
            self.light.write(b'E')
            print("ping engaging")
            sleep(0.2)

    def ping2standby(self):
        for i in range(4):
            self.light.write(b'S')
            print("ping engaging")
            sleep(0.2)

    def ping2default(self):
        for i in range(4):
            self.light.write(b'R')
            print("ping leave")
            sleep(0.2)

    def is_person(self):
        dist = self.ping_dist()
        if 10 < dist < 150:
            return 1
        elif 2 < dist < 10:
            return 0
        elif dist > 150:
            return -1


# the following is used for testing function

# adConn = arduinoConnection()
# # # adConn.read_dist()
# print("the dist is " + str(adConn.ping_dist()))
# print("the dist is " + str(adConn.ping_dist()))
# adConn.ping2processing()

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


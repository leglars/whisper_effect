import threading
from arduino_connection import arduinoConnection
from time import sleep

arConn = arduinoConnection()


class LightController:
    def __init__(self):
        self._pattern = ""
        self._is_engaging = False

    def engaging(self):
        if not self.get_engaging():
            arConn.ping2engaging()
            self.set_pattern("E")
            self.set_engaging(value=True)

    def processing(self):
        arConn.ping2processing()
        self.set_pattern("P")
        self.set_engaging()

    def done(self):
        arConn.ping2done()
        self.set_pattern("D")
        self.set_engaging()

    def recording(self):
        arConn.ping2record()
        self.set_pattern("R")
        self.set_engaging()

    def working(self):
        arConn.ping2working()
        self.set_pattern("W")
        self.set_engaging()

    def standby(self):
        arConn.ping2standby()
        self.set_pattern("S")
        self.set_engaging()

    def reset(self):
        arConn.ping2default()
        self.set_pattern("")
        self.set_engaging()

    def set_engaging(self, value=False):
        """
        :param value: boolean
        :return: None
        """
        self._is_engaging = value

    def get_engaging(self):
        """
        :return: boolean
        """
        return self._is_engaging

    def set_pattern(self, pattern):
        self._pattern = pattern

    def get_pattern(self):
        return self._pattern



lc = LightController()

lc.engaging()
lc.engaging()
sleep(5)
lc.working()
lc.working()
sleep(5)
lc.processing()
lc.processing()
sleep(5)
lc.done()
lc.done()
sleep(3)
lc.standby()
lc.standby()
sleep(5)
lc.recording()
lc.recording()
sleep(5)
lc.reset()
lc.reset()
sleep(5)

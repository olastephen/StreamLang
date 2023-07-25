from sys import *

from Lang.Constants.Constant import Constant


class File:

    def __init__(self):
        self.data = None

    def open_file(self, filename):
        self.data = open("C:\DayoTech\Stream Lang\Test\\" + filename, "r").read()
        self.data += " " + Constant().EOF
        return self.data

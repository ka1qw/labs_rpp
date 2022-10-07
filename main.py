import numpy as np
import math
import random
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        # загрузка интерфейса из файла
        loadUi("gui.ui", self)
        self.encode.clicked.connect(self.encode_func)
        self.decode.clicked.connect(self.decoded)
        self.t = []
        self.ords = []
        self.a = 5
        self.b = 8
        self.m = 2 ** self.b

    @staticmethod
    def xor_my(t, encoded_binary):
        itog_bin = []
        for i in range(len(t)):
            s = ''
            for j in range(len(t[i])):
                s += str(int(t[i][j]) ^ int(encoded_binary[i][j]))
                if j == len(t[i]) - 1:
                    itog_bin.append(s)
        return [chr(int(i, 2)) for i in itog_bin]


    def decoded(self,encoded_bin):
        s1 = self.encoded_string.text()
        local_ords = []
        for i in range(len(s1)):
            local_ords.append(bin(ord(s1[i]))[2:].zfill(8))
        print(local_ords)
        print(self.ords)
        encoded = self.xor_my(self.t, local_ords)
        encoded_bin = [bin(ord(i))[2:].zfill(8) for i in encoded]
        decoded = self.xor_my(self.t, encoded_bin)
        self.decoded_string.setText(str(''.join(encoded)))
        print(encoded)

    def encode_func(self):
        s = self.input_string.text()
        if len(self.t) == 0:
            for i in range(len(s)):
                self.ords.append(bin(ord(s[i]))[2:].zfill(8))
                self.t.append(bin(math.ceil(math.fmod(self.a * math.ceil(random.randint(1, int(time.time()))) + self.b, self.m)))[2:].zfill(8))
        else:
            self.t.clear()
            for i in range(len(s)):
                self.ords.append(bin(ord(s[i]))[2:].zfill(8))
                self.t.append(bin(math.ceil(math.fmod(self.a * math.ceil(random.randint(1, int(time.time()))) + self.b, self.m)))[2:].zfill(8))

        encoded = self.xor_my(self.t, self.ords)
        encoded_bin = [bin(ord(i))[2:].zfill(8) for i in encoded]
        # decoded = self.xor_my(t, encoded_bin)
        self.encoded_string.setText(str(''.join(encoded)))
        print(encoded)
        self.ords.clear()
        # self.t.clear()
        # print(decoded)


application = QApplication(sys.argv)
w = QtWidgets.QStackedWidget()
mainWindow = Window()
w.addWidget(mainWindow)
w.setFixedSize(472, 256)
w.show()
sys.exit(application.exec_())

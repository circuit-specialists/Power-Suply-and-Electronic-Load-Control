#!/usr/bin/python

import msvcrt

class KEYBOARD:
    def __init__(self):
        self.input_buf = ""

    def getInput(self):
        while True:
            if msvcrt.kbhit():
                self.input_buf = msvcrt.getch().decode('UTF-8')
                self.null = msvcrt.getch()
                print(self.input_buf)
                if(self.input_buf == 'q'):
                    exit()
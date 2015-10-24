__author__ = 'jdemp'
import os
import sys

class CodeDestination():

    def __init__(self):
        pass

    def __str__(self):
        pass

    def write_code_snippet(self, snippet):
        pass


def type(arg):
    #print(keystroke_cmd + arg + "'")
    str = """osascript -e 'tell application "System Events" to keystroke "{0}"'""".format(arg)
    os.system(str)

if __name__ == '__main__':
    str = 'Hello World'
    type(str)
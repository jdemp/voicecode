__author__ = 'jdemp'
import os
import sys
import socketserver
from python_parser import PythonParser

def send_keystrokes(arg):
    #print(keystroke_cmd + arg + "'")
    str = """osascript -e 'tell application "System Events" to keystroke "{0}"'""".format(arg)
    os.system(str)

def send_nl():
    #print(keystroke_cmd + arg + "'")
    str = """osascript -e 'tell application "System Events" to key code 36'"""
    os.system(str)

class PythonHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        command = data.decode()
        print(command)
        snippets = parser.parse(command)
        if snippets[0] is False:
            pass
        else:
            for s in snippets:
                if s == 'nl':
                    send_nl()
                else:
                    send_keystrokes(s)

if __name__ == "__main__":
    HOST, PORT = "localhost", 10000

    lang = input("Enter the Language you will be programming in: ")

    if lang.lower() == 'python':
        print("Starting PyVoice")
        server = socketserver.TCPServer((HOST, PORT), PythonHandler)
        parser = PythonParser()
    else:
        server = socketserver.TCPServer((HOST, PORT), PythonHandler)

    server.serve_forever()
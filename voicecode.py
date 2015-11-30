import os
import sys
import socketserver
from python_parser import PythonParser


def send_test(arg):
    print("This is a test")
    for each in arg:
        print(str(each))


def send_keystrokes(snippets):
    for s in snippets:
        if s == 'nl':
            keystrokes = """osascript -e 'tell application "System Events" to key code 36'"""
        elif s == 'quote':
            keystrokes = """osascript -e 'tell application "System Events" to key code 39'"""
        else:
            keystrokes = """osascript -e 'tell application "System Events" to keystroke "{0}"'""".format(s)
        os.system(keystrokes)


class PythonHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        command = data.decode()
        print(command)
        snippets = parser.parse(command)
        send_test(snippets)
        send_keystrokes(snippets)

if __name__ == "__main__":
    HOST, PORT = "localhost", 12003
    if sys.argv[1] == 'python':
        print("Starting PyVoice")
        server = socketserver.TCPServer((HOST, PORT), PythonHandler)
        parser = PythonParser()
    else:
        print("Language not implemented yet")
    server.serve_forever()

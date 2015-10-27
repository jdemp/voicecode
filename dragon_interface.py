#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
import sys
import socket

def send_msg(message):
    HOST, PORT = "localhost", 10000

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(message, "utf-8"))
    finally:
        sock.close()


dictation = sys.argv[1:]
msg = ''
for word in dictation:
    msg += word + ' '
send_msg(msg[:-1])
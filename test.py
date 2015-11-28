import sys
import socket

def send_msg(message):
    HOST, PORT = "localhost", 12000

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(message, "utf-8"))
    finally:
        sock.close()

if __name__ == "__main__":
    while 1:
        command = input("Enter command:")
        send_msg(command)
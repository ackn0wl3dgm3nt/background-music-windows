import sys
import socket


def send(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8880))
    s.send(msg.encode())
    s.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid command")
        sys.exit(-1)
    else:
        send(" ".join(sys.argv[1:]))

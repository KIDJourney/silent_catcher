import socket

def message_generator():
    s = socket.socket(socket.AF_INET , socket.SOCK_RAW , socket.IPPROTO_TCP)
    while True:
        yield s.recvfrom(65565)



if __name__ == "__main__":
    generator = message_generator()
    for i in generator:
        print(i)
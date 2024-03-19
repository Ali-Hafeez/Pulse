import socket
import sys

def client_program(host, port):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    try:
        while True:
            message = input(" -> ")  # take input

            if message.lower().strip() == 'bye':
                break

            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal
    finally:
        client_socket.close()  # close the connection

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python client.py <hostname> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    client_program(host, port)
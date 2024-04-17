import socket
from threading import Thread
def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)



SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"
s = socket.socket()
print(f"Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

name = input("Enter your name: ")

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    # input message we want to send to the server
    to_send = input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    to_send = f" {name}{separator_token}{to_send}"
    # finally, send the message
    s.send(to_send.encode())
# close the socket
s.close()
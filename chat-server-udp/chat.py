import socket
import time
import threading
import sys

print("UDP Chat w/ Multithreading")


# Function u/ Receiving
def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_sender, port_sender))  # Sync antara IP dan Port
    while True:
        msgs = s.recvfrom(1024)
        print("\n" + msgs[0].decode())
        if "exit" in msgs[0].decode() or "bye" in msgs[0].decode():
            sys.exit()


# Function u/ Sending
def sender():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "hello"
    while True:
        if "bye" in text or "exit" in text or "finish" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name + ":" + text
            s.sendto(text.encode(), (ip_receiver, port_receiver))


print("Initializing....")
ip_receiver = input("\nEnter IP Address of Receiver: ")
port_receiver = int(input("\nEnter Port of Receiver: "))
ip_sender = input("\nEnter your IP Address: ")
port_sender = int(input("\nEnter your system's Port: "))
name = input("Enter your name: ")

print("Waiting for client to connect....")
time.sleep(1)
print("Connection established....")

# Multithreading u/ Thread Sender dan Receiver
send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)

send.start()
receive.start()

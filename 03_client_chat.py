import socket as sock
import threading as thread

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(f"Server: {message}")
        except:
            break

def send_messages(client):
    while True:
        message = input("You: ")
        client.sendall(message.encode())

# Create socket
client = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
client.connect(('localhost', 12345))

# Start threads
thread.Thread(target=receive_messages, args=(client,)).start()
thread.Thread(target=send_messages, args=(client,)).start()

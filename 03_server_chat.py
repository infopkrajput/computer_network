import socket as sock
import threading as thread

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")
        except:
            break
    conn.close()

def send_messages(conn):
    while True:
        message = input("You: ")
        conn.sendall(message.encode())

# Create socket
server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server is listening...")

conn, addr = server.accept()

# Start threads
thread.Thread(target=handle_client, args=(conn, addr)).start()
thread.Thread(target=send_messages, args=(conn,)).start()

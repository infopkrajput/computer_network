import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12345)
sock.bind(server_address)
print(f"UDP server is up and listening on {server_address}")

while True:
    print("Waiting to receive message...")
    data, client_address = sock.recvfrom(4096)
    print(f"Received message from {client_address}: {data.decode()}")

    message = input("You: ")
    if message.lower() == 'exit':
        print("Exiting chat.")
        break
    try:
        sock.sendto(message.encode(), client_address)
    except Exception as e:
        print(f"Error sending message: {e}")

sock.close()

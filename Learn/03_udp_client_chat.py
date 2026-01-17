import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = input("Enter server IP address (127.0.0.1 or localhost) : ") or '127.0.0.1'
server_port = int(input("Enter server port (default 12345): ") or 12345)
server = (server_address, server_port)
print(f"Connecting to UDP server at {server}")

while True:
    message = input("You: ")
    if message.lower() == 'exit':
        print("Exiting chat.")
        break
    try:
        sock.sendto(message.encode(), server)
    except Exception as e:
        print(f"Error sending message: {e}")
        break
    
    print("Waiting to receive message from server...")
    data, _ = sock.recvfrom(4096)
    print(f"Server: {data.decode()}")

sock.close()

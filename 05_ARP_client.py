import socket

# Define the server
server_ip = "127.0.0.1"  # Change to actual server IP if needed
server_port = 12345

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send an IP address request
ip_address = "192.168.1.3"
client_socket.sendto(ip_address.encode(), (server_ip, server_port))
mac_address, _ = client_socket.recvfrom(1024)
print(f"MAC Address for {ip_address}: {mac_address.decode()}")

client_socket.close()
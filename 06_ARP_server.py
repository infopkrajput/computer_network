import socket

# ARP table (simulating a network device mapping)
arp_table = {
    "192.168.1.3": "00:1C:2D:3E:4F:6A",
    #My Physical Address. . . . . . . . . : CC-5E-F8-F3-5B-35
}

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 12345))  # Listening on port 12345
print("ARP Server is running...")
 
while True:
    # Receive query from client
    data, addr = server_socket.recvfrom(1024)
    ip_address = data.decode()
    
    # Lookup MAC address
    mac_address = arp_table.get(ip_address, "MAC not found")
    
    # Send response back to client
    server_socket.sendto(mac_address.encode(), addr)
    
   

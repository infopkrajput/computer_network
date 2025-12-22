# import socket module
import socket as sock

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
print ("Socket successfully created TCP.")

# reserve a port on your computer in our
port = 12345

s.bind(('', port))
print ("Socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print ("Socket is listening")

while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    c.close()
    break
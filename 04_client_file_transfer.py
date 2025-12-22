import socket
import tkinter as tk
from tkinter import filedialog
import os

HOST = '127.0.0.1'
PORT = 12345

root = tk.Tk()
root.withdraw()
FILENAME = filedialog.askopenfilename(title="Select a file")

if FILENAME:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Send only the filename, not the whole local path
    base_name = os.path.basename(FILENAME)
    client_socket.send(base_name.encode())
    
    # Small delay to ensure the server processed the filename
    import time
    time.sleep(0.1) 

    # Open and send the file contents in chunks
    with open(FILENAME, 'rb') as file:
        while chunk := file.read(4096):
            client_socket.sendall(chunk) # use sendall for reliability

    print("File transfer complete.")
    client_socket.close()
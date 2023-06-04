#!/usr/bin/python3
#404CTF23
#geoz
#14 MAY 2023

import socket

HOST = "challenges.404ctf.fr"
PORT =  31420
RHINO = "~c`"

socket = socket.socket()
socket.connect((HOST, PORT))
 
i = 0
data = socket.recv(2048).decode('utf-8','ignore')
while True:
    i += 1
    
    if ("erreur" in data) or ("404CTF" in data):
            print(data)
            exit()

    while ">" not in data:
        data += socket.recv(2048).decode('utf-8','ignore')
    
      
    rhinoCount = len(data.split(RHINO)) - 1
    print(f"[{i}] {rhinoCount}")
    socket.send(f"{rhinoCount}\n".encode())
    data = socket.recv(2048).decode('utf-8','ignore')
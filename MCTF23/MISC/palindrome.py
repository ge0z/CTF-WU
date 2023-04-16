#!/usr/bin/python3
#MCTF23
#geoz

import socket

HOST = "palindrome.misc.midnightflag.fr"
PORT =  17002

def GetWord(data):
    return data.split("Voici le mot : ")[1].split("\r\n")[0].upper()

def IsPalindrome(word):
    return (word == word[::-1])

socket = socket.socket()  
socket.connect((HOST, PORT))  
data = socket.recv(1024).decode()

while True:
    data = socket.recv(1024).decode()
    print('[MIDNIGHTFLAG23]\n' + data + '\n[\\MIDNIGHTFLAG23]\n')

    if "MCTF" in data:
        break

    if IsPalindrome(GetWord((data))):
        answer = "oui\n"
    else:
        answer = "non\n"
    socket.send(answer.encode())
    print('[Geoz]\n' + answer + '[\\Geoz]\n')


socket.close()
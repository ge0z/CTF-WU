#!/usr/bin/python3
#404CTF23
#geoz
#14 MAY 2023

import socket
import operator

HOST = "challenges.404ctf.fr"
PORT =  30980
VOWEL = "aeiouyAEIOUY"
CONSONANT = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def text(data):
    text = data.split("Entrée : ")[1].split("{")[1].split("}")[0]
    return text

def rule1(tin):
    tout = tin [::-1]
    return tout

def rule2(tin):
    length = len(tin)
    if  (length % 2) == 0:
        part1 = tin[:length//2]
        part2 = tin[length//2:]
        tout = part2 + part1 
    else:
        central = tin[length//2]
        tout = tin.replace(central, '')
    return tout

# il y a surement plus simple, mais cela fonctionne 
def rule3_vowelMove(tin, direction):
    letterNRank = []
    vowelList = []

    # 1. numerotation du rang des lettres
    for i in range(len(tin)):
        #letterNRank([lettre, #lettre_dans_le_mot])
        letterNRank.append([tin[i],i])
    
    # 2. extraction des voyelles et de leurs rangs
    for letter in letterNRank:
        if letter[0] in VOWEL:
            vowelList.append(list(letter))
    
    # 3. changement du rang des voyelles
    for i in range(len(vowelList)):
        if direction == 'left':
            letterNRank[vowelList[i][1]][1] = vowelList[i-1][1]
        else:
            letterNRank[vowelList[i][1]][1] = vowelList[(i+1)%len(vowelList)][1]
  
    # 4. trie des lettres et creation du nouveau mot
    tout=""
    for letter in sorted(letterNRank, key=lambda letterNRank: letterNRank[1]) :
        tout += letter[0]
    return tout 
    

def rule3(tin):
    length = len(tin)
    t = rule2(rule1(tin))
    if length >= 3:
        if t[2] in CONSONANT:
            tout = rule3_vowelMove(tin, 'left')
        else:
            tout = rule3_vowelMove(tin, 'right')
    # a priori inutile, mais au cas ou
    else:
        tout = tin
    tout = rule2(rule1(tout))
    return tout


def rule4_vp(letter):
    index = ALPHABET.index(letter)
    for i in range(index,-1, -1):
        if ALPHABET[i] in VOWEL:
            break
    number = ord(ALPHABET[i])
    return number

def rule4_s(tin,n):
    sigma = 0
    for i in range(n-1,-1,-1):
        sigma += (ord(tin[i])*2**(n-i)*(1 if (tin[i] in VOWEL) else 0))
    return sigma

def rule4_sort(tin):
    letterNCount = []
    for letter in tin:
        letterNCount.append([letter, tin.count(letter)])
    letterNCount = sorted(letterNCount, key=lambda letterNCount: (letterNCount[1],256-ord(letterNCount[0])), reverse = True)
    tout = ""
    for letter in letterNCount:
        tout += letter[0]
    return tout

def rule4(tin):
    length = len(tin)
    # 1. ajout de caracteres
    tout = tin
    n = 0
    while True:
        if tout[n] in CONSONANT:
            s = rule4_s(tout,n)
            vp = rule4_vp(tout[n])
            tout = tout[:n+1] + chr(( (vp + s) % 95 ) + 32) + tout[n+1:]
        n += 1
        if n >= len(tout):
            break
    
    # 2. trie des lettres
    tout = rule4_sort(tout)
    return tout

def game(min):
    message = min.split(" ")
    mout = ""
    for word in message:
        mout += rule4(rule3(word)) + " "
    return mout[:-1]


socket = socket.socket()
socket.connect((HOST, PORT))

#REGLE 0
data = socket.recv(2048).decode('utf-8','ignore')
print (data)
socket.send(f"{text(data)}\n".encode())

#REGLE 1
data = socket.recv(2048).decode('utf-8','ignore')
print (data)
socket.send(f"{rule1(text(data))}\n".encode())

#REGLE 2
data = socket.recv(2048).decode('utf-8','ignore')
print (data)
socket.send(f"{rule2(rule1(text(data)))}\n".encode())

#REGLE 3
#la regle fait aussi la regle 2 et la 1
data = socket.recv(2048).decode('utf-8','ignore')
print (data)
socket.send(f"{rule3(text(data))}\n".encode())

#REGLE 4
data = socket.recv(2048).decode('utf-8')
print (data)
result = f"{rule4(rule3(text(data)))}\n".encode()
print(result)
socket.send(result)

#JEU
data = socket.recv(2048).decode('utf-8',)
print (data)
socket.send(f"{game(text(data))}\n".encode())

#FLAG
data = socket.recv(2048).decode('utf-8')
print (data)

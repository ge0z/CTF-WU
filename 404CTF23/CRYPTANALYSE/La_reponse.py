#!/usr/bin/python3
#404CTF23
#geoz
#21 MAI 2023

import socket

# Apres plusieurs essais, on constate que :
# - la premiere lettre du chiffre est la somme de toutes celles du clair plus une variable qui depend de la taille N du chiffre
# - la lettre du rang I du chiffre d'un clair de taille N est la lettre du rang I-1 du chiffre plus la somme des N-I premieres lettre du clair plus une varible qui depend de N

# Il faut donc pouvoir chiffrer un clair de meme taille que le message a dechiffrer, en deduire les variables precedement mentionnees et calculer le texte clair

CHIFFRE = "pvfdhtuwgbpxfhocidqcznupamzsezp"
ALPHABET = "zabcdefghijklmnopqrstuvwxy"

HOST = "challenges.404ctf.fr"
PORT =  31682


# 1. Determination des variables 
# 1.1 Creation d'un clair connu
sizeChiffre = len(CHIFFRE)
known = "".join([ 'a' for i in range(sizeChiffre)])

# Calcul des sommes successives des lettres
SumKnown =[]
for i in range(len(known)):
    sumKnown = 0
    for j in range(sizeChiffre-i):
        sumKnown += ALPHABET.index(known[j])
    SumKnown.append(sumKnown)
SumKnown.reverse()

# 1.2 Recuperation d'un chiffre maitrise
socket = socket.socket()
socket.connect((HOST, PORT))
data = socket.recv(2048).decode()
socket.send(f"{known}\n".encode())
knownCipher = socket.recv(2048).decode().split(' : ')[1].split("\n")[0]

# 1.3 Calculs des variables dependant de la taille N du chiffre
variable = []
for i in range(sizeChiffre-1):
    variable.append((ALPHABET.index(knownCipher[-(i+1)]) - ALPHABET.index(knownCipher[-(i+2)])  - SumKnown[i])%26)
    # print(f"{ALPHABET.index(knownCipher[-(i+1)])} - {ALPHABET.index(knownCipher[-(i+2)])} - {SumKnown[i]} = {variable[i]}")
variable.append((ALPHABET.index(knownCipher[0]) - SumKnown[-1])%26)


# 2. Dechiffement du message
TEXT = ALPHABET[(ALPHABET.index(CHIFFRE[-1]) - ALPHABET.index(CHIFFRE[-2]) - variable[0])%26]
# print(f"{ALPHABET.index(CHIFFRE[-1])} - {ALPHABET.index(CHIFFRE[-2])} - {variable[0]} = {TEXT[-1]}")
for i in range(1,sizeChiffre-1):
    sum = 0
    for j in range(len(TEXT)):
        sum += ALPHABET.index(TEXT[j])
    TEXT += ALPHABET[(ALPHABET.index(CHIFFRE[-i-1]) - ALPHABET.index(CHIFFRE[-i-2]) - variable[i] - sum)%26]

    # print(f"{ALPHABET.index(CHIFFRE[-i-1])} - {ALPHABET.index(CHIFFRE[-i-2])} - {variable[i]} - {sum} = {TEXT[-1]}")

sum = 0
for i in range(len(TEXT)):
    sum += ALPHABET.index(TEXT[i])
TEXT += ALPHABET[(ALPHABET.index(CHIFFRE[0])-sum -variable[-1])%26 ]
# print(f"{ALPHABET.index(CHIFFRE[0])} - {variable[-1]} - {sum} = {TEXT[-1]}")

print(f"404CTF{{{TEXT}}}")
#!/usr/bin/python3
#404CTF23
#geoz
#24 MAI 2023

import socket
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Apres quelques tests, on remarque que le fonction oracle(), est capable de dechiffrer les messages de petite taille.
# Apres lecture du code on constate que la fonction oracle() est capable de dechiffrer les message inferieur a q
# Une solution est donc de trouver q par dichotomie. C'est a dire chercher a partir de quelle valeur c oracle(c) != c
# On en deduit q puis p et d (n et e sont donnes).
# On peut donc dechiffrer le message
# Une solution plus elegante doit probablement exister. Mais c'est un CTF, pas un probleme de Mathematiques :)


HOST = "challenges.404ctf.fr"
PORT =  31674

socket = socket.socket()
socket.connect((HOST, PORT))

# 1. Recuperation de n et du chiffre, e est dans le code source fourni
data = socket.recv(2048).decode()
while ("Bonne utilisation!" not in data):
    data += socket.recv(2048).decode()

CIPHER = int(data.split("oracle!:\n")[1].split("\n")[0])
n = int(data.split("oracle n°0x")[1].split(" termin")[0], 16)
e = 0x10001

# 2. Recherche de Q par dichotomie
## fonction qui interoge l'oracle sur le serveur
def oracle(socket,c):
    socket.send((str(c)+"\n").encode())
    data = socket.recv(2048).decode()
    while ("oracle?" not in data):
        data += socket.recv(2048).decode()
    return int(data.split("\n")[0])

## fonction pour la dichotomie	
def dicho(socket,Mn, Mx):
	a = min(Mn,Mx)
	b = max(Mn,Mx)
	c = (b - a)//2 + a
	d = oracle(socket,pow(c,e,n))
	if b-a <= 1:
		return (c,c)
	else:
		if d - c  != 0:
			b = c
		else:
			a = c
		return (a,b)

# 2.1 Initialisation de la dichotomie
# En effet, on constate pendant les tests que le chiffre de 'a'*128 est dechiffre par l'oracle et pas celui de 'a'*129
(a,b) = dicho(socket,bytes_to_long(b"a"*128),bytes_to_long(b"a"*129))

# 2.2 Lancement de la dichotomie
while a != b:
	(a,b) = dicho(socket,a,b)
	print(b-a)

# 2.3 Deduction de q
Q = a + 1

# 3. Calcul de p et d
P = n // Q
print (f" (p,q) = {(P,Q)}")
D = pow(e, -1, (Q-1)*(P-1))

# 4. Dechiffrement du flag
FLAG = pow(CIPHER,D,n)
print(long_to_bytes(FLAG))
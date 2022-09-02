#!/usr/bin/python3

#geoz
#01/09/2022
#crypto

# Résolution d'un challenge proposé par @arcsi
# https://pbs.twimg.com/media/FbUUZT5WAAEno8w?format=jpg&name=900x900

chiffre = "JAOA L,BFP QNPS XPRA QXH{Y TLMC ACKO VNNI CYRK UYHD}"
clair = ""

# Compteurs des incréments de rotation des rotors
INDEX_1 = 0
INDEX_2 = 0
INDEX_3 = 0
INDEX_R = 0

# Position initiale des rotors
INIT_1 = 25
INIT_2 = 2
INIT_3 = 5
INIT_R = 21

# Définition de l'alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Modélisation des rotors 
# Chaque élément represente la valeur de la translation qui est effectuée quand la lettre passe le rotor
# Exemple pour le ROTOR_1 :
# - A donne D en position initiale
# - positionAlphabet('D') - positionAlphabet('A') = 4 - 1 = 3
# - première valeur de ROTOR_1 : 3
ROTOR_1 = [3, 9, 5, -3, 1, -1, 2, -5, -2, 2, -9, -2, 8, 2, 2, -2, -2, 8, 1, -1, -8, 2, 2, -2, -2, -8]
ROTOR_2 = [24, 24, 18, 3, 9, 5, -3, 1, -1, 2, -5, -2, 2, -9, -2, 8, 2, 2, -2, -2, -18, 1, -1, -8, -24, -24]
ROTOR_3 = [18, 2, 2, -2, -2, 18, 3, 9, 5, -3, 1, -1, 2, -5, -2, 2, -9, -2, -18, 2, 2, -2, -2, -18, 1, -1]
ROTOR_R = [1, -1, 2, 21, -2, 2, 17, -2, 8, 2, 2, -2, -2, 8, 1, -1, -8, 2, 2, -2, -2, -8, 3, -17, -21, -3]

# Modélisation du passage d'une lettre dans chaque rotor
# INDEX_X représente le nombre d'incréments de rotation du rotor X par rapport à la position initiale 
def rotor_1(lettre):
	return ALPHABET[(ALPHABET.index(lettre) + ROTOR_1[(ALPHABET.index(lettre) - INDEX_1) % 26]) % 26]

def rotor_2(lettre):
	return ALPHABET[(ALPHABET.index(lettre) + ROTOR_2[(ALPHABET.index(lettre) - INDEX_2) % 26]) % 26]

def rotor_3(lettre):
	return ALPHABET[(ALPHABET.index(lettre) + ROTOR_3[(ALPHABET.index(lettre) - INDEX_3) % 26]) % 26]

def rotor_r(lettre):
	return ALPHABET[(ALPHABET.index(lettre) + ROTOR_R[(ALPHABET.index(lettre) - INDEX_R) % 26]) % 26]

# Routine de déchiffrement
for lettre_chiffree in chiffre :
	if lettre_chiffree not in ALPHABET:
		clair += lettre_chiffree
	else:
		# Déchiffrement : lettre_chiffree -> ROTOR_1 -> ROTOR_2 -> ROTOR_3 -> ROTOR_R -> ROTOR_3 -> ROTOR_2 -> ROTOR_1 -> lettre_claire
		clair += rotor_1(rotor_2(rotor_3(rotor_r(rotor_3(rotor_2(rotor_1(lettre_chiffree)))))))
		
		# Rotation des rotors
		INDEX_1 += 1
		if INDEX_1 + INIT_1 > 26:
			INIT_1 = -2 - 26 * (INDEX_1 - 3) // 26
			INDEX_2 += 1
		if INDEX_2 + INIT_2 > 26:
			INIT_2 = -25 - 26 * (INDEX_2 - 26) // 26
			INDEX_3 += 1
		if INDEX_3 + INIT_3 > 26:
			INIT_3 = -22 - 26 * (INDEX_3 - 23) // 26
			INDEX_R += 1
		if INDEX_R + INIT_R > 26:
			INIT_R = -6 - 26 * (INDEX_3 - 7) // 26
		
print(clair)
	


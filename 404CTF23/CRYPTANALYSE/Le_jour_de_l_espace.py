#!/usr/bin/python3
#404CTF23
#geoz
#20 MAI 2023
# usage : sage -python espace.py
from sage.all import Matrix, vector, Integers

# On constate assez rapidement que 
# - la taille du message chiffre est un multiple de 5 
# - chiffre('b') = chiffre('baaaa')
# - chiffre('bb') = chiffre('bbaaa') = chiffre('baaaa') + chiffre ('abaaa')

# On suppose donc que 
# - c'est une forme de chiffrement matriciel : MATRICE * CLAIR = CHIFFRE
# - la valeur des lettres est leur place dans l'alphabet en partant de 0, 'z' n'est pas pris en compte.
# - la taille du clair doit etre un multiple de 5, le padding est 'a' au besoin

# Ainsi la valeur de 'b' etant 1, on teste les combinaisons suivante pour avoir la matrice de chiffrement:
# b, ab, aab, aaab, aaaab.
# On obtient la matrice suivante :
# |  9  4 18 20  8 |
# | 11  0  2  1  3 |
# |  5  6  7 10 12 |
# | 13 14 15 16 17 |
# | 19 21 22 23 24 |

# MATRICE * CLAIR = CHIFFRE <=> ( MATRICE Inversible et CLAIR = CHIFFRE * MATRICE**(-1) )

# Il faut donc calculer l'inverse de MATRICE
# De plus, les resultats ne pouvant qu'être dans l'interval [0,24], il faut travailler dans le corps fini des entiers
# de 0 a 24 inclus 

ALPHABET = "abcdefghijklmnopqrstuvwxy"
CIPHER = "ueomaspblbppadgidtfn"
TEXT = ""
F = Integers(25)
M = Matrix(F,[[9,4,18,20,8],[11,0,2,1,3],[5,6,7,10,12],[13,14,15,16,17],[19,21,22,23,24]])

# 1. Inversion de la matrice
I = M.inverse()

#2. Dechiffement
cipherArray = []
buffer = []
for i in range(0, len(CIPHER)):
    buffer.append(ALPHABET.index(CIPHER[i]))
    if len(buffer) == 5:
        cipherArray.append(buffer)
        buffer =[]

textArray = []
for c in cipherArray:
    textArray.append(I*vector(c))

for t in textArray:
    for l in t:
        TEXT += ALPHABET[l]

print(TEXT)
# il faut enlever le dernier 'a' qui est du au padding


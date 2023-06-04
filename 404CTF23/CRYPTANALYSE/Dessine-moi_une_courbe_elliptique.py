#!/usr/bin/python3
#404CTF23
#geoz
#18 MAI 2023
#usage : sage -python espace.py

import hashlib
from Crypto.Cipher import AES
from sympy import symbols, Eq, solve, FiniteField, Poly
from sage.all import Matrix, vector, GF

#0. Recuperation des informations depuis le fichier data.txt
GX = 93808707311515764328749048019429156823177018815962831703088729905542530725
GY = 144188081159786866301184058966215079553216226588404139826447829786378964579
HX = 139273587750511132949199077353388298279458715287916158719683257616077625421
HY = 30737261732951428402751520492138972590770609126561688808936331585804316784
P  = 231933770389389338159753408142515592951889415487365399671635245679612352781
CIPHER = "8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22"
IV     = "00b7822a196b00795078b69fcd91280d"

#1. Retrouver A et B

    # E est une courbe elliptique de la forme :
    # 
    # y**2 + a1*x*y + a3*y = x**3 + a2*x**2 + a4*x + a6
    # <=> 
    # y**2 = 4*x**3 + b2*x**2 + 2*b4*x + b6 
    # b2 = a1**2 + 4*a2
    # b4 = 2*a4 + a1*a3
    # b6 = a3**2 + 4*a6
    # source : https://mathworld.wolfram.com/EllipticDiscriminant.html

    # Or

    # EllipticCurve(GF(p), [a,b]) signifie que 
    # a1 = a2 = a3 = 0
    # a4 = a
    # a6 = b
    # source : https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/constructor.html

    # Ainsi

    # La courbe est de la forme :
    # y**2 = x**3 + a*x + b
    # source : https://mathworld.wolfram.com/EllipticDiscriminant.html

    # Sachant que G et H sont des points de la courbe, on a donc :
    # GX*a + b = GY**2 - GX**3
    # HX*a + b = HY**2 - HX**3

    # Il n'y a plus qu'a faire ces operations dans le corps fini GF(P)
    # Pour cela on utilise une equation matricielle de la forme M*RES = Y que l'on resoud dans GF(P)
    # | GX 1 | | a | = |GY**2 - GX**3 |
    # | HX 1 | | b |   |HY**2 - HX**3 |

F = GF(P)
M = Matrix(F, [[GX, 1],[HX,1]])
N = vector(F,[F(GY**2 - GX**3) ,F(HY**2 - HX**3)])
RES = M.solve_right(N)
A = RES[0]
B = RES[1]

#2. Dechiffrer
key = str(A) + str(B)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=bytes.fromhex(IV))
flag = aes.decrypt(bytes.fromhex(CIPHER))
print(flag.decode())
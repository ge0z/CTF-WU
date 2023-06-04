#!/usr/bin/python3
#404CTF23
#geoz
#16 MAI 2023

import re,  base64

CIPHER = "32 69 31 73 34 69 31 73 31 35 64 31 6f 34 39 69 31 6f 34 64 31 6f 33 69 31 6f 31 35 64 31 6f 32 32 64 31 6f 32 30 64 31 6f 31 39 69 31 6f 37 64 31 6f 35 64 31 6f 32 69 31 6f 35 35 69 31 6f 31 64 31 6f 31 39 64 31 6f 31 37 64 31 6f 31 38 64 31 6f 32 39 69 31 6f 31 32 69 31 6f 32 36 69 31 6f 38 64 31 6f 35 39 64 31 6f 32 37 69 31 6f 36 64 31 6f 31 37 69 31 6f 31 32 64 31 6f 37 64 31 6f 35 69 31 6f 31 64 31 6f 32 64 31 6f 31 32 69 31 6f 39 64 31 6f 32 36 64 31 6f"

print(f"[+] Original :\n{CIPHER}\n")

# 1. Conversion depuis l'hexadecimal
UNHEX = bytes.fromhex(CIPHER.replace(" ","")).decode()
print(f"[+] Hexa :\n{UNHEX}\n")

# 2. Developpement
def devNumbers(match_obj):
    return match_obj.group() + "*"

def devLetters(match_obj):
    return "\'" + match_obj.group() + "\'+"

DEV = eval(re.sub("[a-z]",devLetters,re.sub("[0-9]+",devNumbers,UNHEX))[:-1])
print(f"[+] Develop :\n{DEV}\n")

# 3. DeadFish
# source: https://github.com/ellismckenzielee/codewars-python/blob/master/make-the-deadfish-swim.py
def parse(data):
    '''Returns a list according to the data input'''
    output = 0
    output_array = []
    for letter in data:
        if letter == 'i':
            output += 1
        elif letter == 'd':
            output -= 1
        elif letter == 's':
            output *= output
        elif letter == 'o':
            output_array.append(output) 
    return output_array

DEADFISH = "".join([ chr(u) for u in parse(DEV) ])
print(f"[+] Deadfish :\n{DEADFISH}\n")

# 4. base85
UNBASE85 = base64.a85decode(DEADFISH).decode()
print(f"[+] Base 85 : \n{UNBASE85}")
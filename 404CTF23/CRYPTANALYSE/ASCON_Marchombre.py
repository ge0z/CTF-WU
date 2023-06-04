#!/usr/bin/python3
#404CTF23
#geoz
#27 MAI 2023

import ascon

KEY = bytes.fromhex("00456c6c616e61206427416c2d466172")
NONCE = bytes.fromhex("00"*16)
ASSOCIATED_DATA = bytes.fromhex("80400c0600000000")
CIPHER = bytes.fromhex("ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782")

print(len(KEY))
PLAINTEXT = ascon.decrypt(KEY, NONCE, ASSOCIATED_DATA,CIPHER, variant="Ascon-128")

print(PLAINTEXT.decode('latin'))
#!/usr/bin/env python3
"""USC CTF Fall 2024 - Beginner - colors (crypto)

message.txt is wrapped in three encodings: Base64 -> Hex -> Binary.
Run from this folder: python3 solve.py
"""
import base64

with open("message.txt") as f:
    layer1 = f.read().strip()

layer2 = base64.b64decode(layer1).decode()        # "30 31 30 30 ..." (hex)
layer3 = bytes.fromhex(layer2.replace(" ", "")).decode()  # "01000011 01011001 ..." (binary)
flag = "".join(chr(int(byte, 2)) for byte in layer3.split())

print("After Base64:", layer2[:47], "...")
print("After Hex:   ", layer3[:44], "...")
print("Flag:        ", flag)

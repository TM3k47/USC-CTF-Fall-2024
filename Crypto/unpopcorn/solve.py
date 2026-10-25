#!/usr/bin/env python3
"""USC CTF Fall 2024 - Crypto - unpopcorn

Reverses encoder.py step by step:
    pop    : x -> ord(c) ^ 42
    butter : x -> x * p mod m        (p is secret)
    churn  : x -> x << 3, list rotated left by 16, written as hex

The secret p is recovered from known plaintext: every flag starts with "C".
Run from this folder: python3 solve.py
"""
m = 57983  # = 23 * 2521

with open("message.txt") as f:
    out = [int(h, 16) for h in f.read().split()]

# Undo churn. The encoder wrote l[16:] + l[:16], so with n values the
# first n-16 outputs came from the end of l: l = out[-16:] + out[:-16]
l = out[-16:] + out[:-16]
butter = [x >> 3 for x in l]

# Undo butter with known plaintext: butter[0] = (ord('C') ^ 42) * p mod m
known = ord("C") ^ 42
p = butter[0] * pow(known, -1, m) % m
p_inv = pow(p, -1, m)
print("Recovered p =", p)

# Undo pop
flag = "".join(chr((x * p_inv % m) ^ 42) for x in butter)
print("Flag:", flag)

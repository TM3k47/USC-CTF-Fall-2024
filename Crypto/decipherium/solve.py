#!/usr/bin/env python3
"""USC CTF Fall 2024 - Crypto - decipherium

message.txt is a run of chemical element symbols. Each element's atomic number
is an ASCII code; together they spell a hex string, which decodes to the flag.
Run from this folder: python3 solve.py
"""
SYMBOLS = (
    "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
    "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce "
    "Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
    "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl "
    "Mc Lv Ts Og"
).split()
elements = {sym: z for z, sym in enumerate(SYMBOLS, start=1)}

with open("message.txt") as f:
    cipher_text = f.read().strip()

# Step 1: split into element symbols (try two-letter symbols first)
symbols = []
i = 0
while i < len(cipher_text):
    if cipher_text[i:i + 2] in elements:
        symbols.append(cipher_text[i:i + 2])
        i += 2
    elif cipher_text[i] in elements:
        symbols.append(cipher_text[i])
        i += 1
    else:
        raise ValueError(f"Unknown element symbol at index {i}")

# Step 2: atomic number -> ASCII character  (e.g. Te = 52 = '4', Sb = 51 = '3')
hex_string = "".join(chr(elements[s]) for s in symbols)
print("Atomic numbers as text:", hex_string)

# Step 3: hex -> ASCII
print("Flag:", bytes.fromhex(hex_string).decode())

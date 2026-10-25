#!/usr/bin/env python3
"""USC CTF Fall 2024 - Forensics - think_twice

The flag is Base64-encoded twice and stored in the image's EXIF "Software" tag.
Get the value with:  exiftool -Software metadata.png
Run from this folder: python3 solve.py
"""
import base64

software_tag = "UTNsaU1ISm5lMDFqUTJGeWRHaDVmU0E9"  # from exiftool

once = base64.b64decode(software_tag).decode()   # Q3liMHJne01jQ2FydGh5fSA=
twice = base64.b64decode(once).decode()          # Cyb0rg{McCarthy}

print("Decoded once: ", once)
print("Decoded twice:", twice.strip())

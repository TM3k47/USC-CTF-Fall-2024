# USC CTF Fall 2024 — Writeups

Writeups for the challenges I solved at **USC CTF Fall 2024**.

**Author:** Ahammad Tausif Mayeen ([Bl4ckf1sh](https://www.linkedin.com/in/ahammad-tausif-mayeen-677a55242/))

---

## Challenges

| # | Challenge | Category | Points | Technique | Flag |
|---|-----------|----------|--------|-----------|------|
| 1 | [welcome](Welcome/Readme.md) | Welcome | 10 | Read the provided flag file | `CYBORG{lets_go}` |
| 2 | [colors](Beginner/colors%20%28crypto%29/Readme.md) | Beginner · Crypto | 300 | Base64 → Hex → Binary | `CYBORG{tR0jans_love_C4rdinal_@nd_G0ld}` |
| 3 | [iRobots](Beginner/iRobots%20%28web%29/Readme.md) | Beginner · Web | 300 | Hidden path in `robots.txt` | `CYBORG{robots_txt_is_fun}` |
| 4 | [weirdtraffic](Beginner/weirdtraffic%20%28forensics%29/Readme.md) | Beginner · Forensics | 300 | Data hidden in an ICMP payload | `CYBORG{hping3-is-a-cool-tool}` |
| 5 | [decipherium](Crypto/decipherium/Readme.md) | Crypto | 300 | Element symbols → atomic numbers → hex | `CYBORG{PERI0DIC_C1PH3R_0F_3LEMENT5}` |
| 6 | [unpopcorn](Crypto/unpopcorn/Readme.md) | Crypto | 300 | Reversing a custom encoder, key from known plaintext | `CYBORG{R1Ch_BUTT3RY_SUSTENANC3}` |
| 7 | [think_twice](Forensics/think_twice/Readme.md) | Forensics | 300 | EXIF metadata, double Base64 | `Cyb0rg{McCarthy}` |

**Tools used:** CyberChef, Wireshark / tshark, exiftool, curl, Python.

---

## Repository layout

```
Welcome/                    welcome
Beginner/
├── colors (crypto)/        Readme.md · solve.py · message.txt · screenshots
├── iRobots (web)/          Readme.md · screenshot
└── weirdtraffic (forensics)/  Readme.md · weirdtraffic.pcapng · screenshot
Crypto/
├── decipherium/            Readme.md · solve.py · message.txt · screenshots
└── unpopcorn/              Readme.md · solve.py · encoder.py · message.txt
Forensics/
└── think_twice/            Readme.md · solve.py · metadata.png
```

Each challenge folder has its own writeup with the description, step-by-step solution and screenshots. Folders that have a `solve.py` include the challenge files, so you can rerun the solution:

```bash
cd "Crypto/unpopcorn" && python3 solve.py
```

---

*Ahammad Tausif Mayeen · Bl4ckf1sh*

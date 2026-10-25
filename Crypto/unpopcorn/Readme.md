# unpopcorn

**Category:** Crypto · **Points:** 300 · **Author:** neonlian

← [Back to all challenges](../../README.md)

![Challenge description](problem.png)

## Description

> Welcome to the movies! I have here some Flagville Cryptobacher's original gourmet popping corn kernels. I put them in the microwave, pop the kernels, and drizzle some butter on top.
>
> You take the bag of popcorn (the message) and wonder, how can I unpop the popcorn?

**Files:** [`encoder.py`](encoder.py), [`message.txt`](message.txt)

## Analysing the encoder

```python
m = 57983
p = int(open("p.txt").read().strip())      # secret, not given

def pop(s):                                 # XOR each char with 42
    return map(lambda x: ord(x) ^ 42, s)

def butter(s):                              # multiply by p, mod m
    return map(lambda x: x * p % m, s)

def churn(s):                               # shift left 3, rotate the list, print hex
    l = list(map(lambda x: (x << 3), s))
    return " ".join(map(lambda x: "{:x}".format(x).upper(), l[16:] + l[:16]))

message.write(churn(butter(pop(flag))))
```

Each character goes through three steps, and each one can be undone:

| Step | Operation | Inverse |
|------|-----------|---------|
| `pop` | `x ^ 42` | XOR with 42 again |
| `butter` | `x · p mod m` | multiply by `p⁻¹ mod m` |
| `churn` | `x << 3`, then rotate the list left by 16 | `x >> 3`, then rotate back |

The only unknown is the secret multiplier **`p`**.

## Solution

**1. Undo `churn`.** Parse the 31 hex values and shift each one right by 3. To undo the rotation, remember that the encoder output `l[16:] + l[:16]`. With 31 values, the first **15** outputs are the end of the list, so:

```python
l = out[-16:] + out[:-16]      # NOT out[16:] + out[:16]
```

> My first script used `out[16:] + out[:16]`, which is off by one for a list of 31. It printed the flag rotated by one character: `YBORG{...}C`. The correct inverse rotates by `len − 16`.

**2. Recover `p` from known plaintext.** We know the flag starts with `C`, so the first value is:

```
butter[0] = (ord('C') ^ 42) · p  mod m  =  105 · p  mod m
```

`m = 57983 = 23 × 2521`, and `gcd(105, m) = 1`, so 105 has an inverse mod `m` and `p` falls out directly:

```python
p = butter[0] * pow(105, -1, m) % m       # p = 24498
```

Trying every `p` from 1 to `m` also works, since the keyspace is only ~58k. The known-plaintext approach just needs no searching.

**3. Undo `butter` and `pop`.**

```python
p_inv = pow(p, -1, m)
flag = "".join(chr((x * p_inv % m) ^ 42) for x in butter)
```

Full script: [`solve.py`](solve.py)

```
$ python3 solve.py
Recovered p = 24498
Flag: CYBORG{R1Ch_BUTT3RY_SUSTENANC3}
```

## Flag

```
CYBORG{R1Ch_BUTT3RY_SUSTENANC3}
```

## Takeaway

Each character is encrypted on its own with the same key, which makes this a **substitution cipher**. Knowing one character of plaintext (the flag prefix `C`) is enough to recover the whole key.

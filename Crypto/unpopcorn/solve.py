from sympy import mod_inverse

m = 57983

# Encrypted message in hexadecimal format
encrypted_message = ["3FB60", "4F510", "42930", "31058", "DEA8", "4A818", "DEA8", "1AA88", "65AE0", "1C590",
                     "17898", "1C590", "29170", "3FB60", "55D10", "29170", "42930", "6A7D8", "4C320", "4F510",
                     "5FC0", "193A0", "4F510", "2E288", "29170", "643F8", "31058", "6A7D8", "4A818", "1AA88", "1AA88"]

# Convert hex values to integers
encrypted_message = [int(x, 16) for x in encrypted_message]

# Step 1: Undo the churn rotation (rotate the first 16 elements to the back)
reversed_churn = encrypted_message[16:] + encrypted_message[:16]

# Step 2: Reverse the bitwise left shift (shift right by 3 bits)
shifted_message = [x >> 3 for x in reversed_churn]

# Brute-force possible values of p and try to decrypt
for p in range(1, m):
    try:
        p_inv = mod_inverse(p, m)
        buttered_message = [(x * p_inv) % m for x in shifted_message]
        
        # Step 3: Reverse the XOR operation with 42
        decrypted_message = "".join(chr(x ^ 42) for x in buttered_message)
        
        # Check if the message seems readable
        if all(32 <= ord(c) < 127 for c in decrypted_message):  # Check for ASCII printable range
            print(f"Possible decryption with p={p}:")
            print(decrypted_message)
            break

    except ValueError:
        # Skip if p has no modular inverse (i.e., gcd(p, m) != 1)
        continue


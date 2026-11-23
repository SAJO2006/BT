# """Cryptographic utility functions for the assignment."""

# # pylint: disable=invalid-name

# import hashlib
# import secrets
# import math


# # ==========================================================
# # PRIME NUMBER CHECK
# # ==========================================================

# def is_prime(candidate):
#     """Return whether candidate is a prime number."""

#     if candidate < 2:
#         return False

#     if candidate == 2:
#         return True

#     if candidate % 2 == 0:
#         return False

#     i = 3

#     while i * i <= candidate:

#         if candidate % i == 0:
#             return False

#         i += 2

#     return True


# # ==========================================================
# # GENERATE 4-DIGIT PRIME NUMBER
# # ==========================================================

# def generate_prime():
#     """Generate and return a random four-digit prime number."""

#     while True:

#         number = secrets.randbelow(9000) + 1000

#         if is_prime(number):
#             return number


# # ==========================================================
# # RSA KEY GENERATION
# # ==========================================================

# def generate_rsa_keys():
#     """Generate and return RSA key parameters."""

#     # Constant public exponent
#     public_exponent = 65537

#     while True:

#         prime_p = generate_prime()
#         prime_q = generate_prime()

#         if prime_p == prime_q:
#             continue

#         modulus = prime_p * prime_q

#         totient = (prime_p - 1) * (prime_q - 1)

#         # e must be relatively prime to phi
#         if math.gcd(public_exponent, totient) == 1:
#             break

#     # Private exponent
#     private_exponent = pow(public_exponent, -1, totient)

#     return prime_p, prime_q, modulus, totient, public_exponent, private_exponent


# # ==========================================================
# # SHA-256 - SAME BASIC METHOD AS ASSIGNMENT 1
# # ==========================================================

# def generate_hash(data):
#     """Return the SHA-256 hexadecimal digest of the input data."""

#     hash_value = hashlib.sha256(
#         data.encode("utf-8")
#     ).hexdigest()

#     return hash_value


# # ==========================================================
# # MAIN PROGRAM
# # ==========================================================

# print("=" * 55)
# print("        RSA DIGITAL SIGNATURE DEMONSTRATION")
# print("=" * 55)


# # ==========================================================
# # GENERATE RSA KEYS
# # ==========================================================

# print("\nGenerating RSA keys...")

# p, q, n, phi, e, d = generate_rsa_keys()


# # ==========================================================
# # RSA PARAMETERS
# # ==========================================================

# print("\nRSA PARAMETERS")
# print("-" * 25)

# print("p       =", p)
# print("q       =", q)
# print("n       =", n)
# print("phi(n)  =", phi)
# print("e       =", e)
# print("d       =", d)


# # ==========================================================
# # PUBLIC AND PRIVATE KEYS
# # ==========================================================

# print("\nPUBLIC KEY")
# print("-" * 25)

# print("(e, n) =", (e, n))


# print("\nPRIVATE KEY")
# print("-" * 25)

# print("(d, n) =", (d, n))


# # ==========================================================
# # USER INPUT
# # ==========================================================

# print("\n" + "=" * 55)
# print("ENTER TRANSACTION DETAILS")
# print("=" * 55)

# sender = input("Sender   : ")
# receiver = input("Receiver : ")
# amount = input("Amount   : ")


# # Create transaction
# transaction = (
#     f"Sender:{sender}|"
#     f"Receiver:{receiver}|"
#     f"Amount:{amount}"
# )


# print("\nOriginal Transaction")
# print("-" * 25)

# print(transaction)


# # ==========================================================
# # HASH 1
# # ==========================================================

# hash1 = generate_hash(transaction)

# print("\nHASH 1 - SHA-256")
# print("-" * 25)

# print(hash1)


# # Convert SHA-256 hash to integer
# hash1_number = int(hash1, 16)

# # Educational RSA representation
# rsa_hash1 = hash1_number % n


# print("\nRSA Hash Representative:")
# print(rsa_hash1)


# # ==========================================================
# # DIGITAL SIGNATURE
# # ==========================================================

# # Signature = Hash^d mod n

# signature = pow(
#     rsa_hash1,
#     d,
#     n
# )


# print("\nDIGITAL SIGNATURE")
# print("-" * 25)

# print(signature)


# # ==========================================================
# # HASH 2
# # ==========================================================

# # Hash 2 = Signature^e mod n

# rsa_hash2 = pow(
#     signature,
#     e,
#     n
# )


# print("\nHASH 2 - RECOVERED USING PUBLIC KEY")
# print("-" * 25)

# print(rsa_hash2)


# # ==========================================================
# # VERIFICATION
# # ==========================================================

# print("\n" + "=" * 55)
# print("SIGNATURE VERIFICATION")
# print("=" * 55)

# print("\nHash 1 Representative :", rsa_hash1)
# print("Hash 2                :", rsa_hash2)


# if rsa_hash1 == rsa_hash2:

#     print("\n✓ HASH 1 = HASH 2")
#     print("✓ SIGNATURE VERIFICATION: SUCCESS")
#     print("✓ Transaction is authentic and unchanged.")

# else:

#     print("\n✗ HASH 1 ≠ HASH 2")
#     print("✗ SIGNATURE VERIFICATION: FAILED")


# # ==========================================================
# # TAMPERING TEST
# # ==========================================================

# print("\n" + "=" * 55)
# print("TAMPERING TEST")
# print("=" * 55)

# modified_amount = input(
#     "\nEnter modified amount: "
# )


# modified_transaction = (
#     f"Sender:{sender}|"
#     f"Receiver:{receiver}|"
#     f"Amount:{modified_amount}"
# )


# # Generate new SHA-256 hash
# modified_hash = generate_hash(
#     modified_transaction
# )

# modified_hash_number = int(
#     modified_hash,
#     16
# )

# modified_rsa_hash = modified_hash_number % n


# print("\nModified Transaction")
# print("-" * 25)

# print(modified_transaction)


# print("\nModified SHA-256 Hash:")
# print(modified_hash)


# print("\nOriginal Hash Representative :",
#       rsa_hash1)

# print("Modified Hash Representative:",
#       modified_rsa_hash)


# # ==========================================================
# # VERIFY MODIFIED TRANSACTION
# # ==========================================================

# # Original signature is reused
# recovered_hash = pow(
#     signature,
#     e,
#     n
# )


# if modified_rsa_hash == recovered_hash:

#     print("\n✗ Modified Transaction: VALID")

# else:

#     print("\n✓ Modified Transaction: INVALID")
#     print("✓ Hash values do not match.")
#     print("✓ Signature verification failed.")
#     print("✓ Transaction has been modified.")


# # ==========================================================
# # FINAL RESULT
# # ==========================================================

# print("\n" + "=" * 55)
# print("FINAL RESULT")
# print("=" * 55)

# print("Original Transaction : VERIFIED")

# print("Modified Transaction : REJECTED")


import hashlib
import math
import secrets


def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def get_prime():
    while not is_prime(num := secrets.randbelow(9000) + 1000):
        pass
    return num


def generate_keys():
    e = 65537
    while True:
        p, q = get_prime(), get_prime()
        phi = (p - 1) * (q - 1)
        if p != q and math.gcd(e, phi) == 1:
            return p, q, p * q, phi, e, pow(e, -1, phi)


def rsa_hash(data, n):
    h = hashlib.sha256(data.encode()).hexdigest()
    return h, int(h, 16) % n


# 1. Key Generation
p, q, n, phi, e, d = generate_keys()
print(f"Params: p={p}, q={q}, n={n}, phi={phi}, e={e}, d={d}")
print(f"Public Key: {(e, n)} | Private Key: {(d, n)}\n")

# 2. Input & Hashing
sender, receiver, amount = (
    input("Sender: "),
    input("Receiver: "),
    input("Amount: "),
)
tx = f"Sender:{sender}|Receiver:{receiver}|Amount:{amount}"
h1, rsa_h1 = rsa_hash(tx, n)
print(f"\nOriginal Tx: {tx}\nSHA-256: {h1}\nRSA Hash 1: {rsa_h1}")

# 3. Sign & Verify
sig = pow(rsa_h1, d, n)
rsa_h2 = pow(sig, e, n)
print(f"\nSignature: {sig}\nRecovered Hash 2: {rsa_h2}")
print("Verification:", "SUCCESS ✓" if rsa_h1 == rsa_h2 else "FAILED ✗")

# 4. Tampering Test
mod_amt = input("\nEnter modified amount: ")
mod_tx = f"Sender:{sender}|Receiver:{receiver}|Amount:{mod_amt}"
mod_h, mod_rsa_h = rsa_hash(mod_tx, n)
is_valid = mod_rsa_h == pow(sig, e, n)

print(
    f"\nModified Tx: {mod_tx}\nModified SHA-256: {mod_h}\nModified RSA Hash:"
    f" {mod_rsa_h}"
)
print(
    "Tamper Check:",
    "VALID ✗" if is_valid else "INVALID (Tampering Detected) ✓",
)
        

#rsa_decryption.py
#This script demonstrates the decryption formula:
#    plaintext = (ciphertext ** d) % n

#This script prints the numeric plaintext (as an integer).

def rsa_decrypt(n: int, d: int, ciphertext: int) -> int:
    #Perform RSA decryption and return the plaintext integer.
    #Using Python's built-in pow with three arguments is efficient and safe:
        #pow(ciphertext, d, n)
    # pow(a, b, mod) computes (a**b) % mod efficiently
    return pow(ciphertext, d, n)


if __name__ == "__main__":
    # Ask for inputs one by one; validate they are integers
    print("RSA decryption helper (enter values as integers).")

    while True:
        try:
            n = int(input("Enter n (modulus): "))
            break
        except ValueError:
            print("Please enter a valid integer for n.")

    # e is not used for decryption here, but still ask for it to match lab format
    while True:
        try:
            e = int(input("Enter e (public exponent) - this is not used for decryption here: "))
            break
        except ValueError:
            print("Please enter a valid integer for e.")

    while True:
        try:
            d = int(input("Enter d (private exponent): "))
            break
        except ValueError:
            print("Please enter a valid integer for d.")

    while True:
        try:
            ciphertext = int(input("Enter ciphertext (as an integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for ciphertext.")

    plaintext = rsa_decrypt(n, d, ciphertext)
    print("\nDecrypted plaintext (numeric):")
    print(plaintext)

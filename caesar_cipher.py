
#caesar_cipher.py

#This program:
#- Asks the user for a message and a numeric key.
#- Shifts letters by the key (A->D with key=3).
#- Preserves uppercase and lowercase.
#- Leaves spaces and other characters unchanged.


def caesar_cipher(message: str, key: int) -> str:
   
    encrypted = []

    # Process each character one by one
    for char in message:
        # Keep spaces as they are 
        if char == ' ':
            encrypted.append(' ')
        # If the char is uppercase (A-Z) handle separately
        elif char.isupper():
            # Convert letter to number 0-25 using ord()
            shifted = ord(char) - ord('A')        # 'A' -> 0, 'B' -> 1, ...
            shifted = (shifted + key) % 26       # shift and wrap around using modulo
            encrypted.append(chr(shifted + ord('A')))  # convert back to a letter
        # If the char is lowercase (a-z) handle separately
        elif char.islower():
            shifted = ord(char) - ord('a')        # 'a' -> 0, etc.
            shifted = (shifted + key) % 26
            encrypted.append(chr(shifted + ord('a')))
        else:
            # For digits, punctuation, emojis, etc. — leave them unchanged
            encrypted.append(char)

    # Join the list of characters into a single string and return it
    return ''.join(encrypted)


if __name__ == "__main__":
   
    message = input("Enter the message to encrypt: ")

    # Validate key input so the program doesn't crash if they type text
    while True:
        key_input = input("Enter a numeric key (e.g., 3): ")
        try:
            key = int(key_input)
            break
        except ValueError:
            print("That was not an integer. Please enter a whole number (like 3).")

    encrypted_message = caesar_cipher(message, key)
    print("\nEncrypted message:")
    print(encrypted_message)
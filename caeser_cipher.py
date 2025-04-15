def caeser_cipher(text, shift, mode='encode'):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Parameters:
    text (str): The message to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.
    mode (str): 'encode' to encrypt, 'decode' to decrypt. Default is 'encode'.

    Returns:
    str: The encrypted or decrypted message.
    """
    result = ""
    
    # Traverse through each character in the text
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + (shift if mode == 'encode' else -shift)) % 26
            result += chr(base + offset)

        else:
            result += char  # Non-alphabetic characters are unchanged

    return result

if __name__ == "__main__":
    print("Caeser Cipher")
    print("--" * 30)

    choice = input("1. Encode\n2. Decode\nEnter Choice: ").strip()
    if choice not in ('1', '2'):
        print("Invalid choice.")
        exit()

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (eg., 7): "))
    except ValueError:
        print("Shift must be a number.")
        exit()

    mode = 'encode' if choice == '1' else 'decode'
    result = caeser_cipher(message, shift, mode)

    print(f"\n {'Encoded' if mode == 'encode' else 'Decoded'} Message: {result}")

"""
we are implementing caesar cipher algorithm in below code.
"""


def caesar_cipher(text, shift):
    caesar_cipher = ''
    for char in text.strip():
        if char.isalpha():
            if char.isupper():
                ascii_value = (int(ord(char)) - int(shift) - 65) % 26 + 65
                caesar_cipher += chr(ascii_value)
            else:
                ascii_value = (int(ord(char)) - int(shift) - 97) % 26 + 97
                caesar_cipher += chr(ascii_value)
        elif char.isnumeric():
            number_value = int(char) - int(shift)
            caesar_cipher += str(number_value)
        else:
            ascii_value = int(ord(char)) - int(shift)
            caesar_cipher += chr(ascii_value)
    return caesar_cipher


plain_text = input("Enter plain text: ")
shift_value = 3
cipher_text = caesar_cipher(plain_text, shift_value)
print(cipher_text)

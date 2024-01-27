from itertools import cycle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# for i in range(n = 3): # set n to desired value
#     print(alphabet[i % len(alphabet)])
encrypted = []
decrypted = []

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    for letter in text:
       letter_pos = alphabet.index(letter)
       new_letter_pos = ((letter_pos + shift) % len(alphabet))
       encrypted.append(alphabet[new_letter_pos])
    print(f"the encoded text is {''.join(encrypted)}")

encrypt(text,shift)
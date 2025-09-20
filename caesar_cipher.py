from tokenize import endpats
from wsgiref.util import shift_path_info


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function for encrypt()
def encrypt(original_text, shift_amount):
    encoded_result = ""
    
    # for each letter in the original text, find its index in the alphabet and change it to index + shift
    for letter in original_text:
        new_index = (alphabet.index(letter) + shift) % 26
        encoded_result += alphabet[new_index]

    print(encoded_result)

# When use inputs encode, use the encypt function
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
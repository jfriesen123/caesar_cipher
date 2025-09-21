alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    text_result = ''
    
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet: 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            text_result += alphabet[shifted_position]
        elif letter not in alphabet:
            text_result += letter

    print(f"Here is the {direction}d result: {text_result}")

go_again = True

while go_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    continue_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" ).lower()

    if continue_cipher == 'no':
        print("Goodbye!")
        go_again = False
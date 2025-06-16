alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encoded_message = ""
    for char in original_text:
        index_value = alphabet.index(char)
        new_index = (index_value + shift_amount) % len(alphabet)
        encoded_message += alphabet[new_index]

    print(encoded_message)
    return encoded_message

encrypt(text, shift)


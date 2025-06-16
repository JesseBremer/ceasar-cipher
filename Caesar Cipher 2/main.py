alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar():

def encrypt(original_text, shift_amount):
    encoded_message = ""
    for char in original_text:
        index_value = alphabet.index(char)
        new_index = (index_value + shift_amount) % len(alphabet)
        encoded_message += alphabet[new_index]

    print(encoded_message)
    return encoded_message

encrypt(text, shift)

def decrypt(original_text, shift_amount):
    decrypted_message = ""
    for char in original_text:
        index_value = alphabet.index(char)
        new_index = (index_value - shift_amount) % len(alphabet)
        decrypted_message += alphabet[new_index]

    print(decrypted_message)
    return decrypted_message

decrypt(text, shift)



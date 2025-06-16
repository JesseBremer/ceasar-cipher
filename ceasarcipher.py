from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_program = "yes"

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -shift_amount

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



while run_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    while True:
        run_program = input("Use the service again? 'Yes' or 'No' \n").strip().lower()

        if run_program == "yes":
            break
        elif run_program == "no":
            print("Goodbye.")
            exit()
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")





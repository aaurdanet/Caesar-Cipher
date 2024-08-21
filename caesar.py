import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction, key_count):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}, Key used: {key_count}")


def bruteforce_attack(start_text, cipher_direction):
    shift = 0
    for i in range(0, 26):
        shift += 1

        if shift > 26:
            shift = shift % 26

        caesar(start_text=start_text, shift_amount=shift, cipher_direction=cipher_direction, key_count=shift)


continue_cipher = True

while continue_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "decode":
        bruteforce_selection = input("Would you like to bruteforce? Type 'Yes'. Otherwise Type 'No'\n").lower()
    else:
        bruteforce_selection = "no"

    text = input("Type your message:\n").lower()

    if bruteforce_selection == "yes":
        bruteforce_attack(start_text=text, cipher_direction=direction)

    else:

        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        continue_cipher = False
        print("Goodbye")
    elif restart == "yes":
        continue_cipher = True

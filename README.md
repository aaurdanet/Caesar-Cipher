Caesar Cipher Program

This Python program implements a Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet. The program can both encode and decode messages using a user-specified shift value. Additionally, it includes a brute-force attack mode to decrypt a message by trying all possible shift values.
Features

    Encoding and Decoding: The program allows users to encode a message by shifting the letters forward and decode it by shifting them backward.
    Brute-force Attack: When decoding, the user has the option to perform a brute-force attack, which will try all possible shifts (1 through 25) to decrypt the message.
    Input Validation: The program handles non-alphabet characters (such as numbers, spaces, and punctuation) by leaving them unchanged.
    Continuous Use: After each operation, users are prompted to continue with another operation or exit the program.

Usage
Running the Program

    Starting: When the program starts, it displays a logo (imported from the art module) and then prompts the user to choose between encoding or decoding a message.

    Input:
        The user inputs whether they want to "encode" or "decode" a message.
        If decoding, the user is asked if they want to perform a brute-force attack.
        The user then inputs the message they want to process.
        If not using brute-force, the user inputs the shift value (a number).

    Output:
        The program displays the encoded or decoded message.
        If a brute-force attack was chosen, the program will display all possible decoded messages with different shifts.

    Repeating: After completing one operation, the user can choose to perform another operation or exit the program.

Example

    Encoding:

    python

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here's the encoded result: mjqqt

Decoding:

python

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Would you like to bruteforce? Type 'Yes'. Otherwise Type 'No'
no
Type your message:
mjqqt
Type the shift number:
5
Here's the decoded result: hello

Brute-force Attack:

python

    Type 'encode' to encrypt, type 'decode' to decrypt:
    decode
    Would you like to bruteforce? Type 'Yes'. Otherwise Type 'No'
    yes
    Type your message:
    mjqqt
    Here's the decoded result: lipps
    Here's the decoded result: khoor
    Here's the decoded result: jgnnq
    ...

Notes

    The program automatically adjusts the shift value if it exceeds 26 (the length of the alphabet).
    This is a simple implementation and assumes English alphabet (a-z).

Dependencies

    art module is required for displaying the logo.

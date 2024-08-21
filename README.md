Caesar Cipher Program

Features

    Encryption and Decryption: Easily encode or decode text using the Caesar Cipher by specifying the shift value.
    Brute Force Attack: Automatically attempts all possible shift values (1-26) to decrypt messages without a known key.
    Custom Key Display: Shows the key used during the encryption/decryption process for better traceability.
    User Interaction: Intuitive prompts guide users through selecting encryption, decryption, or brute force modes.

Usage

    Start the Program: Run the caesar.py script.
    Select Operation:
        Type encode to encrypt a message.
        Type decode to decrypt a message.
    Brute Force Option:
        If decoding, you'll be prompted to choose whether to brute force the decryption.
        Type yes to initiate brute force decryption.
        Type no to proceed with a specific shift value.
    Input Message: Enter the message you wish to encode or decode.
    Shift Value:
        If not using brute force, input the desired shift number (1-26).
        The tool will adjust the shift value if it exceeds 26.
    View Results: The tool displays the encoded/decoded message and the key used.

Example

python

# Example for encoding a message
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here's the encoded result: mjqqt, Key used: 5

# Example for brute force decoding
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Would you like to bruteforce? Type 'Yes'. Otherwise Type 'No':
yes
Type your message:
mjqqt
# The tool will display possible decoded messages with different keys.

Dependencies

    Python 3.x
    art library (optional for displaying ASCII art logo)

Install the art library via pip if desired:

bash

pip install art

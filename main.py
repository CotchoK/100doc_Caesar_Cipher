import enc_dec_funcs as edf

# ask for whether the message needs to be encrypted or decrypted and store in variable
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()

# ask for the word they use wants to encrypt/decrypt
text = input("Enter your secret word: ").lower()
# ask the user for the shift value
shift = int(input("Enter your shift value: \n"))

# run caesar function
edf.caesar(word=text, encryption=shift, direction=direction)

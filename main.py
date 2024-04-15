import enc_dec_funcs as edf

# ask for whether the message needs to be encrypted or decrypted and store in variable
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()

# ask for the word they use wants to encrypt/decrypt
text = input("Enter your secret word: ").lower()
# ask the user for the shift value
shift = int(input("Enter your shift value: \n"))

# check if encryption or decryption method was chosen and run the appropriate function
if direction == 'encode':
    edf.encrypt(word=text, encryption=shift)
else:
    edf.decrypt(word=text, encryption=shift)
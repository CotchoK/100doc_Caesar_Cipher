import enc_dec_funcs as edf
import ascii_art as aa

# print the logo of the application
print(aa.logo)

def run():
    # ask for whether the message needs to be encrypted or decrypted and store in variable
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()

    # ask for the word they use wants to encrypt/decrypt
    text = input("Enter your secret word: ").lower()
    # ask the user for the shift value
    shift = int(input("Enter your shift value: \n"))

    # run caesar function
    edf.caesar(word=text, encryption=shift, direction=direction)

    re_run = input("Type 'yes' if you want to go again, otherwise type 'no'. ")
    if re_run == 'yes':
        run()
    else:
        print("Goodbye")
        exit()


# run program
run()










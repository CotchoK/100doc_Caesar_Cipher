import enc_dec_funcs as edf

plain_text = input("Enter your secret word: ")
shift = int(input("Enter your shift value: "))

edf.encrypt(word=plain_text, encryption=shift)
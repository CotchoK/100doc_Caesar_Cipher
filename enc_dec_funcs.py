# importing the alphabetic list
import alpha_list


# ##########  ENCRYPT FUNCTION  ##########
def caesar(word, encryption, direction):
    """Encrypts/Decrypts the text passed to it based on encryption and direction passed

    :param word: a string to be encrypted
    :param encryption: the encryption cipher
    :param direction: option on either encrypting/decrypting text passed
    :return: print to screen resultant text
    """
    # variable to store cipher_text we will build up
    resultant_text = ''

    # for loop construct for the length of the word passed to it
    for pos_in_word in range(len(word)):

        # store the index of the same letter from the alpha list
        pos_in_alpha_list = alpha_list.alpha.index(word[pos_in_word])

        # wrap around logic for shift mechanism
        if direction == 'encode':
            if pos_in_alpha_list + encryption > 25:
                cipher_letter_pos = pos_in_alpha_list + encryption - 26
                resultant_text += alpha_list.alpha[cipher_letter_pos]
            else:
                cipher_letter_pos = pos_in_alpha_list + encryption
                resultant_text += alpha_list.alpha[cipher_letter_pos]
        elif direction == 'decode':
            if pos_in_alpha_list - encryption < 0:
                cipher_letter_pos = pos_in_alpha_list - encryption + 26
                resultant_text += alpha_list.alpha[cipher_letter_pos]
            else:
                cipher_letter_pos = pos_in_alpha_list - encryption
                resultant_text += alpha_list.alpha[cipher_letter_pos]


    # print out the cipher text for testing
    print(resultant_text)




# importing the alphabetic list
import alpha_list


def encrypt(word, encryption):
    """Encrypt a word passed to it

    :param word:
    :param encryption:
    :return:
    """
    # variable to store cipher_text we will build up
    cipher_text = ''

    # for loop construct for the length of the word passed to it
    for pos_in_word in range(len(word)):

        # store the index of the same letter from the alpha list
        pos_in_alpha_list = alpha_list.alpha.index(word[pos_in_word])

        # wrap around logic for shift mechanism
        if pos_in_alpha_list + encryption > 25:
            cipher_letter_pos = pos_in_alpha_list + encryption - 26
            cipher_text += alpha_list.alpha[cipher_letter_pos]
        else:
            cipher_letter_pos = pos_in_alpha_list + encryption
            cipher_text += alpha_list.alpha[cipher_letter_pos]

    #print out the cipher text for testing
    print(cipher_text)





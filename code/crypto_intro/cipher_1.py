"""
Ciphering a string with a random key
"""
from random import shuffle
from termcolor import colored


def cipher(message):
    # here the key will be a random permutation of the 26 letters of the
    # alphabet
    key = [i for i in range(26)]
    # shuffle the key in order to have a random permutation
    """
        ADD LINE(S) HERE
    """
    print(f"key : {key}")
    # crypted_message
    crypted_message = ""
    for character in message:
        # encode each string as an integer (here ord returns the unicode code
        # point for a one character string)
        ascii_index = ord(character)
        if ascii_index > 64 and ascii_index < 91:
            # use the key to change the ascii index
            """
                EDIT HERE
            """
            new_index = key[4] + 65
            # the chr function returns the unicode string for a given integer
            new_letter = chr(new_index)
            # in python you can concatenante strings with +
            crypted_message += new_letter
            print(colored(character , "green", attrs=["bold"]), end="")
            print(" is changed to ", end="")
            print(colored(new_letter , "green", attrs=["bold"]))
        else:
            # in this example we only take the uppercase letters into account
            crypted_message += character
    with open("crypted_messages/crypted_message_1.txt", "w") as text_file:
        text_file.write(crypted_message)
    return crypted_message


print(cipher("ALGORITHM COURSE"))

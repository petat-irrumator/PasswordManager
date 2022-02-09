import imp

import random
import secrets


def make_random_password():
    # list that contains all the keywords from which the password would be randomly generated from
    password_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',  'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '`', '~', '?', '/', '|', '<', '>', '.', ',', ';', ':']

    # making the random 20 digit password
    key_1 = secrets.choice(password_list)
    key_2 = secrets.choice(password_list)
    key_3 = secrets.choice(password_list)
    key_4 = secrets.choice(password_list)
    key_5 = secrets.choice(password_list)
    key_6 = secrets.choice(password_list)
    key_7 = secrets.choice(password_list)
    key_8 = secrets.choice(password_list)
    key_9 = secrets.choice(password_list)
    key_10 = secrets.choice(password_list)
    key_11 = secrets.choice(password_list)
    key_12 = secrets.choice(password_list)
    key_13 = secrets.choice(password_list)
    key_14 = secrets.choice(password_list)
    key_15 = secrets.choice(password_list)
    key_16 = secrets.choice(password_list)
    key_17 = secrets.choice(password_list)
    key_18 = secrets.choice(password_list)
    key_19 = secrets.choice(password_list)
    key_20 = secrets.choice(password_list)
    parent_key1 = key_1+key_2+key_3+key_4+key_5+key_6+key_7+key_8+key_9+key_10
    parent_key2 = key_11+key_12+key_13+key_14 + \
        key_15+key_16+key_17+key_18+key_19+key_20
    ultimate_key = parent_key1+parent_key2
    print(ultimate_key)
    input()

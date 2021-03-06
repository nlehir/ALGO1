"""
    not for students
"""

import rsa_functions

primes_couples = [(11, 17),
                  (13, 23),
                  (29, 97),
                  (97, 127),
                  (8191, 127)]


def generate_key_code(p, q, index):
    """
        for a single value
    """
    phi = (p - 1) * (q - 1)
    print('-----')
    print('p, q : ' + str(p) + ', ' + str(q))
    n = p * q
    a, b = rsa_functions.generate_rsa_keys(p, q)
    remainder = a * b % phi
    if remainder == 1:
        print('keys are ok : b is the inverse of a modulo phi')
    else:
        print('probem with keys ! b is not the inverse of a modulo phi')

    public_key = (n, a)
    private_key = b
    print('public key : ' + str(public_key))
    print('private_key : ' + str(private_key))

    # save the keys
    with open('rsa_keys/public_key_' + str(index) +
              '.txt', 'w') as text_file:
        text = text_file.write(
            str(public_key[0]) + ',' + str(public_key[1]))

    with open('rsa_keys/private_key_' + str(index) +
              '.txt', 'w') as text_file:
        text = text_file.write(str(b))

    # text to code
    with open('texts/hidden_text_' + str(index) +
              '.txt', 'r') as text_file:
        text = text_file.read()

    code = rsa_functions.cipher_rsa(text, public_key)

    # save the code
    with open('crypted_messages/crypted_message_rsa_' +
              str(index) + '.txt', 'w') as text_file:
        text_file.write(code)
    print('code : ' + str(code) + '\n')


def generate_keys_codes(primes_couples):
    for couple in enumerate(primes_couples):
        index = couple[0] + 1
        p, q = couple[1]
        generate_key_code(p, q, index)


# generate_keys_codes(primes_couples)
# use Mersene numbers
# generate_key_code(2**607 - 1, 2**1  279 - 1, 6)
generate_key_code(4409, 2003, 6)
# https://www.nombres-premiers.fr/liste.html
# generate_key_code(8191, 127, 6)

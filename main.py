import random
import string
import argparse
from pprint import pprint

import utils
from quipster import Quipster


def generate_cipher(text, vocabulary=string.ascii_lowercase):
    key = list(vocabulary).copy()
    random.shuffle(key)
    text = text.lower()
    cipher = utils.transform(text, key, vocabulary)
    return cipher

def main(args):
    
    if args.cipher_path is not None:
        cipher = utils.load_file(args.cipher_path)
    elif args.plaintext_path is not None:
        plaintext = utils.load_file(args.plaintext_path)
        cipher = generate_cipher(plaintext)
    else:
        raise Exception('Must specify either --cipher_path or --plaintext_path')

    # Instantiate and fit the Quipster substitution cipher solver
    cryptanalyzer = Quipster(
        args.num_trials,
        args.num_swaps,
        args.char_swaps
    )
    key = cryptanalyzer.fit(cipher)
    decrypted = cryptanalyzer.decode(cipher)

    print("\nPlaintext:\n")
    pprint(plaintext)

    print("\nCiphertext:\n")
    pprint(cipher)

    print("\nDecrypted:\n")
    pprint(decrypted)

    print('\nKey:\n')
    pprint(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cipher_path", type=str, default=None, help="Path to file containing ciphertext")
    parser.add_argument("--plaintext_path", type=str, default=None, help="Path to file containing ciphertext")
    parser.add_argument("--num_trials", type=int, default=15, help="Number of trials to execute")
    parser.add_argument("--num_swaps", type=int, default=10**4, help="Number of swaps to perform per trial")
    parser.add_argument("--char_swaps", type=int, default=2, help="Number of characters swapped in key each iteration")
    args = parser.parse_args()
    main(args)
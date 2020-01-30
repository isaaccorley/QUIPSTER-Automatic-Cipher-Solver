import os
import argparse
from pprint import pprint

from quipster import Quipster

def load(file_path):
    with open(file_path, 'r') as f:
        cipher = 

    return cipher

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cipher_path", type=str, help="Path to file containing ciphertext")
    parser.add_argument("--num_trials", type=int, help="Number of trials to execute")
    parser.add_argument("--num_swaps", type=int, help="Number of swaps to perform per trial")
    args = parser.parse_args()
    
    ciphertext = load(args.cipher_path)

    cryptanalyzer = Quipster(
        ciphertext,
        args.num_trials,
        args.num_swaps
    )
    plaintext, key = cryptanalyzer.decode()
    
    print("\nCiphertext:\n")
    pprint(cipher)

    print("\nPlaintext:\n")
    pprint(plaintext)

    print('\nKey:\n')
    pprint(key)
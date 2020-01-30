import os
import glob
import random
import argparse
from pprint import pprint

from quipster import Quipster
from data import load_great_expectations, preprocess, transform


PLAINTEXT_PATH = "./data/plaintexts/"


def load_cipher(file_path):
    with open(file_path, 'r') as f:
        cipher = f.read().strip()

    return cipher

def load_plaintext():
    plaintexts = glob.glob(PLAINTEXT_PATH + "*.txt")
    text = random.sample(plaintexts)

    with open(text, 'r') as f:
        text = f.read().strip()

    text = preprocess(text)
    return text

def generate_cipher(text):
    vocabulary = string.ascii_uppercase
    key = vocabulary.copy()
    random.shuffle(key)

    cipher = transform()



def main(args)
    
    corpus = load_great_expectations()

    cryptanalyzer = Quipster(
        corpus,
        args.num_trials,
        args.num_swaps,
    )
    key = cryptanalyzer.fit(cipher)
    plaintext = cryptanalyzer.decode(ciphertext)
    
    print("\nCiphertext:\n")
    pprint(cipher)

    print("\nPlaintext:\n")
    pprint(plaintext)

    print('\nKey:\n')
    pprint(key)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--cipher_path", type=str, default=None, help="Path to file containing ciphertext")
    parser.add_argument("--num_trials", type=int, help="Number of trials to execute")
    parser.add_argument("--num_swaps", type=int, help="Number of swaps to perform per trial")
    args = parser.parse_args()
    main(args)
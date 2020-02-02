import string
import random
from pprint import pprint


def transform(text, key, vocabulary):
    """ Transform text given some key and vocabulary mapping """
    mapping = str.maketrans("".join(key), "".join(vocabulary))
    return text.translate(mapping)

def swap(key, n):
    """ Randomly swap 2 letters of key """
    new_key = key.copy()
    for k in range(n):
        i, j = random.sample(range(len(new_key)), 2)
        new_key[i], new_key[j] = new_key[j], new_key[i]
    return new_key

def preprocess(raw, vocab=None):
    """ Preprocess cipher to alphabetic chars """
    processed = raw.lower()
    processed = processed.replace(" ", "")

    if vocab is not None:
        processed = "".join([c for c in processed if c in "".join(vocab)])
    else:
        processed = "".join([c for c in processed if c.isalpha()])
    
    return processed

def load_file(file_path):
    """ Read a text file """
    with open(file_path, 'r') as f:
        raw = f.read().strip()

    return raw

def generate_cipher(text, vocabulary=string.ascii_lowercase):
    key = list(vocabulary).copy()
    random.shuffle(key)
    text = text.lower()
    cipher = transform(text, key, vocabulary)
    return cipher

def user_interaction(cryptanalyzer, cipher):
    """
    Interface for user interaction in assisting
    in correcting the key produced by the algorithm
    """

    while True:
        decrypted = cryptanalyzer.decode(cipher)
        print_stdout(cipher, decrypted, cryptanalyzer.key, cryptanalyzer.vocabulary)

        char_incorrect = input('Which character from the decryption is incorrect? ').lower()
        char_suggested = input('Which character should it be replaced with? ').lower()

        print('Changing {} -> {}'.format(char_incorrect, char_suggested))
        cryptanalyzer.key = replace(cryptanalyzer.key, cryptanalyzer.vocabulary, char_incorrect, char_suggested)

        decrypted = cryptanalyzer.decode(cipher)
        print_stdout(cipher, decrypted, cryptanalyzer.key, cryptanalyzer.vocabulary)
        done = input('Is this sufficient? (y/n) ').lower()

        if done == 'y':
            break

    return cryptanalyzer

def replace(key, vocab, char_incorrect, char_suggested):
    """ Lookup char in key and replace with suggested char """
    idx = vocab.index(char_incorrect)
    key_incorrect = key[idx]
    idx_replaced = vocab.index(char_suggested)
    key_suggested = key[idx_replaced]
    key[idx] = key_suggested
    key[idx_replaced] = key_incorrect
    return key

def print_stdout(cipher, decrypted, key, vocab):
    print("\nCiphertext:\n")
    pprint(cipher)
    print("\nDecrypted:\n")
    pprint(decrypted)

    key_mapping = {k: v for k, v in zip(vocab, key)}
    print('\nKey:\n')
    pprint(key_mapping)
import argparse
from pprint import pprint

import utils
from quipster import Quipster


def main(args):
    
    if args.ciphertext_path is not None:
        cipher = utils.load_file(args.ciphertext_path)
        plaintext = 'Plaintext not provided'

    elif args.plaintext_path is not None:
        plaintext = utils.load_file(args.plaintext_path)
        cipher = utils.generate_cipher(plaintext)
        
    else:
        raise Exception('Must specify either --ciphertext_path or --plaintext_path')

    # Instantiate and fit the Quipster substitution cipher solver
    cryptanalyzer = Quipster(
        args.num_trials,
        args.num_swaps,
        args.converge_swaps
    )
    key = cryptanalyzer.fit(cipher)
    decrypted = cryptanalyzer.decode(cipher)

    print("\nPlaintext:\n")
    pprint(plaintext)
    
    utils.print_stdout(cipher, decrypted, key, cryptanalyzer.vocabulary)

    help_the_algorithm = input('\nWould you like to manually help the algorithm? (y/n) ').lower()

    if help_the_algorithm == 'y':
        cryptanalyzer = utils.user_interaction(cryptanalyzer, cipher)
    
    decrypted = cryptanalyzer.decode(cipher)
    utils.print_stdout(cipher, decrypted, cryptanalyzer.key, cryptanalyzer.vocabulary)
    
    print("Saving plaintext to {}".format(args.output))
    with open(args.output, 'w') as f:
        f.write(decrypted)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ciphertext_path", type=str, default=None, help="Path to file containing ciphertext")
    parser.add_argument("--plaintext_path", type=str, default=None, help="Path to file containing ciphertext")
    parser.add_argument("--output", type=str, default='plaintext.txt', help="Path to output plaintext file")
    parser.add_argument("--num_trials", type=int, default=15, help="Number of trials to execute")
    parser.add_argument("--num_swaps", type=int, default=10**4, help="Number of swaps to perform per trial")
    parser.add_argument("--converge_swaps", type=int, default=2, help="Number of characters swapped in key each iteration when convergence has occurred")
    args = parser.parse_args()
    main(args)
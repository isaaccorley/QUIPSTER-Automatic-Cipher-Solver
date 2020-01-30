import string
import random
import math
import nltk



class Quipster(object):

    def __init__(
        self,
        puzzle,
        num_trials,
        num_swaps,
    ):

    # Input parameters
    self.ciphertext = ciphertext
    self.num_trials = num_trials
    self.num_swaps = num_swaps

    # Create vocabulary
    self.distinguished_symbols = ["$", "'"]
    self.d_symbol_end = "'"
    self.vocabulary = list(string.ascii_lowercase) + self.distinguished_symbols
    
    # Initialize parameters
    self.best_score = -math.inf
    self.best_trial_score = -math.inf
    self.best_key = None


    def preprocess(self, ciphertext):
        output = ciphertext.copy()
        output = output.lower()
        return output

    def score(self, x):
        pass

    @staticmethod
    def swap(key):
        """ Randomly swap 2 letters of key """
        new_key = key.copy()
        i, j = random.sample(range(len(new_key)), 2)
        new_key[i], new_key[j] = new_key[j], new_key[i]
        return new_key


    def search(self):
        pass


    def trial(self):
        """ Run a single trial """
        pass


    def transform(self, key):
        return self.puzzle.translate(stringmaketrans("".join(key), string.ascii_lowercase))
        

    def decode(self):
        """ Main decoding loop ""
        best_score = 0
        for
        pass
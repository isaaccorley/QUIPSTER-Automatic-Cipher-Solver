import string
import random
import math
import nltk
from tqdm import tqdm

from data import preprocess, transform


class Quipster(object):

    def __init__(
        self,
        corpus,
        num_trials=15,
        num_swaps=10**4,
    ):

    # Input parameters
    self.corpus = corpus
    self.num_trials = num_trials
    self.num_swaps = num_swaps

    self.vocabulary = list(string.ascii_uppercase)
    self.key = self.vocabulary.copy()

    @staticmethod
    def swap(key):
        """ Randomly swap 2 letters of key """
        i, j = random.sample(range(len(key)), 2)
        new_key = key.copy()
        new_key[i], new_key[j] = new_key[j], new_key[i]
        return new_key

    def score(self, candidate, cipher):
        """ Compute metric score w.r.t cipher and candidate text """
        score = nltk.translate.bleu_score.sentence_bleu(
            cipher,
            candidate,
            weights=(0.33, 0.33, 0.33, 0)
        )
        return score

    def fit(self, cipher):
        """ Main decoding loop """
        cipher = preprocess(cipher)

        best_score = -math.inf
        for i in range(self.num_trials):
            print('Trial {}/{}'.format(i, self.num_trials))

            # Initialize trial key as randomly shuffled vocabulary
            key = self.vocabulary.copy()
            random.shuffle(key)

            best_trial_score = -math.inf
            for j in tqdm(range(self.num_swaps)):
                # Perform random swap
                new_key = self.swap(key)

                # Decode cipher using key
                candidate = transform(new_key, cipher, self.vocabulary)

                # Calculate score
                score = self.score(candidate, cipher)

                if score > best_trial_score:
                    key = new_key
                    best_trial_score = score

            if best_trial_score > best_score:
                self.key = key.copy()
                best_score = best_trial_score


    def decode(self, cipher):
        """ Transform cipher text given the fitted model """
        cipher = preprocess(cipher)
        plaintext = transform(self.key, cipherl self.vocabulary)
        return plaintext
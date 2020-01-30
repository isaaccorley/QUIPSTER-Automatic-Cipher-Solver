import os
import urllib
import string
import nltk


GREAT_EXPECTATIONS_URL = "https://raw.githubusercontent.com/skeeto/markov-text/master/data/great-expectations.txt"


def download_corpus(url, path):
    """ Download text from url and save to file path """
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        raw = urllib.request.urlopen(url).read()

        with open(path, 'w') as f:
            f.write(raw)

def read_corpus():
    path = './data/great-expectations.txt'
    download_text(GREAT_EXPECTATIONS_URL, path)

    with open(path, 'r') as f:
        raw = f.read()

    return raw

def preprocess(text):
    processed = text.copy()
    processed = processed.upper()
    processed = processed.replace(" ", "")
    processed = "".join([c for c in processed if c.isalpha()])
    return processed

def preprocess_corpus(raw)
    """ Preprocess the raw corpus text """
    tokens = nltk.tokenize.word_tokenize(raw)
    
    # Filter non-alphabetic words
    words = [word for word in tokens if word.isalpha()]
    chars = "".join(words)

    # Filter non-alphabetic chars
    corpus = preprocess(chars)
    return corpus

def transform(key, text, vocabulary):
    """ Transform ciphertext given some key and vocabulary mapping """
    return text.translate(string.maketrans("".join(key), "".join(vocabulary)))

def load_great_expectations(n):
    """ Load and preprocess great expectations """
    raw = load_txt()
    corpus = preprocess_corpus(raw)
    return corpus



import random

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

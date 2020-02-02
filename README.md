# QUIPSTER-Automatic-Cipher-Solver
Implementation of the QUIPSTER Substitution Cipher Solving Algorithm from ["Solving Substitution Ciphers" - Hasinoff (2003)](https://people.csail.mit.edu/hasinoff/pubs/hasinoff-quipster-2003.pdf)

Some modifications have been made to the original algorithm and a different dictionary is utilized for assessing the N-gram based scoring metric.

The most notably difficult part about this cryptoalgorithm (and language based cryptoalgorithms in general) is that it easily falls into a local minima and never escapes due to:
- Only swapping 2 characters in the key on every iteration
- Using a scoring metric which can be biased based on your corpus
- Using a corpus which has notably different distributions of language than the plaintext (Even if from the same language)

Therefore to assist in unlocking the perfect mapping of the key, a CLI user interface is added to allow the user to manually make updates to the key based on their own knowledge and viewing the ciphertext compared to the decrypted plaintext.

## Break a ciphertext
```
python main.py \
    --ciphertext_path data/ciphertexts/ciphertext2.txt \
    --output plaintext.txt \
    --num_trials 500 \
    --num_swaps 1000 \
    --converge_swaps 5
```

## Generating a random ciphertext from a plaintext and break it
```
python main.py \
    --plaintext_path data/plaintexts/plaintext0.txt \
    --output plaintext.txt \
    --num_trials 500 \
    --num_swaps 1000 \
    --converge_swaps 5
```
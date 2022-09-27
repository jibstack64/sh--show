# import required libraries
import random
import string
import json
import sys

# get alphabet with json
with open("alphabet.json" if len(sys.argv) == 1 else sys.argv[1], "r") as f:
    alphabet = json.load(f)
    alphabet = {v: k for k, v in alphabet.items()} # add flipped alphabet
    alphabet.update({k[::-1]: v for k, v in alphabet.items()}) # add alphabet with flipped keys

# take input encoded string and split it
to_decode = input(":")
to_decode = [to_decode[y-5:y] for y in range(5, len(to_decode)+5,5)]

# decode string with the alphabet
decoded = ""
for c in to_decode:
    if c not in alphabet.keys():
        continue
    decoded += alphabet[c]

# print the output
print(decoded)

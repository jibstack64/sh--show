# import required libraries
import random
import string
import json
import sys

# get alphabet with json
with open("alphabet.json" if len(sys.argv) == 1 else sys.argv[1], "r") as f:
    alphabet = json.load(f)

# take input string
to_encode = input(":")

# encode the provided string with the loaded alphabet
encoded = ""
for c in to_encode.lower():
    if c not in alphabet.keys():
        continue
    encoded += random.choice([alphabet[c], alphabet[c][::-1]])

# print the output
print(encoded)

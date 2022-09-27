# import required libraries
import random
import string
import json
import sys

# characters to be used to generate the encrypted characters
characters = string.ascii_letters + "$!@_%^*&()"

# generate new alphabet
alphabet = {}
for a in string.ascii_lowercase + " ":
    def gen():
        alphabet[a] = ''.join([random.choice(characters) for x in range(5)])
        if alphabet[a] in list(alphabet.values())[:-1] or alphabet[a][::-1] in list(alphabet.values())[:-1]:
            gen()
    gen()

# write to json
with open("alphabet.json" if len(sys.argv) == 1 else sys.argv[1], "w") as f:
    print(f"{alphabet}\nwritten to {f.name}.")
    json.dump(alphabet, f, indent=4)

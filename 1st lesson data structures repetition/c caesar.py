alphabet = input()
s = int(input()) % len(alphabet)
enc = alphabet[s:] + alphabet[:s]
dec = alphabet[-s:] + alphabet[:-s]
print(enc)
print(alphabet)
print(dec)

import re

text = ""
while True:
    try:
        line = input()
        text += line + " "
    except EOFError:
        break

text = text.lower()
declarative = set()
interrogative = set()
exclamatory = set()

sentences = re.split(r'[.?!]', text)
for sentence in sentences:
    words = set(re.findall(r'\b\w+\b', sentence))
    if sentence.endswith('.'):
        declarative.update(words)
    elif sentence.endswith('?'):
        interrogative.update(words)
    elif sentence.endswith('!'):
        exclamatory.update(words)

result = sorted(list(declarative.intersection(interrogative) - exclamatory))
print(' '.join(result))

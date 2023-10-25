transliteration_table = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "’",
    "б": "b", "ю": "ju", "ё": "jo"
}

with open('cyrillic.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()
transliterated_text = ""
for char in text:
    if char.lower() in transliteration_table:
        if char.isupper():
            transliterated_text += transliteration_table[char.lower()].capitalize()
        else:
            transliterated_text += transliteration_table[char.lower()]
    else:
        transliterated_text += char
with open('transliteration.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(transliterated_text)

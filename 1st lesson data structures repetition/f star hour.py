def check_word(word, valid_word):
    lt = list(valid_word)
    word_letters = list(word)
    for letter in word_letters:
        if letter in lt:
            lt.remove(letter)
        else:
            return False
    return True


valid_word = input().strip()

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    lst = []
    for line in input_file:
        word = line.strip()
        lst.append(word)

    valid_words = []
    for word in lst:
        if check_word(word, valid_word):
            valid_words.append(word)

    output_file.write(str(len(valid_words)) + '\n')
    for word in valid_words:
        output_file.write(word + '\n')

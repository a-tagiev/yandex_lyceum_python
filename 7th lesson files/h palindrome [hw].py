def palindrome():
    with open('input.dat', 'rb') as file:
        data = file.read()
    if data == data[::-1]:
        return True
    else:
        return False
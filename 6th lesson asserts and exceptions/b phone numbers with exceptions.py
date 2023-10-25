class PhoneNumberError(Exception):
    pass


def check_phone_number(numb):
    try:
        cleaned_str = ''.join(filter(str.isdigit, numb))
        if cleaned_str.startswith('7'):
            cleaned_str = '+' + cleaned_str
        elif cleaned_str.startswith('8'):
            cleaned_str = '+7' + cleaned_str[1:]
        else:
            raise PhoneNumberError
        open_brackets = numb.count('(')
        close_brackets = numb.count(')')
        if open_brackets != close_brackets or open_brackets > 1 or close_brackets > 1:
            raise PhoneNumberError
        if open_brackets == 1 and numb.index('(') > numb.index(')'):
            raise PhoneNumberError
        for i in range(len(numb) - 1):
            if numb[i] == '-':
                if numb[i + 1] == '-':
                    raise PhoneNumberError
        if numb.rstrip(' ')[-1] == '-':
            raise PhoneNumberError
        if len(cleaned_str) == 12:
            return cleaned_str
        raise PhoneNumberError
    except PhoneNumberError as e:
        return 'error'


print(check_phone_number(input()))

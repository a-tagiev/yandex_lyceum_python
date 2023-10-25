class PhoneNumberError(Exception):
    pass


def check_phone_number(numb):
    try:
        cleaned_str = ''.join(filter(str.isdigit, numb))
        if numb.startswith('7'):
            raise PhoneNumberError("неверный формат")
        if cleaned_str.startswith('7'):
            cleaned_str = '+' + cleaned_str
        elif cleaned_str.startswith('8'):
            cleaned_str = '+7' + cleaned_str[1:]
        else:
            raise PhoneNumberError("неверный формат")
        open_brackets = numb.count('(')
        close_brackets = numb.count(')')
        if open_brackets != close_brackets or open_brackets > 1 or close_brackets > 1:
            raise PhoneNumberError("неверный формат")
        if open_brackets == 1 and numb.index('(') > numb.index(')'):
            raise PhoneNumberError("неверный формат")
        for i in range(len(numb) - 1):
            if numb[i] == '-':
                if numb[i + 1] == '-':
                    raise PhoneNumberError("неверный формат")
        if numb.rstrip(' ')[-1] == '-':
            raise PhoneNumberError("неверный формат")
        if len(cleaned_str) != 12:
            raise PhoneNumberError('неверное количество цифр')

        else:
            return cleaned_str
    except PhoneNumberError as e:
        return str(e)


def get_operator(numb):
    cleaned_str = ''.join(filter(str.isdigit, numb))
    if cleaned_str.startswith('7'):
        cleaned_str = '+' + cleaned_str
    elif cleaned_str.startswith('8'):
        cleaned_str = '+7' + cleaned_str[1:]
    op = cleaned_str[2:5]
    if op:
        operator_code = int(op)
        if (910 <= operator_code <= 919) or (980 <= operator_code <= 989):
            pass
        elif 920 <= operator_code <= 939:
            pass
        elif (902 <= operator_code <= 906) or (960 <= operator_code <= 969):
            pass

        else:
            return 'не определяется оператор сотовой связи'


a = input()

if not check_phone_number(a):
    print(check_phone_number(a))

else:
    if get_operator(a) == 'не определяется оператор сотовой связи':
        print('не определяется оператор сотовой связи')
    else:
        print(check_phone_number(a))

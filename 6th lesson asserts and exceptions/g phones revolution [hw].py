import re


def validate_phone_number(phone_number):
    if not re.match(r'^[0-9+\s\-()]+$', phone_number):
        return "неверный формат"
    digits_only = re.sub(r'\D', '', phone_number)
    if len(digits_only) != 11:
        return "неверное количество цифр"
    country_codes = ['+7', '+359', '+55', '+1']
    if not any(digits_only.startswith(code) for code in country_codes):
        return "не определяется код страны"
    return f"+{digits_only[:1]} ({digits_only[1:4]}) {digits_only[4:7]}-{digits_only[7:9]}-{digits_only[9:11]}"

def is_good_password(password):
    if len(password) <= 8:
        return "error"
    if not (any(char.isupper() for char in password) and any(char.islower() for char in password)):
        return "error"
    if not any(char.isdigit() for char in password):
        return "error"
    forbidden_combinations = ["QWE", "WERT", "ERTY", "RTYU", "TYUI", "YUIO", "UIOP",
                              "ASD", "SDFG", "DFGH", "FGHJ", "GHJK", "HJKL",
                              "ZXC", "XCVB", "CVBN", "VBNM",
                              "ЙЦУ", "ЦУК", "УКЕ", "КЕН", "ЕНГ", "НГШ", "ГШЩ", "ШЩЗ", "ЩЗХ", "ЗХЪ",
                              "ФЫВ", "ЫВА", "ВАП", "АПР", "ПРО", "РОЛ", "ОЛД", "ЛДЖ", "ДЖЭ", "ЖЭЁ",
                              "ЯЧС", "ЧСМ", "СМИ", "МИТ", "ИТЬ", "ТЬБ", "ЬБЮ"]

    for combination in forbidden_combinations:
        if combination in password.upper():
            return "error"

    return "ok"


password = input()
result = is_good_password(password)
print(result)

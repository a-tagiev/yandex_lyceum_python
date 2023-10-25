rules = {
    "камень": ["ром", "ножницы"],
    "ром": ["пират", "бумага"],
    "пират": ["ножницы", "камень"],
    "ножницы": ["бумага", "ром"],
    "бумага": ["камень", "пират"],
}

pirate1 = input().strip()
pirate2 = input().strip()


def determine_winner(p1, p2):
    if p1 == p2:
        return "ничья"
    elif p2 in rules[p1]:
        return "первый"
    return "второй"


result = determine_winner(pirate1, pirate2)
print(result)

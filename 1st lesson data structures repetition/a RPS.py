def main(a: str, b: str) -> str:
    if a == b:
        return "ничья"
    if (a == "камень" and b == "ножницы") or (a == "ножницы" and b == "бумага") or (a == "бумага" and b == "камень"):
        return "первый"
    return "второй"

print(main(input(), input()))

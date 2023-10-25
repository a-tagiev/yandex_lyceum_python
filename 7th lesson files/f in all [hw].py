total_cost = 0.0
try:
    with open('prices.txt', 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        parts = line.split('\t')
        if len(parts) == 3:
            name, quantity, price = parts
            quantity = int(quantity)
            price = float(price)
            total_cost += quantity * price
    print("{:.2f}".format(total_cost))
except Exception as e:
    print(str(e))

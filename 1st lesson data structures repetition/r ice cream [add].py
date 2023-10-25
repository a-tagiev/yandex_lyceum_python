n = int(input())
menu = {}
for _ in range(n):
    item, price = input().split('\t')
    menu[item] = int(price)

order_number = 1
total_revenue = 0

while True:
    order = input().strip()
    if order == '.':
        break
    if '-' in order:
        continue
    if order:
        order_parts = order.split()
        item = ' '.join(order_parts[:-1])
        quantity = int(order_parts[-1])
        if item in menu:
            cost = menu[item] * quantity
            total_revenue += cost
            print(f"{order_number}) {cost}")
            order_number += 1

print("Итого:", total_revenue)

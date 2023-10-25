# Определим функции для проверки точек

def is_inside_area(x, y):
    return y > abs(x) and y < -abs(x)


# Инициализируем переменные для хранения крайних точек
leftmost = None
rightmost = None
topmost = None
bottommost = None

# Считываем количество точек
n = int(input())

# Проходим по всем точкам
for i in range(n):
    x, y = map(int, input().split())

    # Проверяем, лежит ли точка внутри заданной области
    if is_inside_area(x, y):
        print(f'({x}, {y})')

    # Обновляем крайние точки
    if leftmost is None or x < leftmost[0]:
        leftmost = (x, y)
    if rightmost is None or x > rightmost[0]:
        rightmost = (x, y)
    if topmost is None or y > topmost[1]:
        topmost = (x, y)
    if bottommost is None or y < bottommost[1]:
        bottommost = (x, y)

# Выводим крайние точки
print(f'left: ({leftmost[0]}, {leftmost[1]})')
print(f'right: ({rightmost[0]}, {rightmost[1]})')
print(f'top: ({topmost[0]}, {topmost[1]})')
print(f'bottom: ({bottommost[0]}, {bottommost[1]})')

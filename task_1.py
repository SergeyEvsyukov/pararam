print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
k = 0

if x1 - x2 == 0:
    print('x =', x1)
elif y1 - y2 == 0:
    print('y =', y1)
else:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff
    d = 1000 + 87
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)






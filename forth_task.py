print("""
Напишіть програму, яка отримує на вхід три цілих числа, по одному числу в рядку, і виводить на 
консоль в три рядки спочатку максимальне, потім мінімальне, після чого число, що залишилося (без 
оператора if, функцій max, min)
""")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

maxx = (a >= b) * a + (b > a) * b
maxx = (maxx >= c) * maxx + (c > maxx) * c

minn = (a <= b) * a + (b < a) * b
minn = (minn <= c) * minn + (c < minn) * c

rest_of_number = (a + b + c) - maxx - minn

print(f"Найбільше: {maxx}")
print(f"Найменше: {minn}")
print(f"Інше число: {rest_of_number}")

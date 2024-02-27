print("""
Взуттєва фабрика має намір розпочати випуск елітної моделі черевиків. Дірочки для шнурівки будуть
розташовані в два ряди, відстань між рядами дорівнює a, а відстань між дірочками в ряді b. Кількість дірочок у 
кожному ряду дорівнює N. Шнурівка повинна відбуватися елітним способом "наверх, по горизонталі в інший
ряд, нагору, по горизонталі і т.д." (Див. малюнок). Крім того, щоб шнурки можна було зав'язати елітним
бантиком, довжина вільного кінця шнурка має бути l. Якою має бути довжина шнурка для цих
черевиків?Програма отримує на вхід чотири натуральні числа a, b, l і N - саме в такому порядку - і повинна 
вивести одне число - довжину шнурка.
""")
a = int(input("Введіть відстань між рядками дірок: "))
b = int(input("введіть відстань між дірками в рядку: "))
L = int(input("Введіть довжину вільного кінця шнурка: "))
N = int(input("Введіть кількість дірок в кожному рядку: "))
d = L * 2 + (2 * N - 1) * a + b * (N - 1)
print(f"Довжина шнурка: {d}")
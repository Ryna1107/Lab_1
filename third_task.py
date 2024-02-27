print("""
У школі вирішили набрати три нові математичні класи. Оскільки заняття з математики вони 
проходять одночасно, було вирішено виділити кабінет кожному класу і купити в них нові парти.
За кожною партою може сидіти не більше двох учнів. Відомо кількість учнів у кожному із трьох класів. 
Скільки всього потрібно закупити парт, щоб їх вистачило на всіх учнів? 
Програма отримує на вхід три натуральні числа: кількість учнів у кожному з трьох класів.
""")
fisrt_class = int(input("Введіть кількість учнів у прешому класі: "))
second_class = int(input("Введіть кількість учнів у другому класі: "))
third_class = int(input("Введіть кількість учнів у третьому класі: "))

desk_first_class = fisrt_class // 2
rest_desk_first_class = fisrt_class % 2

desk_second_class = second_class // 2
rest_desk_second_class = second_class % 2

desk_third_class = third_class // 2
rest_desk_third_class = third_class % 2

amount_of_desk = desk_first_class+desk_second_class+desk_third_class

suma_of_rest = rest_desk_third_class+rest_desk_second_class+rest_desk_first_class
if suma_of_rest > 0:
    if suma_of_rest == 1:
        amount_of_desk += 1
    else:
        amount_desk_add = suma_of_rest // 2
        amount_of_desk += amount_desk_add

print(f"Кількість парт для всіх учнів: {amount_of_desk}")

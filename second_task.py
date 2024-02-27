print("""
Катя дізналася, що їй для сну треба ХХ хвилин. 
На відміну від Колі, Катя лягає спати після півночі в HH годин і MM хвилин.
Допоможіть Каті визначити, на який час їй поставити будильник, 
щоб він продзвенів рівно через XX хвилин після того,
як вона ляже спати.На стандартне введення, кожне у  своєму рядку, 
подаються значення XX, HH та MM. Гарантується, що Катя повинна прокинутися того ж 
дня, що заснути. Програма повинна виводити час, на який потрібно поставити будильник: 
у першому рядку - годинник, у другому - хвилини.
""")
xx = int(input("Введіть кількість хвилин , яка потрібна для сну: "))
hh = int(input("Введіть о котрій лягає Катя в годинах: "))
mm = int(input("Введіть о котрій лягає Катя в хвилинах: "))

hours_for_sleep = xx // 60
rest_of_sleep = xx % 60
suma_0f_minutes = rest_of_sleep + mm

if suma_0f_minutes > 60:
    rest_of_minutes = suma_0f_minutes - 60
    result_hour = hh + hours_for_sleep + 1
    print(f"Потрібно поставити будильник на {result_hour} : {rest_of_minutes}")
elif suma_0f_minutes == 60:
    rest_of_minutes = suma_0f_minutes - 60
    result_hour = hh + hours_for_sleep + 1
    print(f"Потрібно поставити будильник на {result_hour} : {rest_of_minutes}0")
else:
    result_hour = hh + hours_for_sleep
    print(f"Потрібно поставити будильник на {result_hour} : {suma_0f_minutes}")

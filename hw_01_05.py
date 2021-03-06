# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

while True:
    try:
        a = int(input('Введите сумму Вашей выручки: '))
        b = int(input('Введите сумму Ваших издержек: '))
    except ValueError:
        print('Вы ввели не число')
    else:
        if a < b:
            print(f'Вы работаете в убыток ({a - b})')
        else:
            print('Вы в плюсе')
            print(f'Рентабельность составляет: {a / b:.2f}')

        while True:
            try:
                c = int(input('Введите количество сотрудников: '))
                if c <= 0:
                    raise ValueError
            except ValueError:
                print('Вы ввели некорретные данные')
            else:
                print(f'Прибыль фирмы на человека: {a / c:.2f}')
                break
        break

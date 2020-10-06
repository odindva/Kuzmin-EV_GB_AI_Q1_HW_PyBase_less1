# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    try:
        n = int(input('Введите целое положительное число: '))
        if n < 0:
            raise ValueError
    except ValueError:
        print('Вы ввели не целое положительное число')
    else:
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        print(max(nums))
        break

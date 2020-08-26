# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def form(i):
    if i == 0:
        return '00'
    elif i < 10:
        return '0' + str(i)
    else:
        return i


user_second = int(input('Введите время в секундах: '))
ss = user_second % 60
hh = user_second // 3600
user_second -= hh * 3600
mm = user_second // 60
ss = user_second % 60

print(f'{form(hh)}:{form(mm)}:{form(ss)}')

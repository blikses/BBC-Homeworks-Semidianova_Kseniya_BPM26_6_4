def calc(a, c, b):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        if b != 0:
            return a / b
        else:
            return 'Ошибка. Делить на 0 нельзя'
    elif c == '//':
        if b != 0:
            return a // b
        else:
            return 'Ошибка. Делить на 0 нельзя'
    elif c == '*':
        return a * b
    elif c == '^' or c == '**':
        return a ** b
    elif c == '%':
        return a % b
    else:
        return 'Ошибка. Знак не распознан'


print('Введите "стоп", чтобы остановить калькулятор')
print('Используйте пробел между числами и знаком')

while True:
    vvod = input()
    if len(vvod.split()) == 3:
        a, c, b = vvod.split()
    elif vvod == 'стоп':
        break
    else:
        print("Ошибка. Пожалуйста, вводите корректные выражения с числами")
        continue
    res = calc(float(a), c, float(b))
    print(res)

def summa(a, b):
    return a + b
def razn(a, b):
    return a - b
def deln(a, b):
    if b != 0:
        return a / b
    else:
        return 'Ошибка. Делить на 0 нельзя'
def prodd(a, b):
    return a * b


a, c, b = map(str, input().split())
a = float(a)
b = float(b)


if c == '+':
    print(summa(a, b))
elif c == '/':
    print(deln(a, b))
elif c == '*':
    print(prodd(a, b))
elif c == '-':
    print(razn(a, b))

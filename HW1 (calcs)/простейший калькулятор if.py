a = int(input())
c = input()
b = int(input())

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('Ошибка. Делить на 0 нельзя')


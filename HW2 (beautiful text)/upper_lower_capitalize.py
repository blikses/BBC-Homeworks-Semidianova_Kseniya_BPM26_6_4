print('1 - преобразовать регистр')
print('2 - поиск слова "круто", замена слова "круто" и счет букв "о"')
print('3 - split и join')
print('4 - проверка и обрезка строки')
print('5 - привести строку в нормальный вид')
print('10 - выйти из программы')


while True:
    print('Выберите уровень:')
    level = input()
    if level.isdecimal() and 1 <= int(level) <= 5 or int(level) == 10:
        if int(level) == 1:
            print('Введите строку, которую Вы хотите преобразовать')
            a = input()
            print('Выберите способ преобразования:')
            print('1 - в верхний регистр, 2 - в нижний, 3 - все, кроме первой буквы в нижний')
            c = input()
            if c.isdecimal() and 1 <= int(c) <= 3:
                if int(c) == 1:
                    print(a.upper())
                elif int(c) == 2:
                    print(a.lower())
                elif int(c) == 3:
                    print(a.capitalize())
            else:
                print('Ошибка! Нужно ввести целое число от 1 до 3')
        elif int(level) == 2:
            print('Введите строку, с которой хотите начать работу')
            a = input()
            print('Выберите действие:')
            print('1 - найти каким по счету идет слово "круто"')
            print('2 - заменить "круто" на любое слово')
            print('3 - посчитать буквы "о"')
            c2 = input()
            if c2.isdecimal() and 1 <= int(c2) <= 3:
                if int(c2) == 1:
                    print(a.find('круто'))
                elif int(c2) == 2:
                    print('Введите слово, на которое нужно заменить слово "круто"')
                    word = input()
                    a = a.replace('круто', word)
                    print(a)
                elif int(c2) == 3:
                    print(a.count('о'))
            else:
                print('Ошибка! Нужно ввести целое число от 1 до 3')
        elif int(level) == 3:
            print('Введите строку, которую Вы хотите "распилить" или "соединить":)')
            a = input()
            print('Выберите действие:')
            print('1 - только пилим, 2 - пилим и соединяем')
            c3 = input()
            if c3.isdecimal() and 1 <= int(c3) <= 2:
                if int(c3) == 1:
                    print('Введите символ, который является разделителем:')
                    symb = input()
                    spisok = a.split(symb)
                    print(spisok)
                elif int(c3) == 2:
                    print('Введите символ, который является разделителем сейчас:')
                    symb = input()
                    a = a.split(symb)
                    print('Введите новый разделитель')
                    symb2 = input()
                    a = symb2.join(a)
                    print(a)
            else:
                print('Ошибка! Нужно ввести целое число от 1 до 2')
        elif int(level) == 4:
            print('Введите строку')
            a = input()
            print('Выберите действие:')
            print('1 - проверить, является ли строка числом или строкой')
            print('2 - откинуть часть строки')
            c4 = input()
            if c4.isdecimal() and 1 <= int(c4) <= 4:
                if int(c4) == 1:
                    if a.isdigit():
                        print('Строка является числом')
                    elif a.isalpha():
                        print('Строка является словом')
                    else:
                        print('Строка смешанного типа')
                elif int(c4) == 2:
                    print('Введите количество символов, которые нужно откинуть слева:')
                    left = input()
                    print('Введите количество символов, которые нужно откинуть справа:')
                    right = input()
                    if left.isdecimal() and right.isdecimal():
                        left = int(left)
                        right = int(right)
                        if right == 0:
                            print(a[left:])
                        else:
                            print(a[left:-right])
                    else:
                        print('Ошибка! Нужно ввести целые числа')
            else:
                print('Ошибка! Нужно ввести целое число от 1 до 2')
        elif int(level) == 5:
            print('Введите строку, которую нужно привести в нормальный вид:')
            a = input()
            a = a.strip().lower()
            while '  ' in a:
                a = a.replace('  ', ' ')
            a = a.capitalize()
            if 'круто' in a:
                a = a.replace('круто', 'отлично')
            words = a.split(' ')
            a = ' '.join(words)
            print('Нормализованная строка:', a)
        if int(level) == 10:
            break
    else:
        print('Ошибка! Введите целое число от 1 до 5')


class Heel:
    def heel(self, a, b, c):
        if a == 1:
            res = round((b / c - 1.61) * 10, 2)
        elif a == 2:
            res = round((b / c - 1.4) * 10, 2)
        elif a == 3:
            res = round((b / c - 1.2) * 10, 2)
        if res > 0:
            return res
        else:
            return 'Перепроверьте данные. Ваши параметры не позволяют рассчитать высоту верно'

    def main(self):
        print('1 - ортопедически идеальная высота каблука')
        print('2 - каблук средней высоты')
        print('3 - высокий каблук')
        print('4 - закончить работу программы')

        while True:
            print('Выберите вариант, который хотите подобрать')
            a = input()
            if a.isdecimal():
                a = int(a)
            if a == 4:
                break
            elif a == 3 or a == 2 or a == 1:
                while True:
                    print('Введите Ваши рост и длину ног через пробел (используйте целые числа)')
                    vvod = input()
                    if len(vvod.split()) == 2:
                        if vvod.split()[0].isdecimal() and vvod.split()[1].isdecimal():
                            b, c = map(float, vvod.split())
                            res = self.heel(a, b, c)
                            print(res)
                            break
                        else:
                            print('Введите данные в правильном формате. Только целые числа через пробел!')
                            continue
                    else:
                        print('Введите данные в правильном формате. Только целые числа через пробел!')
                        continue
            else:
                print('Ошибка! Введите целое число от 1 до 4!')
                continue


if __name__ == '__main__':
    Heel().main()
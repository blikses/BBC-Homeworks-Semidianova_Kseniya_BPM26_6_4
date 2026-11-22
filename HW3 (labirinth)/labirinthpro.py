from random import *


def minigame_key(lives):
    print("ИСПЫТАНИЕ КЛЮЧА")
    print("Реши пример, чтобы забрать ключ. Ошибка — минус жизнь и новый пример!")
    while lives > 0:
        a, b = randint(20, 50), randint(1, 20)
        op = choice(['+', '-'])
        if op == '+':
            correct = a + b
        else:
            correct = abs(a - b)
        try:
            ans = int(input(f"Сколько будет {a} {op} {b}? Твой ответ: "))
        except ValueError:
            print("Ошибка. Это даже не число.")
            lives -= 1
            print(f"Минус жизнь. Осталось: {lives}")
            if lives <= 0:
                return False, lives
            print("Новый пример!")
            continue
        if ans == correct:
            print("Верно! Ключ твой!")
            return True, lives
        else:
            lives -= 1
            print(f"Ошибка. Правильный ответ {correct}. Осталось: {lives} жизней")
            if lives <= 0:
                return False, lives
            print("Новый пример!")
    return False, lives


def minigame_treasure():
    print("КЛАД")
    print("Ты нашёл настоящий клад! В награду +1 жизнь!")
    return True


def minigame_portal():
    print("ПОРТАЛ ОТКРЫЛСЯ!")
    print("В одной из клеток спрятан подарок с +1 жизнью.")
    print()
    print("  1 2 3")
    for i in range(1, 4):
        print(f"{i} . . .")

    gift_x, gift_y = randint(1, 3), randint(1, 3)

    try:
        r = int(input("Выбери строку (1-3): "))
        c = int(input("Выбери столбец (1-3): "))
    except ValueError:
        print("Неверный ввод! Подарок исчезает... Возвращайся попробовать снова!")
        return False
    if not (1 <= r <= 3 and 1 <= c <= 3):
        print("Ты промахнулся мимо поля! Возвращайся попробовать снова!")
        return False
    if r == gift_x and c == gift_y:
        print(f"Угадал! Подарок был в клетке ({gift_x}, {gift_y}). +1 жизнь!")
        return True
    else:
        print(f"Увы, подарок был в клетке ({gift_x}, {gift_y}). Возвращайся, попробуй снова!")
        return False


def minigame_monster():
    print("💀 МОНСТР")
    print("Монстр предлагает сыграть в камень-ножницы-бумага!")
    print("3 раунда. Побеждаешь большинство — монстр убегает. Проиграл — минус жизнь.")
    moves = {'к': 'камень', 'н': 'ножницы', 'б': 'бумага'}
    beats = {'к': 'н', 'н': 'б', 'б': 'к'}
    p_wins, m_wins = 0, 0
    for round_num in range(1, 4):
        print(f"Раунд {round_num}")
        p = input("Твой ход (к - камень, н - ножницы, б - бумага): ").strip().lower()
        if p not in moves:
            print("Неверный ход! Раунд за монстром.")
            m_wins += 1
            continue
        m = choice(['к', 'н', 'б'])
        print(f"Монстр показал: {moves[m]}")
        if p == m:
            print("Ничья!")
        elif beats[p] == m:
            print("Ты выиграл раунд!")
            p_wins += 1
        else:
            print("Монстр выиграл раунд!")
            m_wins += 1

    print(f"Счёт: ты {p_wins} : {m_wins} монстр")
    if p_wins > m_wins:
        print("🏆 Ты победил монстра! Он убегает, путь свободен!")
        return True
    elif p_wins == m_wins:
        print("🤝 Ничья! Монстр отпускает тебя без потерь.")
        return True
    else:
        print("💥 Монстр одолел тебя! Минус жизнь.")
        return False


try:
    x = int(input("Введите высоту лабиринта: "))
    y = int(input("Введите ширину лабиринта: "))
except ValueError:
    print("Ошибка: нужно ввести целые числа!")
    exit()

if x * y < 6:
    print("Лабиринт слишком маленький!")
    exit()

lab = [['*'] * y for i in range(x)]
lab[x - 1][y - 1] = 'E'

available_cells = [(i, j) for i in range(x) for j in range(y)
                   if (i, j) != (0, 0) and (i, j) != (x - 1, y - 1)]

(x1, y1), (x2, y2), (x3, y3), (x4, y4) = sample(available_cells, 4)

lab[x1][y1] = 'T'
lab[x2][y2] = 'M'
lab[x3][y3] = 'K'
lab[x4][y4] = 'P'
known_lab = [['*'] * y for i in range(x)]
known_lab[0][0] = '.'
known_lab[x - 1][y - 1] = 'E'


def lab_print(lab1, robo_pos):
    rx_, ry_ = robo_pos
    for i in range(len(lab1)):
        row = []
        for j in range(len(lab1[i])):
            if (i, j) == (rx_, ry_):
                row.append('R')
            else:
                row.append(lab1[i][j])
        print(' '.join(row))
    print()


def lives_print(lives):
    print(f"Жизни ❤️: {lives}")


rx, ry = 0, 0
has_key = False
has_treasure = False
lives = 3
game_over = False

print("Управление: w - вверх, s - вниз, a - влево, d - вправо")
print(f"У тебя {lives} жизни. Береги их!")
lab_print(known_lab, (rx, ry))
lives_print(lives)

while True:
    go = input("\nХод (w/a/s/d): ").lower()

    if go not in ('w', 'a', 's', 'd'):
        print("Неверный ввод! Используйте w/a/s/d.")
        continue

    new_rx, new_ry = rx, ry
    if go == 'w':
        new_rx -= 1
    elif go == 's':
        new_rx += 1
    elif go == 'a':
        new_ry -= 1
    elif go == 'd':
        new_ry += 1

    if not (0 <= new_rx < x and 0 <= new_ry < y):
        print("Там стена! Так ходить нельзя.")
        continue

    real_cell = lab[new_rx][new_ry]

    if real_cell == 'E' and not has_key:
        print("Дверь заперта! Нужен ключ, чтобы выйти. Ищи дальше!")
        continue

    old_real = lab[rx][ry]
    if old_real in ('K', 'T', 'P', 'M', 'E'):
        known_lab[rx][ry] = old_real
    else:
        known_lab[rx][ry] = '.'

    rx, ry = new_rx, new_ry
    real_cell = lab[rx][ry]
    if real_cell in ('K', 'T', 'P', 'M', 'E'):
        known_lab[rx][ry] = real_cell
    elif known_lab[rx][ry] == '*':
        known_lab[rx][ry] = '.'

    if real_cell == 'K':
        if has_key == False:
            success, lives = minigame_key(lives)
            if not success:
                print("Жизни кончились 💔... Игра окончена.")
                game_over = True
                break
            has_key = True
            print("🔑 Теперь ты можешь выйти из лабиринта!")
        else:
            print('Ты уже забрал ключ! Пойдем дальше')

    elif real_cell == 'T':
        if has_treasure == False:
            minigame_treasure()
            lives += 1
            has_treasure = True
            print(f"Теперь у тебя {lives} жизней.")
        else:
            print('Ты уже забрал клад! Пойдем дальше')

    elif real_cell == 'P':
        if minigame_portal():
            lives += 1
            print(f"Теперь у тебя {lives} жизней.")

    elif real_cell == 'M':
        result = minigame_monster()
        if result is True:
            print("Путь свободен!")
        elif result == 'draw':
            pass
        else:
            lives -= 1
            if lives <= 0:
                print("Жизни кончились 💔... Игра окончена.")
                game_over = True
                break

    elif real_cell == 'E':
        print("🎉 Ты выбрался из лабиринта! Победа!")
        known_lab[rx][ry] = 'E'
        lab_print(known_lab, (rx, ry))
        break

    else:
        print('В этой клеточке ничего не было и не будет:) Продолжай поиски!')

    lab_print(known_lab, (rx, ry))
    lives_print(lives)

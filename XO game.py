# для игры нужен numpy

Player1 = input('Добро пожаловать в крестики-нолики!\nИгрок 1, введите ваше имя: ',)
print()
print(Player1, ', вы играете крестиками Х')
print()

Player2 = input('Игрок 2, введите ваше имя: ',)
print()
print(Player2, ', вы играете ноликами O')
print()

print('Необходимо ввести координаты в формате 01,\nгде 0 - номер строки, 1 - столбец.')
print('Игровое поле 3*3:' )

print('0 1 2')
print('      0\n      1\n      2')
print()
print(Player1, 'начинает игру.')

coordinate = input(Player1 + ': ',)
coordinate_range = ['00', '01', '02', '10', '11', '12', '20', '21', '22']

if coordinate not in coordinate_range:
    print('Введены неверные координаты')
    coordinate = input(Player1 + ': ', )
coordinate_id = list(map(int, coordinate))

used_coord = []
used_coord.append(coordinate)
coordinate = list(map(int, coordinate))

i = coordinate_id[0]  # строка
j = coordinate_id[1]  # столбец

row = 3
column = 3

matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

matrix[i][j] = 'x'

print('0 1 2')

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print(i)

# Первый Ход второго игрока

coordinate = input(Player2 + ': ', )
if coordinate not in coordinate_range:
    print('Введены неверные координаты')
    coordinate = input(Player2 + ': ', )
elif coordinate in used_coord:
    print('Такой ход уже был, введите другой')
    coordinate = input(Player2 + ': ', )

coordinate_id = list(map(int, coordinate))
used_coord.append(coordinate)

i = coordinate_id[0]  # строка
j = coordinate_id[1]  # столбец

matrix[i][j] = 'o'

print('0 1 2')

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print(i)

counter = 2

# Второй Ход первого игрока


def repeat_step():
    winner = None
    while winner is None:
        coordinate = input(Player1 + ': ', )
        if coordinate not in coordinate_range:
            print('Введены неверные координаты')
            coordinate = input(Player1 + ': ', )
        elif coordinate in used_coord:
            print('Такой ход уже был, введите другой')
            coordinate = input(Player1 + ': ', )

        coordinate_id = list(map(int, coordinate))
        used_coord.append(coordinate)

        i = coordinate_id[0]  # строка
        j = coordinate_id[1]  # столбец

        matrix[i][j] = 'x'

        print('0 1 2')

        for i in range(row):
            # global column
            for j in range(3):
                print(matrix[i][j], end=" ")
            print(i)

        # СТРОКИ для проверки результата

        row0 = matrix[0]
        row1 = matrix[1]
        row2 = matrix[2]

        # СТОЛБЦЫ для проверки результата
        import numpy as np
        column = np.array(matrix, str)
        column0 = list(map(str, column[:, 0]))
        column1 = list(map(str, column[:, 1]))
        column2 = list(map(str, column[:, 2]))

        # ДИАГОНАЛИ для проверки результата
        diagonal_left = list(map(str, [matrix[0][0], matrix[1][1], matrix[2][2]]))
        diagonal_right = list(map(str, [matrix[0][2], matrix[1][1], matrix[2][0]]))

        win_player1 = (['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ['x' 'x' 'x'], ['x' 'x' 'x'], ['x' 'x' 'x'])

        global counter
        counter += 1

        if row0 in win_player1 or row1 in win_player1 or row2 in win_player1:
            print('Победил', Player1, 'Поздравляем!')
            break
        elif column0 in win_player1 or column1 in win_player1 or column2 in win_player1:
            print('Победил', Player1, 'Поздравляем!')
            break
        elif diagonal_right in win_player1 or diagonal_left in win_player1:
            print('Победил', Player1, 'Поздравляем!')
            break
        elif counter == 9:
            print('Ходы закончились! Победила дружба!')
            break

        # Второй Ход второго игрока

        coordinate = input(Player2 + ': ', )
        if coordinate not in coordinate_range:
            print('Введены неверные координаты')
            coordinate = input(Player2 + ': ', )
        elif coordinate in used_coord:
            print('Такой ход уже был, введите другой')
            coordinate = input(Player2 + ': ', )

        coordinate_id = list(map(int, coordinate))
        used_coord.append(coordinate)

        i = coordinate_id[0]  # строка
        j = coordinate_id[1]  # столбец

        matrix[i][j] = 'o'

        print('0 1 2')

        for i in range(row):
            for j in range(3):
                print(matrix[i][j], end=" ")
            print(i)

        # СТОЛБЦЫ для проверки результата
        import numpy as np
        column = np.array(matrix, str)
        column0 = list(map(str, column[:, 0]))
        column1 = list(map(str, column[:, 1]))
        column2 = list(map(str, column[:, 2]))

        # ДИАГОНАЛИ для проверки результата
        diagonal_left = list(map(str, [matrix[0][0], matrix[1][1], matrix[2][2]]))
        diagonal_right = list(map(str, [matrix[0][2], matrix[1][1], matrix[2][0]]))

        win_player2 = (['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o'], ['o' 'o' 'o'], ['o' 'o' 'o'], ['o' 'o' 'o'])

        counter += 1

        if row0 in win_player2 or row1 in win_player2 or row2 in win_player2:
            print('Победил', Player2, 'Поздравляем!')
            break
        elif column0 in win_player2 or column1 in win_player2 or column2 in win_player2:
            print('Победил', Player2, 'Поздравляем!')
            break
        elif diagonal_right in win_player2 or diagonal_left in win_player2:
            print('Победил', Player2, 'Поздравляем!')
            break


repeat_step()

field_size = 3

field = [['-' for j in range(field_size)] for i in range(field_size)]

for i in range(field_size):
    for j in range(field_size):
        print(field[i][j], end=' ')
    print()

current_player = 'X'
while True:
    print(f"Ход {current_player}")
    row = int(input("Введите номер строки: ")) - 1
    col = int(input("Введите номер столбца: ")) - 1

    if row < 0 or row >= field_size or col < 0 or col >= field_size:
        print("Попробуйте еще раз.")
        continue

    if field[row][col] != '-':
        print("Клетка уже занята. Попробуйте еще раз.")
        continue

    field[row][col] = current_player

    for i in range(field_size):
        for j in range(field_size):
            print(field[i][j], end=' ')
        print()

    if (field[row][0] == field[row][1] == field[row][2] == current_player or
            field[0][col] == field[1][col] == field[2][col] == current_player or
            field[0][0] == field[1][1] == field[2][2] == current_player or
            field[0][2] == field[1][1] == field[2][0] == current_player):
        print(f"Игрок {current_player} победил!")
        break

    if '-' not in [cell for row in field for cell in row]:
        print("Ничья!")
        break


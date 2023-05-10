import random
def greet():
    print("-------------------")
    print("  Игра крестики-нолики  ")
    print("  Вы играете против AI  ")
    print("-------------------")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while True:
        cords = input(" Ведите через пробел:\n номер строки\n номер столбца ").split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты через пробел ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Координаты вне диапазона ")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята ")
            continue
        
        return x, y

def ask_1():
    while True:
        x1 = random.randint(0, 2)
        y1 = random.randint(0, 2)
        if field[x1][y1] != " ":
            continue
        return x1, y1


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Вы победили!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Вы проиграли.")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик")
        x, y = ask()
    else:
        x1, y1 = ask_1()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x1][y1] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Ничья!")
        break
import random
from game.constants import *


def _ship_cells(start, length, horizontal):
    row, col = start
    cells = []

    for i in range(length): #сколько палуб у корабля
        if horizontal:
            cells.append((row, col + i))
        else:                          #i это счётчик в цикле
            cells.append((row + i, col))
    return cells
#///////////////////за границу
def _can_place(board, cells):
    for row, col in cells:
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            return False
        if board[row][col] != WATER:#
            return False

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]: # перебирают все 9 клеток
                #координаты соседней клетки:
                nr = row + dr  #nr=текущая строка + смещение
                nc = col + dc  #nc=текущий столбец + смещение

                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE: #если соседняя клетка находится в пределах поля
                    if board[nr][nc] != WATER:#если в соседней клетке не вода(нельзя ставить)
                        return False

    return True


def random_place_fleet(board):
    while True:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                board[i][j] = WATER

        success = True

        for length in FLEET:
            placed = False

            for _ in range(300):
                horizontal = random.choice([True, False])
                row = random.randint(0, BOARD_SIZE - 1)
                col = random.randint(0, BOARD_SIZE - 1)

                cells = _ship_cells((row, col), length, horizontal)

                if _can_place(board, cells):
                    for r, c in cells:
                        board[r][c] = SHIP
                    placed = True
                    break

            if not placed:
                success = False
                break

        if success:
            break


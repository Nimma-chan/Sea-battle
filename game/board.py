from game.constants import *
def create_board() -> list[list[str]]:
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for m in range(BOARD_SIZE):
            row.append(WATER)
        board.append(row)
    return board

def render_board(board: list[list[str]], show_ships: bool = True) -> None:
    print("    ", end="")
    for letter in LETTER:
        print(f" {letter}", end="")
    print()
#/////////////////////
    for i in range(BOARD_SIZE):
        if i + 1 < 10:
            print(f" {i + 1} |", end="")
        else:
            print(f"{i + 1} |", end="")
#////////////////////
        for m in range(BOARD_SIZE):
            cell = board[i][m]
            if not show_ships and cell == SHIP:
                print(f" {WATER}", end="")
            else:
                print(f" {cell}", end="")
        print()
#///////////////////
def has_ships_left(board: list[list[str]]) -> bool:
    for i in range(BOARD_SIZE):
        for m in range(BOARD_SIZE):
            if board[i][m] == SHIP:
                return True
    return False
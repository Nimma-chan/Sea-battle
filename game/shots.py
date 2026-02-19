from game.constants import *
def parse_shot(text):
    if not text or len(text) < 2:
        return None

    text = text.upper()
    letter = text[0]
    number = text[1:]
#////////////////////////
    if letter not in LETTER:
        return None

    if not number.isdigit():
        return None

    row = int(number) - 1
    col = LETTER.index(letter)

    if row < 0 or row >= BOARD_SIZE: #
        return None

    return (row, col)
#////////////////////////////////
def ask_shot():
    while True:
        text = input("Введите координаты выстрела (например a5): ")
        coords = parse_shot(text)

        if coords is None:
            print("Ошибка! Введите букву от A до J и число от 1 до 10")
        else:
            return coords

def apply_shot(board, shot):
    row, col = shot

    if board[row][col] == WATER:
        board[row][col] = MISTAKE
        return "miss"
    elif board[row][col] == SHIP:
        board[row][col] = HIT
        return "hit"
    else:
        return "repeat"
import os
from game.board import create_board, render_board, has_ships_left
from game.ships import random_place_fleet
from game.shots import ask_shot, apply_shot

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(current_player): #name
    print("=" * 30)
    print(f"      ХОД ИГРОКА {current_player}")
    print("=" * 30)

def switch_player(current):
    if current == 1:
        return 2
    else:
        return 1

def render_turn(board1, board2, current_player):
    if current_player == 1:
        print("\nПоле Игрока 1 (ваше):")
        render_board(board1, show_ships=True)
        print("\nПоле Игрока 2 (противника):")
        render_board(board2, show_ships=False)
    else:
        print("\nПоле Игрока 1 (противника):")
        render_board(board1, show_ships=False)
        print("\nПоле Игрока 2 (ваше):")
        render_board(board2, show_ships=True)

def check_win(board, player):
    if not has_ships_left(board):
        clear_screen()
        print("=" * 30)
        print(f"    ИГРОК {player} ПОБЕДИЛ!")
        print("=" * 30)
        return True
    return False

def pause(message="Нажмите Enter, чтобы продолжить..."):
    input(message)

def play_game():
    board1 = create_board()
    board2 = create_board()

    print("Расставляем корабли игрока 1...")
    random_place_fleet(board1)
    print("Расставляем корабли игрока 2...")
    random_place_fleet(board2)

    current_player = 1

    while True:
        clear_screen()

        header(current_player)
        render_turn(board1, board2, current_player)

        if current_player == 1:
            shot = ask_shot()
            result = apply_shot(board2, shot)
        else:
            shot = ask_shot()
            result = apply_shot(board1, shot)

        if result == "repeat":
            print("\nВы уже стреляли в эту клетку!")
            pause()
        elif result == "miss":
            print("\n❌ Промах!")
            pause("Нажмите Enter, чтобы передать ход...")
            current_player = switch_player(current_player)
        elif result == "hit":
            print("\n🎯 Попадание!")
            if current_player == 1:
                if check_win(board2, current_player):
                    break
            else:
                if check_win(board1, current_player):
                    break
            pause("Нажмите Enter, чтобы продолжить...")
from termcolor import colored

board = list(range(1, 10))

winners = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

moves = (
    (1, 3, 7, 9),
    (5,),
    (2, 4, 6, 8)
)


def print_board():
    j = 1

    for i in board:
        end = " "

        if j % 3 == 0:
            end = "\n\n"

        if i == "x":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "o":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)

        j += 1


def can_move(brd, mve):
    return mve in range(1, 10) and isinstance(brd[mve - 1], int)


def is_winner(brd, plyr):
    for tup in winners:
        win = True

        for j in tup:
            if brd[j] != plyr:
                win = False
                break

        if win:
            return True

    return False


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr

        win = is_winner(brd, plyr)

        if undo:
            brd[mve - 1] = mve

        return True, win

    return False, False


def has_empty_space():
    return board.count("x") + board.count("o") != 9


def computer_move():
    mv = -1

    # Can computer win?
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break

    # Can player win?
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break

    # Choose corner, center, or edge
    if mv == -1:
        for tup in moves:
            for m in tup:
                if can_move(board, m):
                    mv = m
                    break

            if mv != -1:
                break

    return make_move(board, computer, mv)


player, computer = "x", "o"

print("You're X\nComputer is O\n")

while has_empty_space():
    print_board()

    move = int(input("Choose your move (1-9): "))

    moved, won = make_move(board, player, move)

    if not moved:
        print("Invalid move, try again!")
        continue

    if won:
        print_board()
        print(colored("You won!", "green"))
        break

    computer_moved, computer_won = computer_move()

    if computer_won:
        print_board()
        print(colored("You lose!", "red"))
        break
print_board()
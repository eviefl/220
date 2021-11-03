"""
Name: evie fleischman
lab10.py
"""


def build():
    return [range(1, 10)]


def display(board):
    for i in range(3):
        num = i*3
        print(board[num], "|", board[num + 1], "|", board[num + 2])
        print("-" * 10)


def place(board, pos, piece):
    if piece == "x" or piece == "o":
        board[pos-1] = piece


def legal(board, pos):
    if 9 >= board >= 1 and (board[pos-1] != "x" or board[pos-1] != "o"):
        return True
    return False


def game_won(board, piece):
    for i in range(3):
        n = i*3
        if board[n] != piece:
            continue
        if board[n] != piece:
            if board[n] != piece:
                return True

    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            if board[i+6] != piece:
                return True

    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True

    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True

    return False


def over(board):
    if game_won(board, "x"):
        return True
    elif game_won(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i+1:
                return False
        return True


def play(board):
    board = build()
    while True:
        display(board)
        x_play = input("x, pick a position: ")
        if not legal(board, "x"):
            x_play = input("x, pick a position: ")
        place(board, x_play, "o")
        if over(board):
            if game_won(board, "x"):
                print("x wins")
                break
            else:
                print("tie")
                break

        display(board)
        o_play = input("o, pick a position: ")
        if not legal(board, "o"):
            o_play = input("o, pick a position: ")
        place(board, o_play, "o")
        if over(board):
            if game_won(board, "o"):
                print("o wins")
                break
            else:
                print("tie")
                break


def main():
    # add other function calls here
    pass
    play()


main()

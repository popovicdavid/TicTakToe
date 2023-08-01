player_X = "X"
player_O = "O"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def printboard(board):
    print(board[0] + "  |  " + board[1]+ "  |  " + board[2])
    print("-------------")
    print(board[3] + "  |  " + board[4]+ "  |  " + board[5])
    print("-------------")
    print(board[6] + "  |  " + board[7]+ "  |  " + board[8])

def player_move(board, player):
    number = int(input("chose a number from 1 to 9: "))
    if number <= 9 and number >=1 and board[number-1] == "-":
        board[number-1] = player
        print(printboard(board))
    else:
        print("that place is already taken!")
        player_move(board, player)


def check_horizontal(board):
    if (board[0] == board[1] == board[2] != "-" 
        or board[3] == board[4] == board[5] != "-" 
        or board[6] == board[7] == board[8] != "-"):
        return True
    return False


def check_vertikal(board):
    if (board[0] == board[3] == board[6] != "-" 
        or board[1] == board[4] == board[7] != "-" 
        or board[2] == board[5] == board[8] != "-"):
        return True
    return False

def check_cross(board):
    pass

def check_winner(board):
    return check_vertikal(board) or check_horizontal(board) or check_cross(board)

def main():
    print(printboard(board))
    x_turn = True
    while not check_winner(board):
        if x_turn:
            player = player_X
        else:
            player = player_O
        x_turn = (not x_turn)
        player_move(board, player)

    print("We have a winner!")


if __name__ == "__main__":
    main()














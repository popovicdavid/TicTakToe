player_1 = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def printboard(board):
    print(board[0] + "  |  " + board[1]+ "  |  " + board[2])
    print("-------------")
    print(board[3] + "  |  " + board[4]+ "  |  " + board[5])
    print("-------------")
    print(board[6] + "  |  " + board[7]+ "  |  " + board[8])


def player_1(board):
    number = int(input("chose a number from 1 to 9: "))
    if number <= 9 and number >=1 and board[number] != "-"










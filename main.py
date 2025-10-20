import random

board_size = 5
board = []

def generate_board(board_size):
    board = [[random.choice([True, False]) for _ in range(board_size)] for _ in range(board_size)]
    # if check_board(board): 
    return board

def show_board(board):
    print("   " + "  ".join(str(i+1) for i in range(len(board))))
    for i in range(len(board)):
        print (i+1, end="  ")
        for j in range(len(board)):
            print("*" if board[i][j] else "-", end="  ")
        print()

def switch_points(board, x, y):
    for (i,j) in [(x,y), (x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
        # print(f"{i}, {j}")
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            board[i][j] = not board[i][j]
    return board

def check_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]: return False
    return True

def play(board):
    while not check_board(board):
        show_board(board)
        print("Make a move!")
        try:
            x = int(input("Choose your x cooridnate: "))
            y = int(input("Choose your y cooridnate: "))
            board = switch_points(board, y-1,x-1)
        except ValueError:
            print("Invalid input. Please enter numbers.")
    print ("Congratulations! You won!")

def main():
    print("Lights out!")
    board = generate_board(board_size)
    play(board)

if __name__ == "__main__":
    main()
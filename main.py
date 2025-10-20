import random

board_size = 5
board = []

hardness = {
    "easy": 3,
    "medium": 9,
    "hard": 15
}

def show_welcome_screen():
    print("Lights out!")
    print("Your goal is to turn off all the lights.")
    print("Each move toggles a cell and its neighbors.")
    print("Try to solve the puzzle in as few moves as possible!")
    difficulty = ""
    while difficulty not in hardness:
        difficulty = input("Choose difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty not in hardness:
            print("Invalid choice. Please type: easy, medium, or hard.")
    print("Good luck!")
    return hardness[difficulty]

def generate_random_board(board_size):
    board = [[random.choice([True, False]) for _ in range(board_size)] for _ in range(board_size)]
    # if check_board(board): 
    return board

def generate_solvable_board(board_size, level):
    board = [[False for _ in range(board_size)] for _ in range(board_size)]
    for i in range(level):
        x = random.randint(0, board_size-1)
        y = random.randint(0, board_size-1)
        board = switch_points(board, y,x)
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
    steps = 0
    while not check_board(board):
        show_board(board)
        print("Make a move!")
        steps += 1
        try:
            x = int(input("Choose your x cooridnate: "))
            y = int(input("Choose your y cooridnate: "))
            if 0 <= x-1 < len(board) and 0 <= y-1 < len(board[0]):
                board = switch_points(board, y-1,x-1)
            else:
                print("Coordinates out of range! Try again!")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    show_board(board)
    print("Congratulations! You won!")
    print(f"You needed just {steps} step to complete!")

# def check_if_solvable():
# tbd later

def main():
    level = show_welcome_screen()
    # board = generate_random_board(board_size)
    board = generate_solvable_board(board_size, level)
    play(board)

if __name__ == "__main__":
    main()
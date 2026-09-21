import random

board = {
    1: 1, 2: 2, 3: 3,
    4: 4, 5: 5, 6: 6,
    7: 7, 8: 8, 9: 9
}

print("Welcome to tic-tac-toe!")

def print_board():
    print()
    for key, value in board.items():
        print(value, end="|")
        if key % 3 == 0:
            print("\n-+-+-+-+-")

while True:
    user_choice = input("Enter what you would like to be (X or O): ").upper()
    if user_choice == "X" or user_choice == "O":
        break
    print("Invalid choice, please try again.")

if user_choice == "O":
    robot_move = "X"
else:
    robot_move = "O"

while True:
    print_board()
    
    winning_combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    
    game_over = False
    for a, b, c in winning_combos:
        if board[a] == user_choice and board[b] == user_choice and board[c] == user_choice:
            print("You Won!")
            game_over = True
            break
        elif board[a] == robot_move and board[b] == robot_move and board[c] == robot_move:
            print("You Lost!")
            game_over = True
            break
            
    if game_over:
        break

    board_full = True
    for i in range(1, 10):
        if board[i] != "X" and board[i] != "O":
            board_full = False
            break
            
    if board_full:
        print("\nDraw!")
        break

    while True:
        try:
            user_input = int(input(f"Enter the place for your {user_choice} (1-9): "))
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue
            
        if 1 <= user_input <= 9 and board[user_input] != "X" and board[user_input] != "O":
            board[user_input] = user_choice
            break
        else:
            print("That spot is invalid or already taken. Try again.")

    while True:
        random_place = random.randint(1, 9)
        if board[random_place] != "X" and board[random_place] != "O":
            board[random_place] = robot_move
            break

print_board()
            
    

     







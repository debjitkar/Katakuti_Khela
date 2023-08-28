# Printing the board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Checking for the winner by iterating through each row of the board. 

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    '''
    Checking for the winner in the columns.
    iterating through each column (0, 1, and 2)
    and checking if all cells in that column are owned by the current player
    '''
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    '''
    Checking for the winner in the diagonals.
    The first condition will check the diagonal from top-left to bottom-right,
    and the second condition will check the diagonal from top-right to bottom-left
    '''

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    # if no conditions are met then returning false indiactes the current player did not win

    return False

# Checking if all the cells in the board is occupied or not

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

'''
The game begins in main function.
current player is assigned to X
3x3 empty board is created
'''

def main():
    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]

    '''
    Printing the current state of the board
    asking the current player to input their desired row and column
    '''

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        '''
        checking if the chosen cell is empty
        if it is empty then the current player's symbol is placed in the chosen cell
        '''

        if board[row][col] == " ":
            board[row][col] = current_player

            '''
            checking if the current player has won
            if true then the board is printed & the winner is anounced
            breaking the loop
            '''

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            #If there's no winner but the board is full, printing the board and announcing the draw before breaking out of the loop.

            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already taken. Try again.")

# Running the main function, ensuring that the game starts when the python file is run.

if __name__ == "__main__":
    main()

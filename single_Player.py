# https://github.com/gbrough/battleship/blob/main/single_player.py
# https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=0s
# X for placing battle ship and hit battle ship
# ' ' for available space
# - for missed quest

from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H") # first colunm
   # print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|_".join(row)))  #% = forman %d formant decimal for each row we iterate through we join | 
        row_number += 1

# dictionary to convert board numbers 
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":  # check if the ship exits
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X" # place the ship

def get_ship_location():
    row = input("Enter the row of the ship 1-8: ")
    while row not in "12345678T":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ")
    column = input("Enter the column of the ship A-H: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column] # uses dictionary to convert letter to number 

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
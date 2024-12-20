### Nested list with 8 rows and 8 columns for a chessboard
def grid():
    spaces = [[None for x in range(8)] for x in range(8)]
    return spaces

### Function to label and color the spaces on a chessboard
def colorspaces(ls): 
    for col in range(65,73):    # Using this range as it correlates to the ASCII value of letters A-H
        for row in range(1,9):
            if col % 2 == 0:        # columns B,D,F, and H
                if row % 2 == 0:    # rows 2,4,6, and 8 in the aforementioned columns
                    color = "black"
                else:               # rows 1,3,5, and 7 in the aforementioned columns
                    color = "white"
            else:                   # columns A,C,E, and G
                if row % 2 == 0:    # rows 2,4,6, and 8 in the aforementioned columns
                    color = "white"
                else:               # rows 1,3,5, and 7 in the aforementioned columns
                    color = "black"
            ls[col-65][row-1] = f"{chr(col)}{row}: {color}" # Fills the nested list in order

### Function for user to pick a space on a chessboard and see what color it is
def checkcolor(ls):
    while True:
        space = input("Enter a space to check its color.\n*** Hint: 'A1', 'B4', 'H8', etc. ***\nEnter space: ").upper()
        for col in range(8): 
            for row in range(8):
                if space == ls[col][row][:2]: # only compares the first two characters in each nested list item
                    color = ls[col][row][-5:] # if it's a match, stores the color in a variable
                    return print(f"\n{space} is {color}.\n") # returns the space and color
        print("\nError: Invalid entry.\n")    # keeps looping until a valid space is entered

def main():
    board = grid()          # generates the board
    colorspaces(board)      # adds color to the individual spaces
    checkcolor(board)       # lets user pick a space to check its color

main()

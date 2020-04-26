# DECLARATIONS

# 1) display_board function prints the board based according to the board_state list of symbol locations.

def display_board(board_state):
    board = """
         **BOARD**            **LOCATIONS**

           |   |                  |   |
         {} | {} | {}              0 | 1 | 2
        ___|___|___            ___|___|___
           |   |                  |   |
         {} | {} | {}              3 | 4 | 5
        ___|___|___            ___|___|___
           |   |                  |   |
         {} | {} | {}              6 | 7 | 8
           |   |                  |   |

        """.format(board_state[0], board_state[1], board_state[2], board_state[3], board_state[4], board_state[5], board_state[6],
                   board_state[7], board_state[8], )
    print(board)

# 2) player_input function allows a designated player to place their symbol at an available location on the board
# only accepts number between 0 and 8 that isn't already taken

def player_input(board_state, available_spaces, player, symbol):
    move = input(player + " choose a board location:")
    while (move.isdigit()) == False or int(move) < 0 or int(move) > 8 or available_spaces[int(move)] == False:
        move = input("Inputs may only be an available location from 0 to 8. Try again: ")
    board_state[int(move)] = symbol
    available_spaces[int(move)] = False
    return board_state, available_spaces

# 3) check_win function takes board_state and evaluates whether or not any rows / cols / diags contain 3 identical symbols

def check_win(board_state):
    rowA = [board_state[0], board_state[1], board_state[2]]
    rowB = [board_state[3], board_state[4], board_state[5]]
    rowC = [board_state[6], board_state[7], board_state[8]]
    col1 = [board_state[0], board_state[3], board_state[6]]
    col2 = [board_state[1], board_state[4], board_state[7]]
    col3 = [board_state[2], board_state[5], board_state[8]]
    diagTLBR = [board_state[0], board_state[4], board_state[8]]
    diagTRBL = [board_state[2], board_state[4], board_state[6]]
    lines = [rowA, rowB, rowC, col1, col2, col3, diagTLBR, diagTRBL]

    for x in lines:
        if x[0] == x[1] == x[2] and x[0] == "X":
            print("Player 1 is the winner!!!")
            return True
        elif x[0] == x[1] == x[2] and x[0] == "O":
            print("Player 2 is the winner!!!")
            return True

# 4) game function...
# - initiates lists board_state and avaliable_spaces
# - starts by displaying the display_board
# - alternates between player 1 and player 2 inputting
# - checks for a win after every turn and exits if win found

def game():
    board_state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    available_spaces = [True, True, True, True, True, True, True, True, True]
    display_board(board_state)

    while check_win(board_state) != True:
        player_input(board_state, available_spaces, player="Player 1 (X)", symbol="X")
        display_board(board_state)
        if check_win(board_state) == True:
            break
        print(check_win(board_state))
        computer_input(board_state, available_spaces, player="Player 2 (O)", symbol="O")
        display_board(board_state)
        if check_win(board_state) == True:
            break

# NEW STUFF FROM HERE

def computer_input(board_state, available_spaces, player="Player 2 (O)", symbol="O"):
    move = None
    if win_opportunity(board_state, available_spaces) != False:
        move = win_opportunity(board_state, available_spaces)
    elif stop_loss_opportunity(board_state, available_spaces) != False:
        move = stop_loss_opportunity(board_state, available_spaces)


    board_state[move] = symbol
    available_spaces[move] = False
    return board_state, available_spaces


def win_opportunity(board_state, available_spaces):
    rowA = [board_state[0], board_state[1], board_state[2]]
    rowB = [board_state[3], board_state[4], board_state[5]]
    rowC = [board_state[6], board_state[7], board_state[8]]
    col1 = [board_state[0], board_state[3], board_state[6]]
    col2 = [board_state[1], board_state[4], board_state[7]]
    col3 = [board_state[2], board_state[5], board_state[8]]
    diagTLBR = [board_state[0], board_state[4], board_state[8]]
    diagTRBL = [board_state[2], board_state[4], board_state[6]]
    lines = [rowA, rowB, rowC, col1, col2, col3, diagTLBR, diagTRBL]

    for x in lines:
        if x[0] and x[1] == "X":
            x[2] = "O"
            return
        elif x[0] and x[2] == "X":
            x[1] = "O"
            break
        elif x[1] and x[2] == "X":
            x[0] = "O"
            break









def stop_loss_opportunity(board_state, available_spaces):



# EXECUTIONS

game()
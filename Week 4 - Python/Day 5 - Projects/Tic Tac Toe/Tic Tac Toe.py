# WORK IN PROGRESS


winner = ""
locations = [" "," "," "," "," "," "," "," "," "]

player1 = {
    "name": "Player 1",
    "symbol": "X",
    "locations": [" "," "," "," "," "," "," "," "," "],
}

player2 = {
    "name": "Player 2",
    "symbol": "O",
    "locations": [" "," "," "," "," "," "," "," "," "],
}

def display_board ():
    grid = """
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

    """.format(locations[0], locations[1], locations[2], locations[3], locations[4], locations[5], locations[6], locations[7], locations[8], )
    print(grid)

display_board()

# def check_win():
#     for x in lines:
#         if x[0] == x[1] == x[2]:
#             if x[0] == " ":
#                 break
#             elif x[0] == "X":
#                 print("Player 1 Wins!!")
#             elif x[0] =="O":
#                 print("Players 2 Wins!!")
#         else:
#             print("No winner yet")




def player_input(player):
    move = int(input("Choose a grid location: "))
    locations[int(move)] = player["symbol"]

    display_board()
    # check_win()
    rowA = [locations[0], locations[1], locations[2]]
    rowB = [locations[3], locations[4], locations[5]]
    rowC = [locations[6], locations[7], locations[8]]
    col1 = [locations[0], locations[3], locations[6]]
    col2 = [locations[1], locations[4], locations[7]]
    col3 = [locations[2], locations[5], locations[8]]
    diagTLBR = [locations[0], locations[4], locations[8]]
    diagTRBL = [locations[2], locations[4], locations[6]]
    lines = [rowA, rowB, rowC, col1, col2, col3, diagTLBR, diagTRBL]


    for x in lines:
        if x[0] == x[1] == x[2] and x[0] != " ":
            global winner
            winner = player["name"]
            print(winner + " is the winner!!!")




def game():
    while winner == "":
        player_input(player1)
        player_input(player2)


game()

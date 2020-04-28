# import time for new generations
import time

# Define grid size
# Finite grid rather than infinite
i = 20
j = 200
grid = [0] * i
for p in range(i):
    grid[p] = [0] * j

# Convert list of lists in strings for display
def display(grid):
    for rows in grid:
        print("".join(str(i) for i in rows))
    print("")

# gets locations of cells which user wants to begin in a live state
def starting_conditions(grid):
    start = "no"
    while start != "yes":
        print("Enter coordinates for cells to add.\nType 'begin' instead of a new x coordinate to start the game.\nRemember demo shapes may be affected if you add additional live cells.\n")
        print("Maximum x value is: " + str(i))
        print("Maximum y value is: " + str(j))
        live_cell_x = input("Submit x coordinates of a live cell to add: ")
        if live_cell_x == "begin":
            start = "yes"
            break
        live_cell_y = int(input("Submit y coordinates of the same cell: "))
        grid[int(live_cell_x)][int(live_cell_y)] = 1
        display(grid)
    return(grid)

# counts number of live neighbours for a cell
def check_life(grid, x, y):
    if x == 0 and y == 0:
        sum_neighbours = grid[x][y + 1] + grid[x + 1][y] + grid[x + 1][y + 1]
    elif x == 0 and y == j-1:
        sum_neighbours = grid[x][y - 1] + grid[x + 1][y - 1] + grid[x + 1][y]
    elif x == i-1 and y == j-1:
        sum_neighbours = grid[x - 1][y - 1] + grid[x - 1][y] + grid[x][y - 1]
    elif x == i-1 and y == 0:
        sum_neighbours = grid[x - 1][y] + grid[x - 1][y + 1] + grid[x][y + 1]
    elif x == i-1 and y != 0 and y != j-1:
        sum_neighbours = grid[x - 1][y - 1] + grid[x - 1][y] + grid[x - 1][y + 1] + grid[x][y - 1] + grid[x][y + 1]
    elif y == 0 and x != 0 and x != i-1:
        sum_neighbours = grid[x - 1][y] + grid[x - 1][y + 1] + grid[x][y + 1] + grid[x + 1][y] + grid[x + 1][y + 1]
    elif y == j-1 and x != 0 and x != i-1:
        sum_neighbours = grid[x-1][y-1] + grid[x-1][y] + grid[x][y-1] + grid[x+1][y-1] + grid[x+1][y]
    elif x == 0 and y != 0 and y != j-1:
        sum_neighbours = grid[x][y-1] + grid[x][y+1] + grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1]
    else:
        sum_neighbours = grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1] + grid[x][y-1] + grid[x][y+1] + grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1]
    return sum_neighbours




# updates grid by running checks for live neighbours on all cells
# doesn't wrap around borders, just counts fewer neighbours
# had real difficulty with this one - wanted to define new_grid in terms of grid to begin with rather than generate something completely new,
# but for some reason grid itself was the thing that got updated as the nested loops got to work. don't really understand why.'
def update_grid(grid):

    new_grid = [0] * i
    for p in range(i):
        new_grid[p] = [0] * j

    for x in range(i):
        for y in range(j):

            if grid[x][y] == 0 and check_life(grid, x, y) == 3:
                new_grid[x][y] = 1
            elif grid[x][y] == 1 and check_life(grid, x, y) < 2:
                new_grid[x][y] = 0
            elif grid[x][y] == 1 and check_life(grid, x, y) > 3:
                new_grid[x][y] = 0
            else:
                new_grid[x][y] = grid[x][y]

    return new_grid

# user option to include some basic demo patterns at game set up

def demo_shapes(grid):
    ask = input("Include demo shapes? yes or no: ")
    if ask == "yes":
        # blinker
        grid[3][3] = 1
        grid[3][4] = 1
        grid[3][5] = 1
        # block
        grid[10][3] = 1
        grid[10][4] = 1
        grid[11][3] = 1
        grid[11][4] = 1
        # glider
        grid[4][8] = 1
        grid[4][9] = 1
        grid[4][10] = 1
        grid[3][10] = 1
        grid[2][9] = 1
        # lightweight spaceship
        grid[5][15] = 1
        grid[7][15] = 1
        grid[8][16] = 1
        grid[8][17] = 1
        grid[5][18] = 1
        grid[8][18] = 1
        grid[6][19] = 1
        grid[7][19] = 1
        grid[8][19] = 1
    display(grid)

    return grid

# game begins with inputs including possible demo shaps
# runs update_grid and display_grid in a while loop

def game_of_life (grid):

    display(grid)
    demo_shapes(grid)
    grid = starting_conditions(grid)
    display(grid)

    ready = input("Press any key to begin...")
    generations=0
    while generations < 200:
        new_grid = update_grid(grid)
        display(new_grid)
        grid = new_grid
        generations += 1
        time.sleep(0.25)

# EXECUTION

game_of_life(grid)


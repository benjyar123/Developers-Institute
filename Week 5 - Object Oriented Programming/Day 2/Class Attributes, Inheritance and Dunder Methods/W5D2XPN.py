# Not working yet


import time

i = 10
j = 10
grid = [0] * i
for p in range(i):
    grid[p] = [0] * j


def display(grid):
    for rows in grid:
        print("".join(str(i) for i in rows))
    print("")

def starting_conditions(grid):
    finished = "no"
    while finished != "yes":
        live_cell_x = int(input("Submit x coordinates of a live cell to add: "))
        live_cell_y = int(input("Submit y coordinates of the same cell: "))
        grid[live_cell_x][live_cell_y] = 1
        display(grid)
        finished = input("Finished?")

    return(grid)

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

def update_grid(grid):

    new_grid = grid

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


update_grid(grid)




display(grid)



def game_of_life (grid):

    grid = starting_conditions(grid)
    display(grid)

    ready = input("Ready?")
    generations=0
    while generations < 5:
        new_grid = update_grid(grid)
        display(new_grid)
        grid = new_grid
        generations += 1
        time.sleep(1)


game_of_life(grid)


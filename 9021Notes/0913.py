from random import random

size=10
density=.3



grid=[[None]*10 for _ in range(10)]

# def initialise_grid():
#
#     for i in range(size):
#         for j in range(size):
#             # if random()< 0.3:
#             #     grid[i][j] = 1
#             # else:
#             #     grid[i][j] = 0
#             grid[i][j]=int(random()<density)
def create_and_initialise_grid():
    return [[int(random() < density) for _ in range(10)]
            for _ in range(10)]



def display_grid():
    square={0:"\u2B1C",1:"\u2B1B"}
    for row in grid:
        #print(*row)
        print(' '.join(square[e] for e in row))


def compute_next_generation():

    global grid
    new_grid=[[0] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            nb_of_neighbours = 0
            if i and j and grid[i-1][j-1]:
                nb_of_neighbours+=1
            if i and j and grid[i - 1][j]:
                nb_of_neighbours += 1
            if i and j < (size - 1) and grid[i - 1][j + 1]:
                nb_of_neighbours += 1
            if j and grid[i][j-1]:
                nb_of_neighbours += 1
            if j < (size - 1) and grid[i][j + 1]:
                nb_of_neighbours += 1
            if i < (size - 1) and grid[i +1][j-1]:
                nb_of_neighbours += 1
            if i < (size - 1) and grid[i +1][j]:
                nb_of_neighbours += 1
            if i < (size - 1) and j<(size-1 ) and grid[i +1][j+1]:
                nb_of_neighbours += 1
            if grid[i][j] and nb_of_neighbours==2 or nb_of_neighbours==3:
                new_grid[i][j]=1
        grid=new_grid

grid=create_and_initialise_grid()
#initialise_grid()
display_grid()
print()
compute_next_generation()
display_grid()

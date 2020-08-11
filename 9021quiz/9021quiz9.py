# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
#from queue_adt import *


def display_grid():
    for row in grid:
        print('    ', *row)


def preferred_paths_to_corners():
    pass
    # replace pass above with your code


def BFS(graph):
    queue=[]
    queue.append([(3,3)])
    #起点永远是中心
    already_reach=set()
    already_reach.add((3,3))
    while queue:
        path=queue.pop(0)
        current_point=path[-1]
        if current_point in corners:
            print(path)
            paths[current_point]=path
        current_coor = graph[current_point]
        for ele in current_coor:
            if ele not in already_reach:
                temppath = path.copy()
                temppath.append(ele)
                queue.append(temppath)
                already_reach.add(ele)
        print(path)
    return paths





dim=7
def find_next(point):
    i,j=point
    if grid[i][j] == 'NW' or grid[i][j] == 'WN':
        # NW  西北
        if (i - 1) >= 0 and (j - 1) >= 0:
            tree[(i, j)] = [(i - 1, j - 1), (i - 1, j), (i, j - 1)]
        # if (i - 1) >= 0 and (j - 1) <= 0:
        #     tree[(i, j)] = [(i - 1, j)]
        # elif (i - 1) <= 0 and (j - 1) >= 0:
        #     tree[(i, j)] = [(i, j - 1)]
        # elif (i - 1) >= 0 and (j - 1) >= 0:
        #     tree[(i, j)] = [(i - 1, j - 1), (i - 1, j), (i, j - 1)]
        # else:
        #     tree[(i, j)] = []
        # temp.append((i,j))
    if grid[i][j] == 'NE' or grid[i][j] == 'EN':
        # NE  东北
        if (i + 1) <= (dim - 1) and (j - 1 >= 0):
            tree[(i, j)] = [(i + 1, j - 1), (i + 1, j), (i, j - 1)]
        # elif (i + 1) >= (dim - 1) and (j - 1 >= 0):
        #     tree[(i, j)] = [(i, j - 1)]
        # elif (i + 1) <= (dim - 1) and (j - 1 <= 0):
        #     tree[(i, j)] = [(i + 1, j)]
        # else:
        #     tree[(i, j)] = []
        # temp.append((i, j))
    if grid[i][j] == 'SE' or grid[i][j] == 'ES':
        if (i + 1) <= (dim - 1) and (j + 1) <= (dim - 1):
            tree[(i, j)] = [(i + 1, j + 1), (i + 1, j), (i, j + 1)]
        # elif (i + 1) <= (dim - 1) and (j + 1) >= (dim - 1):
        #     tree[(i, j)] = [(i + 1, j)]
        # elif (i + 1) >= (dim - 1) and (j + 1) <= (dim - 1):
        #     tree[(i, j)] = [(i, j + 1)]
        # else:
        #     tree[(i, j)] = []
        # temp.append((i, j))
    if grid[i][j] == 'SW' or grid[i][j] == 'WS':
        if (i - 1) >= 0 and (j + 1) <= (dim - 1):
            tree[(i, j)] = [(i - 1, j + 1), (i - 1, j), (i, j + 1)]
        # elif (i - 1) <= 0 and (j + 1) <= (dim - 1):
        #     tree[(i, j)] = [(i, j + 1)]
        # elif (i - 1) >= 0 and (j + 1) >= (dim - 1):
        #     tree[(i, j)] = [(i - 1, j)]
        # else:
        #     tree[(i, j)] = []
        # temp.append((i, j))





# try:
#     seed_arg = int(input('Enter an integer: '))
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()
seed_arg=0
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

graph = {}
temp = []
paths={}
# 新建字典

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()


tree={}
start_point=(3,3)

def maketree(start_point):
    x,y=start_point
    find_next((x,y))
    for ele in tree[(x,y)]:
        if 0<=x<=6 and 0<=y<=6:
            if ele not in tree:
                if ele not in corners:
                    maketree(ele)



maketree(start_point)
print(tree)

#make_graph(grid)
#print(graph)
# 我加的 等下要去掉

display_grid()



if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
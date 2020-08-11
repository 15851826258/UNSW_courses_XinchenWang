# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end='')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    if len(height)!=0:
        output=max(height)
    else:
        for i in range(len(grid)):
            if 1 not in grid[i]:
                output = None
    return output

    # Replace pass above with your code

# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    pass
    # Replace pass above with your code


try:
   for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
   for_seed = int(for_seed)
   n = int(n)
   if n <= 0:
       raise ValueError
except ValueError:
   print('Incorrect input, giving up.')
   sys.exit()


seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]\

grid_copy=grid.copy()


for i in range(len(grid)):
    grid[i].append(False)
#print(grid)

list_suoyin = []
list_zuobiao = []
dict={}
count=0
list_didekaishi=[]
list_meihangdedi=[]
for i in range(9, -1, -1):
    list_didekaishi=[]
    for j in range(0,10):
        if grid[i][j]==1:
            for a in range(i,-1,-1):
                if grid[a][j]!=0:
                    count+=1
                else:
                    break
            dict[(i,j)]=count
            list_zuobiao.append((i,j))
            list_didekaishi.append(j)
            count = 0
    list_meihangdedi.append(list_didekaishi)


#得到一个字典{(坐标)：往上数多少个1}
#print(list_zuobiao)
# print(dict)
#print(list_meihangdedi)


list_zuobiaoji=[]
list_final=[]

sum=0
p=[]
k=0
list_temp=[]
list_final=[]
for i in range(9,-1,-1):
    list_temp = []
    for j1 in list_meihangdedi[10-i-1]:

        for j2 in range(j1+1,11):
            if grid[i][j2]==0 :
                list_temp.append([j1,j2-1])
                break
    list_final.append(list_temp)
# print('底是'+f'{list_final[4]}')


height=[]
sum_height=0
for i in range(9,-1,-1):
    for a in range(len(list_final[10-i-1])):
        if list_final[10-i-1][a][0]==list_final[10-i-1][a][1]:
            height.append(dict[(i,list_final[10-i-1][a][0])])
        else:
            for t in range(list_final[10-i-1][a][0],list_final[10-i-1][a][1]+1):
                sum_height=sum_height+dict[(i,t)]
            height.append(sum_height)
            sum_height=0
#print(height)
#print(max(height))












    #     if (i,j) in list_zuobiao:
    #         list_zuobiaoji.append((i,j))
    #         if (i,j+1) in list_zuobiao:
    #             list_zuobiaoji.append((i,j+1))
    #             if (i,j+2) in list_zuobiao:
    #                 list_zuobiaoji.append((i, j + 2))
    #                 if (i,j+3) in list_zuobiao:
    #                     list_zuobiaoji.append((i,j+3))
    #                     if (i,j+4) in list_zuobiao:
    #                         list_zuobiaoji.append((i,j+4))
    #                         if (i,j+5) in list_zuobiao:
    #                             list_zuobiaoji.append((i,j+5))
    #                             if (i,j+6) in list_zuobiao:
    #                                 list_zuobiaoji.append((i,j+6))
    #                                 if (i,j+7) in list_zuobiao:
    #                                     list_zuobiaoji.append((i, j + 7))
    #                                     if (i, j + 8) in list_zuobiao:
    #                                         list_zuobiaoji.append((i, j + 8))
    #                                         if (i, j + 9) in list_zuobiao:
    #                                             list_zuobiaoji.append((i, j + 9))
    #
    # list_final.append(list_zuobiaoji)
    # list_zuobiaoji=[]











print('Here is the grid that has been generated:')

for i in range(len(grid)):
    del grid[i][-1]

display_grid()

size = size_of_largest_construction()
if not size:
   print(f'The largest block construction has no block.')
elif size == 1:
   print(f'The largest block construction has 1 block.')
else:
   print(f'The largest block construction has {size_of_largest_construction()} blocks.')

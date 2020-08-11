# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by XINCHEN WANG and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()


def explore_board():
    whole_path=[]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[j][i]==1:
                recursion(i, j)
                count+=1
    #遍历循环所有是1的点 每一次循环都加一次 次数
    return count


def recursion(i, j):
    paths = []
    if not (0 <= i < 10 and 0 <= j <10):
        return []
    #超出了10x10的范围 递归出口1
    if grid[j][i]==0:
        return []
    #递归到走投无路 注意 递归中的横纵坐标和我们平常看到的不一样是 [j][i]后面也是这样
    #找啊找啊 找到0就退出本次递归 递归出口2（因为题目规定只能走1的部分）
    grid[j][i] = 0
    #把路过的i j的点 就把这个点置为0 防止每次都走一个点
    recursion(i + 1, j - 2)
    recursion(i + 1, j + 2)
    recursion(i - 1, j - 2)
    recursion(i - 1, j + 2)
    recursion(i + 2, j - 1)
    recursion(i + 2, j + 1)
    recursion(i - 2, j - 1)
    recursion(i - 2, j + 1)
    #骑士走L型 然后一共有八种路径，进行递归,每次递归都是调用自身这个方法


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

count=0

# from collections import defaultdict
# all_path = defaultdict(list)


nb_of_knights = explore_board()

#print(all_path)
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

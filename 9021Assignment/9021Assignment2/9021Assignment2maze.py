# 打开文件和生成迷宫的列表开始
import sys

sys.setrecursionlimit(1000000)
filename = 'maze_1.txt'
L = []
# #整个迷宫墙的列表L
# file_obj=open(filename)
# file_context=file_obj.read()
# #print(file_context)
# file_context=file_context.split('\n')
# #print(file_context)
# for ele in file_context:
#     L.append(ele.split())
#     #print(ele.split())
# #print(L)
# for i in range(len(L)):
#     for j in range(len(L[0])):
#         L[i][j]=int(L[i][j])
# #print(L)
with open(filename) as file:
    for line in file:
        temp = []
        if line.isspace():
            continue
        # print(line)
        for i in line.split():
            for ele in i:
                temp.append(int(ele))
        L.append(temp)
    # print(L)


# 打开文件和生成迷宫列表结束

# 九宫格
def makejiugongge(L):
    migonghengxiang = len(L[0])
    migongzongxiang = len(L)
    L_jiugongge = [([0] * migonghengxiang * 3) for i in range(migongzongxiang * 3)]
    for i in range(migongzongxiang):
        for j in range(migonghengxiang):
            if L[i][j] == 0:
                L_jiugongge[i * 3][j * 3] = 0
                L_jiugongge[i * 3][j * 3 + 1] = 0
                L_jiugongge[i * 3][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 1][j * 3] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 2][j * 3] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 0
            if L[i][j] == 1:
                L_jiugongge[i * 3][j * 3] = 1
                L_jiugongge[i * 3][j * 3 + 1] = 1
                L_jiugongge[i * 3][j * 3 + 2] = 1
                L_jiugongge[i * 3 + 1][j * 3] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 2][j * 3] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 0
            if L[i][j] == 2:
                L_jiugongge[i * 3][j * 3] = 1
                L_jiugongge[i * 3][j * 3 + 1] = 0
                L_jiugongge[i * 3][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 1][j * 3] = 1
                L_jiugongge[i * 3 + 1][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 2][j * 3] = 1
                L_jiugongge[i * 3 + 2][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 0
            if L[i][j] == 3:
                L_jiugongge[i * 3][j * 3] = 1
                L_jiugongge[i * 3][j * 3 + 1] = 1
                L_jiugongge[i * 3][j * 3 + 2] = 1
                L_jiugongge[i * 3 + 1][j * 3] = 1
                L_jiugongge[i * 3 + 1][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 1][j * 3 + 2] = 0
                L_jiugongge[i * 3 + 2][j * 3] = 1
                L_jiugongge[i * 3 + 2][j * 3 + 1] = 0
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 0
    for i in range(migongzongxiang - 1):
        for j in range(migonghengxiang - 1):
            if L[i][j + 1] == 2 or L[i][j + 1] == 3:
                # 如果这个方块的右边是2或者3的话 那么把自己的最右边的墙也变为1
                L_jiugongge[i * 3][j * 3 + 2] = 1
                L_jiugongge[i * 3 + 1][j * 3 + 2] = 1
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 1
            if L[i + 1][j] == 1 or L[i + 1][j] == 3:
                # 如果这个方块的下边是2或者3的话 那么把自己的最下边的墙也变为1
                L_jiugongge[i * 3 + 2][j * 3] = 1
                L_jiugongge[i * 3 + 2][j * 3 + 1] = 1
                L_jiugongge[i * 3 + 2][j * 3 + 2] = 1

    for ele in L_jiugongge:
        del ele[-1]
        del ele[-1]
    del L_jiugongge[-1]
    del L_jiugongge[-1]

    return L_jiugongge


L_jiugongge = makejiugongge(L)


# for row in L_jiugongge:
#     print(row)


# 九宫格 end


# Q1
def zhaomen_q1(L):
    siduqiang = [[], [], [], []]
    zuobianqiang = []
    youbianqiang = []
    menshu1 = 0
    menshu2 = 0
    menshu3 = 0
    menshu4 = 0
    menshu = 0
    # 迷宫的四堵墙
    siduqiang[0] = L[0]
    siduqiang[1] = L[-1]
    # 原来生成迷宫的上下两边必定是墙
    for i in range(len(L)):
        zuobianqiang.append(L[i][0])
        youbianqiang.append(L[i][-1])
    siduqiang[2] = zuobianqiang
    siduqiang[3] = youbianqiang
    # print(siduqiang)
    # maze的四堵墙
    for i in range(len(siduqiang[0])):
        if i == len(siduqiang[0]) - 1:
            pass
        else:
            if siduqiang[0][i] == 0 or siduqiang[0][i] == 2:
                menshu1 += 1
                # if not i >= len(siduqiang[0]) - 1:
                #     while siduqiang[0][i + 1] == 0:
                #         i += 1
    for i in range(len(siduqiang[1])):
        if i == len(siduqiang[1]) - 1:
            break
        else:
            if siduqiang[1][i] == 0 or siduqiang[1][i] == 2:
                menshu2 += 1
                # if i<len(siduqiang[1])-1:
                #     while L[-2][i+1]==0 or L[-2][i+1]==1:
                #         i+=1
    for i in range(len(siduqiang[2])):
        if i == len(siduqiang[2]) - 1:
            break
        else:
            if siduqiang[2][i] == 0 or siduqiang[2][i] == 1:
                menshu3 += 1
                # if i<len(siduqiang[2])-1 :
                #     while siduqiang[1][i]==0:
                #         i+=1
    for i in range(len(siduqiang[3])):
        if i == len(siduqiang[3]) - 1:
            break
        else:
            if siduqiang[3][i] == 0 or siduqiang[3][i] == 1:
                menshu4 += 1
    menshu = menshu1 + menshu2 + menshu3 + menshu4
    # print(menshu1)
    # print(menshu2)
    # print(menshu3)
    # print(menshu4)
    print(menshu)


zhaomen_q1(L)
# Q1


# Q2
L_jiugongge_q2 = L_jiugongge.copy()
jiugonggechang = len(L_jiugongge_q2[0])
# 九宫格的长度
jiugonggekuan = len(L_jiugongge_q2)
for row in L_jiugongge_q2:
    print(row)


# 九宫格的宽度
# print(jiugonggechang,jiugonggekuan)
def bianli_q2():
    count_q2 = 0
    for i in range(len(L_jiugongge_q2[0])):
        for j in range(len(L_jiugongge_q2)):
            if L_jiugongge_q2[j][i] == 1:
                explore(i, j)
                count_q2 += 1
    return count_q2

def explore(i, j):
    if i < 0 or i >= len(L_jiugongge_q2[0]) or j < 0 or j >= len(L_jiugongge_q2):
        return 0
    if L_jiugongge_q2[j][i] == 0:
        return 0
    L_jiugongge_q2[j][i] = 0

    directions = [(0,1),(1,0)
        ,(-1,0),(0,-1)]
    for direction_x,direction_y in directions:
        explore(i + direction_x,j + direction_y)

print(bianli_q2())

#q3
def q3():
    count3=0
    for i in range(len(L_jiugongge_q2[0])):
        for j in range(len(L_jiugongge_q2)):
            if L_jiugongge_q2[i][j] == 1:
                count3+=explore3(i, j,count3)
    return count3

def explore3(i,j,count3):
    if i < 0 or i >= len(L_jiugongge_q2[0]) or j < 0 or j >= len(L_jiugongge_q2):
        return 0
    if L_jiugongge_q2[i][j] == 1:
        return 1
    L_jiugongge_q2[i][j] = 0
    explore3(i + 1, j,count3)
    explore3(i - 1, j,count3)
    explore3(i, j + 1,count3)
    explore3(i, j - 1,count3)
# print(bianli_q2())

#q4


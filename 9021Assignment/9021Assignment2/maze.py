import sys
from copy import deepcopy
from sys import setrecursionlimit

sys.setrecursionlimit(100000)


class MazeError(Exception):
    def __init__(self, msg):
        self.msg = msg


class Maze():
    def __init__(self, filename):
        self.filename = filename
        self.L = Maze.openfile(self)

        # print(self.L)
        self.height = len(self.L)
        self.weight = len(self.L[0])
        if self.height < 2:
            raise MazeError('Incorrect input.')
        if self.height > 41:
            raise MazeError('Incorrect input.')
        if self.weight < 2:
            raise MazeError('Incorrect input.')
        if self.weight > 31:
            raise MazeError('Incorrect input.')

        self.fanwei = [1, 2, 3, 0]
        for ele in self.L:
            if len(ele) != self.weight:
                raise MazeError('Incorrect input.')
            # 每行长度不一
            if ele[-1] == 1 or ele[-1] == 3:
                raise MazeError('Input does not represent a maze.')
            # 每行的最后不能是1或3
            for dian in ele:
                if dian not in self.fanwei:
                    raise MazeError('Incorrect input.')
                # 每行的点不是0123中的一个

        if 2 in self.L[-1]:
            raise MazeError('Input does not represent a maze.')
        if 3 in self.L[-1]:
            raise MazeError('Input does not represent a maze.')
        # 最后一行不能出现2或3

        self.jgg = Maze.jiugongge(self)
        self.q5jgg = Maze.Q5jgg(self)
        self.uncutjgg = deepcopy(self.jgg)
        self.jgg = Maze.cutjgg(self)

        # for row in self.q5jgg:
        #     print(row)

        # copy九宫格防止递归变化
        self.jggq2 = deepcopy(self.jgg)
        self.jggq4 = deepcopy(self.jgg)
        self.jggq4 = Maze.cutq4(self)
        # Q4中九宫格去掉三行三列
        self.jggq5 = deepcopy(self.q5jgg)
        self.jggq5 = Maze.cutq5(self)

        # for row in self.q5jgg:
        #     print(row)

        # for row in self.jgg:
        #     print(row)
        # print(self.L)

        # Q1
        self.menzuobiao = []
        self.doornum = Maze.Q1(self)

        # Q1

        # Q2
        self.wallsetnum = Maze.Q2(self)
        # Q2

        # Q4
        self.numofaccarea = Maze.Q4(self)
        # Q4

        # Q3
        # for row in self.jggq4:
        #     print(row)
        # 检查第四问递归过的九宫格是否只剩下走过的路是0
        self.numofinaccarea = Maze.Q3(self)[0]
        self.listinaccareainjgg = Maze.Q3(self)[1]
        # 不可到达点九宫格坐标
        self.listinaccarea = Maze.Q3(self)[2]
        # 不可到达点maze坐标
        # print(self.listinaccarea)
        # print(self.listinaccareainjgg)
        # 无法到达点在九宫格内的坐标
        # Q3

        # Q5
        # for row in self.jggq5:
        #     print(row)

        self.Q5_chulu = Maze.Q5_pre(self)[0]
        self.Q5_nanqiang = Maze.Q5_pre(self)[1]
        self.Q5_luguode = deepcopy(self.Q5_chulu)
        # print('最开始的')
        # for row in self.Q5_chulu:
        #     print(row)
        Maze.Q5(self)
        # print('访问所有3的点 访问过的变成5 墙 Q5_chulu')
        # for row in self.Q5_chulu:
        #     print(row)
        # print('把路过的点 变成8 记录下来  Q5_luguode')
        # for row in self.Q5_luguode:
        #     print(row)
        # print('保留8的那个列表')
        self.q5include8 = deepcopy(self.Q5_luguode)
        # for row in self.q5include8:
        #     print(row)
        self.sihutongshu = Maze.Q5_final(self)
        # for row in self.Q5_luguode:
        #     print(row)
        # Q5

        # Q6
        self.temppath = []
        self.paths = []
        self.temppathdis = []
        self.displaypaths = []
        self.shizhongruyi = []
        self.q5include8 = Maze.Q6_8zuobiao(self)
        self.q6numof0 = deepcopy(self.q5include8)
        self.shizhongruyi = Maze.Q6(self)
        # print(self.shizhongruyi)
        # Q6
        self.mazelist = deepcopy(self.L)

        ###display部分###
        self.lujingtujgg = deepcopy(self.q5include8)
        Maze.displaychuli(self)
        self.zhanshihengxiang = Maze.displaychuli(self)[0]
        self.zhanshizongxiang = Maze.displaychuli(self)[1]
        self.zhuzi = Maze.displaychuli(self)[2]
        self.displaysihutong = Maze.displaychuli(self)[3]
        self.lujingdian = Maze.displaychuli(self)[4]

    def analyse(self):
        # 本方法用来执行所有的操作 最后调用print打印结果
        # print(self.L)
        # Q1找门的个数
        if self.doornum == 0:
            print('The maze has no gate.')
        elif self.doornum == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {self.doornum} gates.')
        # Q1
        # Q2找墙的组数
        if self.wallsetnum == 0:
            print('The maze has no wall.')
        elif self.wallsetnum == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {self.wallsetnum} sets of walls that are all connected.')
        # Q2

        # Q3
        if self.numofinaccarea == 0:
            print('The maze has no inaccessible inner point.')
        elif self.numofinaccarea == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {self.numofinaccarea} inaccessible inner points.')
        # Q3

        # Q4找可到达区域的块数
        if self.numofaccarea == 0:
            print('The maze has no accessible area.')
        elif self.numofaccarea == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {self.numofaccarea} accessible areas.')
        # Q4

        # Q5
        if self.sihutongshu == 0:
            print('The maze has no accessible cul-de-sac.')
        elif self.sihutongshu == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {self.sihutongshu} sets of accessible cul-de-sacs that are all connected.')
        # Q5

        # Q6
        if self.shizhongruyi == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif self.shizhongruyi == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {self.shizhongruyi} entry-exit paths with no intersections not to cul-de-sacs.')
        # Q6

    def openfile(self):
        # 把文件中的内容读出来，读到L中
        L = []
        with open(self.filename) as file:
            for line in file:
                temp = []
                if line.isspace():
                    continue
                # print(line.split())
                for ele_i in line.split():
                    for ele_j in ele_i:
                        temp.append(int(ele_j))
                L.append(temp)
            # print(L) 生成了迷宫的列表

        return L
        # openfile方法最后返回了maze的列表

    def jiugongge(self):
        maze_x = len(self.L[0])
        maze_y = len(self.L)
        jgg = [([0] * maze_x * 3) for i in range(maze_y * 3)]
        for i in range(maze_y):
            for j in range(maze_x):
                if self.L[i][j] == 0:
                    jgg[i * 3][j * 3] = 0
                    jgg[i * 3][j * 3 + 1] = 0
                    jgg[i * 3][j * 3 + 2] = 0
                    jgg[i * 3 + 1][j * 3] = 0
                    jgg[i * 3 + 1][j * 3 + 1] = 0
                    jgg[i * 3 + 1][j * 3 + 2] = 0
                    jgg[i * 3 + 2][j * 3] = 0
                    jgg[i * 3 + 2][j * 3 + 1] = 0
                    jgg[i * 3 + 2][j * 3 + 2] = 0
                if self.L[i][j] == 1:
                    jgg[i * 3][j * 3] = 1
                    jgg[i * 3][j * 3 + 1] = 1
                    jgg[i * 3][j * 3 + 2] = 1
                    jgg[i * 3 + 1][j * 3] = 0
                    jgg[i * 3 + 1][j * 3 + 1] = 0
                    jgg[i * 3 + 1][j * 3 + 2] = 0
                    jgg[i * 3 + 2][j * 3] = 0
                    jgg[i * 3 + 2][j * 3 + 1] = 0
                    jgg[i * 3 + 2][j * 3 + 2] = 0
                if self.L[i][j] == 2:
                    jgg[i * 3][j * 3] = 1
                    jgg[i * 3][j * 3 + 1] = 0
                    jgg[i * 3][j * 3 + 2] = 0
                    jgg[i * 3 + 1][j * 3] = 1
                    jgg[i * 3 + 1][j * 3 + 1] = 0
                    jgg[i * 3 + 1][j * 3 + 2] = 0
                    jgg[i * 3 + 2][j * 3] = 1
                    jgg[i * 3 + 2][j * 3 + 1] = 0
                    jgg[i * 3 + 2][j * 3 + 2] = 0
                if self.L[i][j] == 3:
                    jgg[i * 3][j * 3] = 1
                    jgg[i * 3][j * 3 + 1] = 1
                    jgg[i * 3][j * 3 + 2] = 1
                    jgg[i * 3 + 1][j * 3] = 1
                    jgg[i * 3 + 1][j * 3 + 1] = 0
                    jgg[i * 3 + 1][j * 3 + 2] = 0
                    jgg[i * 3 + 2][j * 3] = 1
                    jgg[i * 3 + 2][j * 3 + 1] = 0
                    jgg[i * 3 + 2][j * 3 + 2] = 0
        for i in range(maze_y - 1):
            for j in range(maze_x - 1):
                if self.L[i][j + 1] == 2 or self.L[i][j + 1] == 3:
                    # 如果这个方块的右边是2或者3的话 那么把自己的最右边的墙也变为1
                    jgg[i * 3][j * 3 + 2] = 1
                    jgg[i * 3 + 1][j * 3 + 2] = 1
                    jgg[i * 3 + 2][j * 3 + 2] = 1
                if self.L[i + 1][j] == 1 or self.L[i + 1][j] == 3:
                    # 如果这个方块的下边是2或者3的话 那么把自己的最下边的墙也变为1
                    jgg[i * 3 + 2][j * 3] = 1
                    jgg[i * 3 + 2][j * 3 + 1] = 1
                    jgg[i * 3 + 2][j * 3 + 2] = 1

        return jgg

    def cutjgg(self):
        for ele in self.jgg:
            del ele[-1]
            del ele[-1]
        del self.jgg[-1]
        del self.jgg[-1]
        return self.jgg

    def Q5jgg(self):
        maze_x = len(self.L[0])
        maze_y = len(self.L)
        Q5jgg = [([0] * maze_x * 3) for i in range(maze_y * 3)]
        for i in range(maze_y):
            for j in range(maze_x):
                if self.L[i][j] == 0:
                    Q5jgg[i * 3][j * 3] = 1
                    Q5jgg[i * 3][j * 3 + 1] = 0
                    Q5jgg[i * 3][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 1][j * 3] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 2] = 0
                    Q5jgg[i * 3 + 2][j * 3] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1
                if self.L[i][j] == 1:
                    Q5jgg[i * 3][j * 3] = 1
                    Q5jgg[i * 3][j * 3 + 1] = 1
                    Q5jgg[i * 3][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 1][j * 3] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 2] = 0
                    Q5jgg[i * 3 + 2][j * 3] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1
                if self.L[i][j] == 2:
                    Q5jgg[i * 3][j * 3] = 1
                    Q5jgg[i * 3][j * 3 + 1] = 0
                    Q5jgg[i * 3][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 1][j * 3] = 1
                    Q5jgg[i * 3 + 1][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 2] = 0
                    Q5jgg[i * 3 + 2][j * 3] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1
                if self.L[i][j] == 3:
                    Q5jgg[i * 3][j * 3] = 1
                    Q5jgg[i * 3][j * 3 + 1] = 1
                    Q5jgg[i * 3][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 1][j * 3] = 1
                    Q5jgg[i * 3 + 1][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 1][j * 3 + 2] = 0
                    Q5jgg[i * 3 + 2][j * 3] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 1] = 0
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1
        for i in range(maze_y - 1):
            for j in range(maze_x - 1):
                if self.L[i][j + 1] == 2 or self.L[i][j + 1] == 3:
                    # 如果这个方块的右边是2或者3的话 那么把自己的最右边的墙也变为1
                    Q5jgg[i * 3][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 1][j * 3 + 2] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1
                if self.L[i + 1][j] == 1 or self.L[i + 1][j] == 3:
                    # 如果这个方块的下边是2或者3的话 那么把自己的最下边的墙也变为1
                    Q5jgg[i * 3 + 2][j * 3] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 1] = 1
                    Q5jgg[i * 3 + 2][j * 3 + 2] = 1

        return Q5jgg

    def cutq4(self):
        for ele in self.jggq4:
            del ele[-1]
        del self.jggq4[-1]
        return self.jggq4
        # Q4要减去三行三列做 不然maze1右下角那边不一样

    def cutq5(self):
        for ele in self.q5jgg:
            del ele[-1]
            del ele[-1]
        del self.q5jgg[-1]
        del self.q5jgg[-1]
        return self.q5jgg

    def Q1(self):
        siduqiang = [[], [], [], []]
        # 放置四堵墙的情况
        leftwall = []
        rightwall = []
        menshu1 = 0
        menshu2 = 0
        menshu3 = 0
        menshu4 = 0
        menshu = 0
        # 迷宫的四堵墙分开计数
        siduqiang[0] = self.L[0]
        siduqiang[1] = self.L[-1]
        # 上下两堵墙是原来maze的第一和最后一个元素
        for i in range(len(self.L)):
            leftwall.append(self.L[i][0])
            # 左边的墙是maze中每个列表的第一个元素
            rightwall.append(self.L[i][-1])
            # 右边的墙是maze中每个列表的最后一个元素
        siduqiang[2] = leftwall
        siduqiang[3] = rightwall
        # maze的四堵墙都被放进了列表
        for i in range(len(siduqiang[0])):
            if i == len(siduqiang[0]) - 1:
                break
            else:
                if siduqiang[0][i] == 0 or siduqiang[0][i] == 2:
                    self.menzuobiao.append([i, 0])
                    menshu1 += 1
        # 上面的墙
        for i in range(len(siduqiang[1])):
            if i == len(siduqiang[1]) - 1:
                break
            else:
                if siduqiang[1][i] == 0 or siduqiang[1][i] == 2:
                    self.menzuobiao.append([i, len(self.L) - 1])
                    menshu2 += 1
        # 下面的墙
        for i in range(len(siduqiang[2])):
            if i == len(siduqiang[2]) - 1:
                break
            else:
                if siduqiang[2][i] == 0 or siduqiang[2][i] == 1:
                    self.menzuobiao.append([i, 0])
                    menshu3 += 1
        # 左边的墙
        for i in range(len(siduqiang[3])):
            if i == len(siduqiang[3]) - 1:
                break
            else:
                if siduqiang[3][i] == 0 or siduqiang[3][i] == 1:
                    self.menzuobiao.append([len(self.L[0]) - 1, i])
                    menshu4 += 1
        # 右边的墙
        menshu = menshu1 + menshu2 + menshu3 + menshu4
        return menshu

    def Q2(self):
        num_of_wallset = 0
        for i in range(len(self.jggq2[0])):
            for j in range(len(self.jggq2)):
                if self.jggq2[j][i] == 1:
                    Maze.Q2_explore(self, i, j)
                    num_of_wallset += 1
        return num_of_wallset

    def Q2_explore(self, i, j):
        if i < 0 or i >= len(self.jggq2[0]) or j < 0 or j >= len(self.jggq2):
            return 0
        if self.jggq2[j][i] == 0:
            return 0
        self.jggq2[j][i] = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for direction_x, direction_y in directions:
            Maze.Q2_explore(self, i + direction_x, j + direction_y)

    def Q4(self):
        # for r in self.jggq4:
        #     print(r)
        num_of_acc_area = 0
        for i in range(len(self.jggq4[0])):
            for j in range(len(self.jggq4)):
                if (j == 0) or (i == 0) or (i == len(self.jggq4[0]) - 1) or (j == len(self.jggq4) - 1):
                    # 这里遍历了四堵围墙 对于等于0的部分开始遍历 找到可到达的区域
                    if self.jggq4[j][i] == 0:
                        Maze.Q4_explore(self, i, j)
                        num_of_acc_area += 1
        # for r in self.jggq4:
        #     print(r)
        return num_of_acc_area

    def Q4_explore(self, i, j):
        if i < 0 or i >= len(self.jggq4[0]) or j < 0 or j >= len(self.jggq4):
            return 0
        if self.jggq4[j][i] == 1:
            return 0
        self.jggq4[j][i] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for direction_x, direction_y in directions:
            Maze.Q4_explore(self, i + direction_x, j + direction_y)

    def Q3(self):
        num_of_inaccarea = 0
        listofinaccarea = []
        list_Q3_result = []
        listinaccareainjgg = []
        # print(len(self.jggq4[0]))
        for i in range(len(self.jggq4[0])):
            for j in range(len(self.jggq4)):
                if self.jggq4[j][i] == 0:
                    listofinaccarea.append([i, j])
            # 找出Q4中走完以后的图中剩下的点
        listinaccareainjgg = deepcopy(listofinaccarea)
        # 保存下来不可到达的点
        # print(listinaccareainjgg)
        for ele in listofinaccarea:
            ele[0] = ele[0] // 3
            ele[1] = ele[1] // 3
            # 把横坐标都整除三 变为九宫格的都会变成一样的整数
        for ele in listofinaccarea:
            if ele not in list_Q3_result:
                list_Q3_result.append(ele)
            # 去重操作得到原本maze中不可到达点的做标的集合
        num_of_inaccarea = len(list_Q3_result)
        # 求数组长度得到个数
        # for row in self.jggq4:
        #     print(row)
        return num_of_inaccarea, listinaccareainjgg, list_Q3_result

    def Q5_pre(self):
        self.jggq5[0][0] = 1
        self.jggq5[-1][-1] = 1
        # 保证四个角是1 其实是多余的
        for ele in self.listinaccareainjgg:
            self.jggq5[ele[1]][ele[0]] = 1
        # 把访问不到的区域（之前求的）全部设置为墙体
        jgg_chulu = deepcopy(self.jggq5)
        # for row in jgg_chulu:
        #     print(row)
        # print('[2,0]', self.jggq5[2][0])
        # print('[0,2]', self.jggq5[0][2])
        for x in range(len(jgg_chulu[0])):
            for y in range(len(jgg_chulu)):
                if self.jggq5[y][x] == 1:
                    jgg_chulu[y][x] = 5
                else:
                    jgg_chulu[y][x] = 0
        # 把墙变成5
        # for row in jgg_chulu:
        #     print(row)
        # print()
        # for row in self.jggq5:
        #     print(row)
        for x in range(len(self.jggq5[0])):
            for y in range(len(self.jggq5)):
                if jgg_chulu[y][x] == 0:
                    if y + 1 < len(self.jggq5) and self.jggq5[y + 1][x] == 1:
                        jgg_chulu[y][x] += 1
                    if y - 1 >= 0 and self.jggq5[y - 1][x] == 1:
                        jgg_chulu[y][x] += 1
                    if x + 1 < len(self.jggq5[0]) and self.jggq5[y][x + 1] == 1:
                        jgg_chulu[y][x] += 1
                    if x - 1 >= 0 and self.jggq5[y][x - 1] == 1:
                        jgg_chulu[y][x] += 1
        # 把chulu这个列表的每个元素设置成当前坐标周围四个地方的1的个数

        # for row in jgg_chulu:
        #     print(row)
        # print()
        nanqiang = []
        for x in range(len(jgg_chulu[0])):
            for y in range(len(jgg_chulu)):
                if jgg_chulu[y][x] == 3:
                    nanqiang.append([x, y])
        # 如果是周围有三个的话 就是死胡同的最后一步 找出这些地方
        # print(nanqiang)
        return jgg_chulu, nanqiang

    def Q5(self):
        num_of_sihutong = 0
        for i in range(len(self.Q5_chulu[0])):
            for j in range(len(self.Q5_chulu)):
                if self.Q5_chulu[j][i] == 3:
                    # self.Q5_chulu[j][i]=9
                    # 测试是否遍历了所有的3
                    Maze.Q5_explore(self, i, j)

    def Q5_explore(self, i, j):
        if i < 0 or i >= len(self.Q5_chulu[0]) or j < 0 or j >= len(self.Q5_chulu):
            return 0
        countq5 = 0
        if j + 1 < len(self.Q5_chulu) and self.Q5_chulu[j + 1][i] == 5:
            countq5 += 1
        if j - 1 >= 0 and self.Q5_chulu[j - 1][i] == 5:
            countq5 += 1
        if i + 1 < len(self.Q5_chulu[0]) and self.Q5_chulu[j][i + 1] == 5:
            countq5 += 1
        if i - 1 >= 0 and self.Q5_chulu[j][i - 1] == 5:
            countq5 += 1
        if countq5 <= 2:
            return 0
        # 数当前格子周围几堵墙

        if self.Q5_chulu[j][i] == 5:
            return 0
        if self.Q5_chulu[j][i] == 8:
            return 0
        self.Q5_chulu[j][i] = 5
        self.Q5_luguode[j][i] = 8
        Maze.Q5_explore(self, i + 1, j)
        Maze.Q5_explore(self, i - 1, j)
        Maze.Q5_explore(self, i, j + 1)
        Maze.Q5_explore(self, i, j - 1)
        # 这里遍历完之后 整个luguode这个列表所有的8都是 死胡同通过的路径

    def Q5_final(self):
        num_of_sihutong = 0
        for i in range(len(self.Q5_luguode[0])):
            for j in range(len(self.Q5_luguode)):
                if self.Q5_luguode[j][i] == 8:
                    Maze.Q5_final_explore(self, i, j)
                    num_of_sihutong += 1

        return num_of_sihutong
        # 找出所有8的点的集合的个数

    def Q5_final_explore(self, i, j):
        if i < 0 or i >= len(self.Q5_luguode[0]) or j < 0 or j >= len(self.Q5_luguode):
            return 0
        if self.Q5_luguode[j][i] != 8:
            return 0
        self.Q5_luguode[j][i] = 5
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for direction_x, direction_y in directions:
            Maze.Q5_final_explore(self, i + direction_x, j + direction_y)

    def Q6_8zuobiao(self):
        for i in range(len(self.q5include8[0])):
            for j in range(len(self.q5include8)):
                if self.q5include8[j][i] == 5:
                    self.q5include8[j][i] = 1
                elif self.q5include8[j][i] != 8:
                    self.q5include8[j][i] = 0
        # print('改过以后')
        # for r in self.q5include8:
        #     print(r)
        return self.q5include8

    def Q6(self):
        # print('改过以后')
        # for r in self.q5include8:
        #     print(r)
        num_of_paths = 0
        num_of_0 = 0

        for i in range(len(self.q6numof0[0])):
            for j in range(len(self.q6numof0)):
                self.q6numof0[j][i] == 0
        for x in range(len(self.q5include8[0])):
            for y in range(len(self.q5include8)):
                if self.q6numof0[y][x] == 0:
                    if y + 1 < len(self.q5include8) and self.q5include8[y + 1][x] == 0:
                        self.q6numof0[y][x] += 1
                    if y - 1 >= 0 and self.q5include8[y - 1][x] == 0:
                        self.q6numof0[y][x] += 1
                    if x + 1 < len(self.q5include8[0]) and self.q5include8[y][x + 1] == 0:
                        self.q6numof0[y][x] += 1
                    if x - 1 >= 0 and self.q5include8[y][x - 1] == 0:
                        self.q6numof0[y][x] += 1
        # 找出每个周围有几个方向 大于三个证明有岔路 那么等下把它变成9 封住
        # print('0的个数')
        # for r in self.q6numof0:
        #     print(r)
        for i in range(len(self.q6numof0[0])):
            for j in range(len(self.q6numof0)):
                if self.q6numof0[j][i] == 3 or self.q6numof0[j][i] == 4:
                    self.q5include8[j][i] = 9
        # 把岔路口都改成9 这样接下来只要路径中有两个门的 都是唯一无岔路的通路
        # for r in self.q5include8:
        #     print(r)
        # 找门
        menzuobiao = Maze.zhaomendezuobiao(self)
        # print('门的坐标')
        # print(menzuobiao)

        for x in range(len(self.q5include8[0])):
            for y in range(len(self.q5include8)):
                if self.q5include8[y][x] == 0 and (
                        x == 0 or y == 0 or x == len(self.q5include8[0]) - 1 or y == len(self.q5include8) - 1):
                    Maze.Q6_explore(self, x, y)
                    num_of_paths += 1
                    self.paths.append(self.temppath)
                    self.displaypaths.append(self.temppathdis)
                    self.temppath = []
                    self.temppathdis = []
                    # 算出的path包含了岔路
        # 这里之所以要减 是因为每一个岔路都有三个0 就是岔路口 需要予以剔除
        # print(self.paths)
        # print('做完以后')
        # for r in self.q5include8:
        #     print(r)

        for lu in self.paths:
            menshu = 0
            for men in menzuobiao:
                if men in lu:
                    menshu += 1
            if menshu == 2:
                self.shizhongruyi.append(lu)
        # print('结果')
        # print(self.shizhongruyi)
        for ele in self.shizhongruyi:
            for dian in ele:
                self.q5include8[dian[1]][dian[0]] = 7
        # for r in self.q5include8:
        #     print(r)

        return len(self.shizhongruyi)

    def Q6_explore(self, x, y):
        if x < 0 or x >= len(self.q5include8[0]) or y < 0 or y >= len(self.q5include8):
            return 0
        if self.q5include8[y][x] != 0:
            return 0
        self.temppath.append((x, y))
        self.temppathdis.append([x, y])
        self.q5include8[y][x] = 6
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for direction_x, direction_y in directions:
            Maze.Q6_explore(self, x + direction_x, y + direction_y)

    def zhaomendezuobiao(self):
        menzuobiao = []
        for i in range(len(self.q5include8[0])):
            for j in range(len(self.q5include8)):
                if (j == 0) or (i == 0) or (i == len(self.q5include8[0]) - 1) or (j == len(self.q5include8) - 1):
                    # 这里遍历了四堵围墙 对于等于0的部分开始遍历 找到可到达的区域
                    if self.q5include8[j][i] == 0:
                        menzuobiao.append((i, j))
        return menzuobiao

    def displaychuli(self):

        #####画墙#####
        # for row in self.L:
        #     print(row)
        # print(self.L[2][0])
        # print(self.L[0][2])
        mazehengxiang = deepcopy(self.L)
        mazezongxiang = deepcopy(self.L)

        for x in range(len(self.L)):
            for y in range(len(self.L[0])):
                if self.L[x][y] == 1 or self.L[x][y] == 3:
                    mazehengxiang[x][y] = 1
                else:
                    mazehengxiang[x][y] = 0
        # print('迷宫横向情况')
        # for r in mazehengxiang:
        #    print(r)
        hengxiang = []
        for x in range(len(mazehengxiang)):
            for y in range(len(mazehengxiang[0])):
                if mazehengxiang[x][y] == 1:
                    hengxiang.append([y, x])
        # print('需要画横线')
        # print(hengxiang)
        zhanshihengxiang = []
        for ele in hengxiang:
            # print(ele)
            x = ele[0]
            y = ele[1]
            x_init = x
            while [x + 1, y] in hengxiang:
                hengxiang.remove([x + 1, y])
                x += 1
            else:
                zhanshihengxiang.append([[x_init, y], [x + 1, y]])
        # print('横向输出')
        # print(zhanshihengxiang)

        for x in range(len(self.L)):
            for y in range(len(self.L[0])):
                if self.L[x][y] == 2 or self.L[x][y] == 3:
                    mazezongxiang[x][y] = 1
                else:
                    mazezongxiang[x][y] = 0
        zongxiang = []
        for y in range(len(mazezongxiang[0])):
            for x in range(len(mazezongxiang)):
                if mazezongxiang[x][y] == 1:
                    zongxiang.append([y, x])
        # print('迷宫纵向情况')
        # for r in mazezongxiang:
        #    print(r)
        # print('需要画竖线')
        # print(zongxiang)
        zhanshizongxiang = []
        for ele in zongxiang:
            # print(ele)
            x = ele[0]
            y = ele[1]
            y_init = y
            while [x, y + 1] in zongxiang:
                zongxiang.remove([x, y + 1])
                y += 1
            else:
                zhanshizongxiang.append([[x, y_init], [x, y + 1]])
        # print('纵向输出')
        # print(zhanshizongxiang)
        #####画墙#####

        #####画柱子#####
        zhuzi = []
        for x in range(len(self.L)):
            for y in range(len(self.L[0])):
                tag = 0
                # print(self.L[x][y])
                if self.L[x][y] == 0:
                    if x - 1 < 0 or self.L[x - 1][y] == 0 or self.L[x - 1][y] == 1:
                        tag += 1
                    if y - 1 < 0 or self.L[x][y - 1] == 2 or self.L[x][y - 1] == 0:
                        tag += 1
                    if tag == 2:
                        zhuzi.append([y, x])
        # print('柱子是')
        # print(zhuzi)
        #####画柱子#####

        #####画死胡同#####
        sihutongjgg = []

        # for row in self.q5include8:
        #     print(row)
        for y in range(1, len(self.q5include8) - 1, 3):
            for x in range(1, len(self.q5include8[0]) - 1, 3):
                if self.q5include8[y][x] == 8:
                    sihutongjgg.append([x // 3 + 0.5, y // 3 + 0.5])
        # print('死胡同')
        # print(sihutongjgg)
        #####画死胡同#####

        ####画路径#####
        xianshilujing = []
        for y in range(1, len(self.q5include8) - 1, 3):
            for x in range(1, len(self.q5include8[0]) - 1, 3):
                if self.q5include8[y][x] == 7:
                    xianshilujing.append([x // 3, y // 3])

        # print('路径')
        # print(xianshilujing)

        return zhanshihengxiang, zhanshizongxiang, zhuzi, sihutongjgg, xianshilujing

    def display(self):
        filenamesplit=self.filename.split('.')
        #print(filenamesplit[0])
        filenamefinal=filenamesplit[0]+'.tex'
        #print(filenamefinal)
        with open(filenamefinal, 'w') as displayfile:
            displayfile.write('\\documentclass[10pt]{article}\n')
            displayfile.write('\\usepackage{tikz}\n')
            displayfile.write('\\usetikzlibrary{shapes.misc}\n')
            displayfile.write('\\usepackage[margin=0cm]{geometry}\n')
            displayfile.write('\\pagestyle{empty}\n')
            displayfile.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
            displayfile.write('\n')
            displayfile.write('\\begin{document}\n')
            displayfile.write('\n')
            displayfile.write('\\vspace*{\\fill}\n')
            displayfile.write('\\begin{center}\n')
            displayfile.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')

            ###展示墙###
            displayfile.write('% Walls\n')
            # print(self.zhanshihengxiang)
            # print(self.zhanshizongxiang)
            for ele in self.zhanshihengxiang:
                x1 = ele[0][0]
                y1 = ele[0][1]
                x2 = ele[1][0]
                y2 = ele[1][1]
                displayfile.write(f'    \\draw ({x1},{y1}) -- ({x2},{y2});\n')
            for ele in self.zhanshizongxiang:
                x1 = ele[0][0]
                y1 = ele[0][1]
                x2 = ele[1][0]
                y2 = ele[1][1]
                displayfile.write(f'    \\draw ({x1},{y1}) -- ({x2},{y2});\n')
            ###展示墙###

            ###展示柱子###
            displayfile.write('% Pillars\n')
            # print(self.zhuzi)
            for ele in self.zhuzi:
                x = ele[0]
                y = ele[1]
                displayfile.write(f'    \\fill[green] ({x},{y}) circle(0.2);\n')
            ###展示柱子###

            ###展示死胡同###
            displayfile.write('% Inner points in accessible cul-de-sacs\n')
            # print(self.displaysihutong)
            for ele in self.displaysihutong:
                x = ele[0]
                y = ele[1]
                displayfile.write(f'    \\node at ({x},{y}) ' + '{};\n')
            ###展示死胡同###

            ###展示路径###
            displayfile.write('% Entry-exit paths without intersections\n')
            heng = []
            arranged_heng = []
            zong = []
            arranged_zong = []
            men = []
            temp = []
            # for r in self.q5include8:
            #     print(r)
            for y in range(len(self.q5include8)):
                for x in range(len(self.q5include8[0])):
                    if self.q5include8[y][x] == 7 and (
                            y == 0 or x == 0 or y == len(self.q5include8) - 1 or x == len(self.q5include8[0]) - 1):
                        men.append((x // 3, y // 3))
            # print('新门')
            # print(men)
            # print('九宫格')
            # for r in self.q5include8:
            #     print(r)
            # for r in self.L:
            #     print(r)

            for i in range(len(self.q5include8)):
                for j in range(len(self.q5include8[0]) - 1):
                    if self.q5include8[i][j] == 7:
                        if self.q5include8[i][j + 1] == 7 and (i // 3, j // 3) not in heng:
                            heng.append((i // 3, j // 3))
            # print('横向raw')
            # print(heng)
            for j in range(len(self.q5include8[0])):
                for i in range(len(self.q5include8) - 1):
                    if self.q5include8[i][j] == 7 and self.q5include8[i + 1][j] == 7 and (i // 3, j // 3) not in zong:
                        zong.append((i // 3, j // 3))
            # print('纵向raw')
            # print(zong)

            for ele in heng:
                x = ele[0]
                y = ele[1]
                if ele not in temp:
                    temp.append((y, x))

                if self.q5include8[x * 3 + 1][y * 3 + 1] == 7:
                    if y < (len(self.L[0])):
                        if self.q5include8[x * 3 + 1][(y + 1) * 3] == 7:
                            if (x, y + 1) not in heng:
                                arranged_heng.append(temp)
                                temp = []
                            else:
                                temp.append((y + 1, x))
                        else:
                            arranged_heng.append(temp)
                            temp = []
            # print('')
            # print(arranged_heng)

            for ele in zong:
                x = ele[0]
                y = ele[1]
                if ele not in temp:
                    temp.append((y, x))

                if self.q5include8[x * 3 + 1][y * 3 + 1] == 7:
                    if y < (len(self.L[0])):
                        if self.q5include8[(x + 1) * 3][y * 3 + 1] == 7:
                            if (x + 1, y) not in zong:
                                arranged_zong.append(temp)
                                temp = []
                            else:
                                temp.append((y, x + 1))
                        else:
                            arranged_zong.append(temp)
                            temp = []
            #print('')
            ## print(arranged_zong)
            output_heng = []
            output_zong = []
            for ele in arranged_heng:
                if len(ele) >= 2:
                    temp.append(ele[0])
                    temp.append(ele[-1])
                else:
                    temp.append(ele[0])
                output_heng.append(temp)
                temp = []
            #print(output_heng)

            for ele in arranged_zong:
                if len(ele) >= 2:
                    temp.append(ele[0])
                    temp.append(ele[-1])
                else:
                    temp.append(ele[0])
                output_zong.append(temp)
                temp = []
            #print(output_zong)

            ###继续输出###
            for ele in output_heng:
                x1 = ele[0][0]
                y1 = ele[0][1]
                x2 = ele[-1][0]
                y2 = ele[-1][1]
                if self.q5include8[y1*3+1][x1*3]==7:
                    #这里查看是否存在下一个是门的情况 即联通了边缘
                    x = x1 - 0.5
                    y = y1 + 0.5
                    displayfile.write(f'    \\draw[dashed, yellow] ({x},{y})')
                else:
                    x = x1 + 0.5
                    y = y1 + 0.5
                    displayfile.write(f'    \\draw[dashed, yellow] ({x},{y})')
                if self.q5include8[y2*3+1][x2*3+2]==7:
                    x = x2 + 1.5
                    y = y2 + 0.5
                    displayfile.write(f' -- ({x},{y});\n')
                else:
                    x = x2 + 0.5
                    y = y2 + 0.5
                    displayfile.write(f' -- ({x},{y});\n')

            for ele in output_zong:
                x1=ele[0][0]
                y1=ele[0][1]
                x2=ele[-1][0]
                y2=ele[-1][1]
                if self.q5include8[y1*3][x1*3+1]==7:
                    x = x1 + 0.5
                    y = y1 - 0.5
                    displayfile.write(f'    \\draw[dashed, yellow] ({x},{y})')
                else:
                    x = x1 + 0.5
                    y = y1 + 0.5
                    displayfile.write(f'    \\draw[dashed, yellow] ({x},{y})')
                if self.q5include8[y2*3+2][x2*3+1]==7:
                    x = x2 + 0.5
                    y = y2 + 1.5
                    displayfile.write(f' -- ({x},{y});\n')
                else:
                    x = x2 + 0.5
                    y = y2 + 0.5
                    displayfile.write(f' -- ({x},{y});\n')



            # print('路径点')
            # print(self.lujingdian)
            # print('门坐标')
            # print(self.menzuobiao)

            ###展示路径###

            displayfile.write('\\end{tikzpicture}\n')
            displayfile.write('\\end{center}\n')
            displayfile.write('\\vspace*{\\fill}\n')
            displayfile.write('\n')
            displayfile.write('\\end{document}\n')


maze = Maze('maze_1.txt')
# #maze = Maze('Ricky_58.txt')
# #maze = Maze('Ricky_58.txt')
# maze= Maze('not_a_maze_2.txt')
maze.analyse()
maze.display()

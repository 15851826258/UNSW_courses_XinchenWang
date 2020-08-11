#定义一个方块 每次可以东南西北四个方向走 但是只能路过1的地方 问题是找出两点间最长的路径


X=[[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,1],[0,1,0,0,1],[0,1,1,1,1]]

def paths_from_to(pt_1,pt_2):
    x_1, y_1 = pt_1
    x_2, y_2 = pt_2
    if not (0 <= x_1 < 5 and 0 <= y_1 < 5) or not (0 <= x_2 < 5 and 0 <= y_2 < 5):
        return []
    if not X[x_1][y_1]:
        return []
    if pt_1 == pt_2:
        return [[pt_2]]
    paths = [None] * 4
    X[x_1][y_1] = 0
    paths[0] = paths_from_to((x_1 - 1, y_1), (x_2, y_2))
    paths[1] = paths_from_to((x_1 + 1, y_1), (x_2, y_2))
    paths[2] = paths_from_to((x_1, y_1 - 1), (x_2, y_2))
    paths[3] = paths_from_to((x_1, y_1 + 1), (x_2, y_2))
    X[x_1][y_1] = 1
    print(paths)
    return [[(x_1, y_1)] + path for i in range(4) for path in paths[i]]

P = paths_from_to((2,2),(0,0))
print()
print(P)
print(len(P))


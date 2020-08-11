import sys
#CODE FROM XINCHEN WANG LOUIS for 9021
try:
    file_name=str(input('Which data file do you want to use? '))
    file_object = open(file_name)
    file_context = file_object.read()
    file_context = file_context.split()
except IOError:
    print('There is no file with that name in the working directory! ')
    sys.exit()
#防止没有这个文件

if file_context:
    pass
else:
    print('The file is empty,giving up!')
    sys.exit()
#防止文件是空的

try:
    sum_of_water = int(input('How many decilitres of water do you want to pour down? '))
    if sum_of_water < 0:
        raise ValueError
except ValueError:
    print('Incorrect input,giving up.')
    sys.exit()
#防止水的量是负数或者字母


pool = []
# 新建目标池
# 将文件的格式规范化成为一个列表(其中的元素是字符串)
try:
    for a in range(len(file_context)):
        pool.append(int(file_context[a]))
except ValueError:
    print()
    sys.exit()

# 得到了所有数字组成的数组



lowest = 0
second_lowest = 0
water_used = 0
rest_water = 0
height = 0
raise_height = 0
result = 0

def rain(total_water, pool):
    lowest = min(pool)
    if len(list(set(pool)))>1:
        second_lowest = sorted(list(set(pool)))[1]
        water_used = (second_lowest - lowest) * (pool.count(lowest))
        rest_water = total_water - water_used
    else:
        #平原的情况，即找不到倒数第二的高度
        second_lowest=lowest
        height=total_water/(pool.count(lowest))
        raise_height=height+lowest
        return raise_height
    rest_water = total_water - water_used
    if rest_water < 0:
        height = total_water / pool.count(lowest)
        raise_height = lowest + height
        return raise_height
        # 如果剩下的水不够填到倒数第二个高度了，那么算一下从目前最低的到现在能填多高
    elif rest_water > 0:
        for a in range(len(pool)):
            if pool[a] == lowest:
                # 遍历把最低水位添加到倒数第二水位
                pool[a] = second_lowest
        return rain(rest_water, pool)
        # 如果还有水的话，统计一下现在池子跟水的情况，然后调回函数继续走
    else:
        raise_height = second_lowest
        return raise_height
        # 如果刚好用完的话，就倒数第二高的情况作为最后的高度

print('The water rises to {:.2f}'.format(rain(sum_of_water, pool))+' centimetres.')



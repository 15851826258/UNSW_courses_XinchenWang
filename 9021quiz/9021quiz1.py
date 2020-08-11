# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

# Written by XINCHEN WANG for COMP9021
List_of_X = list(map(int, str(x)))
#把数字转换成list形式
for index1 in range(len(List_of_X)):
    sum_of_digits_in_x = sum_of_digits_in_x + List_of_X[index1]
# 之后累加得到结果
# get the sum of all digits in X

for index2 in range(len(L)):
    length_of_digits = len(str(L[index2]))
    first_digit = (L[index2]) // (10 ** (length_of_digits - 1))
    #通过和10取商得到了首位数
    last_digit = L[index2] % 10
    # 取到首尾位数 然后通过大小比较得到结果
    if first_digit > last_digit:
        first_digit_greater_than_last += 1
    elif last_digit == first_digit:
        same_first_and_last_digits += 1
    else:
        last_digit_greater_than_first += 1
# first digit that is greater than the last digit, equal to the last digit,and smaller than the last digit,


for index3 in range(len(L)):
    set_of_nums = set(str(L[index3]))
    list_without_same_num = [i for i in set_of_nums]
    distinct_digits[len(list_without_same_num)] += 1
# get the distinct_digits

min_gap = 9
max_gap = 0
list_of_difference = [0] * len(L)
for index4 in range(len(L)):
    length_of_digits = len(str(L[index4]))
    first_digit = (L[index4]) // (10 ** (length_of_digits - 1))
    # 首位就是用10的位数减1次方取整得到
    last_digit = L[index4] % 10
    # 末尾直接和10取余就行了
    if first_digit > last_digit:
        difference_btw_first_and_last_digit = first_digit - last_digit
    elif last_digit > first_digit:
        difference_btw_first_and_last_digit = last_digit - first_digit
    else:
        difference_btw_first_and_last_digit = 0
    list_of_difference[index4] = difference_btw_first_and_last_digit
    # 比大小之后用最大最小值方法快速取出来
max_gap = max(list_of_difference)
min_gap = min(list_of_difference)
# to get the minimal gap and the maximal gap

dict = {}
for index5 in range(len(L)):
    length_of_digits = len(str(L[index5]))
    first_digit = (L[index5]) // (10 ** (length_of_digits - 1))
    last_digit = L[index5] % 10
    if (first_digit, last_digit) in dict:
        dict[(first_digit, last_digit)] += 1
    else:
        dict[(first_digit, last_digit)] = 1
max_key = max(dict, key=dict.get)
# 取出最大值对应的key
max_value = dict[max_key]
# 取出最大值对应的value
for index6 in range(len(dict)):
    max_key = max(dict, key=dict.get)
    # 取出当前字典中剩下最大值的key
    if dict[max_key] == max_value:
        # 如果这个key对应的value跟之前找的一样 那么表示这两个都是最大值对应的key 插入
        first_and_last.add(max_key)
        del dict[max_key]
        # 插入之后从字典里删掉这个记录过的的key
    else:
        break
# to finish the last problem

print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
      )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
      )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
      )

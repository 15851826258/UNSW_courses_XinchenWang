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


sum_of_digits_in_x = sum([int(i) for i in str(x)])
for e in L:
    if int(str(e)[0]) - int(str(e)[-1]) > 0:
        first_digit_greater_than_last += 1
    else:
        if int(str(e)[0]) - int(str(e)[-1]) == 0:
            same_first_and_last_digits += 1
        else:
            last_digit_greater_than_first += 1

p = []
dd=set()
distinct_digits=[0]*10
T=L.copy()
for i in range(0, len(L)):
    while T[i] != 0:
        dd.add(T[i] % 10)
        T[i]=T[i]//10
    distinct_digits[len(dd)-1]+=1
    dd.clear()

    #len(dd)不同的位数
 
M=L.copy()
min_gap = 10
for e in L:
    gap = abs(int(str(e)[0]) - int(str(e)[-1]))
    if gap < min_gap:
        min_gap = gap
max_gap = -1
for e in L:
    gap = abs(int(str(e)[0]) - int(str(e)[-1]))
    if gap > max_gap:
        max_gap = gap

l0 = []
for e in L:
    l1 = (int(str(e)[0]), int(str(e)[-1]))
    l0.append(l1)

l2 = []
for i in range(0, len(l0)):
    l2.append(str(l0[i]))

max_num = 0
for i in range(0, len(l2)):
    num = l2.count(l2[i])
    if num > max_num:
        max_num = num
l_last = []
for i in range(0, len(l2)):
    num = l2.count(l2[i])
    if num == max_num:
        l_last.append(l0[i])
for c in range(0, len(l_last)):
    first_and_last.add(l_last[c])



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
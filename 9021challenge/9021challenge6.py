# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.
#找完美数 例如1+2+4+7+14=28

import sys

#code by XINCHEN WANG for 9021
try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

count=int(1) #循环从2开始 所以要加上1也是因数
for i in range(2, N + 1):
    sum_of_divisor=0
    for tstnum in range(1,i+1):
        if i % tstnum == 0 and i!=tstnum: #如果可以整除 且不是该数字本身（商不为1）
            sum_of_divisor+=tstnum
        else:
            pass
    if sum_of_divisor==i:
        print(f'{i} is a perfect number.')


    # Replace pass above with your code to check whether i is perfect,
    # and print out that it is in case it is.
    # 1 divides i, so counts for one divisor.
    # It is enough to look at 2, ..., i // 2 as other potential divisors.
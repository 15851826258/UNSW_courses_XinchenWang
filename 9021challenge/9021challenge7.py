# Written by XINCHEN WANG for COMP9021

import sys
for x in range(100,1000):
    for y in range(10,100):
        if x * (y % 10) in range(1000, 10000) and x * (y // 10) in range(100, 1000) and x * y in range(1000, 10000):
            a = x * (y % 10)
            # 横线下面第一个数
            b = x * (y // 10)
            # 横线下面第二个数
            sum1 = x % 10 + y % 10 + a % 10 + (x * y) % 10
            sum2 = (x // 10) % 10 + y // 10 + (a // 10) % 10 + b % 10 + ((x * y) // 10) % 10
            sum3 = x // 100 + (a // 100) % 10 + (b // 10) % 10 + ((x * y) // 100) % 10
            sum4 = a // 1000 + b // 100 + (x * y) // 1000
            if sum1 == sum2 and sum2 == sum3 and sum3 == sum4:
                print(f'{x} * {y} = {x*y}, all columns adding up to {sum1}'+'.')







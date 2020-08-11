# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint
from math import gcd

try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE
#code by XINCHEN WANG for 9021


dict_for_simplest_fraction={}
dict_for_complex_fraction={}
max_sum_of_nums=0
max_simplest_numerator=0
max_simplest_denominator=0
for e in range(len(L)):
    for i in range(len(L)):
        max_divisor=gcd(L[e],L[i])
        #e是分子 i是分母
        simplest_numerator=int(L[e]/max_divisor)
        simplest_denominator=int(L[i]/max_divisor)
        if simplest_denominator>=simplest_numerator:
            if simplest_denominator > max_simplest_denominator:
                max_simplest_denominator = simplest_denominator
                # 找出分母最大的位数
            if simplest_numerator > max_simplest_numerator:
                max_simplest_numerator = simplest_numerator
                # 找出分子的最大位数
            if L[e] <= L[i] and L[i] / max_divisor < 10:
                dict_for_simplest_fraction[(simplest_numerator, simplest_denominator)] = L[e] / L[i]
                sorted_dict_for_simplest = sorted(dict_for_simplest_fraction.items(), key=lambda d: d[1], reverse=False)
                size_of_simplest_fraction = 2

max_len_denominator=len(str(max_simplest_denominator))
#分母最大位数
max_len_numerator=len(str(max_simplest_numerator))
#分子最大位数
size_of_most_complex_fraction=max_len_numerator+max_len_denominator
#参数求得

sorted_dict_for_complex=[]

for p in range(len(L)):
    for q in range(len(L)):
        max_divisor = gcd(L[p], L[q])
        #最大公约数
        simplest_numerator = int(L[p]/max_divisor)
        simplest_denominator = int(L[q]/max_divisor)
        #得出分子和分母
        if simplest_numerator<=simplest_denominator and len(str(simplest_numerator))==max_len_numerator and len(str(simplest_denominator))==max_len_denominator:
            #分子小于分母
            dict_for_complex_fraction[(simplest_numerator,simplest_denominator)]=L[p]/L[q]
            #组成字典{(分子/分母),分数值}
            sorted_dict_for_complex=sorted(dict_for_complex_fraction.items(),key=lambda f:f[1],reverse=True)
            #字典排序转列表

for a in range(len(sorted_dict_for_simplest)):
    simplest_fractions.append(sorted_dict_for_simplest[a][0])
for b in range(len(sorted_dict_for_complex)):
    most_complex_fractions.append(sorted_dict_for_complex[b][0])


dict_num_of_factor={}
L_denominator=[]
#建一个列表放所有的分母以此降低时间复杂度。
for m in range(len(L)):
    for n in range(len(L)):
        max_divisor=gcd(L[m],L[n])
        simplest_denominator=int(L[n]/max_divisor)
        simplest_numerator = int(L[m] / max_divisor)
        if simplest_denominator >=simplest_numerator:
            if len(str(simplest_denominator)) == max_len_denominator and len(
                    str(simplest_numerator)) == max_len_numerator:
                L_denominator.append(simplest_denominator)
                # 对分母进行操作

L_denominator=list(set(L_denominator))

max_value_dict=0
dict1={}
dict2={}
dict_keys=[]
L_max_num=[]
max_key_max=[]
max_key_dict=0
dict_num_of_factor={}
for k in range(len(L_denominator)):
    #遍历数组中每一个分母
    for tst_num in range(2,L_denominator[k]+1):
        #从2开始测试质数
        while L_denominator[k] % tst_num == 0 :
            if tst_num in dict_num_of_factor:
                dict_num_of_factor[tst_num] += 1
            else:
                dict_num_of_factor[tst_num] = 1
            # 在字典里key=k 的value计数
            L_denominator[k]=L_denominator[k]/tst_num
        #写循环找出最大次幂,得到一个字典{因子：出现的次数}
    dict2=dict_num_of_factor
        #把dict2所有的键放在一个list里
    dict_keys=[*dict2]
    for w in range(len(dict2)):
        if dict_keys[w] in dict1:
            if dict2[dict_keys[w]]>dict1[dict_keys[w]]:
                    dict1[dict_keys[w]] = dict2[dict_keys[w]]
        else:
            dict1[dict_keys[w]] = dict2[dict_keys[w]]
    if length!=1:
        max_key_dict = max(dict_num_of_factor, key=dict_num_of_factor.get)
        max_value_dict = dict_num_of_factor[max_key_dict]
        L_max_num.append(max_value_dict)
        dict_num_of_factor.clear()
    else:
        L_max_num=[0]


multiplicity_of_largest_prime_factor=max(L_max_num)

if length!=1:
    max_key_dict1 = max(dict1, key=dict1.get)
    max_value_dict1 = dict1[max_key_dict1]
    for r in range(len(dict1)):
        max_key_dict1 = max(dict1, key=dict1.get)
        if dict1[max_key_dict1] == max_value_dict1:
            largest_prime_factors.append(max_key_dict1)
            del dict1[max_key_dict1]
else:
    largest_prime_factors=[]
largest_prime_factors.sort()



print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
      )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
      )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
      )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)


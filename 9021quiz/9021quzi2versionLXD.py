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
from fractions import Fraction

all_num = []
for x in L:
    for y in L:
        if x / y <= 1:
            all_num.append(((int(x / gcd(x, y)), int(y / gcd(x, y))), x / y))

B = sorted(set(all_num), key=lambda s: s[1])

all_fractions = []
for i in B:
    all_fractions.append(i[0])

simplest_fractions = []
size_of_simplest_fraction = 2
for i in all_fractions:
    if len(str(i[0])) + len(str(i[1])) == 2:
        simplest_fractions.append(i)

size_of_most_complex_fraction = 2
for i in all_fractions:
    if len(str(i[0])) + len(str(i[1])) > size_of_most_complex_fraction:
        size_of_most_complex_fraction = len(str(i[0])) + len(str(i[1]))

most_complex_fractions = []
for i in all_fractions:
    if len(str(i[0])) + len(str(i[1])) == size_of_most_complex_fraction:
        most_complex_fractions.append(i)
most_complex_fractions.reverse()

denominator = []  # 分母的列表
for i in most_complex_fractions:
    denominator.append(i[1])
d = []


def f(n):
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            d.append(i)
            return f(int(n / i))
    d.append(n)


dic = {}
F = []
for a in denominator:

    f(a)

    for i in d:
        dic[i] = 1 + dic.get(i, 0)
    max_value = max(dic.values())
    F.append(max_value)
    dic.clear()
    d.clear()

if length!=1:
    multiplicity_of_largest_prime_factor = max(F)
else:
    multiplicity_of_largest_prime_factor=0
# 最后一问 先重复循环
from collections import defaultdict

d = []


def f(n):
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            d.append(i)
            return f(int(n / i))
    d.append(n)


dic = {}
R = []  # 有最大值的key的集合
for a in denominator:

    f(a)

    for i in d:
        dic[i] = 1 + dic.get(i, 0)
        h = defaultdict(list)
        for k, v in dic.items():
            h[v].append(k)
    R.extend(h[multiplicity_of_largest_prime_factor])
    dic.clear()
    d.clear()
if length!=1:
    largest_prime_factors = R
else:
    largest_prime_factors=[]



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
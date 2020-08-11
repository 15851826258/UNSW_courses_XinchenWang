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
zuidafenzi=0
zuidafenmu=0
zuidafenziweishu=0
zuidafenmuweishu=0
jiandanfenshuzidian={}
paiguoxudejiandanfenshuzidian=[]
for b in range(len(L)):
    for a in range(len(L)):
        max_gongyueshu=gcd(L[a],L[b])
        #最大公约数
        zuijianfenzi=int(L[a]/max_gongyueshu)
        zuijianfenmu=int(L[b]/max_gongyueshu)
        if zuijianfenzi<=zuijianfenmu:
        #化到最简以后筛选分子小于分母
            if zuijianfenzi>zuidafenzi:
                zuidafenzi=zuijianfenzi
            #找到分子最大的一项
            if zuijianfenmu>zuidafenmu:
                zuidafenmu=zuijianfenmu
            #找到分母最大的一项
            if zuijianfenmu<10:
                jiandanfenshuzidian[(zuijianfenzi,zuijianfenmu)]=zuijianfenzi/zuijianfenmu
                # 放入字典 以{（分子，分母）：分数值}的形式
                paiguoxudejiandanfenshuzidian=sorted(jiandanfenshuzidian.items(),key=lambda d:d[1],reverse=False)
                size_of_simplest_fraction=2
                #参数1：第一个值无论如何都是2 因为存在自己比自己等于1/1 长度是2

zuidafenziweishu=len(str(zuidafenzi))
zuidafenmuweishu=len(str(zuidafenmu))
#取到分子分母最大的位数
size_of_most_complex_fraction=zuidafenziweishu+zuidafenmuweishu
#参数3：分子分母最大位数的和


fuzafenshuzidian={}
paiguoxudefuzafenshuzidian=[]
fenmujihe=[]
for c in range(len(L)):
    for d in range(len(L)):
        max_gongyueshu=gcd(L[c],L[d])
        #最大公约数
        zuijianfenzi=int(L[c]/max_gongyueshu)
        zuijianfenmu=int(L[d]/max_gongyueshu)
        #最简分子分母
        if zuijianfenzi<=zuijianfenmu and len(str(zuijianfenzi))+len(str(zuijianfenmu))==zuidafenziweishu+zuidafenmuweishu:
            #注意这里是大于等于 因为1的情况分子分母无论如何都会等于
            fuzafenshuzidian[(zuijianfenzi,zuijianfenmu)]=zuijianfenzi/zuijianfenmu
            paiguoxudefuzafenshuzidian=sorted(fuzafenshuzidian.items(),key=lambda f:f[1],reverse=True)
            #字典排序转列表
        if zuijianfenzi<zuijianfenmu and len(str(zuijianfenzi))==zuidafenziweishu and len(str(zuijianfenmu))==zuidafenmuweishu:
            fenmujihe.append(zuijianfenmu)

for e in range(len(paiguoxudejiandanfenshuzidian)):
    simplest_fractions.append((paiguoxudejiandanfenshuzidian[e][0]))
for f in range(len(paiguoxudefuzafenshuzidian)):
    most_complex_fractions.append(paiguoxudefuzafenshuzidian[f][0])
#打印出来简单和复杂的分数

fenmujihe=list(set(fenmujihe))
#分母的集合 排个序 顺便去重
fenmujihecopy=[]
fenmujihecopy=fenmujihe.copy()


zhiyinshujihe=[]
max_zhiyinshugeshu=0
for g in range(len(fenmujihe)):
    for h in range(2,fenmujihe[g]+1):
        while fenmujihe[g]%h==0:
            zhiyinshujihe.append(h)
            fenmujihe[g]=fenmujihe[g]/h
        for i in range(len(zhiyinshujihe)):
            if zhiyinshujihe.count(zhiyinshujihe[i])>max_zhiyinshugeshu:
                max_zhiyinshugeshu=zhiyinshujihe.count(zhiyinshujihe[i])
    #清空列表
    zhiyinshujihe=[]
multiplicity_of_largest_prime_factor=max_zhiyinshugeshu
#取到参数 分母中出现最多的因数的次数

for j in range(len(fenmujihecopy)):
    for k in range(2,fenmujihecopy[j]+1):
        while fenmujihecopy[j]%k==0:
            zhiyinshujihe.append(k)
            fenmujihecopy[j]=fenmujihecopy[j]/k
        for m in range(len(zhiyinshujihe)):
            if zhiyinshujihe.count(zhiyinshujihe[m])==multiplicity_of_largest_prime_factor:
                largest_prime_factors.append(zhiyinshujihe[m])
    zhiyinshujihe=[]
#比对列表里出现次数和最多次数一样的 就是我们要找的 拼进列表中

largest_prime_factors=list(set(largest_prime_factors))
largest_prime_factors.sort(reverse=False)
#排序输出的结果







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

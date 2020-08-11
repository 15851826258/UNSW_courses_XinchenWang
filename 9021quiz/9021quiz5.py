# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by XINCHEN WANG and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


list_q1=[]
list_erjinzhi=[]
list_yaoyongde=[]


zhuanhuanjieguo=bin(encoded_set)
list_erjinzhi=list(zhuanhuanjieguo[2:])
for a in range(len(list_erjinzhi)):
    list_yaoyongde.append(int(list_erjinzhi[a]))



def display(L):
    print('{', end='')
    print(', '.join(str(e) for e in L), end='')
    print('}')


def decode(encoded_set):

    list_q1 = []
    for b in range(len(list_yaoyongde)-1,-1,-1):
        if b%2==0 and list_yaoyongde[(len(list_yaoyongde)-b-1)]==1:
            list_q1.append(int(b/2))
        elif b%2==1 and list_yaoyongde[(len(list_yaoyongde)-b-1)]==1:
            list_q1.append(int(0-(b+1)/2))
    #二进制从右往左遍历 但是存储的是从左往右

    list_q1=list(set(list_q1))
    list_q1 = sorted(list_q1)
    return list_q1
    # REPLACE RETURN [] ABOVE WITH YOUR CODE


def code_derived_set(encoded_set):
    list_iniq2=decode(encoded_set)
    list_sum=[]
    #list_sum是从第一位依次累加
    for a in range(len(list_iniq2)):
        sum=0
        for b in range(0,a+1):
            sum=sum+list_iniq2[b]
        list_sum.append(sum)
    list_sum=sorted(list_sum)
    list_sum=list(set(list_sum))
    list_q2=[]
    q2=0
    for a in range(len(list_sum)):
        if list_sum[a]>=0:
            list_q2.append(list_sum[a] * 2)
        else:
            list_q2.append((0 - list_sum[a]) * 2 - 1)
    #奇偶数不同结果
    for b in range(len(list_q2)):
        q2=q2+2**list_q2[b]
    #转换成n次幂,二进制有1的位数意味着2的位数次方

    return q2





print('The encoded set is: ', end='')
display(decode(encoded_set))



code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end='')

del list_yaoyongde[:]
encoded_set=code_of_derived_set
zhuanhuanjieguo=bin(encoded_set)
list_erjinzhi=list(zhuanhuanjieguo[2:])
for a in range(len(list_erjinzhi)):
    list_yaoyongde.append(int(list_erjinzhi[a]))
#第二次的时候先把第一次的结果转成第二次需要的


display(decode(code_of_derived_set))


import sys
import os.path
import sys

from collections import defaultdict

#CODE BY XINCHEN WANG FOR 9021
#输入检查 文件打开失败报错
try:
    filename=input('Please enter the name of the file you want to get data from: ')
    file = open(filename, 'r')
except IOError:
    print('Sorry, there is no such file.')
    sys.exit()



#第一问
#filename='testcase_Assign1.3.txt'
#file = open(filename, 'r')
# with open(filename,'r') as f:
#     for line in f:
#         arr=line.strip()
#         arr.split()
#         o.append(arr)
        # arr.split(' ')
        # arr.split('\n')
        # print(arr)
        # numbers_int = list(map(int, arr))
        # print(numbers_int)

a = file.read().split()
o= []
try:
    for ele in a:
        o.append(int(ele))
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

#L=[5,10,14,15,20,25,26,27,28,30,31]
#L=[5,8,11,14]
#L=[10,13,20,30,40,42,44,46,48,50,60,70,80,82,85,87,90,100,101,110,113,117,121]
L=o

if len(L)<2:
    print('Sorry, input file does not store valid data.')
    sys.exit()
#排除只有一个数字的情况

for a in range(1,len(L)):
    if L[a]<=L[a-1]:
        print('Sorry, input file does not store valid data.')
        sys.exit()
#排除数字忽大忽小的情况

if all(L):
    #这里如果L里有0就会false
    pass
else:
    print('Sorry, input file does not store valid data.')
    sys.exit()
#排除输入的里面有0的情况

L_dif=[]
L_dif_dif=[]
b=0
max_0s=0
max_length=0
zuidalianxulingcishu=[]
for a in range(len(L)-1):
    L_dif.append(L[a+1]-L[a])
for a in range(len(L_dif)-1):
    L_dif_dif.append(L_dif[a]-L_dif[a+1])
#数列中所有0的项代表相同的数相减


count=0
max_count=0
for a in range(0,len(L_dif_dif)):
    if L_dif_dif[a]==0:
        count=1
        for b in range(1,len(L_dif_dif)-a):
            if L_dif_dif[a+b]==0:
                count+=1
                if count > max_count:
                    max_count = count
            else:
                break
        count=0
if max_count==0:
    max_count=1
#通过计算0的个数得到了最大的连续长度


#第二问

# dict_dif={}
# #建立字典 放入所有的次数{(数字：次数)}
# list_difQ2=[]
# count_cons=0
# #连续的次数
# max_count_cons=0
# #最大的次数 第二问要得到的
# dif=0
# #每次的差 和字典的key比较 如果在字典里就value+1 不然就记录入字典
# list_final=[]
# for a in range(1,len(L)):
#     #列表里的每个元素
#     for b in range(0,a-1):
#         dif=L[a]-L[b]
#         list_difQ2.append(dif)
#         #寻找每一种差的可能
#     for b in range(len(list_difQ2)):
#         dif=list_difQ2[b]
#         temp=L[a]
#         for c in range(1,a):
#             if (temp-dif) in L:
#                 count_cons+=1
#                 temp=temp-dif
#             #减到元素不在L里 那么找出最后一次的
#             if count_cons>max_count_cons:
#                 max_count_cons=count_cons
#                 list_final.append([L[a],dif,max_count_cons])
#                 count_cons=0
#         count_cons=0
#
# list_want=[]
# list_want=list_final[-1]
# k=list_want[2]
# p=len(L)-(k+1)
# print(list_final)
# print(list_want)
# print(p)




#
# list_final=[]
# for a in range(1,len(L)):
#     for c in range(1,a+1):
#         dif =L[a] - L[c]
#         after_one = L[a]
#         for b in range(1, a + 1):
#             next_one = after_one - dif
#             if (next_one) in L:
#                 count_cons += 1
#                 after_one = after_one - dif
#             if count_cons > max_count_cons:
#                 list_final.append([L[a], dif, count_cons])
#                 max_count_cons = count_cons
#                 count_cons = 0
#         else:
#             count_cons = 0
#
#
# print(list_final)
# print(a,b,max_count_cons)




dict_want=defaultdict(dict)
dict_num={}
dict_temp=[]
dif=0
dict_num_pre={}
dict_dif={}
for a in range(len(L)):
    dict_num={}

    for b in range(0,a):
        dif=L[a]-L[b]
        dict_dif=dict_want[L[b]]
        if dif in dict_dif:
            dict_num[dif]=dict_dif[dif]+1
            count_num=dict_dif[dif]+1
        else:
            dict_num[dif]=1
            count_num=1
        #如果字典里没有的话就新增 有的话就自加一
        dict_want[L[a]].update({dif:count_num})


list_times=[]
for a in range(2,len(L)):
    dict_temp=dict_want[L[a]]
    times=dict_temp.get(max(dict_temp,key=dict_temp.get))
    list_times.append(times)
max_cable=max(list_times)

remove_cable=len(L)-(max_cable+1)


if remove_cable==0:
    print('The ride is perfect!')
else:
    print('The ride could be better...')

print(f'The longest good ride has a length of: {max_count+1}')
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {remove_cable}')
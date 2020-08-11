import sys
#CODE BY XINCHEN WANG LOUIS FOR 9021

L_power=[]
try:
    data=input('Please input the heroes \'powers:').split()
    for a in range(len(data)):
        L_power.append(int(data[a]))
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
#限定不能输入小数和字母乱七八糟的

flips=int(input('Please input the number of power flips: '))
if flips>len(L_power) or flips<0:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
#限定反转次数不能多于总的power数 且不能为负

if L_power==[] and flips==0:
    sum1=0
    sum2=0
    sum3=0
    sum4=0



#第一个
L_temp=L_power.copy()
L_temp=sorted(L_temp,reverse=False)
xiaoyulingeshu=0
lindegeshu=0
sum1=0
sum2=0

for a in range(len(L_temp)):
    if L_temp[a]<0:
        xiaoyulingeshu+=1
#求出零的个数
if flips<=xiaoyulingeshu:
    for a in range(1,flips+1):
        L_temp[a-1]=0-L_temp[a-1]
    for a in range(len(L_temp)):
        sum1=sum1+L_temp[a]
        sum2=sum2+L_temp[a]
        #a-1是为了从列表第一个数开始访问，因为反转次数比较少，所以按照反转次数从小到大翻转为正数
else:
    lindegeshu=L_temp.count(0)
    if lindegeshu>0:
        for a in range(1,xiaoyulingeshu+1):
            L_temp[a-1]=0-L_temp[a-1]
        for a in range(len(L_temp)):
            sum1=sum1+L_temp[a]
            #如果有大于零的数，那么就剩余的反转次数都用在0上
    else:
        for a in range(1,xiaoyulingeshu+1):
            L_temp[a-1]=0-L_temp[a-1]
        L_temp=sorted(L_temp,reverse=False)
        #翻转后再排序
        if (flips-xiaoyulingeshu)%2==0:
            for a in range(len(L_temp)):
                sum1=sum1+L_temp[a]
                #还剩下偶数次翻转，那么正负不会再产生变化
        else:
            L_temp[0]=0-L_temp[0]
            for a in range(len(L_temp)):
                sum1=sum1+L_temp[a]
                #剩下奇数次翻转，把最小的翻成负数


#第二个
L_temp2=L_power.copy()
L_temp2=sorted(L_temp2,reverse=False)
for a in range(0,flips):
    L_temp2[a]=0-L_temp2[a]
sum2=sum(L_temp2)
# if flips>xiaoyulingeshu:
#     # 如果反转次数有多的话
#     for a in range(1,xiaoyulingeshu+1):
#         L_temp2[a-1]=0-L_temp2[a-1]
#         #先把负数翻成正数
#     L_temp2=sorted(L_temp2,reverse=False)
#     #排序找绝对值最小的翻
#     for a in range(1,flips-xiaoyulingeshu+1):
#         L_temp2[a-1]=0-L_temp2[a-1]
#     for a in range(len(L_temp2)):
#         sum2=sum2+L_temp2[a]


#第三个
L_temp3=L_power.copy()
L_zuixiaongeshu=[]
L_sum3=[]
max_sum3=0
zuixiaongeshuhe=0
zuixiaodejigeshu=0
L_shengxiadeshu=[]

for a in range(0,len(L_temp3)-flips+1):
    L_zuixiaongeshu.append(L_temp3[a:flips+a])
for a in range(len(L_zuixiaongeshu)):
    L_sum3.append(sum(L_zuixiaongeshu[a]))
zuixiaongeshuhe=min(L_sum3)
#找出最小的和是多少
# for a in range(len(L_zuixiaongeshu)):
#     if sum(L_zuixiaongeshu[a])==zuixiaongeshuhe:
#         zuixiaodejigeshu=(L_zuixiaongeshu[a])
#         #把最小的n个数的列表取出来
sum3=sum(L_temp3)-zuixiaongeshuhe*2
#最大的和等于原本的和减去  2x（最小的n个连续数和）


#第四个
L_temp4=L_power.copy()
L_zuixiaodengeshu_4=[]
L_sum4=[]
zuixiaongeshuhe_4=0
zuixiaodejigeshu_4=0
#和的集合 然后一把max出来最大值
for k in range(0,len(L_temp4)):
    #k是片段可能出现的长度
    for a in range(0,len(L_temp4)-k+1):
        if k!=0:
            L_zuixiaodengeshu_4.append(L_temp4[a:k + a])
        else:
            #k=0的情况 即不需要翻转任何数
            sum4=sum(L_temp4)
    for a in range(len(L_zuixiaodengeshu_4)):
        if k!=0:
            L_sum4.append(sum(L_zuixiaodengeshu_4[a]))
        else:
            break
if L_power==[] and flips==0:
    sum4=0
elif len(L_power)==1:
    if L_power[0]>0:
        sum4=L_power[0]
    else:
        sum4=0-L_power[0]
else:
    zuixiaongeshuhe_4 = min(L_sum4)

if sum(L_temp4)-(zuixiaongeshuhe_4)*2>sum4:
    sum4 = sum(L_temp4) - (zuixiaongeshuhe_4) * 2


print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum1}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum2}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum3}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {sum4}.')
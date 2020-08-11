import sys

try:
    filename=input('Please enter the name of the file you want to get data from: ')
    file=open(filename,'r')
except IOError:
    print('Sorry, there is no such file.')
    sys.exit()
#testcase_Assign1.4.txt本地测试

filecontent=file.read()

list1=[]
list2=[]
filecontent_split=filecontent.split('\n')
while '' in filecontent_split:
    filecontent_split.remove('')
if len(filecontent_split)>=3:
    print('Sorry, input file does not store valid data.')
    sys.exit()

list1_str=filecontent_split[0].split()
list2_str=filecontent_split[1].split()

try:
    for k in range(len(list1_str)):
        list1.append(int(list1_str[k]))
    for k in range(len(list2_str)):
        list2.append(int(list2_str[k]))
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
#把输入的两行拼进列表分别为list1、list2

if len(list1)!=len(list2):
    print('Sorry, input file does not store valid data.')
    sys.exit()
#控制上下必须长度相等
if len(list1)<2 or len(list2)<2:
    print('Sorry, input file does not store valid data.')
    sys.exit()

len_list=len(list1)
list3=[]
height_dif=0
list_daipinjie=[]
list_gaoducha=[]
len_from_left=0

for a in range(len(list1)):
    height_dif=list1[a]-list2[a]
    if height_dif<=0:
        print('Sorry, input file does not store valid data.')
        sys.exit()
    #控制输入中不能出现上下一样高的情况
    for b in range(list2[a],list1[a]):
        list_daipinjie.append(b)
    list_gaoducha.append(list_daipinjie)
    #把每一个数向的可能的高度取出来 然后以列表的形式 拼进list_gaoducha
    list_daipinjie=[]
    max_btm_Q1=list2[0]

# distance_Q1=0
# for a in range(0,len(list_gaoducha[0])):
#     height_wanna=list_gaoducha[0][a]
#     for b in range(a+1,len_list):
#         if height_wanna not in list_gaoducha[b]:
#             distance_Q1=b-a
#             break


height_wanna=0
list_distance=[]
list_Q1=[]
distance=0
for a in range(len_list):
    for b in range(0,len(list_gaoducha[a])):
        height_wanna=list_gaoducha[a][b]
        if a == 0 and len(list_gaoducha[0])>1:
            list_Q1.append(distance)
        if a== 1 and len(list_gaoducha[0])==1:
            if len(list_Q1)<=len(list_gaoducha[0]):
                list_Q1.append(distance)
        #仅把第一个区间的内容取出来
        distance = 1
        for c in range(a+1,len_list):
            if height_wanna in list_gaoducha[c]:
                distance+=1
                if c==len_list-1:
                    distance=len_list-a
                    list_distance.append(distance)
            else:
                list_distance.append(distance)
                break

            # if height_wanna not in list_gaoducha[c]:
            #     distance=c-a
            #     list_distance.append(distance)
            #     if distance==len_list-a:
            #         break
            #     break


print(f'From the west, one can see into the tunnel over a distance of {max(list_Q1)}.')
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {max(list_distance)}.')



#弄出（高，索引）为元素的列表

# print(list3)
# print(list4)
#
# lowest=list4[0][0]
# index=0
# for a in range(1,len_list):
#     if list3[a+1][0] > list4[a][0]:
#         if list4[a][0]>list4[a+1][0]:
#             lowest=list4[a][0]
#             index=a
#         else:
#             lowest=list4[a+1][0]
#             index=a+1







import os.path
import sys
from collections import deque

#filename = input('Please enter the name of the file you want to get data from: ')
filename='testcase_Assign1.4.txt'

if not os.path.exists(filename):
    print(f'Sorry, there is no such file.')
    sys.exit()

alldata = []
displaydata = []
with open(filename) as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        line = line.split()
        alldata.append(line)
for i in alldata:
    if i != []:
        displaydata.append(i)

for i in range(len(displaydata)):
    for j in range(len(displaydata[0])):
        try:
            a = int(displaydata[i][j])

        except ValueError:
            print('Sorry, input file does not store valid data.')
            sys.exit()

if len(displaydata) != 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()

for i in displaydata:
    if len(i) < 2:
        print('Sorry, input file does not store valid data.')
        sys.exit()
    if len(i) != len(displaydata[0]):
        print('Sorry, input file does not store valid data.')
        sys.exit()
for i in range(len(displaydata[0])):
    if int(displaydata[0][i]) <= int(displaydata[1][i]):
        print('Sorry, input file does not store valid data.')
        sys.exit()

# end the test--------------------------------------------------------------------
count = 1
count2 = 1
distance = 0
for i in range(1, len(displaydata[0])):
    if int(displaydata[0][i]) >= int(displaydata[0][0]) and int(displaydata[1][i]) < int(displaydata[0][0]):
        count += 1
    else:
        break
for i in range(1, len(displaydata[0])):
    if int(displaydata[1][i]) <= int(displaydata[1][0]) and int(displaydata[0][i]) > int(displaydata[1][0]):
        count2 += 1
    else:
        break
print(count)
print(count2)
distance = max(count, count2)
print(f'From the west, one can see into the tunnel over a distance of {distance}.')

# function 2
listcount = []
count3 = 0

a = int(max(displaydata[0]))
b = int(min(displaydata[1]))

list_temp=[]
for k in range(len(displaydata[1])):
    list_temp.append(int(displaydata[1][k]))
b=min(list_temp)



for i in range(b, a + 1):
    for m in range(len(displaydata[0])):
        if i >= int(displaydata[1][m]) and i < int(displaydata[0][m]):
            count3 += 1
            if m == len(displaydata[0]) - 1:
                listcount.append(count3)
                count3 = 0

        if i < int(displaydata[1][m]) or i >= int(displaydata[0][m]):
            listcount.append(count3)
            count3 = 0

count3 = max(listcount)
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {count3}.')
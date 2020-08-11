


# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
#
# Written by XINCHEN WANG and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()
source = input('Enter the source (GCAG or GISTEMP): ')


year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')

month = input('Enter a month: ')


average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
#BY XINCHEN WANG LOUIS FOR 9021

# source='GCAG'
# year_or_range_of_years='1890--1901'
# month='December'

dict_month={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'Octomber':10,'November':11,'December':12}
int_month=dict_month[month]
#把月份转成数字

year1=0
year2=0
year_temp=0
if '-' in year_or_range_of_years:
    year_or_range_of_years = year_or_range_of_years.split('--')
    for a in range(len(year_or_range_of_years)):
        year_or_range_of_years[a] = int(year_or_range_of_years[a])
    year1 = year_or_range_of_years[0]
    year2 = year_or_range_of_years[1]
    if year1 > year2:
        year_temp = year1
        year1 = year2
        year2 = year_temp
else:
    year1=int(year_or_range_of_years)
    year2=int(year_or_range_of_years)

#把输入的两个年份塞进变量 xxxx&xxxx 且保证前者大于后者

file=open("monthly_csv.csv")
filecontent=[]
for line in file:
    line=line.strip()
    #去掉空格
    array=line.split(",")
    #每一行的内容分开
    input_source=array[0]
    date=array[1]
    mean=array[2]
    filecontent.append([input_source,date,mean])
del filecontent[0]
#去掉第一行 因为不是记录

list_YYMMDD=[]
for a in range(len(filecontent)):
    filecontent[a][2]=float(filecontent[a][2])
    # 把最后一个mean转化成小数
    list_YYMMDD=filecontent[a][1].split('-')
    for b in range(len(list_YYMMDD)):
        list_YYMMDD[b]=int(list_YYMMDD[b])
    #把年月日用int分离出来
    filecontent[a]=filecontent[a]+list_YYMMDD
    #把年月日拼在列表后面
#列表变成[[source,date,mean,year,month,day]]

year=0
file_month=0
file_source=0
list_fuhetiaojian=[]
for a in range(len(filecontent)):
    year=filecontent[a][3]
    file_month=filecontent[a][4]
    file_source=filecontent[a][0]
    if year<=year2 and year>=year1 and file_month==int_month and file_source == source:
        list_fuhetiaojian.append(filecontent[a])
#把符合条件的年月的记录都塞进列表

sum=0
for a in range(len(list_fuhetiaojian)):
    sum=sum+list_fuhetiaojian[a][2]
if len(list_fuhetiaojian)==0:
    average=0
else:
    average = sum / len(list_fuhetiaojian)

#print(average)

file_mean=0
for a in range(len(list_fuhetiaojian)):
    file_mean=list_fuhetiaojian[a][2]
    if file_mean>average:
        years_above_average.append(list_fuhetiaojian[a][3])

years_above_average.sort(reverse=False)

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
# Written by XINCHEN WANG for COMP9021


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys



# Insert your code here
try:
    arg_for_seed=int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

try:
    nb_of_elements=int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up')
    sys.exit()

if nb_of_elements<=0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

from random import randrange

seed(arg_for_seed)
L=[randrange(-50,50,1) for _ in range (nb_of_elements)]
print('The list is:',L)
print()
#output of the string

sum_of_List=0
mean_of_List=0
median_of_List=0
standard_divation=0
#all we need is value above to compute the result

for index in range(len(L)):
    sum_of_List=sum_of_List+L[index]
mean_of_List=sum_of_List/len(L)
print('The mean is','{:.2f}'.format(mean_of_List)+'.')
#to get the mean

sorted_L=sorted(L)
if len(L)%2==0:
    median_of_List=(sorted_L[len(L)//2]+sorted_L[len(L)//2-1])/2
else:
    median_of_List=sorted_L[len(L)//2]
print('The median is','{:.2f}'.format(median_of_List)+'.')
#to get the median


sum_of_dif2_btw_mean_and_elements=0
for index in range(len(L)):
    sum_of_dif2_btw_mean_and_elements=(L[index]-mean_of_List)*(L[index]-mean_of_List)+sum_of_dif2_btw_mean_and_elements
standard_divation=sqrt(sum_of_dif2_btw_mean_and_elements/len(L))
print('The standard deviation is','{:.2f}'.format(standard_divation)+'.')
print()

print('Confirming with functions from the statistics module:')
print('The mean is','{:.2f}'.format(mean(L))+'.')
print('The median is','{:.2f}'.format(median(L))+'.')
print('The standard deviation is','{:.2f}'.format(pstdev(L))+'.')
#use the method provided by python to check if the results is right

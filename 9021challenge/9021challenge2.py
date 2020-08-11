#written by XINCHEN WANG for 9021 quiz2


from random import seed,randint
import sys

try:
    input4seed=int(input('Input a seed for the random number generator:'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
    #use try-ecxept struct to aviod unexpected input

try:
    inputnb4elements=int(input('How many elements do you want to generate?'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
    #use try-ecxept struct to aviod unexpected input

if inputnb4elements<=0:
    print('Input should be strictly positive,giving up.')
    sys.exit()
    #make sure that the number of the elements to be positive

seed(input4seed)
L=[randint(0,99) for _ in range(inputnb4elements)]
#get the radom elements btw 0-99 but it is not real random with the seed()

print('\nThe list is: ',L)
#print out the list

max_element=0
min_element=99
#the initial value of max should be the smallest one in list while the min should be the biggest num

for e in L:
    if e>=max_element:
        max_element=e
for e in L:
    if e<=min_element:
        min_element=e
#two for loops to get the min & max in the list

maxium_difference= (max_element - min_element)
#use minus to get the difference

print('\nThe maximum difference between largest and smallest values in this list is:',maxium_difference)

print('Confirming with builtin operations: ',max(L)-min(L))
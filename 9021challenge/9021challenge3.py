#Written by XINCHEN WANG for 9021

from random import seed,randrange
import sys


try:
    arg_for_seed=int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

try:
    nb_of_elements=int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

if nb_of_elements<=0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

seed(arg_for_seed)
L=[randrange(20) for _ in range (nb_of_elements)]
print('\nThe list is:',L)
print()


nb_btw=[0]*4
for e in L:
    if e<=4 and e>=0:
        nb_btw[0]+=1
    elif e>=5 and e<=9:
        nb_btw[1]+=1
    elif e>=10 and e<=14:
        nb_btw[2]+=1
    elif e>=15 and e<=19:
        nb_btw[3]+=1

for i in range(4):
    if(nb_btw[i]==0):
        print('There is no element between',end=' ')
    elif(nb_btw[i]==1):
        print('There is 1 element between',end=' ')
    else:
        print(f'There are {nb_btw[i]} elements between',end=' ')
    print(f'{i*5} and {i*5+4}.')
# Written by XINCHEN WANG for COMP9021

min_temperature=0
max_temperature=100
step=10
#min,max & step as the requirement

print('Celsius\tFahrenheit')
#the first line topic

for celsuis in range(min_temperature,max_temperature+step,step):
    #the in range methond won't cover the right edge
    fahrenheit=celsuis*9/5+32
    print(f'{celsuis:7}\t{fahrenheit:10.0f}')
    #7 means the length of the output,as long as the length of celsuis
    #10 means the length of the output is the same as the word"fahrenheit"
    #.0fmeans no ". & the num after"
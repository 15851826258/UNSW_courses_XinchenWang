from math import sqrt

def find_primes_up_to(n):
    daishaixuandeshu = list(range(2, n + 1))
    i=0
    while daishaixuandeshu[i] <= round(sqrt(n)):
        set_daishaixuan=set(daishaixuandeshu)
        #把list转换成set
        k = 0
        while True:
            yinshu = daishaixuandeshu[i] * daishaixuandeshu[i+k]
            if yinshu > n:
                break
            set_daishaixuan.remove(yinshu)
            k+=1
        daishaixuandeshu = sorted(set_daishaixuan)
        i += 1
    return daishaixuandeshu

print(find_primes_up_to(20))



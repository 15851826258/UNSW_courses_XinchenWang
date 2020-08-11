from math import sqrt

def sieve_of_primes_up_to(n):
    sieve = list(range(2, n + 1))
    i = 0
    while sieve[i] <= round(sqrt(n)):
        sieve_as_set = set(sieve)
        k = 0
        while True:
            factor = sieve[i] * sieve[i + k]
            if factor > n:
                break
            sieve_as_set.remove(factor)
            k += 1
        sieve = sorted(sieve_as_set)
        i += 1
    return sieve
#感谢马老师的方法 谢谢

list_prime_temp = sieve_of_primes_up_to(99999)
list_prime=[]

for a in range(len(list_prime_temp)):
    if list_prime_temp[a]>=10000:
        list_prime.append(list_prime_temp[a])

print('The solutions are:')
print()
print()

for a in range(len(list_prime)):
    if (list_prime[a]+2) in list_prime and (list_prime[a]+6) in list_prime and (list_prime[a]+12) in list_prime and (list_prime[a]+20) in list_prime and (list_prime[a]+30) in list_prime:
        if list_prime[a]+2==list_prime[a+1] and list_prime[a]+6==list_prime[a+2] and list_prime[a]+12==list_prime[a+3] and list_prime[a]+20==list_prime[a+4] and list_prime[a]+30==list_prime[a+5]:
            print(list_prime[a],list_prime[a]+2,list_prime[a]+6,list_prime[a]+12,list_prime[a]+20,list_prime[a]+30)



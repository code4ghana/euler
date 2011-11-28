import sys
from p10 import primes_upto

def largePrimediv(num):
    print num
    primes=[(i) for i in primes_upto(10000) if i is not 0]
    largest=1
    
    for i in primes:
        if i> num:
            break;
        if num%i is 0:
            num=num/i
            largest=i

    return largest

print largePrimediv(600851475143)

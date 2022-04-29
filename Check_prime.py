import sys
import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        return True

def Eratos(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <=n:
            array[i * j] = False
            j += 1
    return array
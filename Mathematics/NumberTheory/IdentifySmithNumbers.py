__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/identify-smith-numbers
'''
import math
def prime_factorize(n):
    factors = []
    number = abs(n)
    factor = 2
    while number > 1:
        factor = get_next_prime_factor(number, factor)
        factors.append(factor)
        number /= factor
    if n < -1:
        factors[0] = -factors[0]
    return factors

def get_next_prime_factor(n, f):
    if n % 2 == 0:
        return 2
    for x in range(max(f, 3), int(math.sqrt(n) + 1), 2):
        if n % x == 0:
            return x
    return n

snek = int(input())
if sum(sum(map(int,str(j))) for j in [str(i) for i in prime_factorize(snek)]) == sum([int(i) for i in str(snek)]):
    print(1)
else:
    print(0)
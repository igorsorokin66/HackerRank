__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-square
'''
test_cases = int(input())
MOD = 10 ** 9 + 7

def two_to_the(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        k = two_to_the(n // 2)
        return (k * k) % MOD
    else:
        k = two_to_the(n // 2)
        return (k * k * 2) % MOD

for t in range(test_cases):
    seconds = int(input()) + 1
    result = 2 + two_to_the(seconds)
    print(result % MOD)
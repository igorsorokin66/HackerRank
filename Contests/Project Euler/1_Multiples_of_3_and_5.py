__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
'''
def sum_of_multiples(n, k):
    k_in_n = (n-1) // k
    return (k_in_n + 1) * k_in_n // 2 * k

test_cases = int(raw_input())
for t in range(test_cases):
    n = int(raw_input())
    print(sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15))
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/handshake
'''
test_cases = input()
for t in range(int(test_cases)):
    n = int(input())
    print(n-1+sum([i for i in range(n - 1)]))
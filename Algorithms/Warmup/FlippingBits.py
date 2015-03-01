__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/flipping-bits
'''
test_cases = int(input())

for t in range(test_cases):
    x = int(raw_input())
    print(~x & 0xFFFFFFFF)
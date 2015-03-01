__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/contests/projecteuler/challenges/euler063
'''
power = int(raw_input())
count = 0
for x in range(19):
    calc = x ** power
    if power == len(str(int(calc))):
        print(str(calc))
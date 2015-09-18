__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/priyanka-and-toys
'''
waste = input()
arr = sorted([int(i) for i in input().split()])

total = 0
bound = 0
for a in arr:
    if bound == 0 or bound < a:
        bound = a + 4
        total += 1
print(total)
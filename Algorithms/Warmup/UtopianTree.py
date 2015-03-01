__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/utopian-tree
'''
library = []
start = 1
flag = False
for i in range(60):
    library.append(start)
    if start % 2 == 0:
        start += 1
    else:
        start *= 2

test_cases = int(input())
for t in range(test_cases):
    start = int(input())
    print(library[start])
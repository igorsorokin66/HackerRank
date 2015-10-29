__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/pairs
'''
target = int(input().split()[1])
arr = [int(i) for i in input().split()]
dicto = {}
for f in arr:
    dicto[f] = 0
count = 0
for a in arr:
    if a + target in dicto:
        count += 1
print(count)
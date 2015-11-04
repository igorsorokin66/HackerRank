__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/mark-and-toys
'''
line1 = input().split()
n = int(line1[0])
k = int(line1[1])
arr = sorted([int(i) for i in input().split()])
count = 0
for a in arr:
    if k - a >= 0:
        k -= a
        count += 1
    else:
        break
print(count)
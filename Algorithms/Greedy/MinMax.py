__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/angry-children
'''
n = int(input())
k = int(input())
arr = sorted([int(input()) for i in range(n)])

lowest = 1000000000
for i in range(len(arr)-k+1):
    val = arr[i+k-1] - arr[i]
    if val < lowest:
        lowest = val
print(lowest)
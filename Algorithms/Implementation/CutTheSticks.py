__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/cut-the-sticks
'''
waste = input()
arr = [int(i) for i in input().split()]
print(len(arr))
while len(arr) != 0:
    arr = [a-min(arr) for a in arr if a != min(arr)]
    if len(arr) != 0:
        print(len(arr))

__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/service-lane
'''
waste = int(input().split()[1])
arr = [int(i) for i in input().split()]
for t in range(waste):
    m = [int(i) for i in input().split()]
    print(min(arr[m[0]:m[1]+1]))
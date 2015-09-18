__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/angry-professor
'''
for t in range(int(input())):
    required = int(input().split()[1])
    students = sum([int(i) <= 0 for i in input().split()])
    if students >= required:
        print("NO")
    else:
        print("YES")
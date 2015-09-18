__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/staircase
'''
num = int(input())
for n in range(num):
    print("".join([" " for i in range(num-n-1)]+["#" for i in range(n+1)]))
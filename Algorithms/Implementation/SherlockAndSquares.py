__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-squares
'''
import math
for i in range(int(input())):
    line = input().split()
    a = math.sqrt(int(line[0]))
    b = math.sqrt(int(line[1]))
    c = 0
    if a % 1 == 0:
        c += 1
    print(c+math.floor(b)-math.floor(a))
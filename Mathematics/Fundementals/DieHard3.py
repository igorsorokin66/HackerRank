__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/die-hard-3
'''
testcases = int(input())
for t in range(testcases):
    line = input().split(" ")
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    from fractions import gcd
    if c%gcd(a,b) ==0 and c <= max(b,a):
        print("YES")
    else:
        print("NO")
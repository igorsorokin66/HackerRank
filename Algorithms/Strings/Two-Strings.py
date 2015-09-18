__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/two-strings
'''
for t in range(int(input())):
    s1 = set(input())
    s2 = set(input())
    if len(s1.intersection(s2)) > 1:
        print("YES")
    else:
        print("NO")
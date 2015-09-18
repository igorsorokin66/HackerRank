__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/find-hackerrank
'''
for t in range(int(input())):
    s = input()
    if s == "hackerrank":
        print(0)
    elif s.startswith("hackerrank"):
        print(1)
    elif s.endswith("hackerrank"):
        print(2)
    else:
        print(-1)
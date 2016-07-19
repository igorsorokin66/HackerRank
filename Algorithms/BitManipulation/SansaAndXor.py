__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sansa-and-xor
'''
for i in range(int(input())):
    x = input()
    elem = [int(n) for n in input().split()]
    if len(elem) % 2 == 0:
        print(0)
    else:
        t = 0
        for e in range(0, len(elem), 2):
            t ^= elem[e]
        print(t)
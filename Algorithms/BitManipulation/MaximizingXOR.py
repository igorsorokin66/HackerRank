__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/maximizing-xor
'''
l = int(input())
r = int(input())
biggest = 0
import itertools
shiz = [i for i in range(l, r+1)]
for x, y in itertools.permutations(shiz, 2):
    test = int(bin(x)[2:], 2) ^ int(bin(y)[2:], 2)
    if test > biggest:
        biggest = test
print(biggest)
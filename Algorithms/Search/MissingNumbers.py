__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/missing-numbers
'''
from itertools import groupby

waste = input()
a = dict((key, len(list(group))) for key, group in groupby(sorted(input().split())))

waste = input()
b = dict((key, len(list(group))) for key, group in groupby(sorted(input().split())))

fuu = []
for key in b.keys():
    if a[key] != b[key]:
        fuu.append(key)
print(" ".join(sorted(fuu)))
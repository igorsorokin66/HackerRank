__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/game-of-thrones
'''
from itertools import groupby
a = dict((key, len(list(group))) for key, group in groupby(sorted(list(input()))))

c = 0
for i in list(a.values()):
    if i % 2 != 0:
        c += 1
if c > 1:
    print("NO")
else:
    print("YES")
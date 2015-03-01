__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/encryption
'''
import math
s = raw_input()
s = s.replace(" ", "")

col = int(math.floor(math.sqrt(len(s))))
row = int(math.ceil(math.sqrt(len(s))))
if col * row < len(s):
    if col < row:
        col += 1
    else:
        row += 1
c = 0
r = 0
grid = [[] for i in range(row)]
for i in s:
    if r+1 < row:
        grid[c].append(i)
        r += 1
    else:
        grid[c].append(i)
        c += 1
        r = 0

total = ""
for x in range(row):
    str = ""
    for y in range(col):
        if x < len(grid[y]):
            str += grid[y][x]
    str += " "
    total += str
print(total)
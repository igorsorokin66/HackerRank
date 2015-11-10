__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/cavity-map
'''
map = []
size = int(input())
for l in range(size):
    map.append([int(i) for i in list(input())])

found = []
for x in range(1, size-1):
    for y in range(1, len(map[x])-1):
        arr = [map[x+1][y], map[x-1][y], map[x][y+1], map[x][y-1]]
        if map[x][y] > max(arr):
            found.append([x, y])
for f in found:
    map[f[0]][f[1]] = "X"
for i in map:
    print("".join([str(k) for k in i]))
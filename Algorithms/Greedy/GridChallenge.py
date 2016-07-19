__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/grid-challenge
'''

def check_grid():
    grid = []
    prev = []
    x = int(input())
    flag = "YES"
    for row in range(x):
        grid.append(sorted([ord(l) for l in input()]))
        if len(prev) is not 0:
            for i in range(len(prev)):
                if prev[i] > grid[-1][i]:
                    flag = "NO"
        prev = grid[-1]
    return flag

for t in range(int(input())):
    print(check_grid())
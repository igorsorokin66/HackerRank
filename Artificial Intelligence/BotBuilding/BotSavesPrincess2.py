__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/saveprincess2
'''
def displayPathtoPrincess(mLoc, pLoc, grid):
    while True:
        if mLoc[0] < pLoc[0]:#      DOWN
            print("DOWN")
            mLoc[0] += 1
        elif mLoc[0] > pLoc[0]:     # UP
            print("UP")
            mLoc[0] -= 1
        elif mLoc[1] < pLoc[1]:#  RIGHT
            print("RIGHT")
            mLoc[1] += 1
        elif mLoc[1] > pLoc[1]:# LEFT
            print("LEFT")
            mLoc[1] -= 1
        #if mLoc == pLoc:
        break

m = int(input())
x = input()
mLoc = []
pLoc = []
grid = []
for i in range(0, m):
    line = input().strip()
    if "m" in line:
        mLoc.append(i)
        mLoc.append(line.find("m"))
    if "p" in line:
        pLoc.append(i)
        pLoc.append(line.find("p"))
    grid.append(line)


displayPathtoPrincess(mLoc, pLoc, grid)
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/count-luck
'''
for t in range(int(input())):
    line = input().split()
    x = 0
    y = 0
    matrix = []
    for i in range(int(line[0])):
        line1 = list(input())
        matrix.append(line1)
        if "M" in line1:
            x = i
            y = line1.index("M")

    def printMatrix():
        for col in range(int(line[0])):
            for row in range(int(line[1])):
                print(matrix[col][row], end="\t")
            print()
        print()

    totalCount = 0

    def recur(x, y):
        global totalCount
        if  ((x - 1 >= 0 and matrix[x - 1][y] == "*") or
                 (y + 1 <= len(matrix[x])-1 and matrix[x][y + 1] == "*") or
                 (x + 1 <= len(matrix)-1 and matrix[x + 1][y] == "*") or
                 (y - 1 >= 0 and matrix[x][y - 1] == "*")):
            c = 0
            if (x - 1 >= 0 and matrix[x - 1][y] == "."):c+=1
            if (y + 1 <= len(matrix[x])-1 and matrix[x][y + 1] == "."):c+=1
            if (x + 1 <= len(matrix)-1 and matrix[x + 1][y] == "."):c+=1
            if (y - 1 >= 0 and matrix[x][y - 1] == "."):c+=1
            if c >= 1:
                totalCount += 1
            return True


        matrix[x][y] = "#"
        #printMatrix()

        count = 0
        status = False
        if x - 1 >= 0 and matrix[x - 1][y] == ".":              # up
            status = recur(x-1,y)
            count += 1
        if y + 1 <= len(matrix[x])-1 and matrix[x][y + 1] == ".":   # right
            status = status or recur(x,y+1)
            count += 1
        if x + 1 <= len(matrix)-1 and matrix[x + 1][y] == ".":      # down
            status = status or recur(x+1,y)
            count += 1
        if y - 1 >= 0 and matrix[x][y - 1] == ".":              # left
            status = status or recur(x,y-1)
            count += 1
        if count > 1 and status:
            totalCount += 1
            return status
        else:
            return status
    recur(x, y)
    expected = int(input())
    if expected == totalCount:
        print("Impressed")
    else:
        print("Oops!")
    #print(totalCount)
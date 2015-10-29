line1 = input().split()
size_col = int(line1[0])
size_row = int(line1[1])
rotations = int(line1[2])
same = ((size_col - 1) * 2) + ((size_row - 1) * 2)

matrix = []
for i in range(size_col):
    matrix.append(input().split())

def printMatrix():
    for col in range(size_col):
        for row in range(size_row):
            print(matrix[col][row], end="\t")
        print()
    print()

def splice(matrix, s):


def mess(word, i):
    make = ""

    return word

if rotations % same == 0:
    printMatrix()
else:
    save = 0
    save1 = ""
    for i in range(size_col):
        if i+1 != size_col:
            save = matrix[i][0]
            matrix[i] = save1.split() + mess(matrix[i][1:-1], i) + matrix[i+1][-1].split()
            print(matrix[i])
            save1 = save
        else:
            matrix[i] = save1.split() + matrix[i][:-1]
            print(matrix[i])

'''
3 3 1
1 2 3
4 5 6
7 8 9

4 4 1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

4 3 10
1 2 3
4 5 6
7 8 9
10 11 12

5 5 1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

6 6 1
1  2  3  4  5  6
7  8  9  10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36
'''
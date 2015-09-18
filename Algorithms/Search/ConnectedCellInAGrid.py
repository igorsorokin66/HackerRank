__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
'''
def search(x, y, data, v):
    data[x][y] = "0"
    total = v
    if x - 1 >= 0 and data[x - 1][y] == "1":                                    # up
        total += search(x - 1, y, data, 1)
    if y + 1 <= len(data[x])-1 and data[x][y + 1] == "1":                       # right
        total += search(x, y + 1, data, 1)
    if x - 1 >= 0 and y + 1 <= len(data[x])-1 and data[x-1][y+1] == "1":        # up right
        total += search(x-1, y+1, data, 1)
    if x + 1 <= len(data)-1 and data[x + 1][y] == "1":                          # down
        total += search(x + 1, y, data, 1)
    if x + 1 < len(data)-1 and y + 1 <= len(data[x])-1 and data[x+1][y+1] == "1":# down right
        total += search(x+1, y+1, data, 1)
    if y - 1 >= 0 and data[x][y - 1] == "1":                                    # left
        total += search(x, y - 1, data, 1)
    if x+1 <= len(data)-1 and y-1 >= 0 and data[x+1][y-1] == "1":               #down left
        total += search(x+1, y-1, data, 1)
    if x - 1 >= 0 and y - 1 >= 0 and data[x - 1][y - 1] == "1":                 # up left
        total += search(x-1, y-1, data, 1)
    return total

def test(data):
    largest = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] is "1":
                sav = search(x, y, data, 0)
                if sav > largest:
                    largest = sav
    return largest+1

data = []
useful = input()
waste = input()
for r in range(int(useful)):
    data.append(list(input().replace(" ", "")))
print(test(data))
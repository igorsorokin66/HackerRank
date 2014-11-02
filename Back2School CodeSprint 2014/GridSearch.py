__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved 50/50'

test_cases = input()
for t in range(int(test_cases)):
    grid_dimen = input().split(" ")
    grid_row = int(grid_dimen[0])
    grid_col = int(grid_dimen[1])
    grid = [[0 for x in range(grid_col)] for x in range(grid_row)]
    for c in range(grid_row):
        input_grid = input()
        for r in range(grid_col):
            grid[c][r] = input_grid[r]

    target_dimen = input().split(" ")
    target_row = int(target_dimen[0])
    target_col = int(target_dimen[1])
    target_grid = [[0 for x in range(target_col)] for x in range(target_row)]
    for x in range(target_row):
        input_target_grid = input()
        for y in range(target_col):
            target_grid[x][y] = input_target_grid[y]

    result = "NO"
    flag = False
    count = 1
    for x in range(grid_row - target_row + 1):
        for y in range(grid_col - target_col + 1):
            if target_grid[0] == grid[x][y:y+target_col]:
                for keepGoing in range(x+1, x + target_row):
                    if target_grid[keepGoing-x] == grid[keepGoing][y:y+target_col]:
                        count += 1
            if count == len(target_grid):
                result = "YES"
                flag = True
                break
        if flag:
            break
    print(result)
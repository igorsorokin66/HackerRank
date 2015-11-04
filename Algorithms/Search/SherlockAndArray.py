__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Complete'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-array
'''
def recur(arr, lower, i, upper):
    if i == lower or i == upper:
        return False
    sum1 = sum(arr[:i])
    sum2 = sum(arr[i+1:])
    if sum1 == sum2:
        return True
    elif sum1 > sum2:
        return recur(arr, lower, (i+lower)//2, i)
    else:
        return recur(arr, i, (i+upper)//2, upper)

for t in range(int(input())):
    waste = input()
    arr = [int(i) for i in input().split()]
    if len(arr) == 1:
        flag = True
    else:
        flag = recur(arr, 0, len(arr)//2, len(arr))
    if not flag:
        print("NO")
    else:
        print("YES")
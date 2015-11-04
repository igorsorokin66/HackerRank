__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/insertionsort1
'''
waste = input()
arr = [int(i) for i in input().split()]
for i in range(1, len(arr)):
    sav = arr[i]
    if arr[i-1] > arr[i]:
        for r in range(i, 0, -1):
            if arr[r-1] > sav:
                arr[r] = arr[r-1]
                if r-1 == 0:
                    print(*arr, sep=" ")
                    arr[r-1] = sav
                print(*arr, sep=" ")
            else:
                arr[r] = sav
                print(*arr, sep=" ")
                break
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/runningtime
'''
waste = input()
arr = [int(i) for i in input().split()]
count = 0
for i in range(1, len(arr)):
    sav = arr[i]
    if arr[i-1] > arr[i]:
        for r in range(i, 0, -1):
            if arr[r-1] > sav:
                count += 1
                arr[r] = arr[r-1]
                if r-1 == 0:
                    arr[r-1] = sav
            else:
                arr[r] = sav
                flag = True
                break
print(count)
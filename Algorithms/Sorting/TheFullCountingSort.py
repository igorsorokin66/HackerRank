__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/countingsort4
'''
waste = int(input())
arr = []
for i in range(waste):
    arr.append(input().split())
dicto = {}
for i in range(waste):
    a = arr[i]
    if i < waste//2:
        if a[0] in dicto:
            dicto[a[0]] += "-"
        else:
            dicto[a[0]] = ["-"]
    else:
        if a[0] in dicto:
            dicto[a[0]].append(a[1])
        else:
            dicto[a[0]] = [a[1]]

for k in sorted(dicto):
    print(*dicto[k], sep=" ", end=" ")
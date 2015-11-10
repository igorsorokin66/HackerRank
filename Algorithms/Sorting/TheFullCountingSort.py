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
    k = int(a[0])
    if i < waste//2:
        if k in dicto:
            dicto[k] += "-"
        else:
            dicto[k] = ["-"]
    else:
        if k in dicto:
            dicto[k].append(a[1])
        else:
            dicto[k] = [a[1]]

for k in sorted(dicto):
    #print(" ".join(dicto[k]), end=" ") #both of these work but this is faster?
    print(*dicto[k], sep=" ", end=" ")
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/two-arrays
'''
for t in range(int(input())):
    line = [int(i) for i in input().split()]
    n = line[0]
    k = line[1]
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()], reverse=True)
    flag = True
    for i in range(n):
        if a[i] + b[i] < k:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
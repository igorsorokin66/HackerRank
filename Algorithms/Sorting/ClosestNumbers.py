__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/closest-numbers
'''
waste = input()
arr = [int(i) for i in input().split()]
sarr = sorted(arr)

dicto = {}
for i in range(1, len(sarr)):
    val = sarr[i] - sarr[i-1]
    if val in dicto:
        dicto[val].append(sarr[i-1])
        dicto[val].append(sarr[i])
    else:
        dicto[val] = [sarr[i-1], sarr[i]]
print(*dicto[min(dicto)], sep=" ")
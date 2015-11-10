__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/jim-and-the-orders
'''
dicto = {}
for i in range(int(input())):
    total = sum([int(t) for t in input().split()])
    if total in dicto:
        dicto[total].append(i+1)
    else:
        dicto[total] = [i+1]

for k in sorted(dicto):
    print(*dicto[k], sep=" ", end=" ")
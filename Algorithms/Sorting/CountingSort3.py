__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/countingsort3
'''
waste = int(input())
arr = []
for i in range(waste):
    arr.append(input().split()[0])
dicto = {}
for a in arr:
    if a in dicto:
        dicto[a] += 1
    else:
        dicto[a] = 1

count = 0
for i in range(0, 100):
    if str(i) in dicto:
        count += dicto[str(i)]
    print(count, end=" ")
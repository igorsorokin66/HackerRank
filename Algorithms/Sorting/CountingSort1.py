__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/countingsort1
'''
waste = input()
arr = [i for i in input().split()]
dicto = {}
for a in arr:
    if a in dicto:
        dicto[a] += 1
    else:
        dicto[a] = 1

for i in range(0, 100):
    if str(i) in dicto:
        print(dicto[str(i)],end=" ")
    else:
        print(0, end=" ")
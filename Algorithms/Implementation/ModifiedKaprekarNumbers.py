__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/kaprekar-numbers
'''
p = int(input())
q = int(input())

sav = []
num = p**2
multi = (p+1)**2 - num
if p == 1:
    sav.append(1)
for i in range(p, q+1):
    if str(num)[:len(str(num))/2] != "" and int(str(num)[:len(str(num))/2]) + int(str(num)[len(str(num))/2:]) == i:
        sav.append(i)
    num += multi
    multi += 2

if len(sav) == 0:
    print("INVALID RANGE")
else:
    for s in sav:
        print(s, end="")
    print
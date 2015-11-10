__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/chocolate-feast
'''
T = int(input())

for i in range(T):
    N,C,M = map(int,input().split())
    total = N//C
    temp = total
    while True:
        add = temp // M
        excess = temp % M
        total += add
        add += excess
        temp = add
        if add < M:
            break
    print(total)
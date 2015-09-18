__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/diagonal-difference
'''
sum1 = 0
sum2 = 0
for t in range(int(input())):
    line = [int(i) for i in input().split()]
    sum1 += line[t]
    sum2 += line[len(line)-1-t]
print(abs(sum2-sum1))
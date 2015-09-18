__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/the-love-letter-mystery
'''
for t in range(int(input())):
    total = 0
    s = [ord(i) for i in input()]
    for i in range(0, len(s)//2):
        total += abs(s[i] - s[len(s)-1-i])
    print(total)
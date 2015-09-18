__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/plus-minus
'''
waste = input()
line = [int(i) for i in input().split()]
positives = 0
for l in line:
    if l > 0:
        positives += 1
zeroes = line.count(0)
negatives = len(line) - positives - zeroes
total = float(positives + zeroes + negatives)
print(positives/total)
print(negatives/total)
print(zeroes/total)
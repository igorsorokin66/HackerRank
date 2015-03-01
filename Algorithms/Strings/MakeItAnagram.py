__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/make-it-anagram
'''
def diff(a, b):
    count = 0
    for k in a.keys():
        if k in b:
            if a[k] - b[k] > 0:
                count += a[k] - b[k]
        else:
            count += a[k]
    return count

hashA = {}
a = list(raw_input())
for i in a:
    if i in hashA:
        hashA[i] += 1
    else:
        hashA[i] = 1

hashB = {}
b = list(raw_input())
for i in b:
    if i in hashB:
        hashB[i] += 1
    else:
        hashB[i] = 1

print(diff(hashA, hashB) + diff(hashB, hashA))
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/
'''

input = input()
import collections
letters = collections.Counter(input)
s = ""
for l in letters:
    for c in range(letters[l]):
        s += l

s = sorted(set(list(input)))
print(s)

#abcdabcd
#bcda abcd
#cdab dcba
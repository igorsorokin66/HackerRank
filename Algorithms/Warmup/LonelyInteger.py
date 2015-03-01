__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/lonely-integer
'''

waste = int(raw_input())
hash = {}
elements = raw_input().split(" ")
for i in range(len(elements)):
    if elements[i] in hash:
        del hash[elements[i]]
    else:
        hash[elements[i]] = i
print hash.values()[0]
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/gem-stones
'''
ll = []
for t in range(int(input())):
    ll.append(input())

result = set(list(ll[0]))
for l in ll:
    result = result.intersection(set(list(l)))
print(len(result))
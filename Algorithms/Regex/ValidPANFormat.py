__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/valid-pan-format
'''
for data in [input() for i in range(int(input()))]: print("YES") if list(set([c.isalpha() and c.isupper() for c in data[:5]] + [c.isdigit() for c in data[5:9]] + [c.isalpha() and c.isupper() for c in data[-1:]]))[0] else print("NO")
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/pangrams
'''
print("pangram" if sum(ord(i) for i in list(set(raw_input().lower()))) == 2879 else "not pangram")
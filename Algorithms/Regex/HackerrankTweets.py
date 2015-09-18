__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/hackerrank-tweets
'''
print(sum([1 if data.lower().find("hackerrank") != -1 else 0 for data in [input() for i in range(int(input()))]]))
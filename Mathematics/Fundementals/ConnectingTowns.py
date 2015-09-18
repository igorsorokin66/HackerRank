__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/connecting-towns
'''
testcases = input()
for t in range(testcases):
    towns = input()
    routes = input()
    multi = 1
    for i in routes.split(" "):
        multi *= int(i)
    print(multi % 1234567)
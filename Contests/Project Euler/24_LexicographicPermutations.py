__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/contests/projecteuler/challenges/euler024
'''
#NEEDS CLEANUP
import math
test_cases = int(raw_input())
for t in range(test_cases):
    l1 = list("abcdefghijklm")
    goal = int(raw_input())-1
    n = goal
    i = math.factorial(len(l1))
    v = 0
    output = ""
    while True:
        if i / 2 == 0:
            break
        n = (n - (v * i))
        i = int(math.ceil(i / len(l1)))
        if n % 2 == 0:
            n += 1
        v = n / i
        if i / 2 == 0 and goal % 2 == 0:
            v -= 1
        output += l1[v]
        del l1[v]
    output += l1[0]
    print output
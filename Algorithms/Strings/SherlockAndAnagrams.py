__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-anagrams
'''
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

test_cases = int(input())
for t in range(test_cases):
    dict = []
    hashy = {}
    word = input()#abccdaba
    for i in range(len(word)):
        dict.append(word[i])
        if word[i] in hashy.keys():
            hashy[word[i]] = hashy[word[i]]+1
        else:
            hashy[word[i]] = 1
        for n in range(i+1,len(word)):
            test = "".join(sorted(word[i:n+1]))
            dict.append(test)
            if test in hashy.keys():
                hashy[test] = hashy[test]+1
            else:
                hashy[test] = 1
    #print(dict)
    #print(hashy)
    total = 0
    for h in hashy.keys():
        if hashy[h] is not 1:
            total += nCr(hashy[h], 2)
    print(total)
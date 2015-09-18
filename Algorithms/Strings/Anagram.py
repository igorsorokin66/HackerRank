__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/anagram
'''
for t in range(int(input())):
    word = input()
    if len(word) % 2 != 0:
        print(-1)
    else:
        from collections import Counter
        s1 = Counter(list(word[:len(word)//2]))
        s2 = Counter(list(word[len(word)//2:]))
        diff = s1-s2
        print(len(list(diff.elements())))
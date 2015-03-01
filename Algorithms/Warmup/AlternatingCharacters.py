__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/alternating-characters
'''
test_cases = int(raw_input())

for t in range(test_cases):
    word = list(raw_input())
    prev = word[0]
    count_deletions = 0
    for i in range(1, len(word)):
        current = word[i]
        if len(word) == 1 or i + 1 > len(word):
            break
        if prev == current:
            count_deletions += 1
        prev = current
    print(count_deletions)
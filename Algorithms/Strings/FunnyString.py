__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/funny-string
'''
for t in range(int(input())):
    s = input()
    r = str(s[::-1])
    fail = False
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            print("Not Funny")
            fail = True
            break
    if not fail:
        print("Funny")
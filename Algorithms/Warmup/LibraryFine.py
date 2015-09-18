__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/library-fine
'''
date1 = [int(i) for i in input().split()]
date2 = [int(i) for i in input().split()]
if date2[2] > date1[2] or (date1[2] == date2[2] and date2[1] > date1[1]) or (date1[2] == date2[2] and date2[1] == date1[1] and date2[0] > date1[0]):
    print(0)
elif date1[2] != date2[2] and ((12-date2[1]+date1[1] > 12) or (12-date1[1]+date2[1] == 12 and date2[0] >= date1[0])):
    print(10000)
elif date1[2] != date2[2] and date1[1] == 1 and date1[0] == 1 and date2[1] == 12 and date2[0] == 31:
    print(10000)
elif date1[1] != date2[1]:
    print(500 * abs(date1[1] - date2[1]))
elif date1[0] != date2[0]:
    print(15 * abs(date1[0] - date2[0]))
else:
    print(0)
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/time-conversion
'''
line = input()
if line[:2] == "12" and line[-2:] == "AM":
    print("00"+line[2:-2])
elif line[-2:] == "AM" or line[:2] == "12" and line[-2:] == "PM":
    print(line[:-2])
else:
    print(str(int(line[:2])+12)+line[2:-2])
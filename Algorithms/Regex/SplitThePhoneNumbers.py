__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/find-hackerrank
'''
for t in range(int(input())):
    line = input()
    if "-" in line:
        update = line.split("-")
    else:
        update = line.split(" ")
    print("CountryCode="    + update[0] +
          ",LocalAreaCode=" + update[1] +
          ",Number="        + update[2])
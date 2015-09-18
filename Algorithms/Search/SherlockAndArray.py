__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Incomplete, failing for test cases 3 and 4'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-array
'''
for t in range(int(input())):
    waste = input()
    arr = [int(i) for i in input().split()]
    flag = False
    for i in range(len(arr)):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[i+1:])
        if sum1 == sum2:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")
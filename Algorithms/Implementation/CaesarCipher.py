__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/caesar-cipher-1
'''
waste = input()
arr = [ord(i) for i in list(input())]
r = int(input()) % 26
for i in range(len(arr)):
    if arr[i] >= 97 and arr[i] <= 122:
        if arr[i] + r > 122:
            arr[i] = 96 + (arr[i] + r - 122)
        else:
            arr[i] += r
    elif arr[i] >= 65 and arr[i] <= 90:
        if arr[i] +r > 90:
            arr[i] = 64 + (arr[i] + r - 90)
        else:
            arr[i] += r
print("".join([chr(i) for i in arr]))
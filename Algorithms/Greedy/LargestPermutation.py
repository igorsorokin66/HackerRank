__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/largest-permutation
'''
line1 = input()
n = int(line1.split(" ")[0])
swaps = int(line1.split(" ")[1])
line2 = input()
numbers = [int(i) for i in line2.split(" ")]

hashy = {}
for i in range(len(numbers)):
    hashy[numbers[i]] = i
#print(hashy)

ptr = 0
while swaps != 0 and n != 0 and ptr < len(numbers):
    for i in range(n, 0, -1):
        if hashy[i] != ptr:
            sav = numbers[ptr]
            numbers[hashy[i]], numbers[ptr] = numbers[ptr], numbers[hashy[i]]
            hashy[sav] = hashy[i]
            ptr += 1
            n -= 1
            break
        else:
            ptr += 1
            n -= 1
    swaps -= 1
for i in numbers:
    print(i, end="")
print
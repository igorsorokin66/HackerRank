__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/flowers
'''
firstLine = input()

goalFlowers = int(firstLine.split()[0])
numberOfFriends = int(firstLine.split()[1])
costOfFlowers = [int(i) for i in input().split()]

total = 0
x = 0
while len(costOfFlowers) != 0:
    for f in range(numberOfFriends):
        total += max(costOfFlowers) * (x+1)
        costOfFlowers.remove(max(costOfFlowers))
        if len(costOfFlowers) == 0:
            break
    x += 1
print(total)
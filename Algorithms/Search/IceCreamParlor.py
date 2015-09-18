__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/icecream-parlor
'''
for t in range(int(input())):
    money = int(input())
    waste = input()
    costs = input().split()

    arr = []
    for i in range(money-1, 0, -1):
        if str(money-i) in costs and str(i) in costs:
            arr.append(costs.index(str(money-i))+1)
            if costs.index(str(money-i)) != costs.index(str(i)):
                arr.append(costs.index(str(i))+1)
                break
            if money-i == i:
                costs.remove(str(i))
                arr.append(costs.index(str(i))+2)
    print(" ".join([str(k) for k in sorted(arr)]))
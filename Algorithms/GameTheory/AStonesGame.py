__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Incomplete'
'''
Problem Statement:
https://www.hackerrank.com/challenges/half
'''
for t in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n, 0, -1):
        arr.append(i)
    print(arr)

    #round to the closest power of 2
    for i in range(len(arr)):
        arr[i] = 2**(len(bin(arr[i]).split("b")[1])-1)
    print(arr)

    #orphans
    newArr = []
    for a in arr:
        if a not in newArr:
            newArr.append(a)
        else:
            newArr.remove(a)
    print("Orphans: " + str(newArr))

    if len(newArr) == 1:
        print(newArr[0])
    elif len(newArr) == 2:#two orphans, you cant remove either
        diff = max(newArr) - min(newArr)
        print("Easy Diff: " + str(diff))
        newOrphans = list(set(arr).difference(set(newArr)))
        print("Possible Orphans: " + str(newOrphans))

        if diff < max(newOrphans): #case 6 (3 < 2)
            print(diff)
        else:
            print(max(newOrphans))
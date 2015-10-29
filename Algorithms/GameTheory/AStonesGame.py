__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Incomplete'
'''
Problem Statement:
https://www.hackerrank.com/challenges/half
'''
def perm(orphans):
    for i in range(len(orphans)):
        newOrphans = list(orphans)
        if newOrphans[i] == 1:
            del newOrphans[i]
        else:
            newOrphans[i] /= 2
'''
32 1
32 8 4 1
    16 8 4 1
        16 8 4
            8 4 2
            8 4 1
                4 2 1
1 2 4 8 16 32
1 2 3 4  5  6
6 4 3 1
    5 4 3 1
64 32 16 8 4 2 1
'''

for t in range(1):#int(input())):
    n = 64#int(input())
    arr = []
    for i in range(n, 0, -1):
        arr.append(i)
    print(arr)

    #round to the closest power of 2
    for i in range(len(arr)):
        arr[i] = 2**(len(bin(arr[i]).split("b")[1])-1)
    print(arr)

    #orphans
    orphans = []
    for a in arr:
        if a not in orphans:
            orphans.append(a)
        else:
            orphans.remove(a)
    print("Orphans: " + str(orphans))

    newOrphans = list(set(arr).difference(set(orphans)))
    print("Possible Orphans: " + str(newOrphans))

    for newOrphan in newOrphans:
        choice = list(orphans)
        choice.append(newOrphan)
        print(choice)
        print(perm(choice))
    '''
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
    '''

'''
8 1
'''
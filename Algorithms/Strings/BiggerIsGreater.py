__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/bigger-is-greater
'''
for t in range(int(input())):
    l = [ord(i) for i in input()]

    flag = False
    for i in range(len(l)-1, 0, -1):
        if l[i] > l[i-1]:
            nextBiggestValue = sorted(set(l[i-1:]))[sorted(set(l[i-1:])).index(l[i-1])+1]
            nextBiggestIndex = i-1 + l[i-1:].index(nextBiggestValue)
            l[nextBiggestIndex], l[i-1] = l[i-1], l[nextBiggestIndex]
            l = l[:i] + sorted(l[i:])
            flag = True
            break
    if flag:
        #print(l)
        print("".join([chr(i) for i in l]))
    else:
        print("no answer")
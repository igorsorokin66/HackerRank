__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/
'''

l1 = [1, 2]
l2 = [2, 3]
l3 = [1, 3]


def stones(du):
    for i in range(len(du)):
        cp = list(du)
        print(cp)
        toR = int(cp[0] / 2)
        if 0 is toR:
            print("Removing: " + str(toR) + "\n")
            cp[0] = toR
            print(cp)
            if 0 in cp:
                cp.remove(0)
            stones(cp)
        else:
            for r in range(1, toR+1):
                cp2 = list(cp)
                print("Removing: " + str(toR) + "\n")
                cp2[0] = r
                print(cp2)
                if 0 in cp2:
                    cp2.remove(0)
                stones(cp2)


stones([i for i in range(1, 7)])
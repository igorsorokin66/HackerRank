__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/sherlock-and-the-beast
'''
for t in range(int(input())):
    n = int(input())
    if n < 3:
        print(-1)
    elif n % 3 == 0:
        if n % 3 == 0:
            print(*[5 for i in range(n)], sep="")
    else:
        flag = True
        for r in range(5, (n//5)*5, 5):
            if (n - r) % 3 == 0:
                first = [3 for i in range(r)]
                second = [5 for i in range(n-len(first))]
                print(*second+first, sep="")
                flag = False
                break
        flag2 = True
        if flag:
            for r in range(3, (n//3)*3, 3):
                if (n - r) % 5 == 0:
                    first = [5 for i in range(r)]
                    second = [3 for i in range(n-len(first))]
                    print(*first+second, sep="")
                    flag2 = False
                    break
            if flag2:
                if n % 5 == 0:
                    print(*[3 for i in range(n)], sep="")
                else:
                    print(-1)
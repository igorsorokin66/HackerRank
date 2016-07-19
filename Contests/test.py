__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/build a string
'''
#6-4L
#33 - 1 L
#35 - 32 L = 3 - 2 R
#37 - 32 L = 5 - 4 R
#39 - 32 L = 7 - 4 R 3 - 2 L

count = 0
a = ["3", "4", "7"]
goal = 40
for i in range(15000000):
    if len(set(list(str(i))).intersection(set(a))) == 0:
        count += 1
        print(i)
    if count == goal:
        print(i + 1)
        break

dividend = 1000000
lookup = ["0", "1", "2", "5", "6", "8", "9"]
answer = ""
while not dividend < 7:
    quotient = dividend // 7
    remainder = dividend - (quotient * 7)
    answer += lookup[remainder]
    dividend = quotient
answer += lookup[dividend]
print(answer)
'''
tree = {
        1:
            {2:
                 {4:{},5:{}},
             3:
                 {6:{},7:{}}
             }
    }

def bfs(node, q):
    q2 = []
    for n in node.keys():
        q.append(n)
        q2.extend(bfs(node[n], []))
    q.extend(q2)
    return q

root = tree[1]
q = [i for i in tree.keys()]
bfs(root, q)
print(q)
'''
'''
for t in range(int(input())):
    flag = "Louise"
    n = int(input())
    while n != 1:
        if '1' in bin(n).split("b")[1][1:]:
            if bin(n).split("b")[1][1:].count('1') % 2 == 0:
                flag = "Louise"
           d  else:
                flag = "Richard"
        else:
            if len(bin(n).split("b")[1]) % 2 == 0:
                flag = "Louise"
            else:
                flag = "Richard"
        break
    print(flag)
'''
# def partitions(s):
#     if s:
#         for i in range(1, len(s) + 1):
#             for p in partitions(s[i:]):
#                 yield [s[:i]] + p
#     else:
#         yield []
#
# for t in range(int(input())):
#     l, a, b = [int(i) for i in input().split(" ")]
#     s = input()
#     g = ""
#     subsets = []
#     while len(g) != l:
#         if True:
#             g += s[0]
#             subsets += partitions(g)
#             s = s[1:]


'''
2
9 4 5
aabaacaba
9 8 9
bacbacacb
'''
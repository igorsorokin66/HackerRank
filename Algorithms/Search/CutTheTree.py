__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'InCompleted'
'''
Problem Statement:
https://www.hackerrank.com/challenges/cut-the-tree
'''
waste = int(input())
vals = {}
i = 1
summy = 0
for elem in input().split():
    vals[i] = {'v': int(elem)}
    summy += int(elem)
    i += 1

save = []
used = {}
for c in range(waste-1):
    conn = [int(i) for i in input().split()]

    if conn[1] in used:
        save.append([conn[1],conn[0]])
        vals[conn[1]][conn[0]] = vals[conn[0]]
    else:
        save.append(conn)
        vals[conn[0]][conn[1]] = vals[conn[1]]
    used[conn[1]] = 0
#print(vals)

def trav(ele):
    total = ele['v']
    for k in ele.keys():
        if k != 'v':
            total += trav(ele[k])
    return total

lowest = summy
for s in save:
    found = abs(summy - trav(vals[s[1]]) - trav(vals[s[1]]))
    #print(found)
    if found < lowest:
        lowest = found
print(lowest)
'''
6
100 200 100 500 100 600
1 2
2 3
2 5
4 5
5 6

{1:
    {2:
        {3: {'v': 100},
        5:
            {6: {'v': 600},
        'v': 100},
    'v': 200},
'v': 100},

2:
    {3: {'v': 100},
    5:
        {6: {'v': 600},
    'v': 100},
'v': 200},

3: {'v': 100},

4:
    {5:
        {6: {'v': 600},
    'v': 100},
'v': 500},

5:
    {6: {'v': 600}, 'v': 100},

6: {'v': 600}}

{1:
    {2:
        {3:
            {'v': 100},
        5:
            {4: {'v': 500},
            6: {'v': 600},
        'v': 100},
    'v': 200},
'v': 100},

2:
    {3: {'v': 100},
    5:
        {4: {'v': 500},
        6: {'v': 600},
    'v': 100},
'v': 200},

3: {'v': 100},
    4: {'v': 500},
    5:
        {4:
        {'v': 500}, 6: {'v': 600}, 'v': 100},

6: {'v': 600}}

'''
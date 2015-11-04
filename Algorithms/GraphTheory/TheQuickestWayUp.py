__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/the-quickest-way-up
'''
for t in range(int(input())):
    number_of_ladders = int(input())
    ladders = {}
    for l in range(number_of_ladders):
        line = [int(i) for i in input().split()]
        ladders[line[0]] = line[1]

    number_of_snakes = int(input())
    snakes = {}
    for s in range(number_of_snakes):
        line = [int(i) for i in input().split()]
        snakes[line[0]] = line[1]

    used = []
    found = False
    queue = [[1, 0]]
    while len(queue) != 0:
        current = queue[0][0]
        possible = set([i for i in range(current+1, current + 7)]).difference(set(used))
        if len(possible) == 0:
            break

        count = queue[0][1]
        del queue[0]#dequeue
        if max(possible) not in snakes:
            addToQueue = [max(possible)]
        else:
            addToQueue = []
        possibleLadders = list(possible.intersection(set(ladders)))
        if len(possibleLadders) != 0:
            addToQueue += [ladders[k] for k in possibleLadders]
        possibleSnakes = list(possible.intersection(set(snakes)))
        if len(possibleSnakes) != 0:
            addToQueue += [snakes[k] for k in possibleSnakes]

        used += addToQueue
        if 100 in possible:
            print(count+1)
            found = True
            break
        elif 100 in addToQueue:
            print(count+1)
            found = True
            break
        queue += list(zip(addToQueue, [count+1 for i in range(len(addToQueue))]))
    if not found:
        print(-1)
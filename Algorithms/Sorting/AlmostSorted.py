__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/almost-sorted
'''
useless = input()
suzy = [int(i) for i in input().split()]

reverseFlag = False
reverseCount = 0
start = 0
end = 0
correctOrderFlag = True
swap = False
for i in range(0, len(suzy)-1):
    if correctOrderFlag:
        if suzy[i] > suzy[i+1]:
            start = i
            correctOrderFlag = False
    else:
        if suzy[i] > suzy[i+1] and not swap:
            if reverseCount >= 1:
                reverseFlag = True
            reverseCount += 1
        elif reverseFlag:
            end = i
            break
        elif suzy[i] < suzy[start] and suzy[i+1] > suzy[start]:
            end = i
            swap = True
            break

if swap and not reverseFlag or start + end == 0:
    if start + end == 0:
        end = start + 1
    fix = list(suzy)
    save = fix[start]
    fix[start] = fix[end]
    fix[end] = save
    if fix == sorted(suzy):
        print("yes")
        print("swap " + str(start+1) + " " + str(end+1))
    else:
        print("no")
else:
    fix = suzy[:start] + list(reversed(suzy[start:end+1])) + suzy[end+1:]
    if fix == sorted(suzy):
        print("yes")
        print("reverse " + str(start+1) + " " + str(end+1))
    else:
        print("no")
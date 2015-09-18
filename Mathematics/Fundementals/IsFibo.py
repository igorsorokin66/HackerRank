__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/is-fibo
'''
dict = {0:0, 1:0}
prev = 0
biggest = 1
test_cases = input()
for t in range(int(test_cases)):
    n = input()
    while n > biggest:
        save = biggest
        biggest += prev
        prev = save
        dict[biggest] = 0
    if n in dict.keys():
        print("IsFibo")
    else:
        print("IsNotFibo")
__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/taum-and-bday
'''
test_cases = int(input())
for t in range(test_cases):
    firstLine = input()
    required_black_gifts = int(firstLine.split(" ")[0])
    required_white_gifts = int(firstLine.split(" ")[1])

    secondLine = input()
    cost_of_black_gift = int(secondLine.split(" ")[0])
    cost_of_white_gift = int(secondLine.split(" ")[1])
    cost_of_conversion = int(secondLine.split(" ")[2])

    if cost_of_black_gift is cost_of_white_gift:
        print(required_black_gifts * cost_of_black_gift + required_white_gifts * cost_of_white_gift)
    else:
        if cost_of_black_gift > cost_of_white_gift:
            cost_of_cheaper_gift = cost_of_white_gift
            required_cheaper_gifts = required_white_gifts
            cost_of_expensive_gift = cost_of_black_gift
            required_expensive_gifts = required_black_gifts
        else:
            cost_of_cheaper_gift = cost_of_black_gift
            required_cheaper_gifts = required_black_gifts
            cost_of_expensive_gift = cost_of_white_gift
            required_expensive_gifts = required_white_gifts
        total = 0
        total += cost_of_cheaper_gift * required_cheaper_gifts
        test_expensive_cost = cost_of_expensive_gift * required_expensive_gifts
        test_conversion_cost = required_expensive_gifts * (cost_of_cheaper_gift + cost_of_conversion)
        if test_expensive_cost > test_conversion_cost:
            total += test_conversion_cost
        else:
            total += test_expensive_cost
        print(total)
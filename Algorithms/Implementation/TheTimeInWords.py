__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/the-time-in-words
'''
def numToWord(num):
    if num == 1:    return "one "
    elif num == 2:  return "two "
    elif num == 3:  return "three "
    elif num == 4:  return "four "
    elif num == 5:  return "five "
    elif num == 6:  return "six "
    elif num == 7:  return "seven "
    elif num == 8:  return "eight "
    elif num == 9:  return "nine "
    elif num == 10: return "ten "
    elif num == 11: return "eleven "
    elif num == 12: return "twelve "
    elif num == 13: return "thirteen "
    elif num == 14:  return "fourteen "
    elif num == 15:  return "fifteen "
    elif num == 16:  return "sixteen "
    elif num == 17:  return "seventeen "
    elif num == 18:  return "eighteen "
    elif num == 19:  return "nineteen "
    elif num >= 20 and num < 30:  return "twenty"+" "+numToWord(num-20)
    elif num > 30 and num < 45:    return numToWord(60-num)
    elif num > 45 and num < 60:    return numToWord(60-num)
    return ""

h = int(input())
m = int(input())

if m == 0:
    print(numToWord(h)+"o' clock")       #5:00
elif m <= 30:
    if m == 1:
        print("one minute"), #5:01
    elif m == 15:
        print("quarter"),
    elif m == 30:
        print("half"),       #5:30
    else:
        print(numToWord(m) + "minutes"), #5:02-29
    print("past " + numToWord(h))
else:
    if m == 45:
        print("quarter"),
    else:
        print(numToWord(m) + "minutes"),
    if h+1 == 13:
        h = 0
    print("to " + numToWord(h+1))
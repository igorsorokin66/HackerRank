__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved 20/20'

input = input().split(" ")
a = int(input[0])
b = int(input[1])
n = int(input[2])
sum = b
for i in range(n-2):
    temp = sum
    b = pow(sum, 2)
    sum = b + a
    a = temp
print(sum)
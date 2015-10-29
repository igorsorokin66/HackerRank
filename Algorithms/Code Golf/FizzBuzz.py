__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
https://www.hackerrank.com/challenges/fizzbuzz
'''
print(*[((i,"Buzz")[i%5==0],("Fizz","FizzBuzz")[i%5==0])[i%3==0]for i in range(1,101)],sep='\n')
#Java Solution
#class S{public static void main(String[]a){for(int i=0;i++<100;){System.out.println(i%3<1?i%5<1?"FizzBuzz":"Fizz":i%5<1?"Buzz":i);}}}
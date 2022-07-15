from math import factorial
from numbers import Number
import numbers


number = int(input("Enter number : "))
factorial = 1

if (number < 0):
  print("Not inclusive in the question")
elif (number < 2):
  print("{}! = {}".format(number, factorial))
else:
  for num in range(number, 1, -1):
    factorial = factorial * num
  print("{}! = {}".format(number, factorial))
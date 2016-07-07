"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    expression = raw_input("Enter expression here: ")
    tokens = expression.split(" ")
    if tokens[0] == 'q':
        break

    integer_one = int(tokens[1])
    integer_two = int(tokens[2])

    if tokens[0] == '+':
        print add(integer_one, integer_two)
    elif tokens[0] == '-':
        print subtract(integer_one, integer_two)
    elif tokens[0] == '*':
        print multiply(integer_one, integer_two)
    else:
        break       
# Your code goes here

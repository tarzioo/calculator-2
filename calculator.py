"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    # get input from user
    expression = raw_input("Enter expression here: ")
    #Split expression into elements based on space
    tokens = expression.split(" ")
    # Check the length of tokens, if it is = 1 then check if it is 'q' 
    # or "Q". If neither, then throw error.
    if len(tokens) == 1:
        if tokens[0].lower() == 'q':
            break

        else:
            print "Unexpected input"
            continue
    #Check if length of tokens is 2 
    elif len(tokens) == 2:
        #Type cast from raw_input to integer
        integer_one = int(tokens[1])
        #if tokens[0] is equal to square, call upon the square function,
        #setting integer_one as its parameter
        if tokens[0] == 'square':
            print square(integer_one)
        # if token[0] is equal to 'cube', call cube function from arithmetic
        elif tokens[0] == 'cube':
            print cube(integer_one)
        # throws error if it's anything else
        else:
            print "Unexpected input"
            continue

    elif len(tokens) == 3:
        integer_one = int(tokens[1])
        integer_two = int(tokens[2])

        if tokens[0] == '+':
            print add(integer_one, integer_two)
        elif tokens[0] == '-':
            print subtract(integer_one, integer_two)
        elif tokens[0] == '*':
            print multiply(integer_one, integer_two)
        elif tokens[0] == '/':
            print divide(integer_one, integer_two)
        elif tokens[0] == 'pow':
            print power(integer_one, integer_two)
        elif tokens[0] == 'mod':
            print mod(integer_one, integer_two)
        else:
            print "Unexpected input"
            continue

    else:
        print "Unexpected input"
        continue    

# Your code goes here

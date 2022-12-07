
"""
"""

import doctest

def load_program(filename):
    """ Hint 1: For reading the lines from the file you may want to use 
        file.read.splitlines to build a list of lines.

        >>> len(load_program('step_2.txt'))
        1000
    """
    with open(filename,'r') as fp:
        return fp.read().splitlines()

def calculate( operator_name, operand_1, operand_2):
    """ 
    Write a basic Python "calculator".
    It should accept 3 pieces of input from the user: a string that's one of "x", "+", "
    "--", or
    "/" (an operation), an integer (parameter A), and another integer (parameter B).
    It should then emit the result of performing the operation on A and B.

    For example, if your application asks the user for an operation and 2 numbers, and
    the user enters "+", "1", "2", then the application should output "3".

    >>> calculate( '+', 1, 2)
    3

    If the user supplied "/", "5", "2", the application should output "2.5".

    >>> calculate( '/', 5, 2)
    2.5

    If the user supplied "x", "5", "0", the application should output 0.

    >>> calculate( 'x', 5, 0)
    0

    """
    if operator_name == '+':
        return operand_1 + operand_2
    elif operator_name == '/':
        return operand_1 / operand_2
    else:
        return operand_1 * operand_2

def split_program_line(line):
    """ get the operator and operands from a program line 
    
    >>> split_program_line('calc x 1 2')
    ('x', 1, 2)
    """
    _calc, operator_name, operand_1, operand_2 = line.split()
    return operator_name,int(operand_1), int(operand_2)

def execute_program(program):
    """ given a program, execute it and yield the results of all the calculations
    >>> list(execute_program(['calc x 2 3','calc + 1 4']))
    [6, 5]
    """
    for line in program:
        operator_name, operand_1, operand_2 = split_program_line(line)
        yield calculate(operator_name, operand_1, operand_2)

def main():
    """
    >>> main()
    Answer: 1449679.3057730473

    """
    program = load_program('step_2.txt')
    accumulator=sum(execute_program(program))
    print(f'Answer: {accumulator}')


"""
"""

import doctest

#def

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


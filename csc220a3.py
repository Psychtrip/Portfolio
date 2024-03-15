# Pulled from another file labeled "Array Stack"
from array_stack import ArrayStack


def do_operation(left, operator, right):
    """ Perform an arithmetic operation.
        Input: left - the operand on the left
               operator - the operator
               right - the operand on the right
        Output: the result of the operator
    """
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    else:  # operator == '/'
        return left / right


def evaluate(expression):

    # Checks to see if given parameter is a tuple
    if type(expression) != tuple:
        return None

    # Establishes variables left and right, assigns 'arith_Stack' to ArrayStack()
    arith_Stack = ArrayStack()
    left = 0
    right = 0

    # Loops for the length of the given tuple, so all elements can be inspected
    for i in range(len(expression)):

        # Checks to see if the TYPE of the element at given location is int
        # if it is an int, pushes the element to the top of the stack
        if type(expression[i]) == int:
            arith_Stack.push(expression[i])

        # If element isnt an int, checks to see if it is str
        # If true, pops top of stack to right, and then pops the new element to left
        # Plugs given parameters into do_operation function, pushes its results back into stack
        elif type(expression[i]) == str:
            right = arith_Stack.pop()
            left = arith_Stack.pop()
            arith_Stack.push(do_operation(left, expression[i], right))

        # Guard incase either if statements are not fulfilled
        else:
            return None

    # returns the only number in the stack, use int to confirm it is correctly outputted
    return int(arith_Stack.pop())

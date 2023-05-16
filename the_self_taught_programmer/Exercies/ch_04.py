# Chalenge 1
def squared(x):
    """
    Return square of x.
    :int, float  x: int, float
    :int, float return: int, float 
    """
    return x ** 2

print(squared(2))
print(squared(2.0))

# Chalenge 2
def return_string(str_1):
    """
    Input string, then return back.
    :str str_1: string
    :return: str
    """
    return str_1
print(return_string('String!'))

# Chalenge 3
def sum_numbers(a, b, c, d = 0,e = 0):
    """
    Sum of 5 numbers.
    :int, float a: int, float
    :int, float b: int, float
    :int, float c: int, float
    :int, float d: int, float
    :int, float e: int, float
    """
    return a + b + c + d + e
print(str(sum_numbers(1,2,3,4,5)))

# Chalenge 4
def divide_two(x):
    """
    Divide x by two.
    """
    return int(x / 2)

def multiply_four(y):
    """
    Multiply y by 4
    """
    return y * 4

print(multiply_four(divide_two(21)))

# Chalenge 5
def turn_to_float(text):
    try:
        return float(text)
    except (ValueError):
        return 'Only int or float'

print(turn_to_float(2))
print(turn_to_float(2.0))
print(turn_to_float('text'))
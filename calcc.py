def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def default_operation(x, y):
    return

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator(operator, x, y):
    operation = operators.get(operator, default_operation)
    return operation(x, y)
print(calculator('*', 10, 15))
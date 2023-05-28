import numpy as np

def add(n1, n2):
    if isinstance(n1, str):
        print("n1 should not be a string")
    elif isinstance(n2, str):
        print("n2 should not be a string")
    else:
        return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    
    if n2 != 0:
        return n1/n2
    else:
        print("n2 should not be zero")


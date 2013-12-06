#!/usr/bin/python

def fibonacci(count):
    """
    Shaked created this func in Dec 2013
    fibonacci.fibonacci(num)
    """
    
    first = 0
    second = 1
    
    for i in range(count):
        second = first + second
        first = second - first
    
    return first

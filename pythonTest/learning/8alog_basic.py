#!/usr/bin/env python
n = 10
# Fib in recurrison way
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print fib(n)

# Fib in non-recurrison way (pythonist)
def fib2(n):
    a, b = 0 , 1
    for i in range(n):
        a, b = b, a + b
    return a
print fib2(n)

# Fib in non-recurrison way (non-pythonist)
def fib3(n):
    a, b = 0 , 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a
print fib3(n)

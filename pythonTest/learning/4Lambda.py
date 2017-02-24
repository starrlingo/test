#!/usr/bin/env python

# lambda function
square = lambda x: x**2
print square(3)

min = lambda a, b: a if a < b else b
print min(7, 3)

# execute anonymous lambda immediately
print( (lambda x: x ** 2)(3))

# lambda with sorted function
def keySort(x): return x[1]
print sorted(li, key=keySort)

li = [('C', 180, 65), ('B', 160, 60), ('A', 170, 40)]
print sorted(li, key=lambda x: x[1])


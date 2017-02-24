
# Special argument *, ** in function parameter
# positional argument (unpacking operator)
def f(x, y, z): print (x,y,z)
array = [1,2,3]
f(*array)
f(*range(1,4))

# keyword argument
dictionary = {'x': 1, 'y': 2, 'z': 3}
f(**dictionary)

# positional argument combined with keyword argument
def f(a, b, c, d):
    print (a, b, c, d)
array = [1,2]
dictionary = {'c': 1, 'd': 2}
f(*array, **dictionary)

# Special argument *, ** in function argument
def f(x, y, *t): print(x, y, t)
f(1,2,3,4,5)
def f(x, y, **d): print(x, y, d)
f(1,2,k1=3, k2=4, k3=5)

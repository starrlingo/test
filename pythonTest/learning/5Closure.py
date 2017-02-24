# Closure example1
def target_value(x):
    prefix = 'Result:'  # x and prefix are all closures
    def compare(y):
        return prefix + 'greater than target' if y > x else prefix + 'less than target'
    return compare

func = target_value(10)
print(func(5))

func2 = target_value(3)
print(func2(5))

print('Closure[0]:' + str(func.__closure__[0].cell_contents))
print('Closure[1]:' + str(func.__closure__[1].cell_contents))

# Closure example2
def fib():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo:
            memo[n] = sub(n-1) + sub(n-2)
        print memo
        return memo[n]
    return sub
fib_1 = fib()
print(fib_1(0))

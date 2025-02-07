# GENERATORS
# Generators are a special type of iteraotr that generates values lazily
# They are defined using a function with the "yield" keyword instead of return
# They are memory-efficient because they produce values on-the-fly rather than storing them in a memory

#Fibonacci series using generators

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


fib = fibonacci(10)
for num in fib:
    print(num)
    


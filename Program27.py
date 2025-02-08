def series(n, total=0):
    if n == 0:
        yield total  # Base case: return the final sum
    else:
        yield from series(n - 1, total + n * n)  # Recursively accumulate sum

# Calling the generator with n=6
result = series(6)

# Printing the result
for x in result:
    print(x)

# Lambda, Map, and Filter

# Function to check even/odd using lambda
checkeven = lambda x: print("even") if (x % 2 == 0) else print("odd")

my_number = int(input("Enter a value: "))
checkeven(my_number)

# Lambda function for squaring a number
x = lambda a: a * a
print(x(5))

lst = [3, 3, 4, 5, 2, 3, 4, 52]

# Segregating even and odd numbers
evenLambda = lambda x: x % 2 == 0
oddLambda = lambda x: x % 2 != 0

evenList = list(filter(evenLambda, lst))
oddList = list(filter(oddLambda, lst))

print(evenList)
print(oddList)  # Using list() to correctly display the filtered values

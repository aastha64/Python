# Using generators calculate the following series

# 1 + 4 + 9 + 16 + 25 + 36

def series():
    sum = 0
    counter = 1
    while(counter <= 6):
        sum += counter * counter
        counter += 1
    yield(sum)

result = series()
for x in result:
    print(x)
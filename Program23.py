# ITERATORS
# An iterator is an object that contains a coutable number of values
# They implement the iterator protocol, which requires two methods:  _iter_() and _next_() 
# Iters are used to iterate over containers like lists, sets, tuples and dictionaries

city = ("Mumbai", "Shanghai", "New York", "Tokyo", "Sydney")
y = len(city)
city = iter(city)
print(type(city))
next(city)
#for x in range(0, y):
    #print(next(city))

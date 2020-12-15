from functools import reduce

my_var = lambda x, y: x + y
print(my_var(7, 5))

Lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, Lst)))

print(list(filter(lambda x: x > 2, Lst)))

print(reduce(lambda x, y: x * y, Lst))

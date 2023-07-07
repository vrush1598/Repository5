from functools import reduce
lis = [12, 23, 4, 11]
list1 = reduce(lambda x, y:  x * y, lis)
print(list1)
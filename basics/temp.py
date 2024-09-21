import sys

mygenerator = (i for i in range(10000000) if i % 2 == 0)
print(sys.getsizeof((mygenerator)))
mylist = [i for i in range(10000000) if i % 2 == 0]
print(sys.getsizeof(mylist))

#2). Index() - return the index of particular element.
# Syntax: tuple_name.index(element)

prime=(1,3,5,7,11,5,13,17,19,5,23,27,33,(3,7,8))
print(prime.index(1))
print(prime.index(7))
a,b=prime.index(3),prime.index(27)
print(a,b)
c=prime.index(33)
print(c,prime.index(19))

# if elem. is present more than once it return the index of first elem.
print(prime.index(5))
# if elem. is not present then it return error.

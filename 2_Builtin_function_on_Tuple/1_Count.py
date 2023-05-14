#5]. Different methods or builtin function : there are different methods or builtin function available for tuple.

#1). Count() - return the max. count of particular elem.

# Syntax: tuple_name.count(element)
tuple=(2,5,2,6,2,2,2,7,5,"y",5,"yu",55,"y",":","yu")
print(tuple.count(2))
print(tuple.count(5)) 

# assigning to variable
a,b=tuple.count("y"),tuple.count("yu")
print(a,b)
print(tuple.count(":"))
s=tuple.count(55)
print(s,tuple.count(7))

# it return 0 value when elem. is not present in tuple
print(tuple.count(89))
print(tuple.count("elem. not present"))
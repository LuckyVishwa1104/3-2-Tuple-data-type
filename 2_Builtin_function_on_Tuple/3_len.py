#3) len() - return the total no. of elem. present in tuple.
# Syntax:  len(tuple_name)
tup1=(1,4,6,8,9,22,0b110,0o25,0xAD)
tup2=("eer","hh",223,"id",(8,9,7))
tup3=("v","i","b","g","y","o","r")
tup4=("a","e","i","o","u","rest","consonenet")
# length of tuple
print(len(tup1))
print(len(tup2))
# assigning to variable
a,b=len(tup3),len(tup4)
print(a,b)
# using tuple operation
print(len(tup1+tup2))
print(len(tup3*2))
# passing argument as tuple
print(len((2,4,2,4)))



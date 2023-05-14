#8). any() - return True value when atleast one value is true else return False value.
# it convert the elem. into bool data-type.
# Syntax:  any(tuple_name)
tup1=(7,8,2,6,8.3,0b101,0x2A)
tup2=("sar",7-6j,bool(True),"i",3,0)
tup3=([2,3],("a",7),{(2),bool(0)},{0:0},0)
print(any(tup1))
print(any(tup2))

# for empty tuple it return False value 
empty=()
print(any(empty))

# assigning to variable
a,b=any(tup3),(0,False,bool(0))
print(a,any(b))

# passing tuple as argument
o="out"
print(any((True,88,0,bool(o))))
print(any((tup1+tup2)))

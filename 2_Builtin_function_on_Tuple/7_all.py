# functions like append(), extend(), sort(), insert(), pop(), remove(), del(), clear() cannot be used with tuple as tuples are immutable.

#7). all() - return True value when all elem. are true or tuple is empty else return False value.
# it convert the elem. into bool data-type
#Syntax:  all(tuple_name)
tup1=(7,8,2,6,8.3,0b101,0x2A)
tup2=("sar",7-6j,bool(True),"i",3)
tup3=([2,3],("a",7),{(2),bool(0)},{0:0},0)
print(all(tup1))
print(all(tup2))

# for empty tuple return true value
empty=()
print(all(empty))

# assigning to variable
a,b=all(tup3),(2,8,9)
print(a,all(b))

# passing tuple as argument
print(all((2,8,9,0.0)))
c=all((3,8,"j","i",(9),0.0))
print(c)
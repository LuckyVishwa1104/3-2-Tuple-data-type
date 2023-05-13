#4). max() - return the max. or largest elem. of tuple.
# elem. of tuple should be of same data-type only .
# Syntax:  max(tuple_name)
tup1=(2,4,6,8,10,15,88)
tup2=(0b110,0b101,0b1000,0b10111)
tup3=(0o23,0o34,0o560,0o345)
tup4=(0x34A,0x7D,0x88E,0x67F)
# max. elem. of tuple
print(max(tup1))
print(max(tup2))
# assigning to variable
a,b=max(tup3),max(tup4)
print(a,b)
# passing tuple as argument
print(max((1,1.1,1.11,1.111,1.1111,bool(7))))
# for value other than numeric value it consider ascii value for comparision
tup=("a","e","i","o")
tup5=("jjj","uih","lol","op")
print(max(tup))
print(max(tup5))


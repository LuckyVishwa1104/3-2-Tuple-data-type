#5). min() - return the min. or least elem. of tuple
# elem. should be of same data-type.
#Syntax:  min(tuple_name)
tup1=(-1,-1.1,-1.11,-1.111,-1.1111)
tup2=(0b101,0o45,0xA,8.3)
print(min(tup1))
print(min(tup2))
# assiging to variable
a,b=(tup1+tup2),(2,6,9,9,bool(0))
c=min(b)
print(min(a),c)
# passing tuple as parameter
print(min(0,0.0,0.00,0.000,0.0000))
# for other than numeric value it consider ascii value for comparision
tup3=("a","e","i","o","u")
# for coolection data-type it consider first value only.
tup4=([78,88],[7,8],[37,75])
print(min(tup3))
print(min(tup4))
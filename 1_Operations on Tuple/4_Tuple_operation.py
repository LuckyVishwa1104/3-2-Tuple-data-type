#4]. Tuple operations - there are two operation on tuple.

#1). Concatination '+' - used to join two or more tuple. the resultant tuple will contain al the elements together
tup1=(2,4,6,8,10)
tup2=(1,3,5,7,9)
tup4=("a","b","c","d","e")
tup3=tup1+tup2
print(tup3)
print(tup1+tup4)
tup5=tup1+tup2+tup4
print(tup5)
print(tup4+("x","y","z"))
tup7=(tup2+tup5)
print(tup7+tup1)

#2). Repetition '*' - used to repeate a tuple multiple times
tup1=(2,4,6,8,10)
tup2=(1,3,5,7,9)
tup3=("a","b","c","d","e")
tup4=("@","#","$")
tup5=("rip","op","lol")
print(tup1*2)
tup6=tup2*2
print(tup6)
print((22,33)*3)
print(tup4*4)
# for 0 or negative times it return empty tuple.
print(tup5*0)
#9). tuple() - used to convert other data-type to tuple data-type.
#Syntax:   tuple(data-type)
# data-type = sequence, string, list, set, dict
sequence=66,8.2,"yu",0b101,0x7A,"$#"
a,b=4,5
list=["u",73,"##",(8,9),0b101,a*b]
set={"a","e","i","o","u"}
print(tuple(sequence))
print(tuple(list))

# assigning to varoable
c,d=tuple(set),["¶","#"]
print(c,tuple(d))

# passing as argument
print(tuple("string"))
print(tuple((22,88,"ii")))


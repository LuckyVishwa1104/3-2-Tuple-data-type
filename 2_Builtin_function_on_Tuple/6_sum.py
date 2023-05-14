#6). sum() - return the sum of all elem. of tuple.
# elem. should be of same data-type.
# applicable for only numeric and bool data-type
# Syntax: sum(tuple_name,value)

# value can be a single numeric value only.
num=(1,2,3,4,5,6,7,8,9,10)
num2=(8.7,87.0,7.22,7-4j,6+2j,0j)
num3=(0b101,0o24,0x76A)
print(sum(num))
print(sum(num2))

# the value get added to sum of tuple
print(sum(num3,1000))

# assigning to variable
a,b=sum(num3),sum(num+num3)
print(a,b)

# passiging tuple as parameter
print(sum((0b101,0b110,0x5E,0o45)))
print(sum((1,1.1,1.11,1.111,1.1111)))


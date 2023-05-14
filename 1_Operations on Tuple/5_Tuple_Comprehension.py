#5]. Tuple Comprehension - it not possible directly, but it can be done By using asterix and trailing comma.
#Syntax: *(item for item in range()),

tup=*(n for n in range(1,6)),
print(tup)
# example 1
tup1=*(i for i in range(1,11) if i%2==0),
print(tup1)

# example 2
tup2=*(j for j in range(1,51) if j%2==0 if j%5==0),
print(tup2)

# example 3
tup3=*("even" if n%2==0 else "odd" for n in range(1,11)),
print(tup3)

# example 4.
tup4=*("*" if i%2==0 else "@" for i in range(1,6) for j in range(i)),
print(tup4)

# example 5.
tup5=*(g*k for g in range(2,3) for k in range(1,11)),
print(tup5)
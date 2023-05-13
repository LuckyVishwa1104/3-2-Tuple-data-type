#3]. Traversing a Tuple - printing elem. one by one using loops.
#1). By using tuple as range.
print("1. By using tuple as range.")
''' Syntax:
	  for var in tuple:
	  	print(var) '''
# example 1
tup=(2,6.3,7-6j,0b101,0o34,0xA5)
# using for loop
for i in tup:
	print(i)
# example 2.
vow=("a","e","i","o","u")
# using while loop
i=0
while i<len(vow):
	print(vow[i],end=" ")
	i=i+1
print("")
# example 3
days=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
for day in days:
	print(day)
#2). By using range() function 
print("2. By using range() function ")
''' Syntax:
	  for var in range(tuple_length):
	  	print(tuple[index]) '''	  	
# example 1 - increment in elem. by 2
tup1=(2,4,6,8,10,12)
for i in range(len(tup1)):
	print(tup1[i]+2,end=" ")
print("")
# example 2 - printing only even no.
tup2=(1,2,3,4,5,6,7,8,9,10)
for j in range(len(tup2)):
	if j%2==0:
		print(j,end=" ")
print()
#3). By using enumerate - prints both index as well as corresponding value
print("3. By using enumerate")
''' Syntax :
	  for var in enumerate(tuple_name):
	  	print(var) '''
# example 1
tup3=(11,22,33,44,55,66)
for k in enumerate(tup3):
	print(k)
# example 2
tup4=(0b000,0b001,0b010,0b011,0b100)
for jj in enumerate(tup4):
	print(jj)

	  		  							  	  		  		  		  							  	  		  	
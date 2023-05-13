#2. Tuple data-type - collection of elem. separated by comma in braces.
# Tuple = (val1, val2, val3, - - - ,valn)

#1]. Creating and Declaring a list
''' Syntax :
	    tuple_name=(val1, val2, - - - , valn) '''
''' Tuple - Variable (A to Z, a to z, 0 to 9, _)
 Values - all data-type, variables, input,                        expression '''	    
# even a tuple contain single value comma is used to separate i.e. t=(66,)	    
#1. tuple of similar datatype
tuple1=(23,5,79,87,9,86) 
print(tuple1)  # tuple of intigers
tuple2=("hii","lol","oop","kdk","hily")
print(tuple2)  # tuple of string
#2. tuple of mixed datatype
tuple3=(-3,6,7.2,-6.7,9-7j,0b101,0o45,0xA2E)
print(tuple3)
tuple4=(7,9.2,"strin",bool(88),False,None,True)
print(tuple4)
#3. tuple of complex datatype
a,b,c=5,7,9
tuple5=(2,"uuo",a,8.3,b,-5-7j,c)
print(tuple5)
tuple6=(a*b,b+c,a//c,8-6)
print(tuple6)
#4. tuple of advanced datatype
tuple7=("us",0xA4,[a,b,c],(3,6,9),{2:8,3:27,4:64},{a*b,58})
print(tuple7)
tuple8=(int(input("enter 1 st elem. :")),int(input("enter 2 nd elem. :")),int(input("entet 3 rd elem. : ")))
print(tuple8)

#2]. Accessing element of Tuple - using index value we can access the element of tuple
# Syntax:  tuple_name[ index ]
tuple=(22,7.3,-5-3j,"yo","pop",True,None)
print(tuple[0])
print(tuple[4])
print(tuple[6])

# There are three way to access element
#1). Using positive index : 0 to (n-1)
print("Using positive index")
tup1=(3.14,6-4j,bool(66),None,"tuf",45,"oop")
print(tup1[0])
print(tup1[3])
print(tup1[3+2])
a=tup1[6]
print(a,tup1[4])

#2). Using negative index : -1 to -n
print("Using negative index ")
tup2=(7,"hol",False,(7,8,9),3.8,8-6,"&&","##")
print(tup2[-1])
print(tup2[-5])
b=tup2[-3]
print(b)
print(tup2[3-6],tup2[-8])

#3). Using slice operator ( : ) - using this we can access more than one elem. at a time.
# Syntax: tuple_name[start:ending index]
print("Using slice operator ( : ) ")
tup3=(9,7.3,"hil",[5,7,9],7-8j,0o23,(7,8,9),{"¶","∆"})
print(tup3[0:3])
print(tup3[-8:-5])
print(tup3[3:6])
print(tup3[2:8:2])
print(tup3[-8:-2:2])
# 0 is taken by default
print(tup3[:5])
# if no index provided it print entire tuple
print(tup3[:])

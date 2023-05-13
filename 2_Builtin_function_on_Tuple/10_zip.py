#10. zip() - it is used to convert one or more sequence into list of tuple.
#Syntax:  zip(sequence1,sequence2,..)
#list=[3,8,9,76,-67]
#tuple=(0b101,0o34,0x2AD,38.8,-6+7j)
set={"uaj","j2j","jsj",88,9.2}
lst=6,7,9  # sequence
tuple=(7,92,92)
print(list(zip(lst,tuple)))
print(list(zip(set,lst)))
print(list(zip(lst,set,tuple)))
# assigning to variable.
language=("Python","JAVA","JavaScript")
versions=[3,13,6]
dict={2:8,3:27,4:64,5:125}
a=zip(language,versions)
b=zip(dict,versions)
print(list(a),list(b))
# passigning as argument
print(list(zip(["a","e","i"],(1,2,3))))
print(list(zip(set,(7.7,8.8,9.9),["aa","bb","cc"])))
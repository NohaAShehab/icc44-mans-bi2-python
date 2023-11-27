"""
tuple is immutable data type
"""
"1- to define a tuple"
#
t = ()
myt = tuple()
# 
"2- tuple can have more than one element from different data types"
# 
myt = ('ahmed', 10 , True, 77.7, ["python", 'sql'], "iti", "noha", "iti")
# 
"3- get len of tuple"
print(len(myt))
# 
"4- access element from tuple using index"
print(myt[3])
print(myt[4][1])
# 
"5- tuple is immutable data type ? "
# myt[1]='100' # TypeError: 'tuple' object does not support item assignment

""" count element occurrence """
print(myt.count("iti"))

""" tuple concat"""
t1= ('ahmed', 10, 333.33, 'mina', True)
t2= ('ali', True, 44.33, ['python', 'sql'])
# #
# t3= t1+ t2
# print(t3)
# 

""" loop over a tuple """
for item in t1:
    print(f"item={item}")

"print index of item ?"
print(t1.index("ahmed")) # first occurence of the element
# 
""" get indicies of item"""
t1_enum = enumerate(t1)  #enumarate object
# # generate index for each value
print(t1_enum)  # enumerate object
# # #
# for abbass, test in t1_enum:
#     print(f"{abbass} : {test}")
# 
# cast enum to atuple
items =tuple(t1_enum)
print(items)
# #
# 
""" check if item is in tuple  or not """
print("iti" in myt)
# 


# 
"generate tuple of numbers --> range ? "
r = range(1,10)
print(r, type(r))
""" cast range to tuple """
nums = tuple(r)
print(nums)

# r = range(1,10,2)
# print(r, type(r))
# """ cast range to tuple """
# nums = tuple(r)
# print(nums)

# print(min(even_numbers))  # min , max ->  all elements must be from the same type

# del t2  # remove element from memory
# 
# 

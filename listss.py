

"1- to define a list"

l = []
myl = list()

"2- list can have more than one element from different data types"

myl = ['ahmed', 10 , True, 77.7, ["python", 'sql'], "iti", "noha", "iti"]

"3- get len of list"
print(len(myl))

"4- access element from list using index"
print(myl[3])
print(myl[4][1])

"5- list is mutable data type ? "
myl[1]='100'
# myl[20]="jjj" #list assignment index out of range

""" append element to the list """
myl.append("python")

""" insert element into the list  at certain index """
myl.insert(2, "inserted")

""" pop element from the list """
# popped_item =myl.pop()
# print(myl)
# print(popped_item)

"pop element at index "
popped_item =myl.pop(3)
print(myl)
print(popped_item)

"remove item from list -- first occurence of item "
# myl.remove("iti")
# print(myl)

""" count element occurence """
print(myl.count("iti"))

""" list concat"""
l1= ['ahmed', 10, 333.33, 'mina', True]
l2= ['ali', True, 44.33, ['python', 'sql']]

l3= l1+ l2
print(l3)

""" extend a  list """
print(l1)
l1.extend(l2)
print(l1)

""" loop over a list """
for item in l1:
    print(f"item={item}")

"print index of item ?"
print(l1.index("ali")) # first occurence of the element

""" get indicies of item"""
l1_enum = enumerate(l1)  #enumarate object
# generate index for each value
print(l1_enum)  # enumerate object
# #
# for abbass, test in l1_enum:
#     print(f"{abbass} : {test}")

# cast enum to alist
# items =list(l1_enum)
# print(items)
#

""" check if item is in list  or not """
print("iti" in myl)

""" sort list element ---> all list items must be from the same type """

names = ['test', 'ahmed', 'Ali',"iti", "Mohamed", "mina","Radwa", 33, True ]

# names.sort()  # sort the same object   # sorted
# print(names)

""" sort descending"""
# names.sort(reverse=True)
# print(names)

""" reverse a list ? """
l2= ['ali', True, 44.33, ['python', 'sql']]

l2.reverse()
print(l2)


"generate list of numbers --> range ? "
# r = range(1,10)
# print(r, type(r))
# """ cast range to list """
# nums = list(r)
# print(nums)

r = range(1,10,2)
print(r, type(r))
""" cast range to list """
nums = list(r)
print(nums)

""" loop over the range """
for n in range(1,10):
    print(f"num= {n}")

""" list ---> comprehension  --> even numbers """
even_numbers = []
# for i in range(10):
#     if i%2==0:
#         even_numbers.append(i)
# print(even_numbers)


even_numbers = [ i for i in range(0,10,2)]
print(even_numbers)



print(min(even_numbers))  # min , max ->  all elements must be from the same type


even_numbers.clear()  # remove all elements from the list

del l3  # remove element from memory



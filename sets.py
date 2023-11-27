

""" sets
    -remove duplications
    - un ordered datatype
    - accept different datatypes
    - no index in the set
"""


myset = {"iti","iti",  "Ahmed", True,"iti",  333, 33.344, None , "iti"}

print(myset)

print(len(myset))

""" add element to the set """
myset.add("newitem")
print(myset)

""" pop element from the set """
popped_element = myset.pop()
print(popped_element)

""" update the set --"""
s1= {"python", 'test', 33, 333}
s2 = {'sql', "power bi", ("4months", "itp")}
s1.update(s2)
print(s1)

""" set allow only adding immutable elements  """
""" check this """
# mys = {"Ahmed", "iti", "python", ['sql', "power bi", 'interview skills']}

# print(mys)

mm= {"test", {"bi", "sql", "iti"}}
print(mm)
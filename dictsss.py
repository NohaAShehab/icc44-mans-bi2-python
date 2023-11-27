

"""

    dict ?
    comma separated key/value pairs
"""
"""

    data --> unlabeled data (list, tuple, set)
    data --> labeled data(dict)
"""
info = ["noha", 31, "Cairo"]

myinfo ={"name":"noha", "age":23, 'city':'Cairo'}

d = {}
my_dict = {}

""" comma separated key/value --> doesn't allow key duplication"""

d = {"name":"John", "age":22, "name":"ali"}
print(d)

"access value using key"
print(d['name'])

""" dict is mutable --> datatype """
print(myinfo)
myinfo['age'] = 31
print(myinfo)

myinfo["courses"] = ["python", "sql", 'linux']
print(myinfo)

""" best practice --> key : string """

""" remove key value pairs from dict """

poped_value=myinfo.pop("city")
print(poped_value)

""" check if value is exists"""
print("noha" in myinfo)  # check if elements exists in keys >

"get dict keys"
# keys= myinfo.keys()  # dict_keys
# print(keys)
#
# for k in keys:
#     print(k, myinfo[k])
"get dict values"
values = myinfo.values()
print(values, type(values))

for v in values:
    print(v)

"get dict items "
items = myinfo.items()  # dict_items
print(items)

for k , v in items:
    print(f'{k}:{v}')



"len of dict --> return length of dict no if key:value pairs"
print(len(myinfo))

""" update dict --> """
other_info = {
    "name":"Noha Shehab",
    "work": "iti",
    "track": "bi"
}
print(myinfo)
myinfo.update(other_info)
print(myinfo)


""" loop over the dict ? """
for item in myinfo:
    print(f"item {item}, {myinfo[item]}")

""""""

data = {"name":{
    "first": "noha",
    "last": "shehab"
}}

print(data["name"]["last"])

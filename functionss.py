""" functions with mandatory number of arguments """
# def myfun():
#     pass
#
# "call the function"
# res = myfun()  # None
# print(res)
""
# def myfun():
#     return
#
# "call the function"
# res = myfun()  # None
# print(res)

""" function do something """
# def myfunc():
#     print("--- hello world ----")
#
# res = myfunc()
# print(res)

# def myfunc():
#     print("--- hello world ----")
#     return
#
# res = myfunc()
# print(res)

""" function  that return with value """

# def askforfullname():
#     fname= input("please enter your first name: ")
#     lname = input("please enter your last name: ")
#     fullname = f'{fname} {lname}'
#     return  fullname
#
# res = askforfullname()
# print(res)


# def askforfullname():
#     fname= input("please enter your first name: ")
#     lname = input("please enter your last name: ")
#     fullname = f'{fname} {lname}'
#     return  fullname, fname, lname  # return with more than one  value in tuple
#
# res = askforfullname()
# print(res)


# def askforfullname():
#     fname= input("please enter your first name: ")
#     lname = input("please enter your last name: ")
#     fullname = f'{fname} {lname}'
#     print(fullname)
#     return fullname
#
# res = askforfullname()
# print(res)

""" function require arguments """
# def sumnum(num1,num2):
#     print(f"num1={num1},num2={num2}")
#     res = num1 + num2
#     print(res)
#
# r=sumnum(10 ,20 )
# print(r)
#
# sumnum()

""" function require arguments  and return value """


# def mulnums(num1,num2):
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 * num2
#     return res

# r = mulnums(2,10)
# print(r)

def sayhello():
    print("Hello World")


# sayhello('iti')

""" functions with optional arguments  (default value argument) """

# def mulnums(num1,num2=5):
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 * num2
#     return res
#
# print(mulnums(10))

# def mulnums(num1=10,num2): # SyntaxError: non-default argument follows default argument
#
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 * num2
#     return res
#
# print(mulnums(10))

# def mulnums(num1=10,num2=6): # SyntaxError: non-default argument follows default argument
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 * num2
#     return res
#
# print(mulnums(4))
# print(mulnums(4,5))
# print(mulnums())
# print(mulnums(num2=55))


""" check this """

# def sumnum(num1=10,num2=10):
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 + num2
#     return res

# r = sumnum(20,33)
# print(r)
# r = sumnum("20","33")
# print(r)

# r = sumnum("20",10)
# print(r)


# def sumnum(num1=10,num2=10):
#     print(f"num1= {num1}, num2={num2}")
#     res = int(num1) + int(num2)
#     return res


# print(sumnum('19', 'iti'))

# def sumnum(num1=10,num2=10):
#     print(f"num1= {num1}, num2={num2}")
#     if num1.isdigit() and num2.isdigit():
#         res = int(num1)  + int(num2)
#         return res
#
# sumnum(4,5)

# def sumnum(num1 : int,num2 :int):  # for documentation purpose
#     print(f"num1= {num1}, num2={num2}")
#
#     res = num1  + num2
#     return res
#
# print(sumnum(4,5))
# print(sumnum('ahmed','iti'))
# print(sumnum(3,'iti'))

""" check variable with specific datatype ---? do it on your own """

# print(isinstance(10, int))
# print(isinstance('ahmed', str))
# print(isinstance(10, str))


# def sumnum(num1: int, num2: int):  # for documentation purpose
#     # check if num1 int and num2 --> do process , else --> print message
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1= {num1}, num2={num2}")
#
#         res = num1 + num2
#         return res
#     else:
#         print("===== num1 and num2 must be integers ======")
#
#
# print(sumnum(4, 5))
# print(sumnum('ahmed', 'iti'))
# print(sumnum(3, 'iti'))



""" functions unknown number of arguments ---? """

# print()
# print("ff", 'fff','ff')
# print("iti")
""" functions accepts unknown number of arguments"""

def askforgifts(*gifts):  # * represent zero or more argument
    print(gifts)  # tuple

# askforgifts()
# askforgifts("laptop")
# askforgifts('laptop',"mobile")
# print("ahmed" , end="#")
# print("iti")
#
# print("ahmed", "noha", "ali",sep="|")


""" """


def introduceyourself(**info): # function accept key=value argument, keyword argument.
    print(info)
    for k , v in info.items():
        print(f"{k}:{v}")

introduceyourself(fname='noha', lname='shehab')
introduceyourself()
introduceyourself(fullname='abc')

fname='nohaa'
lname='shEHAB'
temp = '{myfname}+++{mylname}'
print(temp.format(myfname=fname, mylname=lname))


"'abdulrahmanrxz'"

"""
    abdu
    lr
    ahm
    anrxz
"""

"""

    ['apple', 'banana', 'cherry', 'dog']
    name:noha
    guess a word consits of ---
    -o-
    -og
    -og
    dog
    
    

"""
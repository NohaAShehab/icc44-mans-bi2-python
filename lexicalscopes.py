""" lexical scopes """

"global scope"

course = 'python'  # any variable defined in the python script --> scope ==> global scope

"""
    global scope --> variable is accessed any where in the script 
"""
# print(f"course = {course}")
#
#
# print(f"Course= {course}")

""" print global variable from inside the function """


def myfunction():
    print(f"==course from inside the function = {course}")


# myfunction()


""" define variable inside the function  ===> variable is local variable"""

def askforname():
    """ variable with local scope """
    name=input("please enter your name: ")  # can be accessed only inside the function
    print(f"from inside the function name={name}")

# askforname()
# print(name)

"any variable defined in the function can be accessed only inside the function"

################

""" modify global variable from inside the function """
name = "noha"

def modifyname():
    global name  # please don't create new variable ===> use the global one
    name = input("please enter your name: ")
    print(f"name form inside the function {name}")


# modifyname()
#
# print(f"after calling function name={name}")


""" function inside a function """




# def outerfunction():
#     coursename= 'python'  # local variable
#     "can be accessed anywhere in the function"
#
#     def printCourse():
#         print(coursename.upper())
#
#     printCourse()
#     print(f"from outer function, coursename = {coursename}")
#
#
#
# outerfunction()

""" modify local variable from inside inner function"""
def outerfunction():
    coursename= 'python'  # local variable
    "can be accessed anywhere in the function"

    def printCourse():
        print(coursename.upper())

    printCourse()

    def modifycourse():
        nonlocal coursename # please use the local variable of the parent function
        coursename = input("please enter your updated  coursename ") # new local variable
        print(f"from modify  coursename= {coursename}")

    modifycourse()
    print(f"from outer function, coursename = {coursename}")



outerfunction()
print("=======")



















# class Person(object):
#     pass



# class Person:
#     pass
#
# p  = Person()
#
# print(isinstance(p, object))

# o = object()  # customized structure (properties, methods)

######################
"""------------ inheritance ------------ """
# class Employee:
#     pass
#
# class Engineer(Employee):
#     pass
#
#
# eng = Engineer()
# print(isinstance(eng, Employee))



""" check this """

# class Employee:
#     def __init__(self,name):
#         self.name = name
#
# class Engineer(Employee):
#     pass
#
#
# eng = Engineer("noha")

""" and this """
# class Employee:
#     def __init__(self,name):
#         self.name = name
#
#     def printEmp(self):
#         print(f"name={self.name}")
#
# class Engineer(Employee):
#     pass
#
#
# eng = Engineer("noha")
# eng.printEmp()


""" check this again """
# class Employee(object):
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary =salary
#
#     def printEmp(self):
#         print(f"name={self.name}")
#
# class Engineer(Employee):
#     def __init__(self,name, email):
#         # to call parent constructor
#         super().__init__(name, 10000)  # assign properties in the parent class to this instance
#         self.email = email
#
#
#     #overriding
#     def printEmp(self):
#         super().printEmp()
#         print(f"email={self.email}")
#
#
#
#
# eng = Engineer("noha", 'fff@hhh.com')
# eng.printEmp()
# print(eng.__dict__)


# def myfunc(name):
#     print(name)
# def myfunc():
#     print("---- hello world ===")
#
# myfunc("fffff")



""" mutliple inheritance """

class Shape:
    # def __init__(self):
    #     print("---- Shape object is created ")

    def area(self):
        print("--- area = area")


class Item:
    def __init__(self):
        print("--- Item object is created  ---")

    def describe(self):
        print("---this is an item")


class Square(Shape, Item):
    pass


s = Square()
s.describe()
s.area()













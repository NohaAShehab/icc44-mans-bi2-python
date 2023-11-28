
# emp= {
#     "name" :"ahmed",
#     "email" :"ahmed@gmail.com",
#     "salary" :1000
# }
# emp2 = {
#     "fullname" :"ahmedali",
#     "email" :"m@gmail.com",
#     "empsalary" :1000
# }

# def printEmp(emp):
#     print(f"{emp['name']}, {emp['email']}, {emp['salary']}")



# printEmp(emp)
# printEmp(emp2)

""" generate customized data structure  --> statisfy 
your needs 

You need to create a class --blueprint for data structure ->
"""


"""1- define the class """

# class Employee:
#     pass
#
# """ 2- take an object from the class """
# emp  = Employee()
# print(type(emp))
#
# """ add properties  to the object in the runtime"""
# emp.name='ahmed'
# emp.email='ahmed@gmail.com'
#
# emp2= Employee()
# emp2.fullname='ahmed ali'
# emp2.email = 'ahmed@gmail.comm'


""" control object creation """
# class Employee:
#     def __init__(self):  # this is the constructor function
#         # construct the new object
#         # self represent object address when you create it --> in the class
#         print(f"---- new object is being created {self}")
#         self.name='ahmed'
#         self.email='ahmed@gmail.com'
#         self.salary= 1000
#
# """ 2- take an object from the class """
# emp  = Employee()  # emp ---> represent object address from outside the class
# print(emp)
#
# emp2= Employee()
# print(emp2)
#
# emp3= Employee()
# print(emp3)
# emp3.name='noha'

""" customize object creation """
# class Employee:
#     def __init__(self, name, email, salary):  # this is the constructor function
#         # construct the new object
#         # self represent object address when you create it --> in the class
#         print(f"---- new object is being created {self}")
#         """name, email, salary  --> instance variables """
#         self.name= name
#         self.email=email
#         self.salary= salary
#
# """ 2- take an object/instance from the class """
#
# emp  = Employee("ahmed", "ahmed@gmail.com", 10000)  # emp ---> represent object address from outside the class
# print(emp)
#
# emp2= Employee("ali", "ali@gmail.com", 10000)
# print(emp2)
#
# emp3= Employee("mohamed", "mohamed@gmail.com", 10000)
# print(emp3)
# emp3.name='noha'
""" """
# class Employee:
#     def __init__(self, *property):  # this is the constructor function
#         # construct the new object
#         # self represent object address when you create it --> in the class
#         print(f"---- new object is being created {self}")
#         """name, email, salary  --> instance variables """
#         self.property = property



# emp  = Employee("ahmed", "ahmed@gmail.com")  # emp ---> represent object address from outside the class
# print(emp)
#
# emp2= Employee()
# print(emp2)
#
# emp3= Employee("mohamed", "mohamed@gmail.com", 10000)
# print(emp3)
# emp3.name='noha'

class Employee:
    def __init__(self, name, email, salary):  # this is the constructor function
        # print(f"---- new object is being created {self}")
        # """name, email, salary  --> instance variables """
        self.name= name
        self.email=email
        self.salary= salary

    def print_details(self, message='Hi'):  # this is an instance method , function -depends on caller instance-
        print(f"Empname={self.name}, {self.email}, {self.salary}|| {message}")



    def modifName(self):
        self.name=self.name.upper()

    def addcity_to_object(self, city):
        self.city= city


emp = Employee("test", "test@gmail.com", 40000)
emp.name= 'updated'
emp.print_details("Welcome to python course ")
print(emp.name)
emp.modifName()
print(emp.name)

emp3= Employee("ahmed", "ahmed@gmail.com", 4000)
emp3.print_details()

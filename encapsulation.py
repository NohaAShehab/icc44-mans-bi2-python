"""

    encapsulation ?

    access modifiers
    public   --> can be accessed any where inside(self), outside class (object)
    protected  --> can be accessed only in the class and derived classes
    private  --> can be accessed only in the class

    access modifier in python based on variable name ?

    variable/ function name start with char a-z  ---> public
    variable/ function name start with _  ---> protected
    variable/ function name start with __  ---> private



"""

# class Employee:
#
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email = email # protected
#         self.__salary =  salary # private
#
#     def printEmployee(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 1000)
# print(emp.name)
# print(emp._email) # ethically don't do this
# print(emp.__salary)


""" setter and getters 

 use private properties --> limit accessibility , and apply logic on the property
"""
# class Employee:
#
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email = email # protected
#         self.__salary =  salary # private
#
#     def printEmployee(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
#     ## setters and getters for properties
#     # control accessiblity and apply logic before setting value
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise ValueError('Salary must be int or float')
#
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 1000)
# print(emp.name)
# print(emp._email) # ethically don't do this
# # print(emp.__salary)
# print(emp.get_salary())
#
# emp.set_salary(100000)

""" setters and getters """
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email = email # protected
#         self.__salary =  salary # private
#
#     def printEmployee(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
#     def get_salary(self):
#         return self.__salary*.8
#
#     def set_salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float):
#             self.__salary = salary
#
#         else:
#             raise ValueError('Salary must be int or float')
#
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 1000)
# print(emp.get_salary())
# # emp.set_salary("iti")
#
#
# emp3= Employee('noha', 'noha@gmail.com', 'iti')  # problem


"check this solution"
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email = email # protected
#         # self.__salary =  salary # private
#         self.set_salary(salary)
#
#     def printEmployee(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
#     def get_salary(self):
#         return self.__salary*.8
#
#     def set_salary(self, salary):
#         if isinstance(salary, int ) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError('Salary must be int or float')
#
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 1000)
# print(emp.get_salary())
# # emp.set_salary("iti")
#
#
# emp3= Employee('noha', 'noha@gmail.com', 'iti')
# print("------------------")

""" property """


class Employee:
    def __init__(self,name, email, salary):
        self.name = name  # public
        self._email = email # protected
        # self.__salary =  salary # private
        self.salary=  salary

    def printEmployee(self):
        print(f"{self.name}, {self._email}, {self.__salary}")

    # def get_salary(self):
    #     return self.__salary*.8

    @property
    def salary(self):
        return  self.__salary*.8

    "property setter"
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, float) or isinstance(salary, int):
            self.__salary=salary
        else:
            raise  ValueError("Salary must be float or int")




emp = Employee("Ahmed", 'ahmed@gmail.com', 1000)
print(emp.salary)
emp.salary = 47678326
print("----------------")













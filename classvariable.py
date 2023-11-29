# class Employee:
#     """ property related to the class not the instances
#     and this property is shared between all the class instances """
#     count = 0  # class variable
#     def __init__(self, name, email, salary):
#         self.name= name  # instance variables
#         self.email=email
#         self.salary= salary
#         Employee.count +=1
#
#
#     def print_details(self, message='Hi'):  # this is an instance method , function -depends on caller instance-
#         print(f"Empname={self.name}, {self.email}, {self.salary}|| {message}")
#
#
#     def modifName(self):
#         self.name=self.name.upper()
#
#     def addcity_to_object(self, city):
#         self.city= city
#
#
# emp = Employee("test", "test@gmail.com", 40000)
# #
# emp3= Employee("ahmed", "ahmed@gmail.com", 4000)
#
# print(Employee.count)
# Employee.nationality='Palastinian'


""" ============= class method ===================="""
# class Employee:
#     """ property related to the class not the instances
#     and this property is shared between all the class instances """
#     count = 0  # class variable
#     def __init__(self, name='', email='', salary=0):
#         self.name= name  # instance variables
#         self.email=email
#         self.salary= salary
#         Employee.count +=1
#
#
#     def print_details(self, message='Hi'):  # this is an instance method , function -depends on caller instance-
#         print(f"Empname={self.name}, {self.email}, {self.salary}|| {message}")
#
#
#     # function print number of employees in the class
#     "function depends on the class not the instance "
#     @classmethod  # first parameter of the function represent current class
#     def get_no_of_employees(cls):  # cls ---> represent current class
#         print(cls)
#         return cls.count
#
#     # use class method to create default object
#     @classmethod
#     def create_default_object(cls):
#         return  cls("default", "default", 30000)

#
# print(Employee)
# print(Employee.get_no_of_employees())
# # emp1=Employee("fff", '4444', 444)
#
# emp = Employee.create_default_object()






# complex numbers


# class Complexx:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     @classmethod
#     def add_complexx(cls, c1, c2):
#         if isinstance(c1, cls) and isinstance(c2 , cls):
#             newreal = c1.real + c2.real
#             newimg = c1.imag + c2.imag
#             return  cls(newreal, newimg)
#         raise TypeError(f'c1, c2 must be of type {cls}' )
#
#
#
# c = Complexx(3,4)
# c2 = Complexx(4,5)
#
# # add c + c2  ==> new complex number
# c3 = Complexx.add_complexx(c, 10)
# print(c3)


""" ------------------------- check this ----------------------------"""



class Employee:
    count = 0  # class variable
    def __init__(self, name='', email='', salary=0):
        self.name= name  # instance variables
        self.email=email
        self.salary= salary
        Employee.count +=1


    def print_details(self, message='Hi'):  # this is an instance method , function -depends on caller instance-
        print(f"Empname={self.name}, {self.email}, {self.salary}|| {message}")

    @classmethod  # first parameter of the function represent current class
    def get_no_of_employees(cls):  # cls ---> represent current class
        print(cls)
        return cls.count

    @classmethod
    def create_default_object(cls):
        return  cls("default", "default", 30000)

    @staticmethod  # helper method --> doesn't depend on the instance or the class
    def cal_net_salary(salary):
        return salary * .8



emp1= Employee("Ahmed", "ahmed@gmail.com", 40000)
print(emp1.salary)

"calculate net salary "

def cal_net_salary(salary):
    return  salary * .8


print(cal_net_salary(emp1.salary))
print(cal_net_salary(100000))


print(Employee.cal_net_salary(5575686))
print(Employee.cal_net_salary(emp1.salary))




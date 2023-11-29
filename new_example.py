
""" you must have property so you can create property setter"""
# class Person:
#
#     def __init__(self, name, bmonth):
#         self.name = name
#         # self.__bmonth = bmonth
#         # self.set_bmonth(bmonth)
#         self.month = bmonth
#     # bmonth 1, 12
#
#     # def get_bmonth(self):
#     #     return self.__bmonth
#
#     @property
#     def month(self):
#         return self.__bmonth
#
#
#     @month.setter
#     def month(self, month):
#         if isinstance(month, int) and (month > 0 and month <13):
#             self.__bmonth = month
#         else:
#             raise ValueError("Invalid month value ")
#     # def set_bmonth(self, month):
#     #     if isinstance(month, int) and (month > 0 and month <13):
#     #         self.__bmonth = month
#     #     else:
#     #         raise ValueError("Invalid month value ")
#
#
# # p = Person("ahmed",2)
# # print(p.get_bmonth())
#
# # p.set_bmonth(100)
#
# p = Person("ahmed",10)
# # print(p.get_bmonth())


""" class ----> """

class Project:
    def __init__(self, name, duration):
        self.name = name
        self.duration  =duration

    # when you print object call this funcion
    # __str__
    def __str__(self):
        """ must return with string """
        return f'{self.name}, {self.duration}'

    def __call__(self):
        print("---- project object is called -----")

    def __len__(self):
        "mehtod must return with number "
        return  len(self.__dict__)


p = Project("crowd funding", 2)
print(p)

p()

print(len(p))




class QueueOutOfRangeException(Exception):
    pass

namw=''
if namw:
    raise  QueueOutOfRangeException('00000')








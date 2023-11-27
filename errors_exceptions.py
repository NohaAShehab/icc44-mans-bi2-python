"""

    errors ?

    -syntax errors ?    parser --> interpreter
        must be solved by developer

    -logical error ?
        who detect it ? developer ? --> debug code, unit testing
        who solve it ? developer ?

    -runtime error [Exceptions ]?

"""

# def sumnum(num1, num2):
#     res=  num1 * num2
#     print(res)
#
# sumnum(2 ,2)
# sumnum(3 ,4) # result is not correct
# unit testing ---> write test cases
# assert function

""" runtime errors """
# print("-----------------------")
# # print(name) #NameError: name 'name' is not defined
#
#
# age = int(input("please enter your age: "))
# print(age,type(age)) # ValueError: invalid literal for int() with base 10: 'ttt4'
#

""" try except  ---> Exception handling """
#
# try:
#     num = int(input("please enter a number: "))
#     print(num)
# except:
#     print("problem happened ")
#
# print("---- after explosion we are here  ------")
#
#
#
""" check this """
# print(int("iti"))
# try:
#     num = int(input("please enter a number: "))
#     print(10/num)
# except Exception as e:
#     """ any problem ---> handle them with the same action"""
#     print(f"problem happened : {e}")
#
# print("---- after explosion we are here  ------")


# try:
#     num = int(input("please enter a number: "))
#     print(10/num)
# except ValueError as ve:
#     print(f"input value should be number integer ,{ve}")
# except ZeroDivisionError as ze:
#     print(f"Divison by zero is not allowed  {ze}")
# except Exception as e:
#     print(e)
#
# print("---- after explosion we are here  ------")


""" new block ---> executed only when there is no problem """

# try:
#     num = int(input("please enter a number: "))
#     res= 10/num
# except ValueError as ve:
#     print(f"input value should be number integer ,{ve}")
# except ZeroDivisionError as ze:
#     print(f"Divison by zero is not allowed  {ze}")
# except Exception as e:
#     print(e)
# else:
#     "this block is executed only when there is no problem"
#     print(f" res = {res}")
# finally:
#     print("---- this block will be executed always")
#
# print("------------------------------------")


# def divnums(num1, num2):
#     try:
#         res = num1/num2
#     except Exception as e:
#         print(e)
#         return False
#     else:
#         print(f"res = {res}")
#         return res
#     finally:
#         print("this block will be executed before the return ")
#         print("--------- operation completed  -------------")
#
# r = divnums(3,0)
# print(r)


""" raising the exception"""

def divnums():
    num1 = input("please enter num1: ")
    num2= input("please enter num2 : ")
    if num2=='0':
        raise ZeroDivisionError("Num2 must not be zero ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2= int(num2)
        print(f"num1= {num1}, num2={num2}")
        res = num1/num2
        print(f"res = {res}")
        return  res

    print("===== not valid inputs ===========")


r = divnums()
print(r)










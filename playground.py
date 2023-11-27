

" to import module in another one ? "

# import  modules_packages
#
#
# # function cal
# def calculator():
#     num1 = modules_packages.askforNum("please enter first number: ")
#     num2 = modules_packages.askforNum("please enter second number: ")
#     res = num1 + num2
#     print(res)
#
# calculator()

""" alias module """

# import  modules_packages as m
"""
    import pandas as pd 
    import tensorflow as tf 
    import numpy as np
"""



# function cal
# def calculator():
#     num1 = m.askforNum("please enter first number: ")
#     num2 = m.askforNum("please enter second number: ")
#     res = num1 + num2
#     print(res)
#
# calculator()


# print(m.askforname("please enter first name : "))


""" import part of the module """

# from modules_packages import  askforname
#
# print(askforname("please input your name: "))


from modules_packages import  askforNum as num
# from modules_packages import askforNum, askforname

print(num("please input a number: "))





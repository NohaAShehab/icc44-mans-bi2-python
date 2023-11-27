"package --> is a folder / directrory"

""" import packagename.module name """
# import bi.inputs
#
# print(bi.inputs.askforname("please enter your name: "))
" alias package name"
# import bi.inputs as m
#
# print(m.askforname("please enter your name"))

""" import part of the module in package """

# from bi.inputs import  askforname

# print(askforname("please enter your name: "))

""" import modulename, package.modulename """


# import  iti

# import iti.greeting
#
# iti.greeting.say_hello("Ahmed")

""" from packagename import function"""
from iti import say_hello
say_hello("ali")

from iti import cleanstring

print(cleanstring("          noha          "))















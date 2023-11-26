message = "We support Hamas"

"1- calculate length "

print(len(message))

"2- access string parts using index --> start from zero "
print(message[4])
"slicing"
print(message[3:7])  # ignore the last

print(message[3:])  # return new string
print(message[::])
print(message[::-1])  #
print(message)
print(message[::2])

# print(message[25])  #IndexError: string index out of range

""" count char occurrence in the string"""
print(message.count("p"))

""" get index of char in string"""
print(message.index('p'))  # get index of the first occurrence of the char

""" operations on the string """

"""1- ask user to enter value """
# name= input("please enter your name: ")  # always returns with string
# print(name, type(name))
#
#
# "concat the string "
# welcomemessage = 'Welcome ' + name
# print(welcomemessage)

""" string interpolation """
fname = 'Noha '
midname = 'AbdelHady '
lastname = 'Shehab'
# fullname=fname+midname + midname + lastname
# print(fullname)
fullname = fname + midname * 2 + lastname
print(fullname)

""" string is immutable datatype ? """
""" string formatting """
# message = 'we support hamas'
# print(message.upper()) # return new string
# print(message.lower()) # return new string
# print(message.title())
# print(message.capitalize())
# print(message)
#
# message =  message.upper()
# print(message)

"format string "
students = 22
track = 'BI'
# status = "We have {0} students in {1} track mansoura branch"
# print(status)
# print(status.format(students , track))
# print(status.format(track, students))

# format check this
status = "We have {numofstudents} students in {trackname} track mansoura branch"
print(status)
print(status.format(trackname=track, numofstudents=students))
# print(status.format(students , track))
# print(status.format(track, students))
"replace "
msg = 'We support Gaza a a a a '

print(msg.replace('a', '@', 2))

"f-format string "

""" format string depends on existing variables in the scripts """
# status= 'Happy'
# course_description='interesting'
# message  = f'we are very {status} in this {course_description} python course'
# print(message)
#
# """ iterate over the string ?"""
# for char in "noha":
#     print(f"char = {char}")


"""check string status """

# age = input("please enter your age: ")
# print(age, type(age))
#
# print(age.isdigit())  # return True only of string consists of only digits [09]
# print(age.isalpha()) # return True only of string consists of only alphas [a-z]
# print(age.islower())
# print(age.isupper())
# print(age.istitle())
# print(age.isspace())

""" check example with numbers """
num1 = input("please enter your first number: ")
num2 = input("please enter your second number: ")

# res =  num1 + num2
# print(res, type(res))
# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     res =  num1 + num2
#     print(res)
# else:
#     print("--- num1, num2 must be numbers ---")


# print("Mina" +  None)

""" strip string ? """

message = '              we support Hamas              '
print(message, len(message))

# remove spaces into one step ?

print(message.strip())  # remove spaces from the beginning and the end of the string
# then return new string --->

print(message.lstrip())  # remove spaces from the beginning of string
print(message.rstrip())  # remove spaces from the end of the string

# print("noha".ljust(10, "#"))
# print("noha".rjust(10, '$'))

message = '@@   we love python     @@   '
print(message.strip("@ne "))  # strip may accept set of char can be stripped

""" in operator """
if "n" in "noha":
    print("hii")
else:
    print("bye")

print("o" in 'aeiou')

#
# age= input("please enter your age: ")  # always returns with string
# print(age, type(age))


# age= int(input("please enter your age: ")) # always returns with string
# print(age, type(age))

# salary = input("please enter your salary: ")
# print(salary.isdigit())
# if salary.isdigit():
#     salary = int(salary)
#     print(salary)
# else:
#     print("not valid")

r = input("please enter radius:  ")
if r.isdigit():
    r = int(r)
    area = 3.14 * r *r
    print(area)
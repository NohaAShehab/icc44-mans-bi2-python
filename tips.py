

# for i in range(10):
#     if i==4:
#         break
#     print(f"i = {i}")
#
# print("=== after the loop ===")


for i in range(10):
    if i==4:
        continue
    print(f"i = {i}")

print("=== after the loop ===")



""" ask user to enter atm password ? """

for t in range(3):
    password = input("please enter your password: ")
    if password=='abc':
        print("== login successful ==")
        break
else:
    """ this block will be executed when the loop reaches its end"""
    print("account has been locked ")






"""

    if(name=='test'){
    }
"""
name=''
if name=='test':
    pass  # null operation

print("fffffff")

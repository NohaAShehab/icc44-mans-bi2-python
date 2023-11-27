""" any python file with .py ---> python module ?

    so you can use the module in another one or use part of the module
"""


# print("==== Welcome to python module part =====")

def askforNum(message="please enter a number: "):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num
        print("----- please enter valid number -----")


# age= askforNum("please enter age:  ")
# print(f"age ={age}")


def askforname(message="please enter your name: "):
    while True:
        name = input(message)
        if name.isalpha():
            return name
        print("--- please enter valid name ")


""" each time you create new module --> create main --> """

""" when you run application """
if __name__ == "__main__":
    print("--- welcome to modules and packages  ---")
    age = askforNum("please enter your age: ")
    print(age)

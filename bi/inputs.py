
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
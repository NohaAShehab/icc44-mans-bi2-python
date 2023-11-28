

def askforname(message):
    while True:
        name = input(message)
        if name.isalpha():
            return name.lower()

        print("=== not vaild name ====")

def askfornum(message):
    while True:
        try:
            num = int(input(message))
        except Exception as e:
            print("---- please enter an integer: ")
        else:
            return num


import  time
def generate_id():
    "generate random id "
    id= time.time()
    # print(round(id))
    return round(id)

# if __name__=='__main__':
#     generate_id()


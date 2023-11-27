
# 1- open the file
try:
    fileobject = open("names.txt", "r")
    print(fileobject)  # TextIOWrapper

except Exception as e:
    print(e)

else:
    "read file content into one string --"
    data = fileobject.read()
    print(data, type(data))
    """ read file line by line"""
    # for l in fileobject:
    #     print(f"line= {l}")
    """ read line by line without loop """
    fileobject.seek(0)
    lines = fileobject.readlines()
    print(lines, type(lines))
    fileobject.close()
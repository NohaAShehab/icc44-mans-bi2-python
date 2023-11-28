
try:
    fileobject = open("files/names.txt", 'r')  #TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    data = fileobject.read() # string
    print(data)
    "read data line by line "
    # lines = []
    # for l in fileobject:
    #     lines.append(l)
    # print(lines)
    fileobject.seek(0)
    """ --another way --"""
    lines = fileobject.readlines()
    print(lines)
    """ close stream """
    fileobject.close()
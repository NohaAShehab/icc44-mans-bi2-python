"""
    why try to open file with write mode --
    if file doen't exist  python will try to create it.

    when you open file with write mode, python will open file
    for writing starting from the beginning of file
     ==old content will be removed ==

"""
try:
    fileobject = open("files/mycv.txt", 'w')  #TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write("Python is easy to learn and use\n")
    fileobject.write("we support hamas\n")
    fileobject.write("--- test --\n")
    fileobject.write("abc\n")

    fileobject.writelines(["ahmed\n", "ali\n", "mohamed\n"])
    fileobject.writelines({"name":"ahmed", "track":"bi"})
    """ close stream """
    fileobject.close()
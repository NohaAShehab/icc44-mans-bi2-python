"""
    why try to open file with append mode --
    if file doesn't exist  python will try to create it.

    when you open file with append mode, python will open file
    for appending starting from the end of file
     ==old content will be kept ==

"""
try:
    fileobject = open("files/demo.txt", 'a')  #TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write("\n###############################\n")
    # """ close stream """
    fileobject.close()
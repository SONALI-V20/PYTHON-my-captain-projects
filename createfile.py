fn= input("Enter Filename: ")
f = fn.split(".")
if(f[-1]=='py'):
    print ("Extension of the file is : python ")
else:
    print(f)

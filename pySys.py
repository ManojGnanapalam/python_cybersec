import sys
#name = input("enter your name: ")
#print (name)
print("this is the name of the script which running ",sys.argv[0]);
print("the number of arguments is: ",len(sys.argv))

print(sys.version)
print(sys.platform)

print(sys.path)


print("##########################")

import os
pwd = os.getcwd()

list_directory = os.listdir(pwd)

for i in list_directory:
    print(i)

import platform
from platform import python_implementation, python_version_tuple

os = platform.system()

print("your operating system is: ",os)
if(os == "Windows"):
    ping_command = "ping -n 1 127.0.0.1"
elif(os == "Linux"):
    ping_command = "ping -n 1 127.0.0.1"
else:
    print(os);

print(ping_command)


print(python_implementation())
for attribute in python_version_tuple():
    print(attribute)


import socket
import sys
import errno
from datetime import datetime

target = input("Enter the target to scan :")
targetIP = socket.gethostbyname(target)

print("Enter the range of ports to scan")
startPort = input("Enter a start port: ")
endPort = input("Enter a end port:")

print("Scanning target: ", target)
time_init = datetime.now()

try:
    for port in range(int(startPort),int(endPort)):
        print("Checking Port {} ...".format(port))
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target,port))
        if result == 0:
            print("Port {} : Open".format(port))
        else:
            print("Port {}: close".format(port))
            print("Reason: ",errno.errorcode[result])

        sock.close()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

time_finish = datetime.now()
total = time_finish - time_init

print('Port Scanning Completed in: ', total)

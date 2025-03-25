import socket

try:
    host = 'www.google.com'
    ip = socket.gethostbyname(host)
    print("Host by Name", socket.gethostbyname(host))
    print("host by name_ex",socket.gethostbyname_ex(host))
    print("Host by address", socket.gethostbyaddr(ip))
    print("fqdn",socket.getfqdn(host))

    print("addrinfo",socket.getaddrinfo(host,None,0,socket.SOCK_STREAM))

except socket.error as error:
    print(str(error))
    print("connection error")

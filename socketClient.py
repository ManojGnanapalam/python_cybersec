import socket

print('creating socket ...')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
print('connection with remote host')

target_host = "localhost"

target_port = 8080

s.connect((target_host,target_port))
print('connection ok')

request = "GET /HTTP/1.1\r\nHost:%s" % target_host
s.send(request.encode())

data = s.recv(4096)

print("Data",str(bytes(data)))
print("Legth",len(data))

print('closing the socket')
s.close()

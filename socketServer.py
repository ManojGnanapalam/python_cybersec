import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('localhost',8080))

socket.listen(5)

while True:
    print('waiting for connections')
    (recvSocket,address) = socket.accept()
    print('Http request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n <html><body><h1>hola<h1></body></html> \r\n','utf-8'))
    recvSocket.close()


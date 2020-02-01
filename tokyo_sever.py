import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '54.168.91.18'
port = 8000
s.bind((host,port))
s.listen(5)
while True:
    c,addr = s.accept()
    c.close()
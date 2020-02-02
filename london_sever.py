import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000
s.bind((host,port))
s.listen(5)
while True:
    c,addr = s.accept()
    c.sendall(b'a'*1451)
    c.close()
import socket
import time
import csv

s = socket.socket()
london = '3.10.170.181'
singapore = '13.229.198.241'
spalu = '18.228.151.172'
tokyo = '54.168.91.18'
host = socket.gethostname()
port = 8000
data = b'a'*1451

s.connect((tokyo, port))
times = []
for i in range(50):
    time_s = time.time()
    s.send(data)
    s.recv(1024)
    time_e = time.time()
    print(time_e-time_s)
    times.append(time_e-time_s)
s.close()
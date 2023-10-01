import socket

import threading
import time

def func(connection, ip, port):

    recvMessage = connection.recv(16).decode('utf8').rstrip()
    if recvMessage == "Sync":
        serverTime2 = int(time.time()*1000)
        print('Client IP:' + str(ip) + ' Port: ' + str(port))
        serverTime3 = int(time.time()*1000)
        message = str(serverTime2) + ',' + str(serverTime3)
        connection.sendall(message.encode('utf8'))
    connection.close()

host = ""
port = 18442
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen()
print("Server running")

try:
    while True:
        connection, addr = s.accept()
        ip, port = str(addr[0]), str(addr[1])
        try:
            threading.Thread(target=func, args=(connection, ip, port)).start()
        except:
            print('fail')
finally:
    s.close()

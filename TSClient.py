import time
import socket
import sys

host = "127.0.0.1"
port = 14412
if len(sys.argv) >= 2:
    host = sys.argv[1]

while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        soc.connect((host, port))
    except:
        print('no connection')

    time1 = int(time.time()*1000)
    soc.sendall("Sync".encode('utf8'))

    serverResponse = soc.recv(100).decode('utf8').rstrip()
    time4 = int(time.time()*1000)

    serverTime2, serverTime3 = serverResponse.split(',')
    serverTime2 = int(serverTime2)
    serverTime3 = int(serverTime3)

    diff = (serverTime2 - time1) + (serverTime3 - time4)
    diff /= 2

    curTime = time4 + diff

    rtt = (time4 - time1) + (serverTime3 - serverTime2)
    print('REMOTE_TIME ' + str(int(curTime)))
    print('LOCAL_TIME ' + str(int(time4)))
    print('RTT_ESTIMATE ' + str(int(rtt)))
    time.sleep(5)
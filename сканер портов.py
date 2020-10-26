import socket
import threading

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        print('Port :',port,' its open.')
        connect.close()
    except:
        pass

ip = '192.168.0.124'
for i in range(1000):
    scan_port(ip,i)


for i in range(1000):
    potoc = threading.Thread(target=scan_port, args=(ip,i))
    potoc.start()
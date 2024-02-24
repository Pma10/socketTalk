import socket, threading

def send(s):
    while True:
        msg = input("")
        s.send(msg.encode())

def recv(s):
    while True:
        recv_msg = s.recv(1024)
        print(recv_msg.decode())

s = socket.socket()
s.connect(("localhost", 7000))

recv_thread = threading.Thread(target=recv, args=(s,))
recv_thread.start()

send_thread = threading.Thread(target=send, args=(s,))
send_thread.start()

send_thread.join()
recv_thread.join()

s.close()

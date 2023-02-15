import socket

import socket

import threading

HOST = '192.168.141.67'
PORT = 11000
BUFF_SIZE = 1024
clients_th = []


def send_all(msg):
    global clients_th
    for c in clients_th:
        c.send(msg.encode())


def dumb(conn, addr, cv):
    while True:
        msg = conn.recv(BUFF_SIZE).decode()
        print(f'{addr} sent : {msg}')
        send_all(f'{addr} sent : {msg}')

        if '<EOF>' in msg:
            break
    conn.close()


def main():
    ssock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind((HOST, PORT))
    ssock.listen(5)

    name_id = 0

    #while True:
        #global clients_th
    print("Now listening...\n")
    conn, addr = ssock.accept()
    print(f'New Connection from {addr}')

    #th = threading.Thread(target=dumb, args=(conn, "client_" + str(name_id), ""))
    #th.start()
    #clients_th.append(conn)
    #name_id += 1
    while True:
        com = input("enter commend >>> ")
        conn.send(com.encode())
        data = conn.recv(BUFF_SIZE).decode()
        print(data)
    ssock.close()


if __name__ == '__main__':
    main()

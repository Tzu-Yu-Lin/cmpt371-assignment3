import threading              #for use tcp and udp
import socket                 #for many users

host = "0.0.0.0"
port = 8888
clients = []     
name = []   

def sendMes(mm):
    for i in clients:
        i.send(mm)

def recMes(Aclient):
    while True:
        message = Aclient.recv(20000)
        if not message:
            break
        sendMes(message)

def remove_client(client):
    if client not in clients:        #if someone leave just delet it
        return
    i = clients.index(client)
    clients.pop(i)
    name.pop(i)
    client.close()

def PROCrunning(server):
    addr = server.accept()
    client = addr[0]
    address = addr[1]
    print("Connected Successful")
    username = client.recv(20000).decode()
    name.append(username)
    clients.append(client)
    thread = threading.Thread(target=recMes, args=(client,))
    thread.start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    while True:
        PROCrunning(server)

if __name__ == "__main__":
    main()
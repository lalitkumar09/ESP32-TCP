import socket
HEADER_LENGTH=10
IP="192.168.2.110"
PORT=2431
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((IP,PORT))
s.listen(5)
print("Server Is listening...")
clients_sockets,clients_add=s.accept()
print("Cleint connected")

def receive_message(client_sockets):
    try:
        message=client_sockets.recv(7)
        client_sockets.send(b'True')
        if len(message)==0:
            return False
        return message
    except:
        return False
while True:

    message=receive_message(clients_sockets)
    if message is not False:
        print(message)
    else:
        clients_sockets, clients_add = s.accept()



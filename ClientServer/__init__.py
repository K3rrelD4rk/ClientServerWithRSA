import socket
import logging
import threading
from rsa import rsadecode, rsaencode
from dotenv import load_dotenv

def start():
    server = threading.Thread(target=startserver(), args=())
    logging.info('Server is starting...')
    server.start()
    logging.info('\nServer is running!')
    client = threading.Thread(target=startclient(), args=())
    logging.info('\nClient is starting...')
    client.start()
    logging.info('Client is running!')
    
    
def startserver():
    #get_hostname
    host = socket.gethostname()
    port = 5000 #port above 1024
    
    server_socket = socket.socket() #get instance
    #the bind func takes a tuple as args
    server_socket.bind((host, port)) #bind hostname and port together
    
    #conf how many client the server can handle at the same time
    server_socket.listen(1)
    conn, address = server_socket.accept() #accept new conn
    print('Connection from: ' + str(address))
    while True:
        #receive data stream
        data = conn.recv(1024).rsadecode()
        if not data:
            #if data is not received
            break
        print('from connected user: ' + str(data))
        data = input(' -> ')
        conn.send(data.encode()) #send data to client


def startclient():
    host = socket.gethostname() #code on same pc
    port = 5000
    
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    message = input(' -> ') #take input
    
    while message.lower().strip() != 'bye':
        client_socket.send(message.rsaencode()) #send message
        data = client_socket.recv(1024).rsadecode() #receive response
        
        print('Received from server: ' + data) #show in terminal
        
        message = input(' -> ') #again take input
        
    client_socket.close() #close connection
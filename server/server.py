import socket
import threading
import json
from db import connectToDB
from models.data_model import PMData
# Request handler
def handler(sock):
    msg = 'YEE from server. YEEEEEEEEEE'

    sock.send(msg.encode('utf-8'))

    while True:
        msg = sock.recv(1024)
        if not msg:
            print("ERROR : No data")
        else:
            # json format must be double quoted instead of being single quoted
            data = json.loads(msg.decode('utf-8').replace("\'", "\""))
            # unpacking the tuple
            PMData(*tuple(data.values())).save()

    msg = 'Closing connection...'
    sock.send(msg.encode('utf-8'))
    sock.close()

def main():
    # Turn on server
    mainSock = socket.socket()
    mainSock.bind(('0.0.0.0', 8080))# port
    mainSock.listen(5)
    # Connect to mongodb
    connectToDB()
    # testing for insertion

    print('Waiting for connection...')
    while True:
        (soAccept, addr) = mainSock.accept()
        # Create a new thread to handle requests
        thread = threading.Thread(target=handler, args=(soAccept, addr))
        thread.start()

if __name__ == '__main__':
    main()

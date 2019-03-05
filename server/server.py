import socket
import threading
import json
import datetime
import pytz
import pymodm
from db import connect_to_db, BaseDB
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
            try:
                # json format must be double quoted instead of being single quoted
                data = json.loads(msg.decode('utf-8').replace("\'", "\""))
                # unpacking the tuple
                PMData(*tuple(data.values()), datetime.datetime.now()).save()
            except pymodm.errors.ValidationError as err:
                print(err)

    msg = 'Closing connection...'
    sock.send(msg.encode('utf-8'))
    sock.close()

def main():
    # Turn on server
    main_sock = socket.socket()
    main_sock.bind(('0.0.0.0', 8080))# port
    main_sock.listen(5)
    # Connect to mongodb
    connect_to_db()
    # testing for insertion

    print('Waiting for connection...')
    while True:
        (socket_accept, addr) = main_sock.accept()
        # Create a new thread to handle requests
        thread = threading.Thread(target=handler, args=(socket_accept, addr))
        thread.start()

if __name__ == '__main__':
    main()
    

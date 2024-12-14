import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    
    try:
        while True:
            data = connection.recv(128)
            data_str = data.decode('utf-8')
            
            if data:
                fake = Faker()
                response = f"Dear {fake.name()} {data_str} From {fake.name()}"
                connection.sendall(response.encode())
            else:
                break
    finally:
        connection.close()
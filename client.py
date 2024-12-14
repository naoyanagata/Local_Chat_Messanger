import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        message = input('送信するメッセージを入力して下さい。：')
        if message == 'exit':
            sock.close()
            break
        sock.sendall(message.encode())
        data = str(sock.recv(256))
        if data:
            print('返答：' + data)
        else:
            break
finally:
    sock.close()
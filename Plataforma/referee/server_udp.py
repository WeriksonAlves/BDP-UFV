import socket
from proto_db.vssref_command_pb2 import VSSRef_Command
from google.protobuf.json_format import MessageToDict
from read import read
ref = VSSRef_Command()

HOST = "192.168.0.135"  # Standard loopback iip addrnterface address (localhost)
PORT = 20000  # Port to listen on (non-privileged ports are > 1023)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    try:
        message, address = server_socket.recvfrom(1024)
        ref.ParseFromString(message)
        info = read(MessageToDict(ref), 'YELLOW')
        print(MessageToDict(ref))
        print(info)
    except:pass
    

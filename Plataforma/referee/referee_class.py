import socket
import struct
from proto_db.vssref_command_pb2 import VSSRef_Command
from google.protobuf.json_format import MessageToDict

class referee_class(object):

    def __init__(self,  HOST, PORT):
        #temos de definir o endereço e a porta
        self.ref = VSSRef_Command()
        mult_gp = HOST
        addr_server = ('', PORT)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.server_socket.bind(addr_server)

        group = socket.inet_aton(mult_gp)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.penalty, self.kickoff, self.goalkick, self.freeball, self.halt = False, False, False, False, False
        self.cortime = None
        self.play, self.play_ant = False, False
        self.favorable, self.quadrante = False, '1'

    def message(self):#, cor = 'YELLOW'):
        
        #temos que definir a cor do nosso time aqui para verificar se a marcação foi a favor ou contra
        while True:
            try:
                message, address = self.server_socket.recvfrom(1024)
                self.ref.ParseFromString(message)
                self.read(MessageToDict(self.ref), self.cortime)#cor)
                print(self.play,self.penalty, self.freeball, self.goalkick, self.kickoff, self.favorable, self.quadrante,self.halt)
            except: pass

    def read(self, msg,color):
        #retorna as variáveis para False quando o jogo reinicia
        try:
            if bool(msg['foul'] == 'GAME_ON') == True:
                self.penalty, self.freeball, self.goalkick, self.kickoff, self.favorable, self.halt = False, False, False, False, False, False
            self.play = bool(msg['foul'] == 'GAME_ON')
            #verifica se a marcação foi a favor ou contra
            if 'teamcolor' in msg and bool(msg['teamcolor'] == color): self.favorable = True
            #verifica o quadrante da marcação
            if 'foulQuadrant' in msg: self.quadrante = msg['foulQuadrant'][-1]
            #verifica qual das marcações ocorreu
            if bool(msg['foul'] == 'FREE_BALL'): self.freeball, self.play = True, True
            if bool(msg['foul'] == 'PENALTY_KICK'): self.penalty, self.play = True, True
            if bool(msg['foul'] == 'KICKOFF'): self.kickoff, self.play = True, True
            if bool(msg['foul'] == 'GOAL_KICK'): self.goalkick, self.play = True, True
            if bool(msg['foul'] == 'HALT'): self.halt, self.play = True, False
        except:pass

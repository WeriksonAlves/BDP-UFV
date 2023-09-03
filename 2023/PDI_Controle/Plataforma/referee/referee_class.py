import socket
from proto_db.vssref_command_pb2 import VSSRef_Command
from google.protobuf.json_format import MessageToDict

class referee_class(object):

    def __init__(self,  HOST = "192.168.0.123", PORT = 20000):
        #temos de definir o endereço e a porta
        self.ref = VSSRef_Command()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((HOST, PORT))

        self.penalty, self.kickoff, self.goalkick, self.freeball, self.halt = False, False, False, False, False

        self.play, self.play_ant = False, False
        self.favorable, self.quadrante = False, '1'

    def message(self, cor ='YELLOW'):
        #temos que definir a cor do nosso time aqui para verificar se a marcação foi a favor ou contra
        while True:
            try:
                message, address = self.server_socket.recvfrom(1024)
                self.ref.ParseFromString(message)
                self.read(MessageToDict(self.ref), cor)
                print(self.play,self.penalty, self.freeball, self.goalkick, self.kickoff, self.favorable, self.quadrante,self.halt)
            except:pass

    def read(self, msg,color):
        #retorna as variáveis para False quando o jogo reinicia
        try:
            if self.play_ant == False and bool(msg['foul'] == 'GAME_ON') == True:
                self.penalty, self.freeball, self.goalkick, self.kickoff, self.favorable, self.halt = False, False, False, False, False, False
            self.play = bool(msg['foul'] == 'GAME_ON')
            self.play_ant = self.play
            #verifica se a marcação foi a favor ou contra
            if 'teamcolor' in msg and bool(msg['teamcolor'] == color): self.favorable = True
            #verifica o quadrante da marcação
            if 'foulQuadrant' in msg: self.quadrante = msg['foulQuadrant'][-1]
            #verifica qual das marcações ocorreu
            if bool(msg['foul'] == 'FREE_BALL'): self.freeball = True
            if bool(msg['foul'] == 'PENALTY_KICK'): self.penalty = True
            if bool(msg['foul'] == 'KICKOFF'): self.kickoff = True
            if bool(msg['foul'] == 'GOAL_KICK'): self.goalkick = True
            if bool(msg['foul'] == 'HALT'): self.halt = True
        except:pass

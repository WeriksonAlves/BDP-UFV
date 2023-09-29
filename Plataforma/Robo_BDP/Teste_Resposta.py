
import time
from Classe_JOG import*
from Funções.Controls import *
import serial.tools.list_ports
import os
import cv2
import numpy as np

PastaAtual = os.path.dirname(__file__)
ImagemCampo_px = cv2.imread(os.path.join(PastaAtual, 'Campo_px.png'))

def tic():
    return time.time()

def toc(t):
    return time.time() - t

def Comando_DesenhaTeste(P_X, P_Cor, P_Xd, Cor_Xd):
    Campo_Virtual = ImagemCampo_px.copy()
    P_X[[0,1]] = P_X[[0,1]] * 1000
    P_Xd[[0,1]] = P_Xd[[0,1]] * 1000
    # print(f'X= {P_X.T}')
    Comando_DesenhaSeta(Campo_Virtual, P_X, P_Cor[:3],P_Cor[3:])
    Comando_DesenhaCirculo(Campo_Virtual, P_Xd, Cor_Xd,raio=20)
    Campo_Virtual = cv2.resize(Campo_Virtual, [640, 480])
    return Campo_Virtual

def Comando_DesenhaSeta(Campo_Virtual, Posicao, Cor1, Cor2, Comprimento = 80, espessura = 10,raio=40):
    X, Y, Orientacao_Radianos = Posicao[0,0], Posicao[1,0], Posicao[2,0]
    X = int(X + 900)
    Y = int(Y + 750)
    end_point = (int(X + Comprimento * np.cos(Orientacao_Radianos)), int(Y + Comprimento * np.sin(Orientacao_Radianos)))
    start_point = (int(X), int(Y))
    cv2.arrowedLine(Campo_Virtual, start_point, end_point, Cor1, espessura, cv2.LINE_AA, tipLength=0.2)
    cv2.circle(Campo_Virtual, (X, Y), raio, Cor2,espessura)  # O valor -1 preenche o círculo

def Comando_DesenhaCirculo(Campo_Virtual, Posicao, Cor,espessura = 10, raio = 40):
    X, Y = int(Posicao[0,0] + 900), int(Posicao[1,0] + 750)        
    cv2.circle(Campo_Virtual, (X, Y), raio, Cor, espessura)  # O valor -1 preenche o círculo

def Detectar_Porta_Serial_ESP():
    # Lista todas as portas seriais disponíveis
    portas_disponiveis = list(serial.tools.list_ports.comports())
    # Procura por uma porta que contenha "ESP" no nome
    for porta in portas_disponiveis:            
        if "USB TO UART" in porta.description.upper():
            return porta.device  # Retorna o nome da porta COM
    return None  # Retorna None se o dispositivo ESP não for encontrado
# Detecta automaticamente a porta COM do dispositivo ESP
porta_serial = Detectar_Porta_Serial_ESP()

# Inicia a comunicação com o dispositivo serial na porta detectada e define o timeout para 2 segundos
pEsp = serial.Serial(porta_serial, 115200, timeout=2)

pEsp.close()
pEsp.open()

"""Classes initialization - Definindo o Robô"""
# Criando uma variável para representar o Robô

P = Player(0)

# Tempo de esperar para início do experimento/simulação
print('\nInício..............\n\n')
time.sleep(1)
flag = 0
n = 0

for hertz in range(1,30):
    freq = 1/hertz
    print("Freq: ", freq)
    n = 0
    while n < 6:
        # Envia comandos para o dispositivo serial com base no tempo simulado (tsim)
        if flag == 0:
            flag = 1 #Antihorario
            pEsp.write(b'200,-200,0,-0,0,-0\n')
        elif flag == 1:
            flag = 0 # Horario
            pEsp.write(b'-200,200,0,-0,0,-0\n')
        else:
            print('Erro')
        time.sleep(freq)
        print('Mudou o sentido')
        n += 1





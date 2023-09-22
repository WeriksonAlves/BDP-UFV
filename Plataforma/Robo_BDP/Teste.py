import numpy as np
import time
from Classe_JOG import*
from Funções.Controls import *
import serial.tools.list_ports

def tic():
    return time.time()

def toc(t):
    return time.time() - t

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

# Envia comandos para o dispositivo serial com base no tempo simulado (tsim)
start = time.time()
while True:
    t = time.time() - start

    pEsp.write(b'100,-100,100,-100,100,-100\n')
    if t > 2:
        pEsp.write(b'0,0,0,0,0,0\n')
        break
    

"""Classes initialization - Definindo o Robô"""
# Criando uma variável para representar o Robô

to = tic()
P = JOGADOR(0)
print(toc(to))

# Initialize the robot's initial position
robot_x, robot_y = 0, 0

# Tempo de esperar para início do experimento/simulação
print('\nInício..............\n\n')
time.sleep(1)


fig_1 = plt.figure(1, figsize=[5, 5])

P.mCADcolor('g')
plt.xlabel("x")
plt.ylabel("y")
plt.axis([-50, 50, -50, 50])
plt.grid()
plt.title("Robot BDP - Simulator")

ax = plt.gca()
P.Draw(fig=fig_1,axis=ax)
# plt.show()

''' Initial Position'''
# Xo = input('Digite a posição inicial do robô ([x y z psi]): ');
Xo = np.array([[0, 0, 0, 0]]).T
P.rSetPose(Xo)         # define pose do robô

''' Variables initialization '''
#  Xa = P.pPos.X(1:6);    % postura anterior
data = []
Rastro_Xd = []
Rastro_X = []

#  Temporização
T = 60      # Periodo de cada volta da elipse
tsim = 2*T  # Tempo total da simulação
tap = 0.100 # taxa de atualização do pioneer

t = tic()   # Tempo corrente
t_amos = tic() # tempo de amostragem


''' Simulation'''

# Parâmetros de controle
gains_umax = 1 #0.35
gains_wmax = 1 #0.44
gains = np.array([[gains_umax],[gains_wmax]])

# Parâmetros da trajetória
w = (2*np.pi/T)
Rx = 2.5; #[m]
Ry = 1.5; #[m]

# Parâmetros de desempenho
IAE = 0
ITAE = 0
IASC = 0

# Simulação em tempo de máquina
while toc(t) < tsim:
    if toc(t_amos) > tap:
        t_amos = tic()
        # Data aquisition
        P.rGetSensorData()
        
        # Trajetoria Eliptica:
        P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*t)], [Ry*np.sin(w*t)]])
        P.pPos.Xd[[6,7]] = np.array([[-Rx*w*np.sin(w*t)],[Ry*w*np.cos(w*t)]])

        # -----------------------------------------------------
        #P = Controladores(P,gains)
        P = Ctrl_tgh(P)
        #P = Ctrl_inv(P,gains,1,0.41,0.17,0.01)
        # P = Ctrl_exp(P,gains,2,0.06)
        #P = Ctrl_gau(P,gains,1,0.41,0.04,2)
        #P = Ctrl_sqrt(P,gains,0.98,2)
        
        # -----------------------------------------------------
        P.rSend(pEsp)
        # Enviar sinais de controle para o robô

        if t>T:
            ITAE = t*np.linalg.norm(P.pPos.Xtil[0:1])*tap
            IAE = 0
            IASC = 0
        else:
            IASC = np.linalg.norm(P.pSC.Ud[0:1])*tap
            IAE = np.linalg.norm(P.pPos.Xtil[0:1])*tap
            ITAE = 0
        
        # Verifica a saturação
        if (P.pSC.Ud[0]>0.75) or (P.pSC.Ud[1]>1.74):
            print(f'Saturado: {P.pSC.Ud[0]} e {P.pSC.Ud[1]}')
            break
        
        # salva variáveis para plotar no gráfico
        Rastro_Xd.append(P.pPos.Xd[0:1].T)  # formação desejada
        Rastro_X.append(P.pPos.X[0:1].T)    # formação real
        
        data.append([P.pPos.Xd.T, P.pPos.X.T, P.pSC.Ud.T, P.pSC.U.T, P.pPos.rho, P.pPos.alpha, P.pPos.theta, IAE, ITAE, IASC, t])

        # --------------------------------------------------------------- %
        
        ''' Desenha o robô'''
        # P.Draw(fig=fig_1,axis=ax)
        # plt.xlabel("x")
        # plt.ylabel("y")
        # plt.axis(ax)
        # plt.grid()
        # plt.pause(0.001)
        # plt.show()

        



# if t == 2*T:
#     teste = [mean(data(:,32)), mean(data(:,33)), mean(data(:,34));
#              sum(data(:,32),1),sum(data(:,33),1),sum(data(:,34),1)]


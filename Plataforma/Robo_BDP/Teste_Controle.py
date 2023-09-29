
import time
from Classe_JOG import*
from Funções.Controls import *
import os
import cv2
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

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

def Comando_DesenhaSeta(Campo_Virtual, Posicao, Cor1, Cor2, Comprimento = 40, espessura = 10,raio=40):
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

"""Classes initialization - Definindo o Robô"""
# Criando uma variável para representar o Robô

P = Player(0)

''' Initial Position'''
# Xo = input('Digite a posição inicial do robô ([x y z psi]): ');
Xo = np.array([[-.700, -.600, 0, 0]],dtype=np.float64).T
P.rSetPose(Xo)         # define pose do robô

''' Variables initialization '''
#  Xa = P.pPos.X(1:6);    % postura anterior
data = []
Rastro_Xd = []
Rastro_X = []

IAE = 0      # Indices
ITAE = 0     # Indices
IASC = 0     # Indices

''' Simulation'''
# Parâmetros da trajetória
T = 5       # Periodo de cada volta da elipse
w = (2*np.pi/T)
Rx = 0.6; #[m]
Ry = 0.4; #[m]

P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*0)], [Ry*np.sin(w*0)]])
P.pPos.Xd[[5]] = np.arctan2(P.pPos.Xd[[1]],P.pPos.Xd[[0]])

# Tempo de esperar para início do experimento/simulação
print('\nInício..............\n\n')
time.sleep(1)

#  Temporização

tsim = 2*T  # Tempo total da simulação
tap = 0.050 # taxa de atualização do pioneer
t = tic()   # Tempo atual
tc = tic()  # Tempo de controle
tp = tic()  # Tempo para plotar

# Simulation time
# for t in np.arange(0, tsim, tap):
while toc(t) < tsim:                
    if toc(tc) > tap:
        tc = tic()

        '-----------------------------------------------------'
        # Data aquisition
        P.rGetSensorData()

        '-----------------------------------------------------'
        # # Posicionamento Lemniscata
        # if toc(t) > 48:
        #     P.pPos.Xd[[0,1]] = np.array([[0],[0]])
        # elif toc(t) > 36:
        #     P.pPos.Xd[[0,1]] = np.array([[-.375],[-.400]])
        # elif toc(t) > 24:
        #     P.pPos.Xd[[0,1]] = np.array([[-.375],[.400]])
        # elif toc(t) > 12:
        #     P.pPos.Xd[[0,1]] = np.array([[.375],[-.400]])
        # else:
        #     P.pPos.Xd[[0,1]] = np.array([[.375],[.400]])
        
        # Trajetoria Eliptica:  
        XdA = P.pPos.Xd.copy()             
        P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*toc(t))], [Ry*np.sin(w*toc(t))]])
        P.pPos.Xd[[5]] = np.arctan2(P.pPos.Xd[[1]],P.pPos.Xd[[0]])
        P.pPos.Xd[[6,7,11]] = (P.pPos.Xd[[0,1,5]] - XdA[[0,1,5]])/tap
        
        '-----------------------------------------------------'
        P = Ctrl_tgh(P)#,np.array([1,1]))
        # P = Ctrl_tgh_ori(P)#,np.array([1,1,1]))
        # P = Ctrl_tgh_int(P)#,np.array([1,1]),np.array([1,1]))
        # P = ctrl_v22(P)#,np.array([1,1]))

        # # Instantaneous Error:
        # P.pPos.Xtil = (P.pPos.Xd - P.pPos.X)
        
        # for ii in range(3, 6):
        #     if abs(P.pPos.Xtil[ii]) > np.pi:
        #         if P.pPos.Xtil[ii] < 0:
        #             P.pPos.Xtil[ii] = P.pPos.Xtil[ii] + 2 * np.pi
        #         else:
        #             P.pPos.Xtil[ii] = P.pPos.Xtil[ii] - 2 * np.pi

        # A = np.array([
        #     [np.cos(P.pPos.X[5,0]), -P.pPar.a * np.sin(P.pPos.X[5,0] + P.pPar.alpha)],
        #     [np.sin(P.pPos.X[5,0]), P.pPar.a * np.cos(P.pPos.X[5,0] + P.pPar.alpha)]])


        # K = np.diag([0.4,0.4])

        # Func = np.linalg.pinv(A) @ (P.pPos.Xd[[6,7]] + K @ np.tanh(P.pPos.Xtil[[0,1]]))
        # P.pSC.Ud[[0]] = Func[0]
        # P.pSC.Ud[[1]] = Func[1]
        
        '-----------------------------------------------------'
        P.rSendControlSignals()
        
        '-----------------------------------------------------'
        if toc(t)>T:
            ITAE = toc(t)*np.linalg.norm(P.pPos.Xtil[[0,1]])*tap
            IAE = 0
            IASC = 0
        else:
            IASC = np.linalg.norm(P.pSC.Ud[[0,1]])*tap
            IAE = np.linalg.norm(P.pPos.Xtil[[0,1]])*tap
            ITAE = 0

        '-----------------------------------------------------'
        # salva variáveis para plotar no gráfico
        Rastro_Xd.append(P.pPos.Xd.T[0][[0,1]])  # formação desejada
        Rastro_X.append(P.pPos.X.T[0][[0,1]])    # formação real
        # data.append([IAE, ITAE, IASC, P.pPos.Xd[[0,1,5,6,7,11]].T, P.pPos.X[[0,1,5,6,7,11]].T, P.pSC.Ud[0:][0].T, P.pSC.U[0:][0].T,t])
        data.append([P.pPos.Xd[0,0], *P.pPos.X, *P.pSC.Ud, *P.pSC.U, IAE, ITAE, IASC, t])

        '-----------------------------------------------------'

    # Desenha o robo na tela
    if toc(tp) > tap:
        tp = tic()
        Campo_Virtual = Comando_DesenhaTeste(P.pPos.Xc[[0,1,5]], [0,255,0,0,255,0], P.pPos.Xd[[0,1,5]],[255,255,255])                    
        cv2.imshow("Teste Mecanico", Campo_Virtual)
        cv2.waitKey(25) # Está em 25 milisegundos = 40 fps             
        if (cv2.getWindowProperty("Teste Mecanico", cv2.WND_PROP_VISIBLE) < 1):
                    break              

#Destroi a imagem quando termina
if toc(t) >= tsim: 
    cv2.destroyWindow('Teste Mecanico')

    teste = [np.mean(data[:, 4]), np.mean(data[:, 5]), np.mean(data[:, 6]),np.sum(data[:, 4]), np.sum(data[:, 5]), np.sum(data[:, 6])]



'-----------------------------------------------------'
#  Stop robot
P.pSC.Ud = np.array([[0],[0]])         # Zera velocidades do robô
P.rSendControlSignals(0)

# # Save data
# np.save("Trabalhos/T1/Simulação/SAVE/data.npy", data)














# Figures
# Plot the trajectory
plt.figure()
plt.plot(Rastro_Xd[:, 0], Rastro_Xd[:, 1], 'xk', label='$\mathbf{x}_d$', markersize=8.5, linewidth=1)
plt.plot(Rastro_X[:, 0], Rastro_X[:, 1], 'g', label='$\mathbf{x}$', linewidth=1)
plt.legend(fontsize=20, interpreter='latex', loc='upper left')
plt.axis([-5, 5, -5, 5])
plt.grid()
# plt.savefig("Trabalhos/T1/Simulação/SAVE/Fig_1.png")

# Plot control signals
plt.figure()
plt.plot(data[:, -1], data[:, 24], '--k', linewidth=1.5, label='$u$')
plt.plot(data[:, -1], data[:, 25], '-.b', linewidth=1.5, label='$\omega$')
plt.xlabel('$t_{simu}$ [s]', fontsize=16, fontweight='bold', interpreter='latex')
plt.ylabel('Velocidade Linear [m/s]', fontsize=16, fontweight='bold', interpreter='latex')
plt.legend(fontsize=18, interpreter='latex', loc='lower right')
plt.twinx()
plt.plot(data[:, -1], data[:, 25], '-.b', linewidth=1.5)
plt.ylabel('Velocidade Angular [rad/s]', fontsize=16, fontweight='bold', interpreter='latex')
plt.grid()
plt.axis('equal')
plt.axis('tight')
# plt.savefig("Trabalhos/T1/Simulação/SAVE/Fig_2.png")

# Plot position errors
plt.figure()
plt.plot(data[:, -1], data[:, 0] - data[:, 12], '--k', linewidth=1.5, label='$\\tilde{x}$')
plt.plot(data[:, -1], data[:, 1] - data[:, 13], '-.k', linewidth=1.5, label='$\\tilde{y}$')
plt.xlabel('$t_{simu}$ [s]', fontsize=18, fontweight='bold', interpreter='latex')
plt.ylabel('Erro de Posição [m]', fontsize=18, fontweight='bold', interpreter='latex')
plt.legend(fontsize=20, interpreter='latex', loc='upper right')
plt.grid()
plt.axis('tight')
# plt.savefig("Trabalhos/T1/Simulação/SAVE/Fig_3.png")

# Plot orientation errors
plt.figure()
plt.plot(data[:, -1], data[:, 5] - data[:, 17], '-k', linewidth=1.5, label='$\\tilde{\\beta}$')
plt.xlabel('$t_{simu}$ [s]', fontsize=18, fontweight='bold', interpreter='latex')
plt.ylabel('Erro de Orientação [rad]', fontsize=18, fontweight='bold', interpreter='latex')
plt.legend(fontsize=20, interpreter='latex')
plt.grid()
plt.axis('tight')
# plt.savefig("Trabalhos/T1/Simulação/SAVE/Fig_4.png")

# Plot Rho, alpha, and beta
plt.figure()
plt.subplot(311)
plt.plot(data[:, -1], data[:, 28], '-k', linewidth=1.5)
plt.ylabel('$\\rho$ [m]', fontsize=18, fontweight='bold', interpreter='latex')
plt.grid()
plt.axis('tight')

plt.subplot(312)
plt.plot(data[:, -1], data[:, 29], '-.k', linewidth=1.5)
plt.ylabel('$\\alpha$ [rad]', fontsize=18, fontweight='bold', interpreter='latex')
plt.grid()
plt.axis('tight')

plt.subplot(313)
plt.plot(data[:, -1], data[:, 30], '--k', linewidth=1.5)
plt.xlabel('$t_{simu}$ [s]', fontsize=18, fontweight='bold', interpreter='latex')
plt.ylabel('$\\beta$ [m]', fontsize=18, fontweight='bold', interpreter='latex')
plt.grid()
plt.axis('tight')
# plt.savefig("Trabalhos/T1/Simulação/SAVE/Fig_5.png")

plt.show()
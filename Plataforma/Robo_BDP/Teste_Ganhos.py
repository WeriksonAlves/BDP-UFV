
import time
from Classe_JOG import*
from Funções.Controls import *

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

"""Classes initialization - Definindo o Robô"""
# Criando uma variável para representar o Robô

# P = JOGADOR(0)

# Simulação em tempo real
for gx2 in range(1,20,4):#(20,1,-1): #Gx: 1.9, Gy: 1.3, Gp: 0.2
    gx = gx2/10
    for gy2 in range(1,20,4):#(20,1,-1):
        gy = gy2/10
        for gp2 in range(16,20,5):#(30,1,-1):
            gp = gp2/10

        """Classes initialization - Definindo o Robô"""

        P = JOGADOR(0) # Criando uma variável para representar o Robô

        ''' Initial Position'''

        # Xo = input('Digite a posição inicial do robô ([x y z psi]): ');
        Xo = np.array([[0, 0, 0, 0]],dtype=np.float64).T
        P.rSetPose(Xo)         # define pose do robô

        ''' Variables initialization '''

        #  Xa = P.pPos.X(1:6);    % postura anterior
        data = []
        Rastro_Xd = []
        Rastro_X = []

        #  Temporização
        T = 15      # Periodo de cada volta da elipse
        tsim = 2*T    # Tempo total da simulação
        tap = 0.100 # taxa de atualização do pioneer
        t = tic()   # Tempo atual
        tc = tic()  # Tempo de controle
        tp = tic()  # Tempo para plotar

        ''' Simulation'''

        # Parâmetros da trajetória
        w = (2*np.pi/T)
        Rx = 0.3; #[m]
        Ry = 0.3; #[m]


        P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*0)], [Ry*np.sin(w*0)]])
        P.pPos.Xd[[5]] = np.arctan2(P.pPos.Xd[[1]],P.pPos.Xd[[0]])

        ''' Parâmetros para avaliar os ganhos '''

        Erro_mim = 0.01 # Erro minimo aceitavel antes de terminar a primeira volta
        IAE = 0      # Indices
        ITAE = 0     # Indices
        IASC = 0     # Indices
        
        Fim_t  = 0 # Condição de ganho encontrado 
        Fim_gp = 0 # Condição de ganho encontrado 
        Fim_gy = 0 # Condição de ganho encontrado 
        Fim_gx = 0 # Condição de ganho encontrado 

        while toc(t) < tsim:                
            if toc(tc) > tap:
                tc = tic()

                '-----------------------------------------------------'
                # Data aquisition
                P.rGetSensorData()

                '-----------------------------------------------------'
                # Trajetoria Eliptica:  
                XdA = P.pPos.Xd.copy()             
                P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*toc(t))], [Ry*np.sin(w*toc(t))]])
                P.pPos.Xd[[5]] = np.arctan2(P.pPos.Xd[[1]],P.pPos.Xd[[0]])
                P.pPos.Xd[[6,7,11]] = (P.pPos.Xd[[0,1,5]] - XdA[[0,1,5]])/tap
                
                '-----------------------------------------------------'
                P = Ctrl_tgh(P,np.array([gx,gy]))
                # P = Ctrl_tgh_2(P,np.array([gx,gy,gp]))
                
                '-----------------------------------------------------'
                P.rSendControlSignals(0)
                
                '-----------------------------------------------------'
                
                # Verifica o erro
                if (toc(t) <= T/2) and (np.linalg.norm(P.pPos.Xtil[[0,1]]) <= Erro_mim):
                    print(f'Ganho encontrado: Gx: {gx}, Gy: {gy}, Gp: {gp}')
                    Fim_t = 1
                    break
                
                if (toc(t) > T/2) and (np.linalg.norm(P.pPos.Xtil[[0,1]]) > Erro_mim):
                    print('Gx: %.3f, Gy: %.3f, Gp: %.3f' %(gx,gy,gp), f' ==> Erro Atual: {np.linalg.norm(P.pPos.Xtil[[0,1]])}')
                    break

                # Verifica a saturação
                if (abs(P.pSC.RPM[[0]])>600) or (abs(P.pSC.RPM[[1]])>600):
                    print('Gx: %.3f, Gy: %.3f, Gp: %.3f' %(gx,gy,gp), f' ==> Saturado: {P.pSC.RPM.T}' )
                    break
                '-----------------------------------------------------'
                if toc(t)>T:
                    ITAE = toc(t)*np.linalg.norm(P.pPos.Xtil[0:1])*tap
                    IAE = 0
                    IASC = 0
                else:
                    IASC = np.linalg.norm(P.pSC.Ud[0:1])*tap
                    IAE = np.linalg.norm(P.pPos.Xtil[0:1])*tap
                    ITAE = 0

                '-----------------------------------------------------'
                # salva variáveis para plotar no gráfico
                Rastro_Xd.append(P.pPos.Xd.T[0][[0,1]])  # formação desejada
                Rastro_X.append(P.pPos.X.T[0][[0,1]])    # formação real
                data.append([P.pPos.Xd.T, P.pPos.X.T, P.pSC.Ud.T, P.pSC.U.T, IAE, ITAE, IASC, toc(t)])

                '-----------------------------------------------------'
        #     # Desenha o robo na tela
        #     if toc(tp) > tap:
        #         tp = tic()
        #         Campo_Virtual = Comando_DesenhaTeste(P.pPos.Xc[[0,1,5]], [0,255,0,0,255,0], P.pPos.Xd[[0,1,5]],[255,255,255])                    
        #         cv2.imshow("Teste Mecanico", Campo_Virtual)
        #         cv2.waitKey(25) # Está em 25 milisegundos = 40 fps             
        #         if (cv2.getWindowProperty("Teste Mecanico", cv2.WND_PROP_VISIBLE) < 1):
        #                     break              

        # #Destroi a imagem quando termina
        # if toc(t) >= tsim: cv2.destroyWindow('Teste Mecanico')

        if Fim_t == 1:
                print('3')
                Fim_gp = 1
                break
                    
    if Fim_gp == 1:
            print('2')
            Fim_gy = 1
            break

    # if Fim_gy == 1:
    #     print('1')
    #     Fim_gx = 1
    #     break

'''Stop robot'''
# Zera velocidades do robô
P.pSC.Ud[[0,1]] = [[0],[0]]
P.rSendControlSignals(None)
time.sleep(1)

# End of code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
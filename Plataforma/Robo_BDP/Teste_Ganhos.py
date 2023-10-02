
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
# P = Player(0)

# Simulação em tempo real
for Linear in range(100,0,-10):#(20,1,-1): #Gx: 1.9, Gy: 1.3, Gp: 0.2
    Lin = Linear/100
    for Angular in range(100,0,-10):#(20,1,-1):
        Ang = Angular/100
        for Interno1 in range(100,0,-10):#(30,1,-1):
            In1 = Interno1/100
            for Interno2 in range(100,0,-10):#(30,1,-1):
                In2 = Interno2/100
        
                """Classes initialization - Definindo o Robô"""
                P = Player(0) # Criando uma variável para representar o Robô

                ''' Initial Position'''
                # Xo = input('Digite a posição inicial do robô ([x y z psi]): ');
                Xo = np.array([[0, 0, 0, 0]],dtype=np.float64).T
                P.rSetPose(Xo)         # define pose do robô

                ''' Variables initialization '''
                data = []
                Rastro_Xd = []
                Rastro_X = []

                #  Temporização
                T = 30      # Periodo de cada volta da elipse
                tsim = 2*T*10    # Tempo total da simulação
                tap = 0.05 # taxa de atualização do pioneer
                t = tic()   # Tempo atual
                tc = tic()  # Tempo de controle
                tp = tic()  # Tempo para plotar

                ''' Simulation'''
                # Parâmetros da trajetória
                w = (2*np.pi/T)
                Rx = 0.3; #[m]
                Ry = 0.5; #[m]

                P.pPos.Xd[[0,1]] = np.array([[Rx*np.cos(w*0)], [Ry*np.sin(w*0)]])
                P.pPos.Xd[[5]] = np.arctan2(P.pPos.Xd[[1]],P.pPos.Xd[[0]])
                Campo_Virtual = Comando_DesenhaTeste(P.pPos.Xc[[0,1,5]], [0,255,0,0,255,0], P.pPos.Xd[[0,1,5]],[255,255,255])                    
                cv2.imshow("Teste Mecanico", Campo_Virtual)
                
                ''' Parâmetros para avaliar os ganhos '''

                Erro_mim = 0.05 # Erro minimo aceitavel antes de terminar a primeira volta
                IAE = 0      # Indices
                ITAE = 0     # Indices
                IASC = 0     # Indices
        
                Fim_simu = 0 # Condição de ganho encontrado 
                Fim_for1 = 0 # Condição de ganho encontrado 
                Fim_for2 = 0 # Condição de ganho encontrado 
                Fim_for3 = 0 # Condição de ganho encontrado 
                Fim_for4 = 0 # Condição de ganho encontrado 

                for taux in range(0,tsim):
                    t = taux/10
                    # while toc(t) < tsim:                
                    #     if toc(tc) > tap:
                        # tc = tic()

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
                    P = Ctrl_tgh_int(P,np.array([Lin,Ang]),np.array([In1,In2]))
                    # P = Ctrl_tgh_2(P,np.array([Lin,Ang,In1]))
                    
                    '-----------------------------------------------------'
                    P.rSendControlSignals()
                    
                    '-----------------------------------------------------'
                    # Verifica a saturação
                    if (abs(P.pSC.Ud[0,0])>0.8) or (abs(P.pSC.Ud[1,0])>18):
                        print('Lin: %.3f, Ang: %.3f, Int1: %.3f, Int2: %.3f' %(Lin,Ang,In1,In2), f' ==> Saturado l a: {P.pSC.Ud.T}' )
                        break

                    if (abs(P.pSC.RPM[[0]])>500) or (abs(P.pSC.RPM[[1]])>500):
                        print('Lin: %.3f, Ang: %.3f, Int1: %.3f, Int2: %.3f' %(Lin,Ang,In1,In2), f' ==> Saturado rpm: {P.pSC.RPM.T}' )
                        break
                    
                    # Verifica o erro
                    if (t > T/2) and (np.linalg.norm(P.pPos.Xtil[[0,1]]) > Erro_mim):
                        print('Lin: %.3f, Ang: %.3f, Int1: %.3f, Int2: %.3f' %(Lin,Ang,In1,In2), f' ==> Erro Atual: {np.linalg.norm(P.pPos.Xtil[[0,1]])}')
                        break
                    
                    if (t <= T/2) and (np.linalg.norm(P.pPos.Xtil[[0,1]]) <= Erro_mim):
                        print(f'Ganho encontrado: Lin: {Lin}, Ang: {Ang}, Int1: {In1}, Int2: {In2}, RPM: {P.pSC.RPM.T}')
                        Fim_simu = 1
                        break
                    
                    

                    
                    '-----------------------------------------------------'
                    if t>T:
                        ITAE = t*np.linalg.norm(P.pPos.Xtil[0:1])*tap
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
                    data.append([P.pPos.Xd.T, P.pPos.X.T, P.pSC.Ud.T, P.pSC.U.T, IAE, ITAE, IASC, t])

                    '-----------------------------------------------------'
                    # Desenha o robo na tela
                    # if toc(tp) > tap:
                    #     tp = tic()
                    Campo_Virtual = Comando_DesenhaTeste(P.pPos.Xc[[0,1,5]], [0,255,0,0,255,0], P.pPos.Xd[[0,1,5]],[255,255,255])                    
                    cv2.imshow("Teste Mecanico", Campo_Virtual)
                    cv2.waitKey(25) # Está em 25 milisegundos = 40 fps             
                    if (cv2.getWindowProperty("Teste Mecanico", cv2.WND_PROP_VISIBLE) < 1):
                        break              

                #Destroi a imagem quando termina
                if t >= tsim: cv2.destroyWindow('Teste Mecanico')

                if Fim_simu == 1:
                    print('Terminpu a simulação')
                    Fim_for1 = 1
                    break
                            
            if Fim_for1 == 1:
                print('Terminou o for Interno 2')
                Fim_for2 = 1
                break

        if Fim_for2 == 1:
            print('Terminou o for Interno 1')
            Fim_for3 = 1
            break

    if Fim_for2 == 1:
        print('Terminou o for Angular')
        Fim_for3 = 1
        break

'''Stop robot'''
# Zera velocidades do robô
P.pSC.Ud[[0,1]] = [[0],[0]]
P.rSendControlSignals()
time.sleep(1)
print('Teste encerrado')
# End of code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
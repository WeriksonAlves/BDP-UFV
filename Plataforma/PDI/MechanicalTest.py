import numpy as np
import time

class Elipse(object):

    def __init__(self,Rx=1.5,Ry=2.5,T = 60):
        '''
        Rx = Raio no eixo x em m
        Ry = Raio no eixo y em m
        T = Periodo de cada volta da elipse
        '''

        # Temporização
        self.tsim = 2*T   # Tempo total da simulação
        self.tap = 0.100  # taxa de atualização do Jogador

        # Parâmetros de controle
        self.gains_umax = 1 #0.35 
        self.gains_wmax = 1 #0.44 

        # Parâmetros da trajetória
        self.w = (2*np.pi/T) #Frequência em rad/s        
        self.Rx = Rx
        self.Ry = Ry

        # Parâmetros de desempenho
        self.IAE = 0 
        self.ITAE = 0 
        self.IASC = 0 

    def Simula(self,P):
        # Simulação em tempo de máquina
        for t in range(0,self.tsim,self.tap):
            # Data aquisition
            # P.rGetSensorData
            
            # Trajetoria Eliptica:
            P.rBDP_pPos_Xd[0:, 0] = [self.Rx*np.cos(self.w*t), self.Ry*np.sin(self.w*t)]
            P.rBDP_pPos_dXd[0:, 0] = [-self.Rx*self.w*np.sin(self.w*t), self.Ry*self.w*np.cos(self.w*t)]
            
            # -----------------------------------------------------
            # P = Ctrl_exp(P,gains,2,0.06)
            P.xtil()
            P.autonivel()
            P.baixonivel()
            
            # -----------------------------------------------------
            
            # Enviar sinais de controle para o robô
            P.rSendControlSignals
            # if t>self.T:
            #     ITAE = t*norm(P.pPos.Xtil(1:2))*self.tap
            #     IAE = 0
            #     IASC = 0
            # else:
            #     IASC = norm(P.pSC.Ud(1:2))*self.tap
            #     IAE = norm(P.pPos.Xtil(1:2))*self.tap
            #     ITAE = 0

            # # Verifica a saturação
            # if (P.pSC.Ud[1]>0.75) || (P.pSC.Ud(2)>1.74):
            #     disp(['Saturado: ' num2str(P.pSC.Ud(1)) ' e ' num2str(P.pSC.Ud(2))])
            #     break
            
            # # salva variáveis para plotar no gráfico
            # Rastro.Xd = [Rastro.Xd P.pPos.Xd(1:2)']  # formação desejada
            # Rastro.X  = [Rastro.X P.pPos.X(1:2)']    # formação real
            
            # data = [data P.pPos.Xd' P.pPos.X' P.pSC.Ud' P.pSC.U' P.pPos.rho P.pPos.alpha P.pPos.theta IAE ITAE IASC t]


import numpy as np

class MY_TEAM(object):

    def __init__(self,t,j,l,f):
        # Cor do time : t
        # Cor do jogador : j
        # Lado de ataque : l
        # Função em campo : f
        self.rBDP_pPos_X    = np.zeros((3,1),dtype = np.int64)  # Postura atual
        self.rBDP_pPos_Xa   = np.zeros((3,1))  # Postura anterior
        self.rBDP_pPos_Xd   = np.zeros((3,1),dtype = np.int64)  # Postura desejada
        self.rBDP_pPos_Xda  = np.zeros((3,1))  # Postura anterior desejada
        self.rBDP_pPos_dX   = np.zeros((3,1))  # Derivada da postura atual
        self.rBDP_pPos_dXd  = np.zeros((3,1))  # Derivada da postura desejada
        self.rBDP_pPos_Xtil = np.zeros((3,1))  # Erro de posição

        self.rBDP_pSC_a     = 37  # Distância centro ao ponto de controle
        self.rBDP_pSC_alpha = 0  # Angulo de controle
        self.rBDP_pSC_r     = 20 # Raio da roda
        self.rBDP_pSC_d     = 75 # Larguda do robôs
        self.rBDP_pSC_U     = np.zeros((2,1))
        self.rBDP_pSC_W     = np.zeros((2,1))
        self.rBDP_pSC_PWM   = np.zeros((2,1))
        self.rBDP_pSC_GAN   = np.zeros((2,1))
        self.rBDP_pSC_GBN   = np.zeros((2,1))
        # Dados iniciais dos Jogadores

        
        # c: Cyan ou y: Yellow
        self.rBDP_pTime   = t
        # l: l = 1 ou l = -1
        #  Lado de ataque
        self.rBDP_pLado   = l
    
        # r: Red
        # g: Green
        # b: Blue
        # m: Magenta
        self.rBDP_pCor    = j

        # g: goleiro
        # d: defensor
        # a: atacante
        self.rBDP_pFuncao = f
    
    def xtil(self):
        self.rBDP_pPos_Xtil = self.rBDP_pPos_Xd - self.rBDP_pPos_X 
        
    def jogdXd(self):
        self.rBDP_pPos_dXd = self.rBDP_pPos_Xd - self.rBDP_pPos_Xda

    def jogdX(self):
        self.rBDP_pPos_dX = self.rBDP_pPos_X - self.rBDP_pPos_Xa

    def jog_atacante(self):
        pass

    def jog_zagueiro(self):
        pass

    def jog_goleiro(self):
        pass

    def autonivel(self):
        gl = 0.1
        ga = 0.1
        k1 = 1
        k2 = 1
        norma = np.linalg.norm(self.rBDP_pPos_Xtil[0:][0])
        #print(norma)
        A = np.array([[self.rBDP_pPos_dXd[0][0] + k1*(1-np.exp(-k2*((norma))))*self.rBDP_pPos_Xtil[0][0]], [(self.rBDP_pPos_dXd[1][0] + k1*(1-np.exp(-k2*norma))*self.rBDP_pPos_Xtil[1][0])]])

        G = np.array([[gl, 0],
                      [0, ga]])

        #matriz de rotação
        K = np.array([[np.cos(self.rBDP_pPos_X[2][0]), -self.rBDP_pSC_a*np.sin(self.rBDP_pPos_X[2][0])],  
                      [np.sin(self.rBDP_pPos_X[2][0]), self.rBDP_pSC_a*np.cos(self.rBDP_pPos_X[2][0])]])
        Ud = np.linalg.inv(K)@G@A

        self.rBDP_pSC_U[0][0] = Ud[0][0] # velocidade linear
        self.rBDP_pSC_U[1][0] = Ud[1][0] # velocidade angular


    def baixonivel(self):
        Wmax = 2

        # Limites para envia PWM
        limPWMp = np.array([150, 250])  # Velocidade positiva
        limPWMn = np.array([150, 50]) # Velocidade negativa

        K2 = np.array([[1/2, 1/2], [1/self.rBDP_pSC_d, -1/self.rBDP_pSC_d]])

        #  CRIAR: Normalizar valores entre -100 e 100%

        self.rBDP_pSC_W = 1/self.rBDP_pSC_r*(np.linalg.inv(K2)@self.rBDP_pSC_U)
    
        for ii in range(0,2):

            if np.abs(self.rBDP_pSC_W[ii][0]) > Wmax:
                self.rBDP_pSC_W[ii][0] = np.sign(self.rBDP_pSC_W[ii][0])*Wmax

            if self.rBDP_pSC_W[ii][0] > 0:
                self.rBDP_pSC_PWM[ii][0] =  ((limPWMp[1]-limPWMp[0])/Wmax)*self.rBDP_pSC_W[ii] + limPWMp[0]
            else:
                self.rBDP_pSC_PWM[ii][0] = -((limPWMn[1]-limPWMn[0])/Wmax)*self.rBDP_pSC_W[ii] + limPWMn[0]

class OPPONENT:

    def __init__(self,t,l):
        # Cor do time : t
        # Lado de ataque : l

        self.rBDP_pPos_X   = np.zeros(3,1)  # Postura atual
        self.rBDP_pPos_Xa  = np.zeros(3,1)  # Postura anterior
        self.rBDP_pPos_dX  = np.zeros(3,1)  # Derivada da postura atual
        

        # Dados iniciais dos Jogadores
        # Cor do time
        # c: Cyan ou y: Yellow
        self.rBDP_pTime   = t

        #  Lado de ataque
        self.rBDP_pLado   = l

    def opponentdX(self):
        self.rBDP_pPos_dX = self.rBDP_pPos_X - self.rBDP_pPos_Xa

class BALL:

    def __init__(self):
        self.Bola_X = np.zeros(1,2)
        self.Bola_Xa = np.zeros(1,2)
        self.Bola_dX = np.zeros(1,2)

    def balldX(self):
        self.rBDP_pPos_dX = self.Bola_X - self.Bola_Xa
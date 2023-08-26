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
        if (t == np.array([255,255,0])).all():
            self.rBDP_pTime   = 'c'
        elif (t == np.array([0,255,255])).all():
            self.rBDP_pTime   = 'y'
        else:
            print('Erro na cor do time')

        # Lado de ataque
        # Esquerda: -1 ou Direita: 1
        self.rBDP_pLado   = l
    
        # r: Red
        # g: Green
        # b: Blue
        # m: Magenta
        if (j == np.array([0,0,255])).all():
            self.rBDP_pCor   = 'r'
        elif (j == np.array([0,255,0])).all():
            self.rBDP_pCor   = 'g'
        elif (j == np.array([255,0,0])).all():
            self.rBDP_pCor   = 'b'
        elif (j == np.array([238,130,238])).all():
            self.rBDP_pCor   = 'm'
        else:
            print('Erro na cor do jogador')

        # g: goleiro
        # d: defensor
        # a: atacante
        if (f == 0):
            self.rBDP_pFuncao   = 'g'
        elif (f == 1):
            self.rBDP_pFuncao   = 'd'
        elif (f == 2):
            self.rBDP_pFuncao   = 'a'
        else:
            print('Erro na função do jogador')
    
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
        gl = 1
        ga = 1
        k1 = 4
        k2 = 1
        
        norma = np.linalg.norm(self.rBDP_pPos_Xtil[0:2,0:])
        print(norma)
        F_sqrt = self.rBDP_pPos_dXd[0:2,0:] + (k1/np.sqrt(k2**2 + norma**2))*self.rBDP_pPos_Xtil[0:2,0:]

        G = np.array([[gl, 0],
                      [0, ga]])

        #matriz de rotação
        K = np.array([[np.cos( self.rBDP_pPos_X[2][0] + self.rBDP_pSC_alpha), -self.rBDP_pSC_a*np.sin( self.rBDP_pPos_X[2][0] + self.rBDP_pSC_alpha )],  
                      [np.sin( self.rBDP_pPos_X[2][0] + self.rBDP_pSC_alpha),  self.rBDP_pSC_a*np.cos( self.rBDP_pPos_X[2][0] + self.rBDP_pSC_alpha )]])

        Ud = G@np.linalg.inv(K)@F_sqrt

        self.rBDP_pSC_U[0][0] = Ud[0][0] # velocidade linear
        self.rBDP_pSC_U[1][0] = Ud[1][0] # velocidade angular


    def baixonivel(self):
        Wmax = 20

        # Limites para envia PWM
        limPWMp = np.array([40, 80])  # Velocidade positiva
        limPWMn = np.array([-40, -80]) # Velocidade negativa

        K2 = np.array([[1/2, 1/2], [1/self.rBDP_pSC_d, -1/self.rBDP_pSC_d]])

        #  CRIAR: Normalizar valores entre -100 e 100%

        self.rBDP_pSC_W = 1/self.rBDP_pSC_r*(np.linalg.inv(K2)@self.rBDP_pSC_U)
    
        for ii in range(0,2):

            if np.abs(self.rBDP_pSC_W[ii][0]) > Wmax:
                self.rBDP_pSC_W[ii][0] = np.sign(self.rBDP_pSC_W[ii][0])*Wmax

            if self.rBDP_pSC_W[ii][0] > 0:
                self.rBDP_pSC_PWM[ii][0] =  ((limPWMp[1]-limPWMp[0])/Wmax)*self.rBDP_pSC_W[ii] + limPWMp[0] + 150
            else:
                self.rBDP_pSC_PWM[ii][0] = -((limPWMn[1]-limPWMn[0])/Wmax)*self.rBDP_pSC_W[ii] + limPWMn[0] + 150

    # Seta os maximos do sinal
    def set_speed(self,left ,right):
        self.left_speed = max(min(left,100),-100)
        self.right_speed = max(min(right,100),-100)

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
        self.Bola_X = np.zeros(2,1)  # Postura atual
        self.Bola_Xa = np.zeros(2,1) 
        self.Bola_dX = np.zeros(2,1) 

    def balldX(self):
        self.rBDP_pPos_dX = self.Bola_X - self.Bola_Xa
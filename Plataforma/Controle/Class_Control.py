import numpy as np

class MY_TEAM(object):

    def __init__(self,t,j,l,f):
        # Cor do time : t
        # Cor do jogador : j
        # Lado de ataque : l
        # Função em campo : f
        self.rBDP_pPos_X    = np.zeros((3,1),dtype = np.float64)  # Postura atual
        self.rBDP_pPos_Xa   = np.zeros((3,1),dtype = np.float64)  # Postura anterior
        self.rBDP_pPos_Xd   = np.zeros((3,1),dtype = np.float64)  # Postura desejada
        self.rBDP_pPos_Xda  = np.zeros((3,1),dtype = np.float64)  # Postura anterior desejada
        self.rBDP_pPos_dX   = np.zeros((3,1),dtype = np.float64)  # Derivada da postura atual
        self.rBDP_pPos_dXd  = np.zeros((3,1),dtype = np.float64)  # Derivada da postura desejada
        self.rBDP_pPos_Xtil = np.zeros((3,1),dtype = np.float64)  # Erro de posição

        self.rBDP_pSC_a     = 32  # Distância centro ao ponto de controle
        self.rBDP_pSC_alpha = 0  # Angulo de controle
        self.rBDP_pSC_r     = 21.5 # Raio da roda
        self.rBDP_pSC_d     = 75 # Larguda do robôs
        self.rBDP_pSC_U     = np.zeros((2,1),dtype = np.float64)
        self.rBDP_pSC_W     = np.zeros((2,1),dtype = np.float64)
        self.rBDP_pSC_PWM   = np.zeros((2,1),dtype=int)
        self.rBDP_pSC_GAN   = np.zeros((2,1),dtype = np.float64)
        self.rBDP_pSC_GBN   = np.zeros((2,1),dtype = np.float64)
        # Dados iniciais dos Jogadores

        
        # c: Azul ou y: Amarelo
        if (t == np.array([255, 0, 0])).all():
            self.rBDP_pTime   = 'Azul'
        elif (t == np.array([0, 255, 255])).all():
            self.rBDP_pTime   = 'Amarelo'
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
        elif (j == np.array([255, 255, 0])).all():
            self.rBDP_pCor   = 'c'
        elif (j == np.array([238,130,238])).all():
            self.rBDP_pCor   = 'm'
        else:
            print('Erro na cor do jogador')

        # g: goleiro
        # d: defensor
        # a: atacante
        if (f == 0):
            self.rBDP_pFuncao   = 'GK'
        elif (f == 1):
            self.rBDP_pFuncao   = 'DC'
        elif (f == 2):
            self.rBDP_pFuncao   = 'ST'
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
        k1 = 2
        k2 = 1
        
        norma = np.linalg.norm(self.rBDP_pPos_Xtil[0:2,0:])
        # print(norma)
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

        # Limites para envia PWM
        limRPM_p = np.array([0, 100])  # Velocidade positiva
        limRPM_n = np.array([-0, -100]) # Velocidade negativa

        K2 = np.array([[1/2, 1/2], [1/self.rBDP_pSC_d, -1/self.rBDP_pSC_d]])

        #  CRIAR: Normalizar valores entre -100 e 100%

        self.rBDP_pSC_W = 1/self.rBDP_pSC_r*(np.linalg.inv(K2)@self.rBDP_pSC_U)
        self.rBDP_pSC_W = self.rBDP_pSC_W*60/(2*np.pi) # Em RPM

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

class MY_JOYSTICK:
    def __init__(self):
        # Variaveis principais:
        a=0

    def check_analog(self, joysticks, robots):
        for i,joystick in enumerate(joysticks):
            x_axis = joystick.get_axis(3)
            y_axis = joystick.get_axis(1)

            ValorMin = 0
            if x_axis < 0: sum1 = ValorMin
            else: sum1 = -ValorMin
            if y_axis < 0: sum2 = ValorMin
            else: sum2 = -ValorMin

            left_speed = int(-y_axis * 100 + sum2)
            right_speed = int(-x_axis * 100 + sum1)        
            left_speed,right_speed = self.set_speed(left_speed,right_speed)
            robots[i].rBDP_pSC_W = np.array([[left_speed, right_speed]]).T
                        
    def check_RT(self, joysticks, robots):
        for i,joystick in enumerate(joysticks):
            robots[i].rBDP_pSC_W = np.array([[-500,500]]).T

    def check_LT(self, joysticks, robots):
        for i,joystick in enumerate(joysticks):
            robots[i].rBDP_pSC_W = np.array([[500,-500]]).T

    # Seta os maximos do sinal
    def set_speed(self, left ,right):
        left_speed = max(min(left,500),-500)
        right_speed = max(min(right,500),-500)
        return left_speed,right_speed



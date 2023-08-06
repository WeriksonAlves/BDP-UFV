'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem do campo.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*
from math import dist
from tkinter import ttk
from Control.Class_Control import*
from Control.BDP_3D import BDP__3DX

import tkinter as tk
import cv2
import threading
import numpy as np
import os
import serial
import time
import matplotlib.pyplot as plt
import math
#..............................................................................................................
# Cria a janela responsavel pelas configurações da partida
class GameWindow(object):
    def __init__(self,MatrixColor,CamInfo,FPS,Kernel,MedianBlur,PTM):
        # Variaveis principais:
        self.Var_CameraInformation = CamInfo
        self.Var_FPS = FPS
        self.Var_MatrixColor = MatrixColor
        self.Var_Kernel = Kernel
        self.Var_MedianBlur = MedianBlur
        self.Var_Perspective_Transformation_Matrix = PTM

        self.Var_Comunication = False
        self.Var_Play = False
        self.Var_MechanicalTest = False
        self.Current_Folder = os.path.dirname(__file__)
        self.Img_Field_px = cv2.imread(self.Current_Folder+'\Field_px.png')
        self.Var_Game_Parameters = np.array([[0,0,0],
                                             [0,0,0],
                                             [0,0,0],
                                             [0,0,0],
                                             [0,0,0],
                                             [0,0,0],
                                             [0,0,0]], dtype = np.int64) 

        # Executa as funções
        self.Create_Window()
        self.Create_TextInformation()
        self.Create_CheckButton()
        self.Create_ComboBox()
        self.Create_Button()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria e configura a subjanela
    def Create_Window(self):
        self.Window = Toplevel()
        self.Window.title("Tela de Jogo")
        self.Window.minsize(830, 600)
        self.Window.maxsize(830, 600)
        self.Window.configure(bg= '#229A00')

        self.StatusBar = tk.Label(self.Window,
                        text="Instruções: \nConfigurar os jogadores \nIniciar comunicação \n Iniciar partida",
                        bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a barra de status
    def Clear_StatusBar(self):
        try:
            self.StatusBar.config(text="")
            self.StatusBar.update_idletasks() 
        except: pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Sobreescreve a barra de status
    def Set_StatusBar(self, texto):
        try:
            self.StatusBar.config(text=texto)
            self.StatusBar.update_idletasks() 
        except: pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria os textos informativos da janela
    def Create_TextInformation(self):
        Txt_Game_Settings = Label(self.Window,text="Configurações de Jogo",bg= '#229A00')
        Txt_Game_Settings.place(height=30, width=130, x=300, y=0)

        Txt_Player_Information = Label(self.Window,text="Informações dos Jogadores",bg= '#229A00')
        Txt_Player_Information.place(height=30, width=150, x=300, y=170)

        Txt_Player1 = Label(self.Window,text="Jogador 1",bg= '#229A00')
        Txt_Player1.place(height=30, width=100, x=310, y=80)

        Txt_Player2 = Label(self.Window,text="Jogador 2",bg= '#229A00')
        Txt_Player2.place(height=30, width=100, x=430, y=80)

        Txt_Player3 = Label(self.Window,text="Jogador 3",bg= '#229A00')
        Txt_Player3.place(height=30, width=100, x=550, y=80)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria as checkbutton
    def Create_CheckButton(self):
        self.Var_Cyan_Team = tk.IntVar()
        Chebut_Cyan = Checkbutton(self.Window, text="Ciano", bg="cyan", variable=self.Var_Cyan_Team, command=self.Command_CyanTeam)
        Chebut_Cyan.place(height=50, width=120, x=300, y=30)

        self.Var_Yellow_Team = tk.IntVar()
        Chebut_Yellow = Checkbutton(self.Window, text="Amarelo", bg="yellow", variable=self.Var_Yellow_Team, command=self.Command_YellowTeam)
        Chebut_Yellow.place(height=50, width=120, x=420, y=30)
        
        self.Var_Left_Attack = tk.IntVar()
        Chebut_Left_Attack = Checkbutton(self.Window, text="<<<===", bg="grey", variable=self.Var_Left_Attack, command=self.Command_LeftAttack)
        Chebut_Left_Attack.place(height=50, width=120, x=540, y=30)

        self.Var_Right_Attack = tk.IntVar()
        Chebut_Right_Attack = Checkbutton(self.Window, text="===>>>", bg="grey", variable=self.Var_Right_Attack, command=self.Command_RightAttack)
        Chebut_Right_Attack.place(height=50, width=120, x=660, y=30)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_CyanTeam(self):
        self.Var_Cyan_Team.set(True)
        self.Var_Yellow_Team.set(False)
        
        self.Var_MyTeam_Color = 4
        self.Var_MyTeam_Color_BGR = (255,255,0)

        self.Var_Opp_Color = 2
        self.Var_Opp_Color_BGR = (0,255,255)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_YellowTeam(self):
        self.Var_Cyan_Team.set(False)
        self.Var_Yellow_Team.set(True)

        self.Var_MyTeam_Color = 2
        self.Var_MyTeam_Color_BGR = (0,255,255)

        self.Var_Opp_Color = 4
        self.Var_Opp_Color_BGR = (255,255,0)            
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_LeftAttack(self):
        self.Var_Right_Attack.set(False)
        self.Var_Left_Attack.set(True)

        self.Var_AttackSide = -1
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_RightAttack(self):
        self.Var_Right_Attack.set(True)
        self.Var_Left_Attack.set(False)

        self.Var_AttackSide = 1
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Create_ComboBox(self):
        Player_Role_List = ['GK', 'DC','ST']     
        Player_Shirts_List = ['Azul', 'Magenta','Verde', 'Vermelho']

        P1_Player_Role = tk.StringVar()
        self.Var_P1_Function = ttk.Combobox(self.Window, state= 'readonly', textvariable= P1_Player_Role, values= Player_Role_List, justify='center')
        self.Var_P1_Function.place(height= 20, width= 100, x=310, y=110)

        P2_Player_Role = tk.StringVar()
        self.Var_P2_Function = ttk.Combobox(self.Window, state= 'readonly', textvariable = P2_Player_Role, values = Player_Role_List, justify='center')
        self.Var_P2_Function.place(height= 20, width= 100, x=430, y=110)

        P3_Player_Role = tk.StringVar()
        self.Var_P3_Function = ttk.Combobox(self.Window, state= 'readonly', textvariable = P3_Player_Role, values = Player_Role_List, justify='center')
        self.Var_P3_Function.place(height= 20, width= 100, x=550, y=110)

        P1_Player_Color = tk.StringVar()
        self.Var_P1_Color = ttk.Combobox(self.Window, state= 'readonly', textvariable = P1_Player_Color, values = Player_Shirts_List, justify='center')
        self.Var_P1_Color.place(height= 20, width= 100, x=310, y=140)

        P2_Player_Color = tk.StringVar()
        self.Var_P2_Color = ttk.Combobox(self.Window, state= 'readonly', textvariable = P2_Player_Color, values = Player_Shirts_List, justify='center')
        self.Var_P2_Color.place(height= 20, width= 100, x=430, y=140)

        P3_Player_Color = tk.StringVar()
        self.Var_P3_Color = ttk.Combobox(self.Window, state= 'readonly', textvariable = P3_Player_Color, values = Player_Shirts_List, justify='center')
        self.Var_P3_Color.place(height= 20, width= 100, x=550, y=140)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria os botões na janela
    def Create_Button(self):
        But_SaveCalibration = Button(self.Window, text="Salvar\nConfiguração", command = self.Command_SaveSettings)
        But_SaveCalibration.place(height=50, width=200, x=50, y=10)

        But_SaveCalibration = Button(self.Window, text="Carregar\nConfiguração", command = self.Command_LoadSettings)#, state='disabled')
        But_SaveCalibration.place(height=50, width=200, x=50, y=70)

        But_StartComunication = Button(self.Window, text="Abrir/Fechar \nComunicação", command = self.Command_StartComunication)
        But_StartComunication.place(height=50, width=200, x=50, y=130)

        But_MechanicalTest = Button(self.Window, text="Teste Mecânico", command = lambda: threading.Thread(target=self.Command_MechanicalTest).start())
        But_MechanicalTest.place(height=50, width=200, x=50, y=190)

        But_StartGame = Button(self.Window, text="Iniciar Partida", command = lambda: threading.Thread(target=self.Command_StartGame).start())
        But_StartGame.place(height=50, width=200, x=50, y=250)

        But_StopGame = Button(self.Window, text="Parar Partida", command=self.Command_StopGame)
        But_StopGame.place(height=50, width=200, x=50, y=310)

        But_ViewCamera = Button(self.Window, text="Ver Câmera", command = lambda: threading.Thread(target=self.Command_ViewCamera).start())
        But_ViewCamera.place(height=50, width=200, x=50, y=370)

        But_ViewSegmentation = Button(self.Window, text="Ver Segmentação", command = lambda: threading.Thread(target=self.Command_ViewSegmentation).start(), state='disabled')
        But_ViewSegmentation.place(height=50, width=200, x=50, y=430)

        But_ViewAssociation = Button(self.Window, text="Ver Associação", command = lambda: threading.Thread(target=self.Command_ViewAssociation).start())
        But_ViewAssociation.place(height=50, width=200, x=50, y=490)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_SaveSettings(self): # Voltar aqui depois
        self.Var_Game_Settings = np.array([[self.Var_P1_Function.current(), self.Var_P1_Color.current()],
                                           [self.Var_P2_Function.current(), self.Var_P2_Color.current()],
                                           [self.Var_P3_Function.current(), self.Var_P3_Color.current()],
                                           [self.Var_Cyan_Team.get(),       self.Var_Yellow_Team.get()],
                                           [self.Var_Left_Attack.get(),     self.Var_Right_Attack.get()]])
        print('Teste Config\n', self.Var_Game_Settings)

        Matrix = self.Command_Save_Load()
        
        if ((-1 in Matrix)==False) and ((self.Var_Cyan_Team.get()==True) or (self.Var_Yellow_Team.get()==True)) and ((self.Var_Left_Attack.get()==True) or (self.Var_Right_Attack.get()==True)):
            self.Clear_StatusBar()
            self.Set_StatusBar("Salvando calibração")

            np.savetxt(self.Current_Folder+'\Game_Settings.txt', self.Var_Game_Settings, newline='\n')
            
            self.Clear_StatusBar()
            self.Set_StatusBar('As configurações foram salvas. \nInicie a comunicação.')
        else:
            self.Clear_StatusBar()
            self.Set_StatusBar('Complete todos os \ncampos antes de salvar.')
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Carrega a configuração
    def Command_LoadSettings(self):
        try:
            self.Var_Game_Settings = np.loadtxt(self.Current_Folder+'\Game_Settings.txt',dtype=int)
            self.Var_P1_Function.current(self.Var_Game_Settings[0][0])
            self.Var_P1_Color.current(self.Var_Game_Settings[0][1])
            self.Var_P2_Function.current(self.Var_Game_Settings[1][0])
            self.Var_P2_Color.current(self.Var_Game_Settings[1][1])
            self.Var_P3_Function.current(self.Var_Game_Settings[2][0])
            self.Var_P3_Color.current(self.Var_Game_Settings[2][1])

            if self.Var_Game_Settings[3][0] == 1: self.Command_CyanTeam()
            elif self.Var_Game_Settings[3][1] == 1: self.Command_YellowTeam()
            else: print('Error 1')
            if self.Var_Game_Settings[4][0] == 1: self.Command_LeftAttack()
            elif self.Var_Game_Settings[4][1] == 1: self.Command_RightAttack()
            else: print('Error 2')

            _ = self.Command_Save_Load()

            self.Clear_StatusBar()
            self.Set_StatusBar("Calibragem carregada.")
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Arquivo não encontrado, faça uma nova calibração.")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Save_Load(self):    
        Matrix = np.array([[self.Var_P1_Function.current(), self.Var_P1_Color.current()],
                           [self.Var_P2_Function.current(), self.Var_P2_Color.current()],
                           [self.Var_P3_Function.current(), self.Var_P3_Color.current()]])
            
        self.Colors_Shirts = np.zeros([3,6])
        self.Colors_Shirts_BGR = np.zeros([3,3])
        for linha in range(len(Matrix)):
            if Matrix[linha][1] == 0: #Azul
                self.Colors_Shirts[linha] = self.Var_MatrixColor[5][0:]
                self.Colors_Shirts_BGR[linha] = (255,0,0)            
            elif Matrix[linha][1] == 1: #Magenta
                self.Colors_Shirts[linha] = self.Var_MatrixColor[6][0:]
                self.Colors_Shirts_BGR[linha] = (238,130,238)  
            elif Matrix[linha][1] == 2: #Verde
                self.Colors_Shirts[linha] = self.Var_MatrixColor[3][0:]
                self.Colors_Shirts_BGR[linha] = (0,255,0)  
            elif Matrix[linha][1] == 3: #Vermelho
                self.Colors_Shirts[linha] = self.Var_MatrixColor[0][0:]
                self.Colors_Shirts_BGR[linha] = (0,0,255) 
        
        # Cria os robôs
        self.P1 = MY_TEAM(self.Var_MyTeam_Color_BGR,self.Colors_Shirts_BGR[0][0:],self.Var_AttackSide,self.Var_P1_Function.current())
        self.P2 = MY_TEAM(self.Var_MyTeam_Color_BGR,self.Colors_Shirts_BGR[1][0:],self.Var_AttackSide,self.Var_P2_Function.current())
        self.P3 = MY_TEAM(self.Var_MyTeam_Color_BGR,self.Colors_Shirts_BGR[2][0:],self.Var_AttackSide,self.Var_P3_Function.current())
        return Matrix
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_StartComunication(self,tsim=5):
        try:
            self.pEsp = serial.Serial('COM4', 115200, timeout=2)
            if self.Var_Comunication == False:
                self.pEsp.close()
                self.pEsp.open()

                #1,2,3 subtitui B,D,P
                start = time.time()
                while True:
                    t = time.time() - start

                    if t > 4*tsim/5: n = 100
                    elif t > 3*tsim/5: n = 80
                    elif t > 2*tsim/5: n = 60
                    elif t > 1*tsim/5: n = 40
                    else: n = 20

                    # print(n,t)
                    self.pEsp.write([1, 2, int(150+n), int(150+n), int(150+n), int(150+n), 150, 150, 3, 10])
                    if t > tsim:
                        self.pEsp.write([1, 2, int(0), int(0), int(0), int(0), 150, 150, 3, 10])
                        break
                self.Var_Comunication = True
                self.Clear_StatusBar()
                self.Set_StatusBar("Comunição Iniciada")
        except:
            try:
                self.pEsp.close()

                self.Var_Comunication = False
                self.Clear_StatusBar()
                self.Set_StatusBar("Comunição Encerrada")
            except:
                self.Clear_StatusBar()
                self.Set_StatusBar("Conecte o transmissor")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_MechanicalTest(self):
        '''
        Executa uma elipse para cada robô seguir
        Rx: Raio em x
        Ry: Raio em y
        w: Periodo da elipse
        '''

        self.Clear_StatusBar()
        self.Set_StatusBar("Teste mecânico iniciado")

        self.Var_MechanicalTest = True
        
        # Define os parametros do circulo
        Rx=375
        Ry=325
        T = 90
        center_x = 0  # coordenada x do centro
        center_y = 0  # coordenada y do centro
        w = 2*np.pi/T  # Frequéncia angular (em radianos)
        elapsed_time = np.inf
        StartCycle = time.time()

        self.Get_Game_Data()

        p = BDP__3DX(self.Var_MyTeam_Color_BGR,self.Colors_Shirts_BGR[0][0:],self.Var_AttackSide,self.Var_P1_Function.current())
        # axis = [-5, 5, -5, 5]
        # fig = plt.figure(1, figsize=[5, 5])

        while self.Var_MechanicalTest == True:
            # Obtém o tempo decorrido desde o início do ciclo
            elapsed_time = time.time() - StartCycle

            # Calcula a posição atual em coordenadas polares 
            # self.P1.rBDP_pPos_X[0:, 0] 
            aaaa = np.array([[center_x + Rx * math.cos(w*elapsed_time)],
                                                     [center_y + Ry * math.sin(w*elapsed_time)],
                                                     [-np.pi/2 +w*elapsed_time]])

            print("Teste:",[w,elapsed_time,aaaa])

            Campo_Virtual = self.Command_DrawAll(aaaa,self.Color_Player_1, self.Posture_P2,self.Color_Player_2, self.Posture_P3,self.Color_Player_3,
                                                    self.Position_Oponent_1, self.Position_Oponent_2, self.Position_Oponent_3, self.Color_Opp, 
                                                    self.Position_Ball, self.Color_Ball)

            cv2.imshow("Visao Associacao", Campo_Virtual)
            cv2.waitKey(self.Var_FPS) #Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("Visao Associacao", cv2.WND_PROP_VISIBLE) <1):
                break



        #     # Plota os pontos no eixo x e y
        #     plt.scatter(x, y,marker='.',s=5)
        #     plt.show()

        #     # Atualize a posição do robô usando as coordenadas geradas

        #     # self.Update_Robot_Position(x, y)  # Substitua este método pelo método correto para atualizar a posição do robô

        #     self.Get_Game_Data()

        #     # self.Get_Game_Data()
        #     # self.Game_Action()

        self.Clear_StatusBar()
        self.Set_StatusBar('Partida Encerrada')
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_StartGame(self):
        self.Var_Play = True
        self.Clear_StatusBar()
        self.Set_StatusBar("Partida Iniciada")

        while self.Var_Play == True:
            self.StartCycle = time.time()
            self.Get_Game_Data()
            self.Game_Action()

        self.Clear_StatusBar()
        self.Set_StatusBar('Partida Encerrada')
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Get_Game_Data(self):
        _, Var_Frames = self.Var_CameraInformation.read()
        Var_Frames = cv2.resize(cv2.medianBlur(Var_Frames,self.Var_MedianBlur), [640,480]) #Aplica um filtro de mediana

        # Posição da bola em pixel
        self.Position_Ball = self.Command_SearchBall(Var_Frames, self.Var_MatrixColor[1][0:])
        
        # Posição das cores do meu time e do oponente
        MyTeam = self.Command_SearchPositionColor(Var_Frames, self.Var_MatrixColor[self.Var_MyTeam_Color][0:])
        Opponent = self.Command_SearchPositionColor_Opp(Var_Frames, self.Var_MatrixColor[self.Var_Opp_Color][0:])

        #Posição das cores dos meus jogadores
        Centroid_P1 = self.Command_SearchPositionColor(Var_Frames, self.Colors_Shirts[0][0:])
        Centroid_P2 = self.Command_SearchPositionColor(Var_Frames, self.Colors_Shirts[1][0:])
        Centroid_P3 = self.Command_SearchPositionColor(Var_Frames, self.Colors_Shirts[2][0:])
        

        self.Posture_P1, self.Posture_P2, self.Posture_P3  = self.Command_Associate_Shirts(MyTeam, Centroid_P1, Centroid_P2, Centroid_P3) 
                    
        self.Position_Oponent_1 = [Opponent[0][0],Opponent[0][1]]
        self.Position_Oponent_2 = [Opponent[1][0],Opponent[1][1]]
        self.Position_Oponent_3 = [Opponent[2][0],Opponent[2][1]]

        self.Color_Player_1 = self.Colors_Shirts_BGR[0][0:]
        self.Color_Player_2 = self.Colors_Shirts_BGR[1][0:]
        self.Color_Player_3 = self.Colors_Shirts_BGR[2][0:]
        self.Color_Opp = self.Var_Opp_Color_BGR
        self.Color_Ball = (0,165,255)

        if(len(self.Posture_P1) != 0):
            self.Var_Game_Parameters[0, 0:] = np.array(self.Posture_P1).T
            self.Var_Game_Parameters[0, 0] = self.Var_Game_Parameters[0, 0]*-1
        if(len(self.Posture_P2) != 0): 
            self.Var_Game_Parameters[1, 0:] = np.array(self.Posture_P2).T
            self.Var_Game_Parameters[1, 0] = self.Var_Game_Parameters[1, 0]*-1
        if(len(self.Posture_P3) != 0):
            self.Var_Game_Parameters[2, 0:] = np.array(self.Posture_P3).T
            self.Var_Game_Parameters[2, 0] = self.Var_Game_Parameters[2, 0]*-1
        if(len(self.Position_Oponent_1) != 0):
            self.Var_Game_Parameters[3, 0:2] = np.array(self.Position_Oponent_1).T
            self.Var_Game_Parameters[3, 0] = self.Var_Game_Parameters[3, 0]*-1
        if(len(self.Position_Oponent_2) != 0):
            self.Var_Game_Parameters[4, 0:2] = np.array(self.Position_Oponent_2).T
            self.Var_Game_Parameters[4, 0] = self.Var_Game_Parameters[4, 0]*-1
        if(len(self.Position_Oponent_3) != 0): 
            self.Var_Game_Parameters[5, 0:2] = np.array(self.Position_Oponent_3).T
            self.Var_Game_Parameters[5, 0] = self.Var_Game_Parameters[5, 0]*-1
        if(len(self.Position_Ball) != 0): 
            self.Var_Game_Parameters[6, 0:2] = self.Position_Ball.T
            self.Var_Game_Parameters[6, 0] = self.Var_Game_Parameters[6, 0]*-1
        # print(self.Position_Ball,'\na',self.Var_Game_Parameters)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_SearchBall(self, frame, vector_limites, MaxArea = 200, MinArea = 100):
        #encontra as posições de todos os objetos de cor pré-determinada na imagem segmentada.
        Area_Atual = 0
        BallPosition = np.ones((3,1))

        Var_Color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        LimitColorLower = np.array([vector_limites[0],vector_limites[2],vector_limites[4]])
        LimitColorUpper = np.array([vector_limites[1],vector_limites[3],vector_limites[5]])
        
        Var_Color = cv2.inRange(Var_Color, LimitColorLower, LimitColorUpper)
        Var_Color = cv2.dilate(Var_Color, self.Var_Kernel, iterations=1) #testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        # Var_Color = cv2.morphologyEx(Var_Color, cv2.MORPH_OPEN, self.Var_Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur

        Contours, _ = cv2.findContours(Var_Color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Size_Contours = len(Contours)

        if Size_Contours > 0: 
            for i in range(Size_Contours):
                tupla = Contours[i]
                M = cv2.moments(tupla)
                try:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    x = np.array([cx,cy])
                    Area = cv2.contourArea(tupla)

                    if (MinArea < Area) and (Area < MaxArea) and (Area > Area_Atual): 
                        BallPosition[0][0] = x[0]
                        BallPosition[1][0] = x[1]
                        Area_Atual = Area
                except: pass

            BallPosition = self.Var_Perspective_Transformation_Matrix@BallPosition
            return BallPosition[0:2,0:]
        else: 
            BallPosition = [] 
            return BallPosition
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_SearchPositionColor(self, frame, vector_limites,MinArea = 200,MaxArea = 500):
        #encontra as posições de todos os objetos de cor pré-determinada na imagem segmentada.        
        PositionColor = []
        ColorPosition = np.ones((3,1))
         
        Color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        LimitColorLower = np.array([vector_limites[0],vector_limites[2],vector_limites[4]])
        LimitColorUpper = np.array([vector_limites[1],vector_limites[3],vector_limites[5]])

        Color = cv2.inRange(Color, LimitColorLower, LimitColorUpper)
        Color = cv2.dilate(Color, self.Var_Kernel, iterations=1) #testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        #PositionColor = cv2.morphologyEx(PositionColor, cv2.MORPH_OPEN, Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        
        contours, _ = cv2.findContours(Color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Size_Contours = len(contours)

        if Size_Contours > 0:
            for i in range(Size_Contours):
                tupla = contours[i]
                M = cv2.moments(tupla)
                try:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    x = np.array([cx,cy])
                    Area = cv2.contourArea(tupla)

                    if (Area > MinArea) and (Area < MaxArea):
                        ColorPosition[0,0] = x[0]
                        ColorPosition[1,0] = x[1]
                        x = self.Var_Perspective_Transformation_Matrix@ColorPosition
                        PositionColor.append(x[0:2,0:])
                except: pass
        else: 
            PositionColor = []
        return PositionColor
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_SearchPositionColor_Opp(self, frame, vector_limites,MinArea = 200,MaxArea = 500):
        #encontra as posições de todos os objetos de cor pré-determinada na imagem segmentada.
        PositionColor_Opp = []
        ColorPosition = np.ones((3,1))
         
        Color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        LimitColorLower = np.array([vector_limites[0],vector_limites[2],vector_limites[4]])
        LimitColorUpper = np.array([vector_limites[1],vector_limites[3],vector_limites[5]])

        Color = cv2.inRange(Color, LimitColorLower, LimitColorUpper)
        Color = cv2.dilate(Color, self.Var_Kernel, iterations=1) #testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        #PositionColor_Opp = cv2.morphologyEx(PositionColor_Opp, cv2.MORPH_OPEN, Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        
        contours, _ = cv2.findContours(Color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Size_Contours = len(contours)
        VectorFinal = []

        if Size_Contours > 0:
            VectorArea = []
            for i in range(Size_Contours):
                tupla = contours[i]
                M = cv2.moments(tupla)
                try:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    x = np.array([cx,cy])
                    Area = cv2.contourArea(tupla)
                    if (Area > MinArea) and (Area < MaxArea):
                        ColorPosition[0,0] = x[0]
                        ColorPosition[1,0] = x[1]
                        x = self.Var_Perspective_Transformation_Matrix@ColorPosition
                        PositionColor_Opp.append(x[0:2,0:])
                        VectorArea.append(Area)
                except: pass

            Vector_Array = np.array(VectorArea)
            Vector_Index = Vector_Array.argsort()[-3:][::-1]
            for E in Vector_Index:
                VectorFinal.append(PositionColor_Opp[E])

        if(len(VectorFinal)==3):
            return VectorFinal
        elif(len(VectorFinal)==2):
            VectorFinal.append(np.array([250,685]))
            return VectorFinal
        elif(len(VectorFinal)==1):
            VectorFinal.append(np.array([230,685]))
            VectorFinal.append(np.array([250,685]))
            return VectorFinal
        elif(len(VectorFinal)==0):
            VectorFinal.append(np.array([200,685]))
            VectorFinal.append(np.array([250,685]))
            VectorFinal.append(np.array([300,685]))
            return VectorFinal
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Associate_Shirts(self, Position_Shirt_Team, Position_Shirts_P1, Position_Shirts_P2, Position_Shirts_P3):
        Posture_Player_1 = self.Command_Associate_Single_Shirts(Position_Shirt_Team, Position_Shirts_P1)
        Posture_Player_2 = self.Command_Associate_Single_Shirts(Position_Shirt_Team, Position_Shirts_P2)
        Posture_Player_3 = self.Command_Associate_Single_Shirts(Position_Shirt_Team, Position_Shirts_P3)
        
        return Posture_Player_1, Posture_Player_2, Posture_Player_3
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Associate_Single_Shirts(self, Position_Shirt_Team, Position_Shirts_Players, Maximum_Distance = 80):
        #função deve receber posição transformada pela matriz de transformação de perspectiva.
        Position_Possible = []
        List_Dist = []
        Angles = []

        NumberPlayers = np.shape(Position_Shirt_Team)[0] #numero de jogadores
        NumberShirts = np.shape(Position_Shirts_Players)[0] #numero de camisas
        if (NumberPlayers > 0) and (NumberShirts > 0):
            for k in range(NumberPlayers):
                StoreDistance = []
                for i in range(NumberShirts):
                    StoreDistance.append(dist(Position_Shirt_Team[k][0:],Position_Shirts_Players[i][0:]))
                List_Dist.append(min(StoreDistance)) # Contem todas as distâncias possiveis
                Index_1 = np.argmin(StoreDistance) # Pega o indice de menor valor
                Position_Possible.append(np.mean(np.array([Position_Shirt_Team[k][0:],Position_Shirts_Players[Index_1][0:]]), axis=0)) #media das colunas
                DifferenceVector  = np.array(Position_Shirts_Players[Index_1][0:]) - np.array(Position_Shirt_Team[k][0:])
                if DifferenceVector[1] > 0:
                    Angles.append(-np.arccos(np.dot(DifferenceVector.T/np.linalg.norm(DifferenceVector.T),np.array([1,0]))))
                else:
                    Angles.append(np.arccos(np.dot(DifferenceVector.T/np.linalg.norm(DifferenceVector.T),np.array([1,0]))))

            #condição para caso não houver a captura de todas as camisas do time
            if np.min(List_Dist) < Maximum_Distance:
                Index_2 = np.argmin(np.array(List_Dist))
                Position_Final_Player = Position_Possible[Index_2][0:]
                Orientation = Angles[Index_2]
                Posture_Player = [Position_Final_Player[0], Position_Final_Player[1], Orientation]
            else:
                Posture_Player = []
        else:
            Posture_Player = []

        return Posture_Player
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_StopGame(self):
        self.Var_Play = False
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ViewCamera(self):
        while True:
            _, Frames = self.Var_CameraInformation.read()
            Frames = cv2.resize(cv2.medianBlur(Frames,self.Var_MedianBlur), [640,480]) #Aplica um filtro de mediana

            cv2.imshow("Visao Camera", Frames)
            k = cv2.waitKey(self.Var_FPS) #Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("Visao Camera", cv2.WND_PROP_VISIBLE) <1):
                break
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ViewSegmentation(self):
        pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ViewAssociation(self):
        while True:
            Campo_Virtual = self.Command_DrawAll(self.Posture_P1,self.Color_Player_1, self.Posture_P2,self.Color_Player_2, self.Posture_P3,self.Color_Player_3,
                                                    self.Position_Oponent_1, self.Position_Oponent_2, self.Position_Oponent_3, self.Color_Opp, 
                                                    self.Position_Ball, self.Color_Ball)

            cv2.imshow("Visao Associacao", Campo_Virtual)
            cv2.waitKey(self.Var_FPS) #Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("Visao Associacao", cv2.WND_PROP_VISIBLE) <1):
                break
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Draw_Arrow(self, Campo_Virtual, X, Y, Orientacao, Color = (0,255,0), Comprimento = 60):
        X = X + 900
        Y = Y + 750
        end_point = (int(X + Comprimento*np.cos(-Orientacao)),int(Y + Comprimento*np.sin(-Orientacao)))
        start_point = (int(X),int(Y))
        thickness = 10
        cv2.arrowedLine(Campo_Virtual, start_point, end_point, Color, thickness,cv2.LINE_AA, tipLength = 0.2)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    #função para desenhar robos adversário
    def Command_Draw_Circle_Openent(self, Campo_Virtual, X, Y, Color = (255,255,0), Radius = 20):
        X = X + 900
        Y = Y + 750
        center_coordinates = (int(X),int(Y))
        thickness = 10
        cv2.circle(Campo_Virtual, center_coordinates, Radius, Color, thickness, cv2.LINE_AA)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    #função para desenhar a bola
    def Command_Draw_Ball(self, Campo_Virtual, X, Y, Color = (0,255,255), Radius = 15):
        X = X + 900
        Y = Y + 750
        center_coordinates = (int(X),int(Y))
        thickness = 20
        cv2.circle(Campo_Virtual, center_coordinates, Radius, Color, thickness, cv2.LINE_AA)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    #função para desenhar robos do time e robos adversários
    def Command_DrawAll(self, Posture_Player_1,Color_1, Posture_Player_2,Color_2, Posture_Player_3,Color_3, 
                                   Position_Oponent_1, Position_Oponent_2, Position_Oponent_3, Color_Opponent, 
                                   Position_Ball, Color_Ball):    
        Campo_Virtual = self.Img_Field_px.copy()
        
        if len(Posture_Player_1) == 3:
            self.Command_Draw_Arrow(Campo_Virtual, Posture_Player_1[0], Posture_Player_1[1], Posture_Player_1[2], Color_1)
        if len(Posture_Player_2) == 3:
            self.Command_Draw_Arrow(Campo_Virtual, Posture_Player_2[0], Posture_Player_2[1], Posture_Player_2[2], Color_2)
        if len(Posture_Player_3) == 3:
            self.Command_Draw_Arrow(Campo_Virtual, Posture_Player_3[0], Posture_Player_3[1], Posture_Player_3[2], Color_3)
        if len(Position_Oponent_1) == 2:
            self.Command_Draw_Circle_Openent(Campo_Virtual, Position_Oponent_1[0], Position_Oponent_1[1], Color_Opponent)
        if len(Position_Oponent_2) == 2:
            self.Command_Draw_Circle_Openent(Campo_Virtual, Position_Oponent_2[0], Position_Oponent_2[1], Color_Opponent)
        if len(Position_Oponent_3) == 2:
            self.Command_Draw_Circle_Openent(Campo_Virtual, Position_Oponent_3[0], Position_Oponent_3[1], Color_Opponent)
        if len(Position_Ball) == 2:
            self.Command_Draw_Ball(Campo_Virtual, Position_Ball[0], Position_Ball[1],Color_Ball)
        Campo_Virtual = cv2.resize(Campo_Virtual, (384,288))
        return Campo_Virtual
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Game_Action(self):
        # B = BALL()
        # B.Bola_X[0:, 0] = self.Var_Game_Parameters[6, 0:2]

        self.P1.rBDP_pPos_X[0:, 0] = self.Var_Game_Parameters[0, 0:]
        self.P1.rBDP_pPos_Xd[0:, 0] = self.Var_Game_Parameters[6, 0:]
        self.P1.xtil()
        self.P1.autonivel()
        self.P1.baixonivel()

        self.P2.rBDP_pPos_X[0:, 0] = self.Var_Game_Parameters[1, 0:]
        self.P2.rBDP_pPos_Xd[0:, 0] = self.Var_Game_Parameters[6, 0:]
        self.P2.xtil()
        self.P2.autonivel()
        self.P2.baixonivel()

        self.P3.rBDP_pPos_X[0:, 0] = self.Var_Game_Parameters[2, 0:]
        self.P3.rBDP_pPos_Xd[0:, 0] = self.Var_Game_Parameters[6, 0:]
        self.P3.xtil()
        self.P3.autonivel()
        self.P3.baixonivel()

        print('1: ',self.P1.rBDP_pSC_PWM[0],self.P1.rBDP_pSC_PWM[1],'2: ',self.P2.rBDP_pSC_PWM[0],self.P2.rBDP_pSC_PWM[1],'3: ',self.P3.rBDP_pSC_PWM[0],self.P3.rBDP_pSC_PWM[1])
        
        try:
            self.pEsp.write([1, 2, int(self.P1.rBDP_pSC_PWM[0,0]), int(self.P1.rBDP_pSC_PWM[1,0]), int(self.P2.rBDP_pSC_PWM[0,0]), int(self.P2.rBDP_pSC_PWM[1,0]), int(self.P3.rBDP_pSC_PWM[0,0]), int(self.P3.rBDP_pSC_PWM[1,0]), 3, 10])
            EndCycle = time.time()
            CheckTime =  EndCycle - self.StartCycle
            self.Clear_StatusBar()
            self.Set_StatusBar('Frequência de Amostragem: %f' %CheckTime)
        except:
            EndCycle = time.time()
            CheckTime =  EndCycle - self.StartCycle
            self.Clear_StatusBar()
            self.Set_StatusBar('Atenção cominicação não Foi iniciada => Frequência de Amostragem: %f' %CheckTime)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz o loop da janela 
    def Command_Run(self):
        try:
            self.Window.protocol("WM_DELETE_WINDOW", self.Command_Close_Communication)
            self.Window.mainloop()
        except:
            pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Close_Communication(self):
        try:
            self.porta.close()
            self.Window.destroy()
        except:
            self.Window.destroy()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Encerra a janela
  
    def Command_Stop(self):
        try:
            self.Window.quit()
        except:
            pass
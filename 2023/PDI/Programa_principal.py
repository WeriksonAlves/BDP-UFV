'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:Data de início: 01/05/2022 - Data de término: ?? :
:::::::::::::::::::::::::::::::::::::::::::::::::::

PLATAFORMA BDP 2023

Conjunto de janelas para as informações do sistema
Através de um conjunto de botões será possível selecionar 
as janelas que serão abertas e cada uma será correspondente às
etapas de calibração, ajuste, comunicação e jogo.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*
import sys
import tkinter as tk
import cv2
import threading
import numpy as np
from PIL import ImageTk, Image
from math import dist
#..............................................................................................................
class Plataforma(object):
    def __init__(self, **kw): 
#..............................................................................................................
# Funções relaciona a janela de configuração da Plataforma
        self.Window_Main = Tk() #Cria a janela
        self.Window_Main.title("PLATAFORMA BDP 2023") #Titulo da janela
        self.Window_Main.geometry('300x500') # Tamanho da janela
        self.Window_Main.configure(bg='#229A00') # Cor de fundo da janela
        self.Main_StatusBar_Create() # Cria a nota de rodapé
        self.Main_Menu_Create() # Menu inicial do sistema
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria a notas de rodapé
    def Main_StatusBar_Create(self): 
        self.Main_StatusBar = Label(self.Window_Main,
                               text="Painel Geral do Sistema \nEtapas a se seguir: \nInicializar a câmera \nCalibrar o sistema \nIniciar a partida",
                               bd=1, relief=SUNKEN, anchor=CENTER)
        self.Main_StatusBar.pack(side=BOTTOM, fill=X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a nota de rodapé
    def Main_StatusBar_Clear(self): 
        self.Main_StatusBar.config(text="")
        self.Main_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Atualiza a nota de rodapé
    def Main_StatusBar_Set(self, texto): 
        self.Main_StatusBar.config(text=texto)
        self.Main_StatusBar.update_idletasks()       
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Main_Menu_Create(self): # Menu inicial do sistema
        # Abre a janela de configurações da camera
        Main_Button_OpenWindowCamera = Button(self.Window_Main, text= "Câmera", command = self.Main_Command_OpenCameraWindow) 
        Main_Button_OpenWindowCamera.place(height=50, width=200, x=50, y=10)

        # Abre a janela de calibração de cores
        Main_Button_OpenWindowColors = Button(self.Window_Main, text= "Calibrar Cores", command = self.Main_Command_OpenColorsWindow)
        Main_Button_OpenWindowColors.place(height=50, width=200, x=50, y=70)

        # Abre a janela de calibração de campo
        Main_Button_OpenWindowField = Button(self.Window_Main, text= "Calibrar Campo", command = self.Main_Command_OpenFieldWindow)
        Main_Button_OpenWindowField.place(height=50, width=200, x=50, y=130)

        # Abre a janela de configurações da partida
        Main_Button_OpenWindowGame = Button(self.Window_Main, text= "Habilitar Partida", command = self.Main_Command_OpenGameWindow)
        Main_Button_OpenWindowGame.place(height=50, width=200, x=50, y=190)

        #Encerra o software
        Main_Button_CloseAll = Button(self.Window_Main, text= "Encerrar o programa", bg='grey', activebackground='red', command=self.finaliza_software)
        Main_Button_CloseAll.place(height=50, width=200, x=50, y=250)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Encerra o programa
    def finaliza_software(self):
        self.Window_Main.quit()       
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz o loop da janela ?    
    def execute(self):
        self.Window_Main.mainloop()
#..............................................................................................................
# Funções relaciona a janela de configuração da câmera
    Camer_Variable_CameraMode = 0
    def Main_Command_OpenCameraWindow(self):
        self.Window_Camera = Toplevel() # Cria a subjanela
        self.Window_Camera.title("Câmera")# Titulo da subjanela
        self.Window_Camera.geometry('300x500')# Tamanho da subjanela
        self.Window_Camera.configure(bg= '#229A00')# Cor de fundo da subjanela
        
        self.Camera_Menu_Create()# Menu inicial da subjanela
        self.Camera_StatusBar_Create()# Cria a nota de rodapé

        self.Main_StatusBar_Clear()# Limpa a nota de rodapé
        self.Main_StatusBar_Set("Configurando a câmera")# Atualiza a nota de rodapé

        self.Camera_Variable_CameraOn = False# Inicializa a câmera como desligada
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Camera_StatusBar_Create(self):
        self.Camera_StatusBar = tk.Label(self.Window_Camera,
                               text="Painel de configuração da câmera \nEtapas a se seguir: \nConectar a câmera \nVisualizar o preview",
                               bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.Camera_StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
    def Camera_StatusBar_Clear(self):
        self.Camera_StatusBar.config(text="")
        self.Camera_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Camera_StatusBar_Set(self, texto):
        self.Camera_StatusBar.config(text=texto)
        self.Camera_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Camera_Menu_Create(self):
        Camera_Button_ConnectCamera = Button(self.Window_Camera, text= "Conectar", command = self.Camera_Command_ConnectCamera)
        Camera_Button_ConnectCamera.place(height=50, width=200, x=50, y=10)

        Camera_Button_OpenPreview = Button(self.Window_Camera, text= "Abrir Preview", command = lambda: threading.Thread(target=self.Camera_Command_OpenPreview).start())
        Camera_Button_OpenPreview.place(height=50, width=200, x=50, y=70)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Camera_Command_ConnectCamera(self):
        if(self.Camera_Variable_CameraOn==False):
            self.Camera_StatusBar_Clear()
            self.Camera_StatusBar_Set("Conectando a câmera")
            self.Camera_Variable_CameraInformation = cv2.VideoCapture(self.Camer_Variable_CameraMode, cv2.CAP_DSHOW)#corrigi bug ao fechar aplicação
            self.Camera_Variable_CameraOn, self.Camera_Variable_Frames = self.Camera_Variable_CameraInformation.read() # retorna True ou False para a camera
            self.Camera_Variable_Frames = cv2.medianBlur(self.Camera_Variable_Frames,3) #Aplica um filtro de mediana
            if(self.Camera_Variable_CameraOn == True):
                self.Camera_StatusBar_Clear()
                self.Camera_StatusBar_Set("Câmera conectada com sucesso")
            else:
                self.Camera_StatusBar_Clear()
                self.Camera_StatusBar_Set("A câmera não está conectada")
        else:
            self.Camera_StatusBar_Clear()
            self.Camera_StatusBar_Set("A câmera já está conectada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Camera_Command_OpenPreview(self):
        while True:
            self.Camera_Variable_CameraOn, self.Camera_Variable_Frames = self.Camera_Variable_CameraInformation.read() # retorna True ou False para a camera
            self.Camera_Variable_Frames = cv2.medianBlur(self.Camera_Variable_Frames,3) #Aplica um filtro de mediana
            if not self.Camera_Variable_CameraOn:
                print("Câmera desativada")
                break
            cv2.imshow("preview", self.Camera_Variable_Frames)
            k = cv2.waitKey(25) #Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("preview", cv2.WND_PROP_VISIBLE) <1):
                break
        cv2.destroyAllWindows()
#..............................................................................................................
#Funções relacionadas a janela de calibração de cores
    #Colors_Variable_MatrixColor = np.zeros([7,6], dtype=np.uint8)
    Colors_Variable_MatrixColor = np.array([[170, 181, 105, 156, 137, 201],
                                            [  9,  17, 158, 213, 190, 234],
                                            [ 20,  46, 142, 231, 168, 255],
                                            [ 72,  91,  66, 131, 126, 189],
                                            [ 96, 113,  61, 123, 206, 255],
                                            [ 99, 105, 128, 181, 150, 205],
                                            [156, 168,  35,  69, 192, 225]], dtype=np.uint8)
    def Main_Command_OpenColorsWindow(self):
        self.Window_Colors = Toplevel()# Cria a subjanela de calibração de cores
        self.Window_Colors.title("Calibrar cores")# Titulo da subjanela
        self.Window_Colors.geometry('940x700')# Tamanho da subjanela
        self.Window_Colors.configure(bg= '#229A00')# Cor de fundo da subjanela

        self.Main_StatusBar_Clear()# Limpa a nota de rodapé
        self.Main_StatusBar_Set("Calibrando as cores")# Atualiza a nota de rodapé
        self.Colors_Variable_Corlor = 7
        self.Colors_StatusBar_Create()# Cria a nota de rodapé
        self.Colors_CheckBoxs_Create()# Cria os checkboxs
        self.Colors_TextInformation_Create()# Cria o texto de informação
        self.Colors_Button_Create()# Cria os botões
        self.Colors_Scale_Create()# Cria as escalas para calibração da imagem
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_StatusBar_Create(self):
        self.Colors_StatusBar = tk.Label(self.Window_Colors,
                               text="Painel de calibração de cores\nEtapas a se seguir:\nCalibrar cores\nSalvar calibração",
                               bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.Colors_StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_StatusBar_Clear(self):
        self.Colors_StatusBar.config(text="")
        self.Colors_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;    
    def Colors_StatusBar_Set(self, texto):
        self.Colors_StatusBar.config(text=texto)
        self.Colors_StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_CheckBoxs_Create(self):
        self.Colors_Variable_Red = tk.IntVar()
        Colors_Checkbutton_Red = Checkbutton(self.Window_Colors, text="Vermelho", bg="red", variable=self.Colors_Variable_Red, command=self.Colors_Command_OnlyRed)
        Colors_Checkbutton_Red.place(height=50, width=120, x=0, y=0)

        self.Colors_Variable_Orange = tk.IntVar()
        Colors_Checkbutton_Orange = Checkbutton(self.Window_Colors, text="Laranja", bg="orange", variable=self.Colors_Variable_Orange, command=self.Colors_Command_OnlyOrange)
        Colors_Checkbutton_Orange.place(height=50, width=120, x=120, y=0)

        self.Colors_Variable_Yellow = tk.IntVar()
        Colors_Checkbutton_Yellow = Checkbutton(self.Window_Colors, text="Amarelo", bg="yellow", variable=self.Colors_Variable_Yellow, command=self.Colors_Command_OnlyYellow)
        Colors_Checkbutton_Yellow.place(height=50, width=120, x=240, y=0)

        self.Colors_Variable_Green = tk.IntVar()
        Colors_Checkbutton_Green = Checkbutton(self.Window_Colors, text="Verde", bg="green", variable=self.Colors_Variable_Green, command=self.Colors_Command_OnlyGreen)
        Colors_Checkbutton_Green.place(height=50, width=120, x=360, y=0)

        self.Colors_Variable_Cyan = tk.IntVar()
        Colors_Checkbutton_Cyan = Checkbutton(self.Window_Colors, text="Ciano", bg="cyan", variable=self.Colors_Variable_Cyan, command=self.Colors_Command_OnlyCyan)
        Colors_Checkbutton_Cyan.place(height=50, width=120, x=480, y=0)

        self.Colors_Variable_Blue = tk.IntVar()
        Colors_Checkbutton_Blue = Checkbutton(self.Window_Colors, text="Azul", bg="blue", variable=self.Colors_Variable_Blue, command=self.Colors_Command_OnlyBlue)
        Colors_Checkbutton_Blue.place(height=50, width=120, x=600, y=0)

        self.Colors_Variable_Magenta = tk.IntVar()
        Colors_Checkbutton_Magenta = Checkbutton(self.Window_Colors, text="Magenta", bg="magenta", variable=self.Colors_Variable_Magenta, command=self.Colors_Command_OnlyMagenta)
        Colors_Checkbutton_Magenta.place(height=50, width=120, x=720, y=0)

        self.Colors_Variable_Gray = tk.IntVar()
        Colors_Checkbutton_Gray = Checkbutton(self.Window_Colors, text="Total", bg="gray", variable=self.Colors_Variable_Gray, command=self.Colors_Command_OnlyGray)
        Colors_Checkbutton_Gray.place(height=50, width=120, x=840, y=0)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_TextInformation_Create(self):
        Colors_Text_Matrix = Label(self.Window_Colors,text="Matriz",bg= '#229A00')
        Colors_Text_Matrix.place(height=30, width=50, x=180, y=(60))
        Colors_Text_Saturation = Label(self.Window_Colors,text="Saturação",bg= '#229A00')
        Colors_Text_Saturation.place(height=30, width=60, x=470, y=(60))
        Colors_Text_Luminosity = Label(self.Window_Colors,text="Luminosidade",bg= '#229A00')
        Colors_Text_Luminosity.place(height=30, width=80, x=750, y=(60))
        Colors_Text_SegmentedField = Label(self.Window_Colors,text="Campo Segmentado:",bg= '#229A00')
        Colors_Text_SegmentedField.place(height=20, width=120, x=15, y=(270))
        self.Colors_Text_Label = Label(self.Window_Colors)
        self.Colors_Text_Label.place(height=300, width=800, x=70, y=(300))
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Button_Create(self):
        Colors_Button_DisplayImage = Button(self.Window_Colors, text="Exibir Imagem", command= lambda: self.Colors_Command_HSV())
        Colors_Button_DisplayImage.place(height=40, width=150, x=20, y=(200))

        Colors_Button_SaveCalibration = Button(self.Window_Colors, text="Salvar Calibração", command=self.Colors_Command_LimitsMatrix)
        Colors_Button_SaveCalibration.place(height=40, width=150, x=770, y=(200))
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Scale_Create(self):
        self.Colors_Variable_VarM1 = tk.IntVar()
        self.Colors_Variable_ScaleM1 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM1, bg= '#229A00')
        self.Colors_Variable_ScaleM1.place(height=70, width=200, x=110, y=(85))
        
        self.Colors_Variable_VarM2 = tk.IntVar()
        self.Colors_Variable_ScaleM2 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM2, bg= '#229A00')
        self.Colors_Variable_ScaleM2.place(height=70, width=200, x=110, y=(120))

        self.Colors_Variable_VarM3 = tk.IntVar()
        self.Colors_Variable_ScaleS1 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM3, bg= '#229A00')
        self.Colors_Variable_ScaleS1.place(height=70, width=200, x=400, y=(85))

        self.Colors_Variable_VarM4 = tk.IntVar()
        self.Colors_Variable_ScaleS2 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM4, bg= '#229A00')
        self.Colors_Variable_ScaleS2.place(height=70, width=200, x=400, y=(120))
        
        self.Colors_Variable_VarM5 = tk.IntVar()
        self.Colors_Variable_ScaleL1 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM5, bg= '#229A00')
        self.Colors_Variable_ScaleL1.place(height=70, width=200, x=690, y=(85))
        
        self.Colors_Variable_VarM6 = tk.IntVar()
        self.Colors_Variable_ScaleL2 = Scale(self.Window_Colors, from_ = 0, to = 255, orient = "horizontal", variable= self.Colors_Variable_VarM6, bg= '#229A00')
        self.Colors_Variable_ScaleL2.place(height=70, width=200, x=690, y=(120))  
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Command_DeselectAll(self):
        self.Colors_Variable_Red.set(False)
        self.Colors_Variable_Orange.set(False)
        self.Colors_Variable_Yellow.set(False)
        self.Colors_Variable_Green.set(False)
        self.Colors_Variable_Cyan.set(False)
        self.Colors_Variable_Blue.set(False)
        self.Colors_Variable_Magenta.set(False)
        self.Colors_Variable_Gray.set(False)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def setValues(self):
        self.Colors_Variable_ScaleM1.set(0)
        self.Colors_Variable_ScaleM2.set(255)
        self.Colors_Variable_ScaleS1.set(0)
        self.Colors_Variable_ScaleS2.set(255)
        self.Colors_Variable_ScaleL1.set(0)
        self.Colors_Variable_ScaleL2.set(255)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Command_OnlyRed(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Red.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 0
    def Colors_Command_OnlyOrange(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Orange.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 1
    def Colors_Command_OnlyYellow(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Yellow.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 2
    def Colors_Command_OnlyGreen(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Green.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 3
    def Colors_Command_OnlyCyan(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Cyan.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 4
    def Colors_Command_OnlyBlue(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Blue.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 5
    def Colors_Command_OnlyMagenta(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Magenta.set(True)
        self.setValues()
        self.Colors_Variable_Corlor = 6
    def Colors_Command_OnlyGray(self):
        self.Colors_Command_DeselectAll()
        self.Colors_Variable_Gray.set(True)
        self.setValues()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Command_HSV(self):
        self.Camera_Variable_CameraOn, self.Camera_Variable_Frames = self.Camera_Variable_CameraInformation.read() #Lê a imagem
        self.Camera_Variable_Frames = cv2.medianBlur(self.Camera_Variable_Frames,3) #Aplica um filtro de mediana

        self.Camera_Variable_Frames = cv2.resize(self.Camera_Variable_Frames, [640,480])
        if(self.Colors_Variable_Corlor == 0 or self.Colors_Variable_Corlor == 1 or self.Colors_Variable_Corlor == 2 or self.Colors_Variable_Corlor == 3 or self.Colors_Variable_Corlor == 4 or self.Colors_Variable_Corlor == 5 or self.Colors_Variable_Corlor == 6):
            self.Camera_Command_SearchPositionRobot(self.Camera_Variable_Frames)#Busca a posição do robô

        self.Colors_Variable_ColorHSV = cv2.cvtColor(self.Camera_Variable_Frames, cv2.COLOR_BGR2HSV) #Colre a imagem em HSV
        
        self.Colors_Variable_LimitColorLower = np.array([self.Colors_Variable_VarM1.get(),self.Colors_Variable_VarM3.get(),self.Colors_Variable_VarM5.get()]) #Limite inferior da cor
        self.Colors_Variable_LimitColorUpper = np.array([self.Colors_Variable_VarM2.get(),self.Colors_Variable_VarM4.get(),self.Colors_Variable_VarM6.get()]) #Limite superior da cor
        
        self.Colors_Variable_ColorMask = cv2.inRange(self.Colors_Variable_ColorHSV, self.Colors_Variable_LimitColorLower, self.Colors_Variable_LimitColorUpper)#Filtra a imagem
        Colors_Variable_Kernel = np.ones((1,1), np.uint8) 
        self.Colors_Variable_ColorMask = cv2.morphologyEx(self.Colors_Variable_ColorMask, cv2.MORPH_OPEN, Colors_Variable_Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        self.Colors_Variable_ApplicationColor = cv2.bitwise_and(self.Camera_Variable_Frames,self.Camera_Variable_Frames, mask= self.Colors_Variable_ColorMask) #Aplica a mascara na imagem
        
        self.Camera_Variable_Frames = cv2.resize(self.Camera_Variable_Frames,(400,300)) #Redimensiona a imagem
        self.Colors_Variable_ApplicationColor = cv2.resize(self.Colors_Variable_ApplicationColor,(400,300))#Redimensiona a imagem
        
        self.Colors_Variable_ConcatenateH = np.concatenate((self.Camera_Variable_Frames, self.Colors_Variable_ApplicationColor), axis=1) #Concatena a imagem em horizontal         
        self.Colors_Variable_ConvertedRGB = cv2.cvtColor(self.Colors_Variable_ConcatenateH, cv2.COLOR_BGR2RGB) #Converte a imagem para RGB
        self.Colors_Variable_Image = ImageTk.PhotoImage(Image.fromarray(self.Colors_Variable_ConvertedRGB))#Converte a imagem para imagem tkinter
        
        self.Colors_Text_Label.configure(image=self.Colors_Variable_Image)#Coloca a imagem na label
        self.Colors_Text_Label.after(25, self.Colors_Command_HSV) #Executa a função a cada 25ms
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Colors_Command_LimitsMatrix(self):
        #Esta função verifica qual cor está selecionada e altera os valores da cor selecionada. Sempre que o botâo
        #"salvar cor" é pressionado a função é executado e os parametros da matriz de limites é alterada.
        self.Colors_Variable_ColorVector = [self.Colors_Variable_VarM1.get(),self.Colors_Variable_VarM2.get(),self.Colors_Variable_VarM3.get(),self.Colors_Variable_VarM4.get(),self.Colors_Variable_VarM5.get(),self.Colors_Variable_VarM6.get()]        
        if self.Colors_Variable_Red.get() ==  True:
            self.Colors_Variable_MatrixColor[0, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Orange.get() == True:
            self.Colors_Variable_MatrixColor[1, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Yellow.get() == True:
            self.Colors_Variable_MatrixColor[2, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Green.get() == True:
            self.Colors_Variable_MatrixColor[3, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Cyan.get() == True:
            self.Colors_Variable_MatrixColor[4, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Blue.get() == True:
            self.Colors_Variable_MatrixColor[5, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Magenta.get() == True:
            self.Colors_Variable_MatrixColor[6, 0:] = self.Colors_Variable_ColorVector
        elif self.Colors_Variable_Gray.get() == True:
            self.Colors_Variable_MatrixColor[7, 0:] = self.Colors_Variable_ColorVector
        print(self.Colors_Variable_MatrixColor)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    Colors_Variable_PositionRobot = []
    def Camera_Command_SearchPositionRobot(self,frame):
        #frame = cv2.imread('imagem_teste.jpeg')  
        
        #aplicar filtro medianblur
        Colors_Variable_ColorHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Colors_Variable_LimitColorLower = np.array([self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][0],self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][2],self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][4]])
        Colors_Variable_LimitColorUpper = np.array([self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][1],self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][3],self.Colors_Variable_MatrixColor[self.Colors_Variable_Corlor][5]])
        
        Colors_Variable_ColorMask = cv2.inRange(Colors_Variable_ColorHSV, Colors_Variable_LimitColorLower, Colors_Variable_LimitColorUpper)
        Colors_Variable_Kernel = np.ones((1,1), np.uint8) 
        Colors_Variable_Opening = cv2.morphologyEx(Colors_Variable_ColorMask, cv2.MORPH_OPEN, Colors_Variable_Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        Colors_Variable_Contours, Colors_Variable_Hierarchy = cv2.findContours(Colors_Variable_Opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for i in range(len(Colors_Variable_Contours)):
            Colors_Variable_Tupla = Colors_Variable_Contours[i]
            Colors_Variable_Tupla = np.asarray(Colors_Variable_Tupla)
            Colors_Variable_Mat = np.reshape(Colors_Variable_Tupla, [np.shape(Colors_Variable_Tupla)[0],np.shape(Colors_Variable_Tupla)[2]])
            Colors_Variable_Position = np.mean(np.array([[Colors_Variable_Mat.min(0)[0], Colors_Variable_Mat.min(0)[1]],[Colors_Variable_Mat.max(0)[0],Colors_Variable_Mat.max(0)[1]]]), axis=0)
            self.Colors_Variable_PositionRobot.append(Colors_Variable_Position)  
        print(len(Colors_Variable_Contours))
#..............................................................................................................
#Funções relacionadas a janela de calibração de Campo
    def Main_Command_OpenFieldWindow(self):
        self.Window_Field = Toplevel()# Cria a subjanela de calibração de campo
        self.Window_Field.title("Calibrar Campo")# Titulo da subjanela
        self.Window_Field.geometry('300x500')# Tamanho da subjanela
        self.Window_Field.configure(bg= '#229A00')# Cor de fundo da subjanela

        self.Main_StatusBar_Clear()# Limpa a nota de rodapé
        self.Main_StatusBar_Set("Calibrando o campo")# Atualiza a nota de rodapé

        self.Field_StatusBar_Create()# Cria a nota de rodapé
        self.Field_Button_Create()# Cria os botões
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_StatusBar_Create(self):
        self.Field_StatusBar = tk.Label(self.Window_Field,
                               text="Painel de calibração do campo\nEtapas a se seguir:\nCapturar e recortar a imagem\nCorrelacionar os pontos\nSalvar calibração",
                               bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.Field_StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_StatusBar_Clear(self):
        self.Field_StatusBar.config(text="")
        self.Field_StatusBar.update_idletasks()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_StatusBar_Set(self, text):
        self.Field_StatusBar.config(text=text)
        self.Field_StatusBar.update_idletasks()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Button_Create(self):
        Field_Button_CaptureImage = Button(self.Window_Field, text="Capturar Imagem", command=self.Field_Command_CaptureImage)
        Field_Button_CaptureImage.place(height=50, width=200, x=50, y=10)

        Field_Button_CorrelatePoints = Button(self.Window_Field, text="Correlacionar Pontos", command=self.Field_Command_CorrelatePoints)
        Field_Button_CorrelatePoints.place(height=50, width=200, x=50, y=70)

        Field_Button_ValidatePoints = Button(self.Window_Field, text="Validar Pontos", command=self.Field_Command_ValidatePoints)
        Field_Button_ValidatePoints.place(height=50, width=200, x=50, y=130)

        Field_Button_SaveCalibration = Button(self.Window_Field, text="Salvar Calibração", command=self.Field_Command_SaveCalibration)
        Field_Button_SaveCalibration.place(height=50, width=200, x=50, y=190)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_CaptureImage(self):
        self.Field_StatusBar_Set("Capturando imagem do campo")
        self.Field_Variable_CameraOn, self.Field_Variable_Frames = self.Camera_Variable_CameraInformation.read()
        # Atualiza a nota de rodapé
        self.Field_StatusBar_Set("Imagem capturada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    Field_Variable_Points = []
    Field_Variable_Perspective_Transformation_Matrix = []
    Field_Variable_Field_Drawing = cv2.imread('Desenho_do_campo.png')
    Field_Variable_Validate_Points = np.array([0,0])
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_CorrelatePoints(self):
        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Correlacionando pontos")

        self.Field_Variable_Points = []
        while True:
            self.Field_Variable_Frames = cv2.resize(self.Field_Variable_Frames,(640,480))
            self.Field_Variable_Field_Drawing = cv2.resize(self.Field_Variable_Field_Drawing,(640,480))
            Field_Variable_Concatenate_Images= np.concatenate((self.Field_Variable_Field_Drawing,self.Field_Variable_Frames), axis=1)

            if (len(self.Field_Variable_Points) == 8):
                Real_Points = np.float32([[self.Field_Variable_Points[0],self.Field_Variable_Points[1]], [self.Field_Variable_Points[2], self.Field_Variable_Points[3]], [self.Field_Variable_Points[4], self.Field_Variable_Points[5]], [self.Field_Variable_Points[6], self.Field_Variable_Points[7]]]) 
                Offset = np.float32([[640, 0],[640, 0],[640, 0],[640, 0]])
                Real_Points = Real_Points - Offset 
                Target = np.float32([[55, 33], [586, 33], [586, 448], [55, 448]])
                self.Field_Variable_Perspective_Transformation_Matrix = cv2.getPerspectiveTransform(Real_Points, Target)
                break
            
            cv2.imshow('Capturar pontos', Field_Variable_Concatenate_Images)
            cv2.setMouseCallback('Capturar pontos', self.Field_Command_CorrelatePoints_Mouse)
            cv2.waitKey(25)

            if (cv2.getWindowProperty('Capturar pontos', cv2.WND_PROP_VISIBLE) < 1):
                break
        
        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Pontos correlacionados")
        cv2.destroyAllWindows()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_CorrelatePoints_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.Field_Variable_Points.append(x)
            self.Field_Variable_Points.append(y)        
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_ValidatePoints_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.Field_Variable_Validate_Points[0] = x - 640
            self.Field_Variable_Validate_Points[1] = y        
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_ValidatePoints(self):
        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Validando pontos")

        while True:
            self.Field_Variable_Frames = cv2.resize(self.Field_Variable_Frames,(640,480))
            self.Field_Variable_Field_Drawing = cv2.resize(self.Field_Variable_Field_Drawing,(640,480))
            Field_Variable_Concatenate_Images1= np.concatenate((self.Field_Variable_Field_Drawing,self.Field_Variable_Frames), axis=1)

            x,y = self.Field_Command_Search_Point(self.Field_Variable_Perspective_Transformation_Matrix, self.Field_Variable_Validate_Points)
            Center_Coordinates = (int(x),int(y))
            Radius = 3
            Color = (255, 0, 0)
            Thickness = 2
            cv2.circle(Field_Variable_Concatenate_Images1, Center_Coordinates, Radius, Color, Thickness)

            cv2.imshow('Validação dos Pontos', Field_Variable_Concatenate_Images1)
            cv2.setMouseCallback('Validação dos Pontos', self.Field_Command_ValidatePoints_Mouse) 
            cv2.waitKey(25) 

            if (cv2.getWindowProperty("Validação dos Pontos", cv2.WND_PROP_VISIBLE) <1) :
                break
            
        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Ponto Validado")
        cv2.destroyAllWindows()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_Search_Point(self, Validation_Transformation_Matrix, Field_Variable_Virtual_Position):
        Field_Variable_Actual_Position_x = (Validation_Transformation_Matrix[0][0]*Field_Variable_Virtual_Position[0] + Validation_Transformation_Matrix[0][1]*Field_Variable_Virtual_Position[1] + Validation_Transformation_Matrix[0][2]) / ((Validation_Transformation_Matrix[2][0]*Field_Variable_Virtual_Position[0] + Validation_Transformation_Matrix[2][1]*Field_Variable_Virtual_Position[1] + Validation_Transformation_Matrix[2][2]))
        Field_Variable_Actual_Position_y = (Validation_Transformation_Matrix[1][0]*Field_Variable_Virtual_Position[0] + Validation_Transformation_Matrix[1][1]*Field_Variable_Virtual_Position[1] + Validation_Transformation_Matrix[1][2]) / ((Validation_Transformation_Matrix[2][0]*Field_Variable_Virtual_Position[0] + Validation_Transformation_Matrix[2][1]*Field_Variable_Virtual_Position[1] + Validation_Transformation_Matrix[2][2]))

        return Field_Variable_Actual_Position_x, Field_Variable_Actual_Position_y
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Field_Command_SaveCalibration(self):
        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Salvando calibração")

        self.Field_Variable_Definitive_Transformation_Matrix = self.Field_Variable_Perspective_Transformation_Matrix
        print(self.Field_Variable_Definitive_Transformation_Matrix)

        self.Field_StatusBar_Clear()
        self.Field_StatusBar_Set("Calibração salva")
#..............................................................................................................
#Funções relacionadas a janela de partida
    def Main_Command_OpenGameWindow(self):
        self.Window_Game = Toplevel()# Cria a subjanela de calibração de campo
        self.Window_Game.title("Tela de Jogo")# Titulo da subjanela
        self.Window_Game.geometry('940x700')# Tamanho da subjanela
        self.Window_Game.configure(bg= '#229A00')# Cor de fundo da subjanela

        self.Main_StatusBar_Clear()# Limpa a nota de rodapé
        self.Main_StatusBar_Set("Iniciando partida")# Atualiza a nota de rodapé

        self.Game_StatusBar_Create()# Cria a nota de rodapé
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Game_StatusBar_Create(self):
        self.Game_StatusBar = tk.Label(self.Window_Game,
                               text="Painel de partida\nEtapas a se seguir:\nDefinir os campo e jogadores\nIniciar a comunicação\nIniciar a partida",
                               bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.Game_StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Game_StatusBar_Clear(self):
        self.Game_StatusBar.config(text="")
        self.Game_StatusBar.update_idletasks()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Game_StatusBar_Set(self, text):
        self.Game_StatusBar.config(text=text)
        self.Game_StatusBar.update_idletasks()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    def teste(self):
        pass

#..............................................................................................................

#Colocar isto no programa principal 

def main(args):
    #Escolha qual camera será utilizada:
    #0 = webcam, 1 = realsense
    #OBS.: Conferir no gerenciador de dispositivos
    Plataforma.Camer_Variable_CameraMode = 1
    app_proc = Plataforma()
    app_proc.execute()

 

if __name__ == '__main__':
    sys.exit(main(sys.argv))

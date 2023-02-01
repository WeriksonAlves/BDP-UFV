'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem de cores.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*
from PIL import ImageTk, Image

import tkinter as tk
import cv2
import numpy as np
import os
#..............................................................................................................
# Cria a janela responsavel pelas configurações da câmera
class ColorsWindow(object):
    def __init__(self,Kernel,MedianBlur,MatrixColor,CameraInformation,FPS):
        # Variaveis principais:
        self.Var_MedianBlur = MedianBlur
        self.Var_Kernel = Kernel
        self.Var_MatrixColor = MatrixColor
        self.Var_CameraInformation = CameraInformation
        self.Var_FPS = FPS
        
        self.Var_Color = 7      
        self.Current_Folder = os.path.dirname(__file__)

        # Executa as funções
        self.Create_Window()
        self.Create_CheckButton()
        self.Create_TextInformation()
        self.Create_Button()
        self.Create_Scale()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria e configura a subjanela
    def Create_Window(self):
        self.Window = Toplevel()
        self.Window.title("Calibrar cores")
        self.Window.minsize(940, 700)
        self.Window.maxsize(940, 700)
        self.Window.configure(bg= '#229A00')

        
        # self.Colors_CheckBoxs_Create()# Cria os checkboxs
        # self.Colors_TextInformation_Create()# Cria o texto de informação
        # self.Colors_Button_Create()# Cria os botões
        # self.Colors_Scale_Create()# Cria as escalas para calibração da imagem
        
        self.StatusBar = tk.Label(self.Window,
                        text='Instruções: \nSelecionar uma cor \nExibir imagem \nCalibrar a cor desejada \nSalvar calibração',
                        bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a barra de status
    def Clear_StatusBar(self):
        self.StatusBar.config(text="")
        self.StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Sobreescreve a barra de status
    def Set_StatusBar(self, texto):
        self.StatusBar.config(text=texto)
        self.StatusBar.update_idletasks() 
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria as checkbutton de para cada cor
    def Create_CheckButton(self):
        self.Var_Red = tk.IntVar()
        Chebut_Red = Checkbutton(self.Window, text="Vermelho", bg="red", variable=self.Var_Red, command=self.Command_OnlyRed)
        Chebut_Red.place(height=50, width=120, x=0, y=0)

        self.Var_Orange = tk.IntVar()
        Chebut_Orange = Checkbutton(self.Window, text="Laranja", bg="orange", variable=self.Var_Orange, command=self.Command_OnlyOrange)
        Chebut_Orange.place(height=50, width=120, x=120, y=0)

        self.Var_Yellow = tk.IntVar()
        Chebut_Yellow = Checkbutton(self.Window, text="Amarelo", bg="yellow", variable=self.Var_Yellow, command=self.Command_OnlyYellow)
        Chebut_Yellow.place(height=50, width=120, x=240, y=0)

        self.Var_Green = tk.IntVar()
        Chebut_Green = Checkbutton(self.Window, text="Verde", bg="green", variable=self.Var_Green, command=self.Command_OnlyGreen)
        Chebut_Green.place(height=50, width=120, x=360, y=0)

        self.Var_Cyan = tk.IntVar()
        Chebut_Cyan = Checkbutton(self.Window, text="Ciano", bg="cyan", variable=self.Var_Cyan, command=self.Command_OnlyCyan)
        Chebut_Cyan.place(height=50, width=120, x=480, y=0)

        self.Var_Blue = tk.IntVar()
        Chebut_Blue = Checkbutton(self.Window, text="Azul", bg="blue", variable=self.Var_Blue, command=self.Command_OnlyBlue)
        Chebut_Blue.place(height=50, width=120, x=600, y=0)

        self.Var_Magenta = tk.IntVar()
        Chebut_Magenta = Checkbutton(self.Window, text="Magenta", bg="magenta", variable=self.Var_Magenta, command=self.Command_OnlyMagenta)
        Chebut_Magenta.place(height=50, width=120, x=720, y=0)

        self.Var_Gray = tk.IntVar()
        Chebut_Gray = Checkbutton(self.Window, text="Total", bg="gray", variable=self.Var_Gray, command=self.Command_OnlyGray)
        Chebut_Gray.place(height=50, width=120, x=840, y=0)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria os textos informativos da janela
    def Create_TextInformation(self):
        Txt_Matrix = Label(self.Window,text="Matriz",bg= '#229A00')
        Txt_Matrix.place(height=30, width=50, x=180, y=60)

        Txt_Saturation = Label(self.Window,text="Saturação",bg= '#229A00')
        Txt_Saturation.place(height=30, width=60, x=470, y=60)

        Txt_Luminosity = Label(self.Window,text="Luminosidade",bg= '#229A00')
        Txt_Luminosity.place(height=30, width=80, x=750, y=60)

        Txt_SegmentedField = Label(self.Window,text="Campo Segmentado",bg= '#229A00')
        Txt_SegmentedField.place(height=20, width=120, x=15, y=270)

        self.Txt_Label = Label(self.Window)
        self.Txt_Label.place(height=300, width=800, x=70, y=300)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria os botões na janela
    def Create_Button(self):
        But_LoadSetting = Button(self.Window, text="Carregar Calibração", command= self.Command_Loadtxt)
        But_LoadSetting.place(height=40, width=150, x=20, y=(200))

        But_DisplayImage = Button(self.Window, text="Exibir Imagem", command= lambda: self.Command_HSV())
        But_DisplayImage.place(height=40, width=150, x=395, y=(200))

        But_SaveCalibration = Button(self.Window, text="Salvar Calibração", command=self.Command_Savetxt)
        But_SaveCalibration.place(height=40, width=150, x=770, y=(200))
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria as barras deslizantes para calibragem das cores
    def Create_Scale(self):
        self.VarM1 = tk.IntVar()
        self.Sca_M1 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM1, bg= '#229A00')
        self.Sca_M1.place(height=70, width=200, x=110, y=(85))
        
        self.VarM2 = tk.IntVar()
        self.Sca_M2 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM2, bg= '#229A00')
        self.Sca_M2.place(height=70, width=200, x=110, y=(120))

        self.VarM3 = tk.IntVar()
        self.Sca_S1 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM3, bg= '#229A00')
        self.Sca_S1.place(height=70, width=200, x=400, y=(85))

        self.VarM4 = tk.IntVar()
        self.Sca_S2 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM4, bg= '#229A00')
        self.Sca_S2.place(height=70, width=200, x=400, y=(120))
        
        self.VarM5 = tk.IntVar()
        self.Sca_L1 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM5, bg= '#229A00')
        self.Sca_L1.place(height=70, width=200, x=690, y=(85))
        
        self.VarM6 = tk.IntVar()
        self.Sca_L2 = Scale(self.Window, from_ = 0, to = 255, orient = "horizontal", variable= self.VarM6, bg= '#229A00')
        self.Sca_L2.place(height=70, width=200, x=690, y=(120))  
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Desmarca todas as checkbuttons
    def Command_DeselectAll(self):
        self.Var_Red.set(False)
        self.Var_Orange.set(False)
        self.Var_Yellow.set(False)
        self.Var_Green.set(False)
        self.Var_Cyan.set(False)
        self.Var_Blue.set(False)
        self.Var_Magenta.set(False)
        self.Var_Gray.set(False)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Seleciona apenas uma cor 
    def Command_OnlyRed(self):
        self.Command_DeselectAll()
        self.Var_Red.set(True)
        self.Var_Color = 0
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyOrange(self):
        self.Command_DeselectAll()
        self.Var_Orange.set(True)
        self.Var_Color = 1
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyYellow(self):
        self.Command_DeselectAll()
        self.Var_Yellow.set(True)
        self.Var_Color = 2
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyGreen(self):
        self.Command_DeselectAll()
        self.Var_Green.set(True)
        self.Var_Color = 3
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyCyan(self):
        self.Command_DeselectAll()
        self.Var_Cyan.set(True)
        self.Var_Color = 4
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyBlue(self):
        self.Command_DeselectAll()
        self.Var_Blue.set(True)
        self.Var_Color = 5
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyMagenta(self):
        self.Command_DeselectAll()
        self.Var_Magenta.set(True)
        self.Var_Color = 6
        self.Sca_M1.set(self.Var_MatrixColor[self.Var_Color, 0])
        self.Sca_M2.set(self.Var_MatrixColor[self.Var_Color, 1])
        self.Sca_S1.set(self.Var_MatrixColor[self.Var_Color, 2])
        self.Sca_S2.set(self.Var_MatrixColor[self.Var_Color, 3])
        self.Sca_L1.set(self.Var_MatrixColor[self.Var_Color, 4])
        self.Sca_L2.set(self.Var_MatrixColor[self.Var_Color, 5])
    def Command_OnlyGray(self):
        self.Command_DeselectAll()
        self.Var_Gray.set(True)
        self.Sca_M1.set(0)
        self.Sca_M2.set(255)
        self.Sca_S1.set(0)
        self.Sca_S2.set(255)
        self.Sca_L1.set(0)
        self.Sca_L2.set(255)
        self.Var_Color = 7
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz a filtragem da cor
    def Command_HSV(self):
        _, self.Var_Frames = self.Var_CameraInformation.read() #Lê a imagem
        self.Var_Frames = cv2.medianBlur(self.Var_Frames,self.Var_MedianBlur) #Aplica um filtro de mediana

        self.Var_Frames = cv2.resize(self.Var_Frames, [640,480])
        try:
            if(self.Var_Color == 0 or self.Var_Color == 1 or self.Var_Color == 2 or self.Var_Color == 3 or self.Var_Color == 4 or self.Var_Color == 5 or self.Var_Color == 6):
                self.Command_IdColor(self.Var_Frames)
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Selecione uma cor para ser calibrada.")

        self.Var_ColorHSV = cv2.cvtColor(self.Var_Frames, cv2.COLOR_BGR2HSV) #Colre a imagem em HSV
        
        self.Var_LimitColorLower = np.array([self.VarM1.get(),self.VarM3.get(),self.VarM5.get()]) #Limite inferior da cor
        self.Var_LimitColorUpper = np.array([self.VarM2.get(),self.VarM4.get(),self.VarM6.get()]) #Limite superior da cor
        
        self.Var_ColorMask = cv2.inRange(self.Var_ColorHSV, self.Var_LimitColorLower, self.Var_LimitColorUpper)#Filtra a imagem
        Var_Kernel = self.Var_Kernel
        self.Var_ColorMask = cv2.dilate(self.Var_ColorMask, Var_Kernel, iterations=1) #testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        self.Var_ApplicationColor = cv2.bitwise_and(self.Var_Frames,self.Var_Frames, mask= self.Var_ColorMask) #Aplica a mascara na imagem
        
        self.Var_Frames = cv2.resize(self.Var_Frames,(400,300)) #Redimensiona a imagem
        self.Var_ApplicationColor = cv2.resize(self.Var_ApplicationColor,(400,300))#Redimensiona a imagem
        
        self.Var_ConcatenateH = np.concatenate((self.Var_Frames, self.Var_ApplicationColor), axis=1) #Concatena a imagem em horizontal         
        self.Var_ConvertedRGB = cv2.cvtColor(self.Var_ConcatenateH, cv2.COLOR_BGR2RGB) #Converte a imagem para RGB
        self.Var_Image = ImageTk.PhotoImage(Image.fromarray(self.Var_ConvertedRGB))#Converte a imagem para imagem tkinter
        
        self.Txt_Label.configure(image=self.Var_Image)#Coloca a imagem na label
        self.Txt_Label.after(self.Var_FPS, self.Command_HSV) #Executa a função a cada t ms
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Atualiza e salva a matriz HSV com a calibragem das cores
    def Command_Savetxt(self):
        self.Clear_StatusBar()
        self.Set_StatusBar("Salvando calibragem da cor.")

        ColorVector = [self.VarM1.get(),self.VarM2.get(),self.VarM3.get(),self.VarM4.get(),self.VarM5.get(),self.VarM6.get()]        
        if self.Var_Red.get() ==  True:
            self.Var_MatrixColor[0, 0:] = ColorVector
        elif self.Var_Orange.get() == True:
            self.Var_MatrixColor[1, 0:] = ColorVector
        elif self.Var_Yellow.get() == True:
            self.Var_MatrixColor[2, 0:] = ColorVector
        elif self.Var_Green.get() == True:
            self.Var_MatrixColor[3, 0:] = ColorVector
        elif self.Var_Cyan.get() == True:
            self.Var_MatrixColor[4, 0:] = ColorVector
        elif self.Var_Blue.get() == True:
            self.Var_MatrixColor[5, 0:] = ColorVector
        elif self.Var_Magenta.get() == True:
            self.Var_MatrixColor[6, 0:] = ColorVector
        elif self.Var_Gray.get() == True:
            self.Var_MatrixColor[7, 0:] = ColorVector

        np.savetxt(self.Current_Folder+'\MatrixHSV.txt', self.Var_MatrixColor, newline='\n')

        self.Clear_StatusBar()
        Num = self.Var_Color+1
        self.Set_StatusBar("Número de itens identificados: %d." %len(self.Contours) + "\nCalibragem da cor %d salva" %Num)
        self.Var_Color = 7
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_Loadtxt(self):
        try:
            self.Var_MatrixColor = np.loadtxt(self.Current_Folder+'\MatrixHSV.txt')
            self.Clear_StatusBar()
            self.Set_StatusBar("Calibragem carregada.")
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Arquivo não encontrado, faça uma nova calibração.")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_IdColor(self,Frame):        
        ColorHSV = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)
        LimitColorLower = np.array([self.Var_MatrixColor[self.Var_Color][0],self.Var_MatrixColor[self.Var_Color][2],self.Var_MatrixColor[self.Var_Color][4]])
        LimitColorUpper = np.array([self.Var_MatrixColor[self.Var_Color][1],self.Var_MatrixColor[self.Var_Color][3],self.Var_MatrixColor[self.Var_Color][5]])
        
        ColorMask = cv2.inRange(ColorHSV, LimitColorLower, LimitColorUpper)
        ColorMask = cv2.dilate(ColorMask, self.Var_Kernel, iterations=1) #testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        # Var_ColorMask = cv2.morphologyEx(Var_ColorMask, cv2.MORPH_OPEN, Var_Kernel)#testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        self.Contours, _ = cv2.findContours(ColorMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        self.Clear_StatusBar()
        self.Set_StatusBar("Número de itens identificados: %d." %len(self.Contours))
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz o loop da janela 
    def Command_Run(self):
        try:
            self.Window.mainloop()
        except:
            pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Encerra a janela 
    def Command_Stop(self):
        try:
            self.Window.quit()
        except:
            pass
'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem do campo.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*

import tkinter as tk
import cv2
import numpy as np
import os
#..............................................................................................................
# Cria a janela responsavel pelas configurações da câmera
class FieldWindow(object):
    def __init__(self,CamInfo,FPS):
        # Variaveis principais:
        self.Var_CameraInformation = CamInfo
        self.Var_FPS = FPS

        self.Current_Folder = os.path.dirname(__file__)
        self.Var_Target = np.ones((3,1))
        self.Var_Val_Points = np.ones((3,1))
        self.Img_Field_mm = cv2.imread(self.Current_Folder+'\Field_mm.png')
        self.Img_Field_px = cv2.imread(self.Current_Folder+'\Field_px.png')
        self.OK = False
        
        # Executa as funções
        self.Create_Window()
        self.Create_Button()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria e configura a subjanela
    def Create_Window(self):
        self.Window = Toplevel()
        self.Window.title("Calibrar Campo")
        self.Window.minsize(300, 500)
        self.Window.maxsize(300, 500)
        self.Window.configure(bg= '#229A00')

        self.StatusBar = tk.Label(self.Window,
                        text="Instruções: \nCapturar e recortar a imagem\nCorrelacionar os pontos\nSalvar calibração",
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
    # Cria os botões na janela
    def Create_Button(self):
        But_CorrelatePoints = Button(self.Window, text="Carregar Calibração", command=self.Command_Loadtxt)
        But_CorrelatePoints.place(height=50, width=200, x=50, y=10)
        
        But_CaptureImage = Button(self.Window, text="Capturar Imagem", command=self.Command_CaptureImage)
        But_CaptureImage.place(height=50, width=200, x=50, y=70)

        But_CorrelatePoints = Button(self.Window, text="Correlacionar Pontos", command=self.Command_CorrelatePoints)
        But_CorrelatePoints.place(height=50, width=200, x=50, y=130)

        But_ValidatePoints = Button(self.Window, text="Validar Pontos", command=self.Command_ValidatePoints)
        But_ValidatePoints.place(height=50, width=200, x=50, y=190)

        But_SaveCalibration = Button(self.Window, text="Salvar Calibração", command=self.Command_SaveCalibration)
        But_SaveCalibration.place(height=50, width=200, x=50, y=250)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Carrega a calibração do campo
    def Command_Loadtxt(self):
        try:
            self.Var_Perspective_Transformation_Matrix = np.loadtxt(self.Current_Folder+'\MatrixTransformação.txt')
            self.Clear_StatusBar()
            self.Set_StatusBar("Calibração carregada")
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Arquivo não encontrado, faça uma nova calibração.")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Captura a imagem atual
    def Command_CaptureImage(self):
        self.Clear_StatusBar()
        self.Set_StatusBar("Capturando imagem do campo")
        _, self.Var_Frames = self.Var_CameraInformation.read()
        self.Clear_StatusBar()
        self.Set_StatusBar("Imagem capturada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Obtem a matriz de transformação de perspectiva do campo
    def Command_CorrelatePoints(self):
        self.Clear_StatusBar()
        self.Set_StatusBar("Correlacionando pontos")

        WF = 750
        WA = 600
        HF = 650
        HA = 350
        Real_Points = np.array([[-WF,0,WF,WF,0,-WF,-WA,WA,WA,-WA],[-HF,-HF,-HF,HF,HF,HF,-HA,-HA,HA,HA],[1,1,1,1,1,1,1,1,1,1]])

        if (np.size(self.Var_Target,1) > 1):
            self.Var_Target = self.Var_Target[0:, :1]

        try:
            while True:
                Frame = cv2.resize(self.Var_Frames,(640,480))
                Field_Image = cv2.resize(self.Img_Field_mm,(640,480))
                Concatenate_Images= np.concatenate((Field_Image,Frame), axis=1)

                if (np.size(self.Var_Target,1) == 11):
                    self.Var_Perspective_Transformation_Matrix = Real_Points@np.linalg.pinv(self.Var_Target[0:, 1:])
                    break
                
                cv2.imshow('Capturar pontos', Concatenate_Images)
                cv2.setMouseCallback('Capturar pontos', self.Command_CorrelatePoints_Mouse)
                cv2.waitKey(self.Var_FPS)

                if (cv2.getWindowProperty('Capturar pontos', cv2.WND_PROP_VISIBLE) < 1):
                    break
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Capture uma imagem primeiro")
        
        self.Clear_StatusBar()
        self.Set_StatusBar("Matriz de transformação obtida.")
        cv2.destroyAllWindows()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_CorrelatePoints_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            Point = np.array([[x-640],[y],[1]])
            self.Var_Target = np.concatenate((self.Var_Target,Point),1) 
        elif event == cv2.EVENT_RBUTTONDOWN:
            if np.size(self.Var_Target,1) > 1:
                self.Var_Target = self.Var_Target[0:, 0:-1]
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ValidatePoints(self):
        self.Clear_StatusBar()
        self.Set_StatusBar("Validando calibração")

        try:
            self.IMG_Frame = cv2.resize(self.Var_Frames,(640,480))
            Img_Preview = cv2.resize(self.Img_Field_px,(640,480))
            self.Var_Concatenate_Image= np.concatenate((Img_Preview,self.IMG_Frame), axis=1)

            while True:                
                cv2.imshow('Validação dos Pontos', self.Var_Concatenate_Image)
                cv2.setMouseCallback('Validação dos Pontos', self.Command_ValidatePoints_Mouse)
                cv2.waitKey(self.Var_FPS)

                if (cv2.getWindowProperty('Validação dos Pontos', cv2.WND_PROP_VISIBLE) < 1):
                    break
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Capture uma imagem primeiro")

        if self.OK == True:
            self.Clear_StatusBar()
            self.Set_StatusBar("Calibração validada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ValidatePoints_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.Var_Val_Points[0, 0] = x - 640
            self.Var_Val_Points[1, 0] = y 

            try:
                AP = self.Var_Perspective_Transformation_Matrix@self.Var_Val_Points + np.array([[900],[750],[0]])

                self.Img_Validation = self.Img_Field_px.copy()
                cv2.circle(self.Img_Validation, (int(AP[0, 0]), int(AP[1, 0])), 15, (255, 0, 0), 10)

                Field_Image = cv2.resize(self.Img_Validation,(640,480))
                self.Var_Concatenate_Image= np.concatenate((Field_Image,self.IMG_Frame), axis=1)
                self.OK = True
            except:
                self.Clear_StatusBar()
                self.Set_StatusBar('Carregue ou faça uma calibração.')    
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_SaveCalibration(self):
        self.Clear_StatusBar()
        self.Set_StatusBar("Salvando calibração")

        np.savetxt(self.Current_Folder+'\MatrixTransformação.txt', self.Var_Perspective_Transformation_Matrix, newline='\n')

        self.Clear_StatusBar()
        self.Set_StatusBar("Calibração salva")
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
'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções relacionadas à camera.
'''
#..............................................................................................................
#Bibliotecas usadas:
from tkinter import*
from tkinter import ttk

import tkinter as tk
import cv2
import threading
#..............................................................................................................
# Cria a janela responsavel pelas configurações da câmera
class CameraWindow(object):
    def __init__(self,CameraOn,MedianBlur, FPS):
        # Variaveis principais:
        self.Var_CameraOn = CameraOn 
        self.MedianBlur = MedianBlur
        self.FPS = FPS

        self.Var_PreviewOn = False 

        # Executa as funções
        self.Create_Window()
        self.Create_Menu()
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria e configura a subjanela
    def Create_Window(self):
        self.Window = Toplevel()
        self.Window.title("Configuração da câmera")
        self.Window.minsize(300, 500)
        self.Window.maxsize(300, 500)
        self.Window.configure(bg= '#229A00')
        
        self.StatusBar = tk.Label(self.Window,
                        text="Instruções: \nSelecionar câmera \n Conectar câmera \nVisualizar o preview",
                        bd=1, relief=tk.SUNKEN, anchor=tk.CENTER)
        self.StatusBar.pack(side=tk.BOTTOM, fill=tk.X)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a barra de status
    def Clear_StatusBar(self):
        try:
            self.StatusBar.config(text="")
            self.StatusBar.update_idletasks() 
        except TclError:
            pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Sobreescreve a barra de status
    def Set_StatusBar(self, texto):
        try:
            self.StatusBar.config(text=texto)
            self.StatusBar.update_idletasks()
        except TclError:
            pass
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria o menu de opções da janela atual
    def Create_Menu(self):
        self.Var_SelectCamera = tk.StringVar()
        Var_CameraList = ('0: Webcam', '1: PC do BDP', '2: Notebook') # Procurar uma forma de pegar direto do gerenciador de dispositivos
        self.Var_ChosenCamera = ttk.Combobox(self.Window, state= 'readonly', textvariable= self.Var_SelectCamera, values= Var_CameraList, justify='center')
        self.Var_ChosenCamera.place(height= 20, width= 200, x=50, y=10)
        self.Var_SelectCamera.trace('w', self.Command_GetIndex)
        
        But_ConnectCamera = Button(self.Window, text= "Conectar", command = self.Command_ConnectCamera)
        But_ConnectCamera.place(height=50, width=200, x=50, y=40)

        But_DisconnectCamera = Button(self.Window, text= "Desconectar", command = self.Command_DisconnectCamera)
        But_DisconnectCamera.place(height=50, width=200, x=50, y=100)

        But_OpenPreview = Button(self.Window, text= "Abrir Preview", command = lambda: threading.Thread(target=self.Command_OpenPreview).start())
        But_OpenPreview.place(height=50, width=200, x=50, y=160)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_GetIndex(self, *arg):
        self.Var_CameraMode = self.Var_ChosenCamera.current()
        self.Var_CameraInformation = cv2.VideoCapture(self.Var_CameraMode, cv2.CAP_DSHOW)
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_ConnectCamera(self):
        if(self.Var_CameraOn==False):
            self.Clear_StatusBar()
            self.Set_StatusBar("Conectando a câmera")
            try:
                self.Var_CameraOn, _ = self.Var_CameraInformation.read() 
                self.Clear_StatusBar()
                self.Set_StatusBar("Câmera conectada com sucesso")
            except:
                self.Clear_StatusBar()
                self.Set_StatusBar("Falha na conexão da câmera\n Verifique a câmera")
        else:
            self.Clear_StatusBar()
            self.Set_StatusBar("A câmera já está conectada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_DisconnectCamera(self):
        if(self.Var_CameraOn==True):
            self.Clear_StatusBar()
            self.Set_StatusBar("Desconectando a câmera")
            try:
                self.Var_CameraOn = False       
                self.Clear_StatusBar()
                self.Set_StatusBar("Câmera desconectada com sucesso")
            except:
                self.Clear_StatusBar()
                self.Set_StatusBar("Falha na desconexão da câmera")
        else:
            self.Clear_StatusBar()
            self.Set_StatusBar("A câmera já está desconectada")
    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_OpenPreview(self):
        if (self.Var_CameraOn==True and self.Var_PreviewOn==False):
            try:
                self.Clear_StatusBar()
                self.Set_StatusBar("Vizualizando na janela Preview.")

                while True:
                    _, self.Var_Frames = self.Var_CameraInformation.read() # retorna True ou False para a camera
                    self.Var_Frames = cv2.medianBlur(self.Var_Frames,self.MedianBlur) #Aplica um filtro de mediana
                    cv2.imshow("Preview", self.Var_Frames)
                    cv2.waitKey(self.FPS) #Está em 25 milisegundos = 40 fps

                    self.Var_PreviewOn=True
                    
                    if (cv2.getWindowProperty("Preview", cv2.WND_PROP_VISIBLE) <1):
                        self.Clear_StatusBar()
                        self.Set_StatusBar("Sistema de visão conectado\nVá para calibração de cores")
                        self.Var_PreviewOn=False
                        break
                # cv2.destroyAllWindows()
            except:
                self.Clear_StatusBar()
                self.Set_StatusBar("Primeiro, selecione qual câmera será usada.")
        elif(self.Var_CameraOn==True and self.Var_PreviewOn==True):
            self.Clear_StatusBar()
            self.Set_StatusBar("O preview já está aberto.")
        else:
            self.Clear_StatusBar()
            self.Set_StatusBar("A câmera está desconectada.")
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
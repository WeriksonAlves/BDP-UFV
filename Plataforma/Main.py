"""
:::::::::::::::::::::::::::::::::::::::::::::::::::
Programadores: Mateus Souza e Werikson Alves   
Data de início: 01/05/2022 - Data de término: 31/01/2023
Data de revisão: ??/08/2023
:::::::::::::::::::::::::::::::::::::::::::::::::::

PLATAFORMA BDP 2023

Conjunto de janelas para as informações do sistema
Através de um conjunto de botões será possível selecionar 
as janelas que serão abertas e cada uma será correspondente às
etapas de calibração, ajuste, comunicação e jogo.
"""
# ..............................................................................................................
# Bibliotecas e scripts necessários:
from tkinter import *

from Camera.Classe_Camera import *
from Cores.Classe_Cores import *
from Campo.Classe_Campo import *
from PDI.Classe_PDI import *

import sys
import os
import numpy as np


# ..............................................................................................................
class App_BDP:
    def __init__(self):
        # Variaveis principais:
        self.Var_MedianBlur = 3
        self.Var_Kernel = np.ones((3, 3), np.uint8)
        self.Var_CameraOn = False
        self.Var_FPS = 15
        self.Var_PTM = np.ones((3, 3))
        self.Current_Folder = os.path.dirname(__file__)
        self.Var_MatrixColor = np.array(
            [
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
                [0, 255, 0, 255, 0, 255],
            ],
            dtype=np.uint8,
        )

        # Cria as classes de cada janela
        # self.WindowCamera = JanelaCamera(self.Var_CameraOn,self.Var_MedianBlur,self.Var_FPS)
        # self.WindowColors = ColorsWindow(self.Var_Kernel,self.Var_MedianBlur,self.Var_MatrixColor,self.Var_CamInfo,self.Var_FPS)
        # self.WindowField = FieldWindow(self.Var_CamInfo,self.Var_FPS)
        # self.WindowGame = JanelaPDI(self.Var_CamInfo,self.Var_FPS,self.Var_MatrixColor)

        # Executa as funções
        self.Create_Window()
        self.Create_Button()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Create_Window(self):
        self.WindowMain = Tk()  # Cria a janela
        self.WindowMain.title("PLATAFORMA BDP 2023")  # Titulo da janela
        self.WindowMain.minsize(300, 500)  # Tamanho mínimo da janela
        self.WindowMain.maxsize(300, 500)  # Tamanho máximo da janela
        self.WindowMain.configure(bg="#229A00")  # Cor de fundo da janela

        self.Main_StatusBar = Label(
            self.WindowMain,
            text="Instruções: \nInicializar a câmera \nCarregar a calibração \nIniciar a partida",
            bd=1,
            relief=SUNKEN,
            anchor=CENTER,
        )
        self.Main_StatusBar.pack(side=BOTTOM, fill=X)

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Limpa a nota de rodapé
    def Clear_StatusBar(self):
        self.Main_StatusBar.config(text="")
        self.Main_StatusBar.update_idletasks()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Atualiza a nota de rodapé
    def Set_StatusBar(self, texto):
        self.Main_StatusBar.config(text=texto)
        self.Main_StatusBar.update_idletasks()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria o menu inicial do sistema
    def Create_Button(self):
        # Abre a janela de configurações da camera
        OpenWindowCamera = Button(
            self.WindowMain, text="Câmera", command=self.Command_OpenWindowCamera
        )  # lambda: threading.Thread(target=self.Command_OpenWindowCamera).start())
        OpenWindowCamera.place(height=50, width=200, x=50, y=10)

        # Abre a janela de configurações da camera
        LoadSettings = Button(
            self.WindowMain,
            text="Carrega a última calibração",
            command=self.Command_LoadSettings,
        )
        LoadSettings.place(height=50, width=200, x=50, y=70)

        # Abre a janela de configurações da partida
        OpenWindowGame = Button(
            self.WindowMain,
            text="Habilitar Partida",
            command=self.Command_OpenGameWindow,
        )
        OpenWindowGame.place(height=50, width=200, x=50, y=130)

        # Abre a janela de calibração de cores
        OpenWindowColors = Button(
            self.WindowMain,
            text="Calibrar Cores",
            command=self.Command_OpenWindowColors,
        )
        OpenWindowColors.place(height=50, width=200, x=50, y=190)

        # Abre a janela de calibração de campo
        OpenWindowField = Button(
            self.WindowMain, text="Calibrar Campo", command=self.Command_OpenWindowField
        )
        OpenWindowField.place(height=50, width=200, x=50, y=250)

        # Encerra o software
        CloseAll = Button(
            self.WindowMain,
            text="Encerrar o programa",
            bg="grey",
            activebackground="red",
            command=self.Command_Stop,
        )
        CloseAll.place(height=50, width=200, x=50, y=310)

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_LoadSettings(self):
        try:
            self.Var_MatrixColor = np.loadtxt(
                self.Current_Folder + "\Cores\MatriZHSV.txt"
            )
            self.Var_PTM = np.loadtxt(
                self.Current_Folder + "\Campo\MatrizTransformação.txt"
            )
            self.Clear_StatusBar()
            self.Set_StatusBar("Calibragem carregada.")
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar("Arquivo não encontrado, faça uma nova calibração.")

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria a janela e as funções da camera
    def Command_OpenWindowCamera(self):
        self.WindowCamera = JanelaCamera(
            self.Var_CameraOn, self.Var_MedianBlur, self.Var_FPS
        )
        self.Clear_StatusBar()
        self.Set_StatusBar(
            "Instruções: \nInicializar a câmera: Em progresso \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
        )
        self.WindowCamera.Comando_Iniciar()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria a janela e as funções de calibragem de cores
    def Command_OpenWindowColors(self):
        try:
            self.Var_CameraOn = self.WindowCamera.Var_CameraOn
            self.Var_CamInfo = self.WindowCamera.Var_CameraInformation

            self.WindowColors = JanelaCores(
                self.Var_Kernel,
                self.Var_MedianBlur,
                self.Var_MatrixColor,
                self.Var_CamInfo,
                self.Var_FPS,
            )

            self.Clear_StatusBar()
            self.Set_StatusBar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Em progresso \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

            self.WindowColors.Comando_Iniciar()
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar(
                "Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Cria a janela de calibragem do campo
    def Command_OpenWindowField(self):
        try:
            self.Var_CameraOn = self.WindowCamera.Var_CameraOn
            self.Var_CamInfo = self.WindowCamera.Var_CameraInformation

            self.WindowField = JanelaCampo(self.Var_CamInfo, self.Var_FPS)

            self.Clear_StatusBar()
            self.Set_StatusBar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Em progresso \nIniciar a partida: Faltando"
            )

            self.WindowField.Comando_Iniciar()
        except:
            self.Clear_StatusBar()
            self.Set_StatusBar(
                "Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def Command_OpenGameWindow(self):
        # try:
            self.Var_CameraOn = self.WindowCamera.Var_CameraOn
            self.Var_CamInfo = self.WindowCamera.Var_CameraInformation

            self.WindowGame = JanelaPDI(
                self.Var_MatrixColor,
                self.Var_CamInfo,
                self.Var_FPS,
                self.Var_Kernel,
                self.Var_MedianBlur,
                self.Var_PTM,
            )

            self.Clear_StatusBar()
            self.Set_StatusBar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Feito \nIniciar a partida: Em progresso"
            )

            self.WindowGame.Comando_Iniciar()
        # except:
        #     self.Clear_StatusBar()
        #     self.Set_StatusBar(
        #         "Instruções: \nFaça ou carregue as calibrações \nda Câmera, Cores e/ou Campo"
        #     )

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Encerra o programa
    def Command_Stop(self):
        self.WindowMain.quit()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    # Faz o loop da janela ?
    def Command_Run(self):
        self.WindowMain.mainloop()


# ..............................................................................................................
# Bibliotecas usadas:
# Colocar isto no programa principal


def main(args):
    app_proc = App_BDP()
    app_proc.Command_Run()


if __name__ == "__main__":
    sys.exit(main(sys.argv))

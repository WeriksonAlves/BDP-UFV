"""
:::::::::::::::::::::::::::::::::::::::::::::::::::
Programmers: Mateus Souza and Werikson Alves   
Start date: 01/05/2022 - End date: 31/01/2023
Revision date: ??/08/2023
:::::::::::::::::::::::::::::::::::::::::::::::::::

BDP PLATFORM 2023

Set of windows for system information
Through a set of buttons it will be possible to select 
the windows that will be opened and each one will correspond to the
calibration, adjustment, communication and game stages.
"""

import tkinter as tk
import numpy as np
import os

from Camera.mainCamera import CameraConfigWindow  # Import only what's needed
# from Cores.Classe_Cores import JanelaCores
# from Campo.Classe_Campo import JanelaCampo
# from PDI.Classe_PDI import JanelaPDI

class AppBDP:
    def __init__(self):
        # Default settings and variables
        self.Var_MedianBlur = 3
        self.Var_Kernel = np.ones((3, 3), np.uint8)
        self.Var_CameraOn = False
        self.Var_FPS = 15
        self.Var_PTM = np.ones((3, 3))
        self.Current_Folder = os.path.dirname(__file__)
        self.Var_MatrixColor = np.array([
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
            [0, 255, 0, 255, 0, 255],
        ], dtype=np.uint8)

        # Create the main window
        self.create_window()
        self.create_buttons()

    def create_window(self):
        self.WindowMain = tk.Tk()
        self.WindowMain.title("PLATAFORMA BDP 2023")
        self.WindowMain.geometry("300x500")  # Use geometry to set window size
        self.WindowMain.configure(bg="#229A00")  # Use configure to set background color

        # Create a status bar
        self.Main_StatusBar = tk.Label(
            self.WindowMain,
            text="Instruções: \nInicializar a câmera \nCarregar a calibração \nIniciar a partida",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.CENTER,
        )
        self.Main_StatusBar.pack(side=tk.BOTTOM, fill=tk.X)

    def clear_status_bar(self):
        self.Main_StatusBar.config(text="")
        self.Main_StatusBar.update_idletasks()

    def set_status_bar(self, text):
        self.Main_StatusBar.config(text=text)
        self.Main_StatusBar.update_idletasks()

    def create_buttons(self):
        # Create buttons with improved formatting
        button_settings = [
            ("Câmera", self.command_open_window_camera),
            ("Carrega a última calibração", self.command_load_settings),
            ("Habilitar Partida", self.command_open_game_window),
            ("Calibrar Cores", self.command_open_window_colors),
            ("Calibrar Campo", self.command_open_window_field),
            ("Encerrar o programa", self.command_stop),
        ]

        for text, command in button_settings:
            button = tk.Button(self.WindowMain, text=text, command=command)
            button.place(height=50, width=200, x=50, y=button_settings.index((text, command)) * 60 + 10)

    def command_load_settings(self):
        try:
            self.Var_MatrixColor = np.loadtxt(os.path.join(self.Current_Folder, "Cores", "MatriZHSV.txt"))
            self.Var_PTM = np.loadtxt(os.path.join(self.Current_Folder, "Campo", "MatrizTransformação.txt"))
            self.clear_status_bar()
            self.set_status_bar("Calibragem carregada.")
        except FileNotFoundError:
            self.clear_status_bar()
            self.set_status_bar("Arquivo não encontrado, faça uma nova calibração.")

    def command_open_window_camera(self):
        self.WindowCamera = CameraConfigWindow(self.Var_CameraOn, self.Var_MedianBlur, self.Var_FPS)
        self.clear_status_bar()
        self.set_status_bar(
            "Instructions: \nInitialize camera: In progress \nCalibrate colors: Missing \nCalibrate field: Missing \nStart match: Missing"
        )
        self.WindowCamera.start()

    def command_open_window_colors(self):
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

            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Em progresso \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

            self.WindowColors.Comando_Iniciar()
        except AttributeError:
            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

    def command_open_window_field(self):
        try:
            self.Var_CameraOn = self.WindowCamera.Var_CameraOn
            self.Var_CamInfo = self.WindowCamera.Var_CameraInformation

            self.WindowField = JanelaCampo(self.Var_CamInfo, self.Var_FPS)

            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Em progresso \nIniciar a partida: Faltando"
            )

            self.WindowField.Comando_Iniciar()
        except AttributeError:
            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nInicializar a câmera: Conecte uma câmera primeiro \nCalibrar as cores: Faltando \nCalibrar o campo: Faltando \nIniciar a partida: Faltando"
            )

    def command_open_game_window(self):
        try:
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

            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nInicializar a câmera: Feito \nCalibrar as cores: Feito \nCalibrar o campo: Feito \nIniciar a partida: Em progresso"
            )

            self.WindowGame.Comando_Iniciar()
        except AttributeError:
            self.clear_status_bar()
            self.set_status_bar(
                "Instruções: \nFaça ou carregue as calibrações \nda Câmera, Cores e/ou Campo"
            )

    def command_stop(self):
        self.WindowMain.quit()

    def command_run(self):
        self.WindowMain.mainloop()

def main():
    app_proc = AppBDP()
    app_proc.command_run()

if __name__ == "__main__":
    main()

'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem do campo.
'''

# Importando bibliotecas necessárias
from tkinter import *
from math import dist
from tkinter import ttk,messagebox

from referee.referee_class import*
from Controle.Class_Control import*

from Robo_BDP.Classe_JOG import*
from Robo_BDP.Funções.Controls import *

from Estrategia.Atacante import*
from Estrategia.Defensor import*
from Estrategia.Goleiro import*

import pygame as pg
import cv2
import threading
import numpy as np
import os
# import serial
import serial.tools.list_ports
import time
import math
import itertools
import matplotlib.pyplot as plt

# Criação da janela responsável pelas configurações da partida
class JanelaPDI(object):
    player_fcn = {0: None,
                  1: None,
                  2: None}
    def __init__(self, MatrizCor, InformacoesCamera, FPS, Kernel, MedianBlur, MatrizTransfPerspectiva):
        """
        Classe responsável pela criação da janela de configurações e visualização.
        MatrizCor: Matriz contendo informações sobre as cores a serem detectadas.
        InformacoesCamera: Objeto responsável por capturar imagens da câmera.
        FPS: Taxa de quadros por segundo para a visualização das imagens da câmera.
        Kernel: Matriz de convolução utilizada em algumas operações de processamento de imagens.
        MedianBlur: Parâmetro para aplicar um filtro de mediana nas imagens.
        MatrizTransfPerspectiva: Matriz de transformação de perspectiva utilizada em algumas operações.
        """

        self.Var_InformacoesCamera = InformacoesCamera
        self.Var_FPS = FPS
        self.Var_MatrizCor = MatrizCor
        self.Var_Kernel = Kernel
        self.Var_MedianBlur = MedianBlur
        self.Var_MatrizTransfPerspectiva = MatrizTransfPerspectiva

        self.Var_Comunicacao = False
        self.Var_Jogando = False
        self.Var_TesteMecanico = False
        self.Var_Joystick = False
        self.PastaAtual = os.path.dirname(__file__)
        self.ImagemCampo_px = cv2.imread(os.path.join(self.PastaAtual, 'Campo_px.png'))
        self.Var_PosPart = np.zeros((3,7), dtype=np.float64)
        self.Sai = False
        self.Var_ConfigInfo = False
        self.rpm_list = [0,0,0,0,0,0]

        # Executa as funções de criação dos elementos da janela
        self.Criar_Janela()
        self.Criar_TextoInformacoes()
        self.Criar_CheckButton()
        self.Criar_ComboBox()
        self.Criar_Botoes()
        
        self.juiz = referee_class(HOST='224.5.23.2',PORT=10313)
        threading.Thread(target=self.juiz.message).start()
        pg.init() # Inicializa a biblioteca pg
        threading.Thread(target=self.Comando_Main).start()

    # Cria e configura a sub janela
    def Criar_Janela(self):
        self.Janela = Toplevel()
        self.Janela.title("Tela de Jogo")
        self.Janela.minsize(830, 700)
        self.Janela.maxsize(830, 700)
        self.Janela.configure(bg='#229A00')

        self.BarraDeStatus = Label(self.Janela,
                                text="Instruções: \nConfigurar os jogadores \nIniciar comunicação \nIniciar partida",
                                bd=1, relief=SUNKEN, anchor=CENTER)
        self.BarraDeStatus.pack(side=BOTTOM, fill=X)
       
    def Limpar_BarraDeStatus(self):
        """
        Limpa o texto exibido na barra de status.
        """
        try:
            self.BarraDeStatus.config(text="")
            self.BarraDeStatus.update_idletasks()
        except:
            pass

    def Atualizar_BarrraDeStatus(self, texto):
        """
        Atualiza o texto exibido na barra de status.
        :param texto: O novo texto a ser exibido na barra de status.
        """
        try:
            self.BarraDeStatus.config(text=texto)
            self.BarraDeStatus.update_idletasks()
        except: pass

    # Cria os textos informativos da janela
    def Criar_TextoInformacoes(self):
        Txt_ConfiguracoesJogo = Label(self.Janela, text="Configurações de Jogo", bg='#229A00')
        Txt_ConfiguracoesJogo.place(height=30, width=130, x=300, y=0)

        Txt_InformacoesJogadores = Label(self.Janela, text="Informações dos Jogadores", bg='#229A00')
        Txt_InformacoesJogadores.place(height=30, width=150, x=300, y=200)

        Txt_Jogador1 = Label(self.Janela, text="Jogador 1", bg='#229A00')
        Txt_Jogador1.place(height=30, width=100, x=310, y=80)

        Txt_Jogador2 = Label(self.Janela, text="Jogador 2", bg='#229A00')
        Txt_Jogador2.place(height=30, width=100, x=430, y=80)

        Txt_Jogador3 = Label(self.Janela, text="Jogador 3", bg='#229A00')
        Txt_Jogador3.place(height=30, width=100, x=550, y=80)
   
    # Cria as caixas de seleção (CheckButtons)
    def Criar_CheckButton(self):
        self.Var_EquipeAzul = IntVar()
        self.Var_EquipeAmarelo = IntVar()
        self.Var_AtacanteEsquerdo = IntVar()
        self.Var_AtacanteDireito = IntVar()

        CheBut_Configs = [
            {"text": " Azul ", "bg": "blue",   "variable": self.Var_EquipeAzul,      "command": self.Comando_EquipeAzul},
            {"text": "Amarelo", "bg": "yellow", "variable": self.Var_EquipeAmarelo,    "command": self.Comando_EquipeAmarelo},
            {"text": "<<<====", "bg": "grey",   "variable": self.Var_AtacanteEsquerdo, "command": self.Comando_AtacanteEsquerdo},
            {"text": "====>>>", "bg": "grey",   "variable": self.Var_AtacanteDireito,  "command": self.Comando_AtacanteDireito}
        ]

        Largura_widget = 120
        Altura_widget = 50
        x_Inicial = 300
        y_Final = 30
        x_Dist = 120

        for index, config in enumerate(CheBut_Configs):
            x_position = x_Inicial + index * x_Dist
            checkbutton = Checkbutton(self.Janela, **config)
            checkbutton.place(height=Altura_widget, width=Largura_widget, x=x_position, y=y_Final)

    def Comando_EquipeAzul(self):
        # Define as variáveis de equipe
        self.Var_EquipeAzul.set(True)
        self.Var_EquipeAmarelo.set(False)

        # Define a cor da minha equipe como ciano
        self.juiz.cortime = 'BLUE'
        print(f'self.juiz.cortime {self.juiz.cortime}')
        self.Var_CorMinhaEquipe = 5
        self.Var_CorMinhaEquipe_BGR = (255, 0, 0)

        # Define a cor da equipe adversária como amarelo
        self.Var_CorEquipeAdversaria = 2
        self.Var_CorEquipeAdversaria_BGR = (0, 255, 255)

    def Comando_EquipeAmarelo(self):
        # Define as variáveis de equipe
        self.Var_EquipeAzul.set(False)
        self.Var_EquipeAmarelo.set(True)

        # Define a cor da minha equipe como amarelo
        self.juiz.cortime = 'YELLOW'
        self.Var_CorMinhaEquipe = 2
        self.Var_CorMinhaEquipe_BGR = (0, 255, 255)

        # Define a cor da equipe adversária como ciano
        self.Var_CorEquipeAdversaria = 5
        self.Var_CorEquipeAdversaria_BGR = (255, 0, 0)

    def Comando_AtacanteEsquerdo(self):
        # Define as variáveis de ataque
        self.Var_AtacanteDireito.set(False)
        self.Var_AtacanteEsquerdo.set(True)

        # Define o lado do ataque como esquerdo (-1)
        self.Var_LadoAtaque = -1

    def Comando_AtacanteDireito(self):
        # Define as variáveis de ataque
        self.Var_AtacanteDireito.set(True)
        self.Var_AtacanteEsquerdo.set(False)

        # Define o lado do ataque como direito (1)
        self.Var_LadoAtaque = 1
    
    # Cria as caixas de opção de cada jogador
    def Criar_ComboBox(self):
        Lista_Funcoes = ['GK', 'DC','ST']     
        Lista_Camisas = ['Ciano', 'Magenta','Verde', 'Vermelho']

        Funcao_J1 = StringVar()
        Funcao_J2 = StringVar()
        Funcao_J3 = StringVar()

        Cor_J1_1 = StringVar()
        Cor_J2_1 = StringVar()
        Cor_J3_1 = StringVar()

        Cor_J1_2 = StringVar()
        Cor_J2_2 = StringVar()
        Cor_J3_2 = StringVar()

        self.Var_J1_Funcao = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Funcao_J1, values= Lista_Funcoes, justify= 'center')
        self.Var_J1_Funcao.place(height= 20, width= 100, x= 310, y= 110)        
        self.Var_J2_Funcao = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Funcao_J2, values= Lista_Funcoes, justify= 'center')
        self.Var_J2_Funcao.place(height= 20, width= 100, x= 430, y= 110)        
        self.Var_J3_Funcao = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Funcao_J3, values= Lista_Funcoes, justify= 'center')
        self.Var_J3_Funcao.place(height= 20, width= 100, x= 550, y= 110)

        
        self.Var_J1_Cor_1 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J1_1, values= Lista_Camisas, justify= 'center')
        self.Var_J1_Cor_1.place(height= 20, width= 100, x= 310, y= 140)
        self.Var_J2_Cor_1 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J2_1, values= Lista_Camisas, justify= 'center')
        self.Var_J2_Cor_1.place(height= 20, width= 100, x= 430, y= 140)
        self.Var_J3_Cor_1 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J3_1, values= Lista_Camisas, justify= 'center')
        self.Var_J3_Cor_1.place(height= 20, width= 100, x= 550, y= 140)

        self.Var_J1_Cor_2 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J1_2, values= Lista_Camisas, justify= 'center')
        self.Var_J1_Cor_2.place(height= 20, width= 100, x= 310, y =170)
        self.Var_J2_Cor_2 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J2_2, values= Lista_Camisas, justify= 'center')
        self.Var_J2_Cor_2.place(height= 20, width= 100, x= 430, y= 170)
        self.Var_J3_Cor_2 = ttk.Combobox(self.Janela, state= 'readonly', textvariable= Cor_J3_2, values= Lista_Camisas, justify= 'center')
        self.Var_J3_Cor_2.place(height= 20, width= 100, x= 550, y= 170)

    # Cria os botões na janela
    def Criar_Botoes(self):
        But_SalvarCalibracao = Button(self.Janela, text="Salvar\nConfiguração", command=self.Comando_SalvarConfiguracao)
        But_SalvarCalibracao.place(height=50, width=200, x=50, y=10)

        But_CarregarCalibracao = Button(self.Janela, text="Carregar\nConfiguração", command=self.Comando_CarregarConfiguracao)
        But_CarregarCalibracao.place(height=50, width=200, x=50, y=70)

        But_IniciarComunicacao = Button(self.Janela, text="Abrir/Fechar \nComunicação", command=self.Comando_IniciarComunicacao)
        But_IniciarComunicacao.place(height=50, width=200, x=50, y=130)

        # But_Joystick = Button(self.Janela, text="Ativar Sistema", command=lambda: threading.Thread(target=self.Comando_Main).start())
        # But_Joystick.place(height=50, width=200, x=50, y=190)

        But_IniciarPartida = Button(self.Janela, text="Iniciar Partida", command=self.Comando_IniciarPartida)
        But_IniciarPartida.place(height=50, width=200, x=50, y=190)

        self.But_PararPartida = Button(self.Janela, text="Parar Partida", command=self.Comando_EncerrarPartida)
        self.But_PararPartida.place(height=50, width=200, x=50, y=250)

        But_Sistema = Button(self.Janela, text="Ativar joystick", command= self.Comando_joystick)
        But_Sistema.place(height=50, width=200, x=50, y=310)

        But_TesteMecanico = Button(self.Janela, text="Teste Mecânico", command=lambda: threading.Thread(target=self.Comando_TesteMecanico).start())
        But_TesteMecanico.place(height=50, width=200, x=50, y=370)

        But_VisualizarCamera = Button(self.Janela, text="Ver Câmera", command=lambda: threading.Thread(target=self.Comando_VisualizarCamera).start())
        But_VisualizarCamera.place(height=50, width=200, x=50, y=430)

        But_VisualizarSegmentacao = Button(self.Janela, text="Ver Segmentação", command=lambda: threading.Thread(target=self.Comando_VisualizarSegmentacao).start())
        But_VisualizarSegmentacao.place(height=50, width=200, x=50, y=490)

        But_VisualizarAssociacao = Button(self.Janela, text="Ver Associação", command=lambda: threading.Thread(target=self.Comando_VisualizarAssociacao).start())
        But_VisualizarAssociacao.place(height=50, width=200, x=50, y=550)
    '''Funções para configurações da janela: Fim'''











    '''Funções para configurações de jogo: inicio'''
    def Comando_SalvarConfiguracao(self):
        # Cria a matriz de configurações de jogo
        self.Var_ConfiguracoesJogo = np.array([[self.Var_J1_Funcao.current(), self.Var_J1_Cor_1.current(), self.Var_J1_Cor_2.current()],
                                               [self.Var_J2_Funcao.current(), self.Var_J2_Cor_1.current(), self.Var_J2_Cor_2.current()],
                                               [self.Var_J3_Funcao.current(), self.Var_J3_Cor_1.current(), self.Var_J3_Cor_2.current()],
                                               [self.Var_EquipeAzul.get(),    self.Var_EquipeAmarelo.get(), 0],
                                               [self.Var_AtacanteEsquerdo.get(), self.Var_AtacanteDireito.get(),0]])

        # Verifica se a matriz de configurações está completa e se as seleções das equipes e atacantes foram feitas
        Matriz = self.Comando_Salvar_Carregar()
        
        if ((-1 in Matriz) == False) and ((self.Var_EquipeAzul.get() == True) or (self.Var_EquipeAmarelo.get() == True)) and ((self.Var_AtacanteEsquerdo.get() == True) or (self.Var_AtacanteDireito.get() == True)):
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus("Salvando calibração")

            # Salva as configurações no arquivo 'Game_Settings.txt'
            np.savetxt(self.PastaAtual + '\Game_Settings.txt', self.Var_ConfiguracoesJogo, newline='\n')
            
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus('As configurações foram salvas. \nInicie a comunicação.')
        else:
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus('Complete todos os \ncampos antes de salvar.')
   
    # Carrega a configuração
    def Comando_CarregarConfiguracao(self):
        try:
            # Carrega as configurações do arquivo 'Game_Settings.txt'
            self.Var_ConfiguracoesJogo = np.loadtxt(self.PastaAtual + '\Game_Settings.txt', dtype=int)
            self.Var_J1_Funcao.current(self.Var_ConfiguracoesJogo[0][0])
            self.Var_J1_Cor_1.current(self.Var_ConfiguracoesJogo[0][1])
            self.Var_J1_Cor_2.current(self.Var_ConfiguracoesJogo[0][2])

            self.Var_J2_Funcao.current(self.Var_ConfiguracoesJogo[1][0])
            self.Var_J2_Cor_1.current(self.Var_ConfiguracoesJogo[1][1])
            self.Var_J2_Cor_2.current(self.Var_ConfiguracoesJogo[1][2])

            self.Var_J3_Funcao.current(self.Var_ConfiguracoesJogo[2][0])
            self.Var_J3_Cor_1.current(self.Var_ConfiguracoesJogo[2][1])
            self.Var_J3_Cor_2.current(self.Var_ConfiguracoesJogo[2][2])

            # Verifica qual equipe foi selecionada e atualiza a seleção
            if self.Var_ConfiguracoesJogo[3][0] == 1:
                self.Comando_EquipeAzul()
            elif self.Var_ConfiguracoesJogo[3][1] == 1:
                self.Comando_EquipeAmarelo()
            else:
                print('Erro 1')

            # Verifica qual atacante foi selecionado e atualiza a seleção
            if self.Var_ConfiguracoesJogo[4][0] == 1:
                self.Comando_AtacanteEsquerdo()
            elif self.Var_ConfiguracoesJogo[4][1] == 1:
                self.Comando_AtacanteDireito()
            else:
                print('Erro 2')

            _ = self.Comando_Salvar_Carregar()

            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus("Calibração carregada.")
        except:
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus("Arquivo não encontrado, faça uma nova calibração.")
    
    def Comando_Salvar_Carregar(self):    
        # Cria uma matriz de configuração de camisas
        Matriz = np.array([[self.Var_J1_Funcao.current(), self.Var_J1_Cor_1.current(), self.Var_J1_Cor_2.current()],
                           [self.Var_J2_Funcao.current(), self.Var_J2_Cor_1.current(), self.Var_J2_Cor_2.current()],
                           [self.Var_J3_Funcao.current(), self.Var_J3_Cor_1.current(), self.Var_J3_Cor_2.current()]])

        # Inicializa arrays para as cores das camisas e cores em formato BGR
        self.CoresCamisas = np.zeros([3, 12])
        self.CorCamisa_BGR = np.zeros([3, 6])
        
        for linha in range(len(Matriz)):
            if Matriz[linha][1] == 0:  # Ciano
                self.CoresCamisas[linha][:6] = self.Var_MatrizCor[4][0:]
                self.CorCamisa_BGR[linha][:3] = (255, 255, 0)            
            elif Matriz[linha][1] == 1:  # Magenta
                self.CoresCamisas[linha][:6] = self.Var_MatrizCor[6][0:]
                self.CorCamisa_BGR[linha][:3] = (238, 130, 238)  
            elif Matriz[linha][1] == 2:  # Verde
                self.CoresCamisas[linha][:6] = self.Var_MatrizCor[3][0:]
                self.CorCamisa_BGR[linha][:3] = (0, 255, 0)  
            elif Matriz[linha][1] == 3:  # Vermelho
                self.CoresCamisas[linha][:6] = self.Var_MatrizCor[0][0:]
                self.CorCamisa_BGR[linha][:3] = (0, 0, 255) 

            if Matriz[linha][2] == 0:  # Ciano
                self.CoresCamisas[linha][6:] = self.Var_MatrizCor[4][0:]
                self.CorCamisa_BGR[linha][3:] = (255, 255, 0)            
            elif Matriz[linha][2] == 1:  # Magenta
                self.CoresCamisas[linha][6:] = self.Var_MatrizCor[6][0:]
                self.CorCamisa_BGR[linha][3:] = (238, 130, 238)  
            elif Matriz[linha][2] == 2:  # Verde
                self.CoresCamisas[linha][6:] = self.Var_MatrizCor[3][0:]
                self.CorCamisa_BGR[linha][3:] = (0, 255, 0)  
            elif Matriz[linha][2] == 3:  # Vermelho
                self.CoresCamisas[linha][6:] = self.Var_MatrizCor[0][0:]
                self.CorCamisa_BGR[linha][3:] = (0, 0, 255)
            
        # Cria os objetos dos robôs da minha equipe (J1, J2 e J3) com as configurações obtidas
        self.P1 = Player(1,self.Var_LadoAtaque, Matriz[0,0])
        self.P2 = Player(2,self.Var_LadoAtaque, Matriz[1,0])
        self.P3 = Player(3,self.Var_LadoAtaque, Matriz[2,0])
        self.B = Ball()

        self.P1.rSetPose([[-.6], [.685], [0], [0]])
        self.P2.rSetPose([[-.4], [.685], [0], [0]])
        self.P3.rSetPose([[-.2], [.685], [0], [0]])

        self.Var_ConfigInfo = True

        players_fcn = {1: self.P1,
                       2: self.P2,
                       3: self.P3}
        
        for idx, J in enumerate([self.Var_J1_Funcao.current(),self.Var_J2_Funcao.current(),self.Var_J3_Funcao.current()]):
            print(idx, J)
            self.player_fcn[J] = players_fcn[idx + 1]
        
        return Matriz
    
    # Procura e conecta o transmissor
    def Comando_IniciarComunicacao(self, tsim=2):
        try:
            # Detecta automaticamente a porta COM do dispositivo ESP
            porta_serial = self.Detectar_Porta_Serial_ESP()

            if porta_serial is None:
                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus("Dispositivo ESP não encontrado")
                return

            # Inicia a comunicação com o dispositivo serial na porta detectada e define o timeout para 2 segundos
            self.pEsp = serial.Serial(porta_serial, 115200, timeout=2)

            if not self.Var_Comunicacao:
                self.pEsp.close()
                self.pEsp.open()

                # Envia comandos para o dispositivo serial com base no tempo simulado (tsim)
                start = time.time()
                while True:
                    t = time.time() - start

                    self.pEsp.write(b'200,-200,200,-200,200,-200\n') #Direita esquerda
                    if t > tsim:
                        self.pEsp.write(b'0,0,0,0,0,0\n')
                        break

                # start = time.time()
                # while True:
                #     t = time.time() - start

                #     self.pEsp.write(b'-200,200,-200,200,-200,200\n') #Direita esquerda
                #     if t > tsim:
                #         self.pEsp.write(b'0,0,0,0,0,0\n')
                #         break

                # Ativa a variável de controle de comunicação e atualiza a barra de status
                self.Var_Comunicacao = True
                
                self.P1.pFlag.Connected = True; 
                self.P2.pFlag.Connected = True; 
                self.P3.pFlag.Connected = True; 

                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus("Comunicação Iniciada")
        except:
            try:
                # Fecha a comunicação serial e desativa a variável de controle de comunicação
                self.pEsp.close()
                self.Var_Comunicacao = False
                self.P1.pFlag.Connected = False; 
                self.P2.pFlag.Connected = False; 
                self.P3.pFlag.Connected = False; 
                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus("Comunicação Encerrada")
            except:
                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus("Conecte o transmissor")
    
    def Detectar_Porta_Serial_ESP(self):
        # Lista todas as portas seriais disponíveis
        portas_disponiveis = list(serial.tools.list_ports.comports())
        # Procura por uma porta que contenha "ESP" no nome
        for porta in portas_disponiveis:            
            if "USB TO UART" in porta.description.upper():
                return porta.device  # Retorna o nome da porta COM
        return None  # Retorna None se o dispositivo ESP não for encontrado
    '''Funções para configurações de jogo: fim'''









    '''Funções para comandar o robo em campo: inicio'''
    def Comando_TesteMecanico(self):
        if self.Var_Joystick or self.Var_Jogando: return None
        print('Teste Mecânico')
        self.Var_TesteMecanico = True
    
    def Comando_Main(self):        
        tempo = self.tic()
        while True: 
            if self.Var_ConfigInfo:
                self.Obter_DadosJogo()
                # self.Comando_AutoPosicionamento()

            if self.Sai == True:
                print('Sai')
                break

            if self.Var_Jogando or self.juiz.play:
                self.Var_Joystick = False
                self.Var_TesteMecanico = False

                if tempo > ((self.P1.pPar.Ts + self.P2.pPar.Ts + self.P3.pPar.Ts)/3): # self.Tempo_PDI:
                    # print('X1: [%.3f, %.3f, %.3f], X2: [%.3f, %.3f, %.3f], X3: [%.3f, %.3f, %.3f], tPDI: %.3f, t_ctrl: %.3f, ' 
                    #     %(self.P1.pPos.X[0,0],self.P1.pPos.X[1,0],self.P1.pPos.X[5,0],
                    #       self.P2.pPos.X[0,0],self.P2.pPos.X[1,0],self.P2.pPos.X[5,0],
                    #       self.P3.pPos.X[0,0],self.P3.pPos.X[1,0],self.P3.pPos.X[5,0],
                    #       self.Tempo_PDI, self.toc(tempo)), end='')
                    
                    tempo = self.tic()
                    self.InicioCiclo = self.tic()

                    self.B.pPos.Xc[[0,1,5]] = self.Var_PosPart.T[[0]].T
                    self.P1.pPos.Xc[[0,1,5]] = self.Var_PosPart.T[[1]].T
                    self.P2.pPos.Xc[[0,1,5]] = self.Var_PosPart.T[[2]].T
                    self.P3.pPos.Xc[[0,1,5]] = self.Var_PosPart.T[[3]].T
                    
                    self.B.bGetSensorData()
                    self.P1.rGetSensorData()
                    self.P2.rGetSensorData()
                    self.P3.rGetSensorData()                       
                    
                    self.Comando_AutoPosicionamento()

                    self.P1.rSendControlSignals()
                    self.P2.rSendControlSignals()
                    self.P3.rSendControlSignals()                   

                    self.rpm_list = [int(self.P1.pSC.RPM[[0]]),int(self.P1.pSC.RPM[[1]]),int(self.P2.pSC.RPM[[0]]),int(self.P2.pSC.RPM[[1]]),int(self.P3.pSC.RPM[[0]]),int(self.P3.pSC.RPM[[1]])]
                    #self.rpm_list = [100,100 ,0,0, 0,0]
                    self.send_rpm()
                
                
            elif self.Var_Joystick == True:
                # Inicializa os robôs(pode dar erro pq a gente tem q fornecer alguns parâmetros, verifica isso por favor)
                robots = [self.P1,self.P2,self.P3]
                print('Joystick')

                # Captura os joysticks
                joysticks = []
                for i in range(pg.joystick.get_count()):
                    joystick = pg.joystick.Joystick(i)
                    joystick.init()
                    joysticks.append(joystick)

                Ctrl_Joystick = MY_JOYSTICK()

                while self.Var_Joystick == True:
                    self.Var_Jogando = False
                    self.InicioCiclo = self.tic()                    

                    # Captura eventos dos joysticks
                    for event in pg.event.get():
                        
                        if event.type == pg.JOYAXISMOTION:
                            # Lê os valores dos joysticks
                            Ctrl_Joystick.check_analog(joysticks, robots)

                        if event.type == pg.JOYBUTTONDOWN:

                                if event.button == 4:
                                    # print('LB')
                                    Ctrl_Joystick.check_LT(joysticks, robots)
                                if event.button == 5:
                                    # print('RB')
                                    Ctrl_Joystick.check_RT(joysticks, robots)  
                            
                    # Aguarda um tempo para evitar sobrecarga do processador(pode tirar se quiser)
                    self.send_rpm()

            elif self.Var_TesteMecanico == True:
                def Comando_DesenhaTeste(XP1,CP1,XdP1,CdP1,  XP2,CP2,XdP2,CdP2,  XP3,CP3,XdP3,CdP3):
                    Campo_Virtual = self.ImagemCampo_px.copy()
                    self.Comando_DesenhaSeta(Campo_Virtual, XP1, CP1[:3], CP1[3:])
                    self.Comando_DesenhaCirculo(Campo_Virtual, XdP1, CdP1, raio=20)

                    self.Comando_DesenhaSeta(Campo_Virtual, XP2, CP2[:3], CP2[3:])
                    self.Comando_DesenhaCirculo(Campo_Virtual, XdP2, CdP2, raio=20)
                    
                    self.Comando_DesenhaSeta(Campo_Virtual, XP3, CP3[:3], CP3[3:])
                    self.Comando_DesenhaCirculo(Campo_Virtual, XdP3, CdP3, raio=20)

                    Campo_Virtual = cv2.resize(Campo_Virtual, [640, 480])
                    return Campo_Virtual

                ''' Variables initialization '''
                Rx = 0.2
                Ry = 0.5
                tsim = 30 # Tempo total da simulação
                nvoltas = 4
                w = (nvoltas*np.pi/(tsim/2))

                ''' Initial Position'''
                self.P1.rSetPose(np.array([[-0.5, 0, 0, 0]],dtype=np.float64).T)  
                self.P2.rSetPose(np.array([[0, 0, 0, 0]],dtype=np.float64).T)
                self.P3.rSetPose(np.array([[0.5, 0, 0, 0]],dtype=np.float64).T)

                # Tempo de esperar para início do experimento/simulação
                print('\nInício..............\n\n')
                time.sleep(1)

                '''Temporizadores'''
                tap = 0.05 # taxa de atualização do robo
                t = self.tic()   # Tempo atual
                tc = self.tic()  # Tempo de controle
                tp = self.tic()  # Tempo para plotar

                # Simulação em tempo real
                while self.toc(t) < tsim:
                    if self.toc(tc) > tap:
                        tc = self.tic() 
                        self.InicioCiclo = self.tic()
                        '-----------------------------------------------------'
                        # Data aquisition
                        if self.Var_Comunicacao:
                            self.P1.pPos.X[[0,1,5]] = self.Var_PosPart.T[[1]].T
                            self.P2.pPos.X[[0,1,5]] = self.Var_PosPart.T[[2]].T
                            self.P3.pPos.X[[0,1,5]] = self.Var_PosPart.T[[3]].T
                        
                        self.P1.rGetSensorData()
                        self.P2.rGetSensorData()
                        self.P3.rGetSensorData()
                        '-----------------------------------------------------'
                        # Posicionamento Lemniscata
                        if self.toc(t) > 48:
                            self.B.pPos.X[[0,1]] = np.array([[0],[0]])
                        elif self.toc(t) > 36:
                            self.B.pPos.X[[0,1]] = np.array([[-.375],[-.400]])
                        elif self.toc(t) > 24:
                            self.B.pPos.X[[0,1]] = np.array([[-.375],[.400]])
                        elif self.toc(t) > 12:
                            self.B.pPos.X[[0,1]] = np.array([[.375],[-.400]])
                        else:
                            self.B.pPos.X[[0,1]] = np.array([[.375],[.400]])

                        #Definir a estrategia
                        self.P1.pPos.Xd[[0,1]] = self.B.pPos.X[[0,1]]
                        self.P2.pPos.Xd[[0,1]] = self.B.pPos.X[[0,1]]
                        self.P3.pPos.Xd[[0,1]] = self.B.pPos.X[[0,1]]
                        '-----------------------------------------------------'
                        self.P1 = f1(self.P1)
                        self.P2 = f1(self.P2)
                        self.P3 = f1(self.P3)
                        '-----------------------------------------------------'
                        self.P1.rSendControlSignals()
                        self.P2.rSendControlSignals()
                        self.P3.rSendControlSignals()

                        if self.Var_Comunicacao:
                            self.rpm_list = [int(self.P1.pSC.RPM[[0]]),int(self.P1.pSC.RPM[[1]]),int(self.P2.pSC.RPM[[0]]),int(self.P2.pSC.RPM[[1]]),int(self.P3.pSC.RPM[[0]]),int(self.P3.pSC.RPM[[1]])]
                            self.send_rpm()
                        
                        #print('X2: [%.3f, %.3f, %.3f], Xd: [%.3f, %.3f, %.3f], ' 
                        #        %(self.P2.pPos.X[0,0],self.P2.pPos.X[1,0],self.P2.pPos.X[2,0],
                        #        self.P2.pPos.Xd[0,0],self.P2.pPos.Xd[1,0],self.P2.pPos.Xd[2,0]), end='')
                       # print(f'Players [1D,1E,2D,2E,3D,3E] ==> {self.rpm_list}')
                    '-----------------------------------------------------'
                    
                    # Desenha o robo na tela   
                    if self.toc(tp) > tap:
                        tp = self.tic()
                        Campo_Virtual = Comando_DesenhaTeste(self.P1.pPos.Xc[[0,1,5]], self.CorCamisa_BGR[0], self.P1.pPos.Xd[[0,1,5]],[0,255,255],
                                                            self.P2.pPos.Xc[[0,1,5]], self.CorCamisa_BGR[1], self.P2.pPos.Xd[[0,1,5]],[255,0,255],
                                                            self.P3.pPos.Xc[[0,1,5]], self.CorCamisa_BGR[2], self.P3.pPos.Xd[[0,1,5]],[255,255,0])                    
                        cv2.imshow("Teste do Controle e Mecanica", Campo_Virtual)
                        cv2.waitKey(self.Var_FPS) # Está em 25 milisegundos = 40 fps
                        if (cv2.getWindowProperty("Teste do Controle e Mecanica", cv2.WND_PROP_VISIBLE) < 1):
                            self.Var_TesteMecanico = False
                            break  
                    
                #Destroi a imagem quando termina
                if self.toc(t) >= tsim: 
                    cv2.destroyWindow('Teste do Controle e Mecanica')
                    self.Var_TesteMecanico = False

                '-----------------------------------------------------'
                #  Stop robot
                self.P1.pSC.Ud = np.array([[0],[0]])         # Zera velocidades do robô
                self.P2.pSC.Ud = np.array([[0],[0]])
                self.P3.pSC.Ud = np.array([[0],[0]])

                self.P1.rSendControlSignals()
                self.P2.rSendControlSignals()
                self.P3.rSendControlSignals()

                if self.Var_Comunicacao:
                    self.rpm_list[:2] = [int(self.P1.pSC.RPM[[0]]),int(self.P1.pSC.RPM[[1]])]
                    self.rpm_list[2:4] = [int(self.P2.pSC.RPM[[0]]),int(self.P2.pSC.RPM[[1]])]
                    self.rpm_list[4:] = [int(self.P3.pSC.RPM[[0]]),int(self.P3.pSC.RPM[[1]])]      
                    self.send_rpm()

                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus('Treino Encerrado')

    def Comando_IniciarPartida(self):
        if self.Var_Joystick: return None
        print('Partida')
        self.Var_Jogando = True
        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus("Partida Iniciada")

    def Comando_EncerrarPartida(self):
        self.Var_Jogando = False
        self.Var_Joystick = False
        self.Var_TesteMecanico = False
        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus("Partida/Treino Parado")
    
    def send_rpm(self):
        try:            
           #print(f'[1D,1E,2D,2E,3D,3E] {self.rpm_list}')
           self.pEsp.write(self.__conver2byte(self.rpm_list))
        #    EndCycle = time.time()
        #    TempoVerificacao = EndCycle - self.InicioCiclo
           self.Limpar_BarraDeStatus()
           self.Atualizar_BarrraDeStatus('Partida Iniciada.\nFrequência de Amostragem: %.4f' % self.toc(self.InicioCiclo))
        except:
            # EndCycle = time.time()
            # TempoVerificacao = EndCycle - self.InicioCiclo
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus('Partida Iniciada.\nAtenção cominicação não Foi iniciada \nFrequência de Amostragem: %.4f' % self.toc(self.InicioCiclo))

    def Comando_joystick(self):
        if self.Var_Jogando or self.juiz.play: return None
        self.Var_Joystick = True
        print('Joy')
            
    def Comando_AutoPosicionamento(self):
        if self.juiz.kickoff: # Tiro livre
            print(f'Kickoff: True, Favoravel: {self.juiz.favorable}')
            if self.Var_LadoAtaque == -1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[ .675],[ .000],[np.pi/2]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .000],[ .000],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.175],[ .000],[np.pi]])
                elif not self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .600],[-.250],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .600],[ .250],[np.pi]])
                else: print('Erro em favoravel')
            
            elif self.Var_LadoAtaque == 1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[-.675],[ .000],[np.pi/2]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .000],[ .000],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .175],[ .000],[0]])
                elif not self.juiz.favorable:    
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[-.600],[-.250],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.600],[ .250],[0]])
                else: print('Erro em favoravel')
            
            else:print('Erro em kickoff')

            self.player_fcn[0] = autonomos_pos_gk(self.player_fcn[0])
            self.player_fcn[1] = autonomos_pos(self.player_fcn[1],self.player_fcn[2],[1.5,.09])
            self.player_fcn[2] = autonomos_pos(self.player_fcn[2],self.player_fcn[1],[1.5,.09])

        elif self.juiz.penalty:
            print(f'Penalty: True, Favoravel: {self.juiz.favorable}')
            if self.Var_LadoAtaque == -1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[.650],[0],[np.pi/2]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .160],[-.370],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[],[.0],[np.pi]])
                elif not self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .175],[-.40],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .175],[ .40],[np.pi]])

            elif self.Var_LadoAtaque == 1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[-.750],[0],[np.pi/2]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[-.275],[.0],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .275],[.0],[0]])
                elif not self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[-.175],[-.40],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.175],[ .40],[0]])

            else: print('Erro no lado de ataque')
            
            self.player_fcn[0] = autonomos_pos_gk(self.player_fcn[0])
            self.player_fcn[1] = autonomos_pos(self.player_fcn[1],self.player_fcn[2],[1.5,.09])
            self.player_fcn[2] = autonomos_pos(self.player_fcn[2],self.player_fcn[1],[1.5,.09])

        elif self.juiz.goalkick:
            print(f'Goalkick: True, Favoravel: {self.juiz.favorable}')
            if self.Var_LadoAtaque == -1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[.675],[0],[np.pi]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .575],[-.400],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .375],[ .400],[np.pi]])
                elif not self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[ .100],[-.400],[np.pi]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .000],[ .400],[np.pi]])

            elif self.Var_LadoAtaque == 1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = np.array([[-.675],[0],[0]])
                if self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[-.575],[ .400],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.375],[-.400],[0]])
                elif not self.juiz.favorable:
                    self.player_fcn[1].pPos.Xd[[0,1,5]] = np.array([[-.100],[-.400],[0]])
                    self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .000],[ .400],[0]])

            else: print('Erro no lado de ataque')
            
            self.player_fcn[0] = autonomos_pos_gk(self.player_fcn[0])
            self.player_fcn[1] = autonomos_pos(self.player_fcn[1],self.player_fcn[2],[1.5,.09])
            self.player_fcn[2] = autonomos_pos(self.player_fcn[2],self.player_fcn[1],[1.5,.09])
        
        elif self.juiz.freeball:
            # print(f'Freball: True, Quadrante: {self.juiz.quadrante} ',end='')
            
            if self.Var_LadoAtaque == -1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = self.player_fcn[0].pPos.X[[0,1,5]]
                self.player_fcn[1].pPos.Xd[[0,1,5]] = self.player_fcn[1].pPos.X[[0,1,5]]
                if self.juiz.quadrante == '1':   self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .575],[ .400],[np.pi]])
                elif self.juiz.quadrante == '2': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.175],[ .400],[np.pi]])
                elif self.juiz.quadrante == '3': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.175],[-.400],[np.pi]])
                elif self.juiz.quadrante == '4': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .575],[-.400],[np.pi]])
                else: print('Erro no quadrante. Ataque para esquerda.')

            elif self.Var_LadoAtaque == 1:
                self.player_fcn[0].pPos.Xd[[0,1,5]] = self.player_fcn[0].pPos.X[[0,1,5]]
                self.player_fcn[1].pPos.Xd[[0,1,5]] = self.player_fcn[1].pPos.X[[0,1,5]]
                if self.juiz.quadrante == '1':   self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .175],[ .400],[0]])
                elif self.juiz.quadrante == '2': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.575],[ .400],[0]])
                elif self.juiz.quadrante == '3': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[-.575],[-.400],[0]])
                elif self.juiz.quadrante == '4': self.player_fcn[2].pPos.Xd[[0,1,5]] = np.array([[ .175],[-.400],[0]])
                else: print('Erro no quadrante. Ataque para esquerda.')
                print('Xc: [%.3f, %.3f, %.3f], ' %(self.player_fcn[1].pPos.Xc[0,0],self.player_fcn[1].pPos.Xc[1,0],self.player_fcn[1].pPos.Xc[5,0]),end='')
                print('Xd: [%.3f, %.3f, %.3f], ' %(self.player_fcn[1].pPos.Xd[0,0],self.player_fcn[1].pPos.Xd[1,0],self.player_fcn[1].pPos.Xd[5,0]),end='')

            else: print('Erro no lado de ataque')
            
            # self.player_fcn[0] = ctrl_rbin(self.player_fcn[0])
            # self.player_fcn[1] = ctrl_rbin(self.player_fcn[1])
            # self.player_fcn[2] = ctrl_rbin(self.player_fcn[2])
            self.player_fcn[0] = autonomos_pos_gk(self.player_fcn[0])
            self.player_fcn[1] = autonomos_pos(self.player_fcn[1],self.player_fcn[2],[1.5,.09])
            self.player_fcn[2] = autonomos_pos(self.player_fcn[2],self.player_fcn[1],[1.5,.09])
           
        else: # Jogo normal
            self.P1.pPos.Xd[[0,1,5]] = self.Var_PosPart.T[[0]].T
            self.P2.pPos.Xd[[0,1,5]] = self.Var_PosPart.T[[0]].T
            self.P3.pPos.Xd[[0,1,5]] = self.Var_PosPart.T[[0]].T

            #self.P1 = Ctrl_tgh_int(self.P1,[.8, .7]) # 0.8 0.7
            self.player_fcn[0] = OfficialDefenser(self.player_fcn[0],self.B, [1.5,.07])#,[.8, .7]) # 0.7 0.7
            self.player_fcn[1] = OfficialAttacker(self.player_fcn[1], self.player_fcn[2], self.player_fcn[0], self.B, [1.6,.085])
            self.player_fcn[2] = OfficialAttacker(self.player_fcn[2],self.player_fcn[1], self.player_fcn[0], self.B, [1.6,.085])#,[.8, .7]) # 0.7 0.7
 
    def __conver2byte(self, elements:np.array) -> str : 
        string_empty = ''
        for value in elements:
            string_empty += str(value) + ','
        string_empty = string_empty[:-1] + '\n'
        return string_empty.encode('utf-8')
    
    def tic(self):
        return time.time()

    def toc(self,t):
        return time.time() - t
    
    '''Funções para comandar o robo em campo: fim'''
   









    exemplo = []
    '''Funções para obter informações sobre o pdi: Inicio'''
    def Obter_DadosJogo(self):
        t_PDI = self.tic()
        _, frames = self.Var_InformacoesCamera.read()
        frames = cv2.resize(cv2.medianBlur(frames, self.Var_MedianBlur), [640, 480])  # Aplica um filtro de mediana

        # Posição da bola em pixels
        Ball_Pos = self.Comando_BuscarBola(frames, self.Var_MatrizCor[1][0:],50,200)        
        # Ball_Pos = self.Comando_BuscarPosicaoCor(frames,self.Var_MatrizCor[1][0:],100,200)

        # Posição das cores da minha equipe e do oponente
        MinhaEquipe,_ = self.Comando_BuscarPosicaoCor(frames, self.Var_MatrizCor[self.Var_CorMinhaEquipe][0:],50,300)
        OpPos = self.Comando_BuscarPosicaoCor_Opp(frames, self.Var_MatrizCor[self.Var_CorEquipeAdversaria][0:],50,300)

        # Posição das cores dos meus jogadores
        P1_Centroide_Cor_1,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[0][:6],50,175)
        P2_Centroide_Cor_1,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[1][:6],50,175)
        P3_Centroide_Cor_1,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[2][:6],50,175)
        
        P1_Centroide_Cor_2,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[0][6:],50,175)
        P2_Centroide_Cor_2,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[1][6:],50,175)
        P3_Centroide_Cor_2,_ = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[2][6:],50,175)

        # Posição do centroide de identificação de cada jogador
        Centroide_Cor_P1,_ = self.Comando_AssociarCores(P1_Centroide_Cor_1,P1_Centroide_Cor_2,80)
        Centroide_Cor_P2,_ = self.Comando_AssociarCores(P2_Centroide_Cor_1,P2_Centroide_Cor_2,80)
        Centroide_Cor_P3,_ = self.Comando_AssociarCores(P3_Centroide_Cor_1,P3_Centroide_Cor_2,80)

        # Postura do robo
        # print('Inicio')
        P1_MyPos = self.Comando_EncontraPostura(MinhaEquipe,Centroide_Cor_P1)
        P2_MyPos = self.Comando_EncontraPostura(MinhaEquipe,Centroide_Cor_P2)
        P3_MyPos = self.Comando_EncontraPostura(MinhaEquipe,Centroide_Cor_P3)
        # print('Final')
        self.Cor_Jog1 = self.CorCamisa_BGR[0][0:]
        self.Cor_Jog2 = self.CorCamisa_BGR[1][0:]
        self.Cor_Jog3 = self.CorCamisa_BGR[2][0:]
        self.Cor_Opo = self.Var_CorEquipeAdversaria_BGR
        self.Cor_Bola = (0, 165, 255)
        
        if(len(Ball_Pos) != 0): self.Var_PosPart[0:,0] = Ball_Pos[0:,0]
        if(len(P1_MyPos) != 0): self.Var_PosPart[0:,1] = P1_MyPos[0:,0]
        if(len(P2_MyPos) != 0): self.Var_PosPart[0:,2] = P2_MyPos[0:,0]
        if(len(P3_MyPos) != 0): self.Var_PosPart[0:,3] = P3_MyPos[0:,0]
        if(len(OpPos) != 0): self.Var_PosPart[0:,4] = OpPos[0][0:,0]
        if(len(OpPos) != 0): self.Var_PosPart[0:,5] = OpPos[1][0:,0]
        if(len(OpPos) != 0): self.Var_PosPart[0:,6] = OpPos[2][0:,0]

        self.Tempo_PDI = self.toc(t_PDI)
    
    def Camando_CriaMascara(self,quadro,vetor_limites):
        # Cria a mascara apartir do vetor de limites em HSV
        CorHSV = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)
        # h,s,v = cv2.split(CorHSV)
        # vequalizado = cv2.equalizeHist(v)
        # CorHSV = cv2.merge((h,s,vequalizado))
        LimiteCorInferior = np.array([vetor_limites[0], vetor_limites[2], vetor_limites[4]])
        LimiteCorSuperior = np.array([vetor_limites[1], vetor_limites[3], vetor_limites[5]])
        MascaraCor = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        MascaraCor = cv2.dilate(MascaraCor, self.Var_Kernel, iterations=1)
        MascaraCor = cv2.medianBlur(MascaraCor, self.Var_MedianBlur+4)
        return MascaraCor

    def Comando_BuscarBola(self, quadro, vetor_limites, AreaMinima=100, AreaMaxima=200):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        # Posicao_Bola = np.array([[0], [.685], [0]])
        Pos_Possivel, Area_Possivel = self.Comando_BuscarPosicaoCor(quadro,vetor_limites,AreaMinima,AreaMaxima)
        if len(Area_Possivel)>0:
            Id = np.argmax(Area_Possivel)
            Posicao_Bola = np.concatenate((Pos_Possivel[Id]/1000, [[0]]), axis=0)
        else:
            Posicao_Bola = []
        return Posicao_Bola

    def Comando_BuscarPosicaoCor(self, quadro, vetor_limites, AreaMinima=0, AreaMaxima=500):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        PosicaoCor = []
        AreaCor = []
        PosicaoCorBGR = np.ones((3, 1))
        MascaraCor = self.Camando_CriaMascara(quadro,vetor_limites)
        contornos, _ = cv2.findContours(MascaraCor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Tamanho_Contornos = len(contornos)

        if Tamanho_Contornos > 0:
            for i in range(Tamanho_Contornos):
                tupla = contornos[i]
                M = cv2.moments(tupla)
                try:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    x = np.array([cx, cy])
                    Area = cv2.contourArea(tupla)

                    if (Area > AreaMinima) and (Area < AreaMaxima):
                        PosicaoCorBGR[0, 0] = x[0]
                        PosicaoCorBGR[1, 0] = x[1]
                        x = self.Var_MatrizTransfPerspectiva @ PosicaoCorBGR
                        PosicaoCor.append(x[:2])
                        AreaCor.append(Area)
                except:
                    pass
        else:
            PosicaoCor = []
            AreaCor = []
        return PosicaoCor,AreaCor

    def Comando_BuscarPosicaoCor_Opp(self, quadro, vetor_limites, AreaMinima=0, AreaMaxima=500):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        Pos_Possivel, Area_Possivel = self.Comando_BuscarPosicaoCor(quadro,vetor_limites,AreaMinima,AreaMaxima)
        VectorFinal = []
        Area_Possivel = np.array(Area_Possivel)
        if len(Area_Possivel) > 0:
            Vector_Index = Area_Possivel.argsort()[-3:][::-1]
            for E in Vector_Index:
                VectorFinal.append(np.concatenate((Pos_Possivel[E]/1000, [[0]]), axis=0))        

        if len(VectorFinal) == 3:
            return VectorFinal
        elif len(VectorFinal) == 2:
            VectorFinal.append(np.array([[.250], [.685], [0]]))
            return VectorFinal
        elif len(VectorFinal) == 1:
            VectorFinal.append(np.array([[.230], [.685], [0]]))
            VectorFinal.append(np.array([[.250], [.685], [0]]))
            return VectorFinal
        elif len(VectorFinal) == 0:
            VectorFinal.append(np.array([[.200], [.685], [0]]))
            VectorFinal.append(np.array([[.250], [.685], [0]]))
            VectorFinal.append(np.array([[.300], [.685], [0]]))
            return VectorFinal

    def Comando_CalcDistance(self,point1, point2):
        return np.linalg.norm(np.array(point2) - np.array(point1))

    def Comando_CalcCenter(self,point1, point2):
        return (np.array(point1) + np.array(point2)) / 2

    def Comando_AssociarCores(self,VetorCor1,VetorCor2,Dist=40):
        # Obtem a posição das duas cores de jogadores mais proximas
        Centroide_Cor = []
        Dados = []
        
        object_positions = list(VetorCor1) # Lista de posições (x, y) dos objetos
        for col in range(np.shape(VetorCor2)[0]):
            object_positions.append(VetorCor2[col])       
        
        num_to_combine = 2 # Número de objetos para combinar
        closest_combinations = list(itertools.combinations(object_positions, num_to_combine))
        closest_combinations.sort(key=lambda combo: self.Comando_CalcDistance(combo[0], combo[1]))

        # Imprime as combinações mais próximas e seus centros
        for combo in closest_combinations:
            combo_distance = self.Comando_CalcDistance(combo[0], combo[1])   
            # print(f'Par: {combo[0].T}, {combo[1].T}, Dist das combinações: {combo_distance}')         
            if combo_distance > Dist:
                break
            combo_center = self.Comando_CalcCenter(combo[0], combo[1])            
            Centroide_Cor.append(combo_center)
            Dados.append(np.squeeze(np.stack((combo[0], combo[1]), axis=-1)))            
        return Centroide_Cor, Dados

    def Comando_EncontraPostura(self,VetorCorTime,Centroide_Cor):
        try:
            # Encontra o angulo entre a cor do time e o centroide da cores do respectivo jogador        
            Pos, Dados = self.Comando_AssociarCores(VetorCorTime,Centroide_Cor) # Numero pequeno para o azul
            vetor_dif = Dados[0][:,1] - Dados[0][:,0] # Vetor que aponta do centroide das cores do jogador 1 para a cor do time
            angulo_rad = np.arctan2(vetor_dif[1], vetor_dif[0]) # Calcula o ângulo entre o vetor e o eixo X da imagem (em radianos)
            Postura = np.array([[Pos[0][0][0]/1000],[Pos[0][1][0]/1000],[angulo_rad]])
            # print("X: %.4f, Y: %.4f, Angº: %3.2f" %(Postura[0],Postura[1],np.rad2deg(Postura[2])))
        except:
            Postura = []
        return Postura
    '''Funções para obter informações sobre o pdi: Fim'''











    '''Funções para visualizaçãod e informações: inicio'''
    # Função para visualizar a câmera em uma thread
    def Comando_VisualizarCamera(self):
        while True:
            _, Quadros = self.Var_InformacoesCamera.read()
            Quadros = cv2.resize(cv2.medianBlur(Quadros, self.Var_MedianBlur), [640, 480]) # Aplica um filtro de mediana

            cv2.imshow("Visao Camera", Quadros)
            cv2.waitKey(self.Var_FPS)
            if (cv2.getWindowProperty("Visao Camera", cv2.WND_PROP_VISIBLE) < 1):
                break

    # Função para visualizar a segmentação em uma thread
    def Comando_VisualizarSegmentacao(self):
        while True:
            _, Quadros = self.Var_InformacoesCamera.read()
            Quadros = cv2.resize(cv2.medianBlur(Quadros, self.Var_MedianBlur), [640, 480]) # Aplica um filtro de mediana

            # Inicializar uma máscara vazia
            # CorHSV = cv2.cvtColor(Quadros, cv2.COLOR_BGR2HSV)
            MatrizCores = [None] * 7

            # Aplicar o filtro de cor para cada cor calibrada e realizar a combinação lógica "OR"
            for Id, Dados in enumerate(self.Var_MatrizCor):
                MascaraCor = self.Camando_CriaMascara(Quadros,Dados)            
                MatrizCores[Id] = cv2.bitwise_and(Quadros, Quadros, mask=MascaraCor)
            AplicacaoCor = MatrizCores[0]
            for i in range(1, 7):
                AplicacaoCor = cv2.bitwise_or(AplicacaoCor, MatrizCores[i])            

            cv2.imshow("Visao Segmentacao", AplicacaoCor)
            cv2.waitKey(self.Var_FPS)
            if (cv2.getWindowProperty("Visao Segmentacao", cv2.WND_PROP_VISIBLE) < 1):
                break
    
    def Comando_VisualizarAssociacao(self):
        while True:
            Campo_Virtual = self.Comando_DesenhaTudo(self.Var_PosPart[0:,1],self.Var_PosPart[0:,2],self.Var_PosPart[0:,3],
                                                     self.CorCamisa_BGR[0],self.CorCamisa_BGR[1],self.CorCamisa_BGR[2],
                                                     self.Var_PosPart[0:,4], self.Var_PosPart[0:,5], self.Var_PosPart[0:,6],
                                                     self.Cor_Opo, self.Var_PosPart[0:,0], self.Cor_Bola)

            cv2.imshow("Visao Associacao", Campo_Virtual)
            cv2.waitKey(self.Var_FPS) # Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("Visao Associacao", cv2.WND_PROP_VISIBLE) < 1):
                break

    # Função para desenhar robôs do time e robôs adversários
    def Comando_DesenhaTudo(self, P1_Pos, P2_Pos, P3_Pos, P1_Cor, P2_Cor, P3_Cor, Op1_Pos, Op2_Pos, Op3_Pos, Op_Cor, Ball_Pos, Ball_Cor):
        Campo_Virtual = self.ImagemCampo_px.copy()
        self.Comando_DesenhaSeta(Campo_Virtual, P1_Pos, P1_Cor[:3],P1_Cor[3:])
        self.Comando_DesenhaSeta(Campo_Virtual, P2_Pos, P2_Cor[:3],P2_Cor[3:])
        self.Comando_DesenhaSeta(Campo_Virtual, P3_Pos, P3_Cor[:3],P3_Cor[3:])
        self.Comando_DesenhaCirculo(Campo_Virtual, Op1_Pos, Op_Cor)
        self.Comando_DesenhaCirculo(Campo_Virtual, Op2_Pos, Op_Cor)
        self.Comando_DesenhaCirculo(Campo_Virtual, Op3_Pos, Op_Cor)
        self.Comando_DesenhaBola(Campo_Virtual, Ball_Pos, Ball_Cor)

        Campo_Virtual = cv2.resize(Campo_Virtual, [640, 480])
        return Campo_Virtual

    def Comando_DesenhaSeta(self, Campo_Virtual, Posicao, Cor1, Cor2, Comprimento = 40, espessura = 10,raio=40):
        X, Y, Orientacao_Radianos = Posicao[0]*1000, Posicao[1]*1000, Posicao[2]
        X = int(X + 900)
        Y = int(Y + 750)
        end_point = (int(X + Comprimento * np.cos(Orientacao_Radianos)), int(Y + Comprimento * np.sin(Orientacao_Radianos)))
        start_point = (int(X), int(Y))
        cv2.arrowedLine(Campo_Virtual, start_point, end_point, Cor1, espessura, cv2.LINE_AA, tipLength=0.2)
        cv2.circle(Campo_Virtual, (X, Y), raio, Cor2,espessura)  # O valor -1 preenche o círculo

    def Comando_DesenhaCirculo(self, Campo_Virtual, Posicao, Cor,espessura = 10, raio = 40):
        X, Y = int(Posicao[0]*1000 + 900), int(Posicao[1]*1000 + 750)        
        cv2.circle(Campo_Virtual, (X, Y), raio, Cor, espessura)  # O valor -1 preenche o círculo

    def Comando_DesenhaBola(self, Campo_Virtual, Posicao, Cor, raio = 21):
        X, Y = int(Posicao[0]*1000 + 900), int(Posicao[1]*1000 + 750)        
        cv2.circle(Campo_Virtual, (X, Y), raio, Cor, -1)  # O valor -1 preenche o círculo
    '''Funções para visualizaçãod e informações: Fim'''











    # Executa o loop da janela
    def Comando_Iniciar(self):
        try:
            self.Janela.protocol("WM_DELETE_WINDOW", self.Encerrar_Comunicacao)
            self.Janela.mainloop()
        except Exception as e:            
            print(f"Erro ao iniciar a janela: {str(e)}")

    # Encerra a comunicação e fecha a janela
    def Encerrar_Comunicacao(self):
        try:
            self.juiz.server_socket.close()
            self.Sai = True
        except Exception as e:
            print(f"Erro ao encerrar a comunicação: {str(e)}")
        
        self.Janela.destroy()

    # Encerra a janela
    def Comando_Parar(self):
        try:
            self.Janela.destroy()
        except Exception as e:
            print(f"Erro ao encerrar a janela: {str(e)}")



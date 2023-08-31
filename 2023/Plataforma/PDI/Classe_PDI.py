'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem do campo.
'''

# Importando bibliotecas necessárias
from tkinter import *
from math import dist
from tkinter import ttk


from Controle.Class_Control import*

import cv2
import threading
import numpy as np
import os
# import serial
import serial.tools.list_ports
import time
import math
import itertools

# Criação da janela responsável pelas configurações da partida
class JanelaPDI(object):
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
        # self.Var_Jogar = False
        self.Var_TesteMecanico = False
        self.PastaAtual = os.path.dirname(__file__)
        self.ImagemCampo_px = cv2.imread(os.path.join(self.PastaAtual, 'Campo_px.png'))
        self.Var_ParametrosJogo = np.zeros((7, 3), dtype=np.int64)

        # Executa as funções de criação dos elementos da janela
        self.Criar_Janela()
        self.Criar_TextoInformacoes()
        self.Criar_CheckButton()
        self.Criar_ComboBox()
        self.Criar_Botoes()
    
    # Cria e configura a sub janela
    def Criar_Janela(self):
        self.Janela = Toplevel()
        self.Janela.title("Tela de Jogo")
        self.Janela.minsize(830, 600)
        self.Janela.maxsize(830, 600)
        self.Janela.configure(bg='#229A00')

        self.BarraDeStatus = Label(self.Janela,
                                text="Instruções: \nConfigurar os jogadores \nIniciar comunicação \nIniciar partida",
                                bd=1, relief=SUNKEN, anchor=CENTER)
        self.BarraDeStatus.pack(side=BOTTOM, fill=X)

    def Limpar_BarraDeStatus(self):
        """
        Limpa o texto exibido na barra de status.
        """
        self.BarraDeStatus.config(text="")
        self.BarraDeStatus.update_idletasks()

    def Atualizar_BarrraDeStatus(self, texto):
        """
        Atualiza o texto exibido na barra de status.
        :param texto: O novo texto a ser exibido na barra de status.
        """
        self.BarraDeStatus.config(text=texto)
        self.BarraDeStatus.update_idletasks()

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

        But_TesteMecanico = Button(self.Janela, text="Teste Mecânico", command=lambda: threading.Thread(target=self.Comando_TesteMecanico).start())
        But_TesteMecanico.place(height=50, width=200, x=50, y=190)

        But_IniciarPartida = Button(self.Janela, text="Iniciar Partida", command=lambda: threading.Thread(target=self.Comando_IniciarPartida).start())
        But_IniciarPartida.place(height=50, width=200, x=50, y=250)

        But_PararPartida = Button(self.Janela, text="Parar Partida", command=self.Comando_EncerrarPartida)
        But_PararPartida.place(height=50, width=200, x=50, y=310)

        But_VisualizarCamera = Button(self.Janela, text="Ver Câmera", command=lambda: threading.Thread(target=self.Comando_VisualizarCamera).start())
        But_VisualizarCamera.place(height=50, width=200, x=50, y=370)

        But_VisualizarSegmentacao = Button(self.Janela, text="Ver Segmentação", command=lambda: threading.Thread(target=self.Comando_VisualizarSegmentacao).start())
        But_VisualizarSegmentacao.place(height=50, width=200, x=50, y=430)

        But_VisualizarAssociacao = Button(self.Janela, text="Ver Associação", command=lambda: threading.Thread(target=self.Comando_VisualizarAssociacao).start())
        But_VisualizarAssociacao.place(height=50, width=200, x=50, y=490)

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
        self.J1 = MY_TEAM(self.Var_CorMinhaEquipe_BGR, self.CorCamisa_BGR[0][:3], self.Var_LadoAtaque, self.Var_J1_Funcao.current())
        self.J2 = MY_TEAM(self.Var_CorMinhaEquipe_BGR, self.CorCamisa_BGR[1][:3], self.Var_LadoAtaque, self.Var_J2_Funcao.current())
        self.J3 = MY_TEAM(self.Var_CorMinhaEquipe_BGR, self.CorCamisa_BGR[2][:3], self.Var_LadoAtaque, self.Var_J3_Funcao.current())
        return Matriz
   
    def Comando_IniciarComunicacao(self, tsim=3):
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

                    if t > 4*tsim/5: n = 100
                    elif t > 3*tsim/5: n = 80
                    elif t > 2*tsim/5: n = 60
                    elif t > 1*tsim/5: n = 40
                    else: n = 20

                    self.pEsp.write([1, 2, int(150+n), int(150+n), int(150+n), int(150+n), 150, 150, 3, 10])
                    if t > tsim:
                        self.pEsp.write([1, 2, int(0), int(0), int(0), int(0), 150, 150, 3, 10])
                        break

                # Ativa a variável de controle de comunicação e atualiza a barra de status
                self.Var_Comunicacao = True
                self.Limpar_BarraDeStatus()
                self.Atualizar_BarrraDeStatus("Comunicação Iniciada")
        except:
            try:
                # Fecha a comunicação serial e desativa a variável de controle de comunicação
                self.pEsp.close()
                self.Var_Comunicacao = False
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

    def Comando_TesteMecanico(self):
        '''
        Executa uma elipse para cada robô seguir
        Rx: Raio em x
        Ry: Raio em y
        w: Período da elipse
        '''

        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus("Teste mecânico iniciado")

        self.Var_TesteMecanico = True
        self.Obter_DadosJogo()
        # Define os parâmetros do círculo
        Rx = 250
        Ry = 250
        T = 30
        simulacao = 0
        w = 2*np.pi/T  # Frequência angular (em radianos)
        elapsed_time = np.inf
        StartCycle = time.time()      

        while self.Var_TesteMecanico == True:
            # Obtém o tempo decorrido desde o início do ciclo
            elapsed_time = time.time() - StartCycle
            self.InicioCiclo = time.time()
            self.Obter_DadosJogo()
            # Calcula a posição atual em coordenadas polares 
            self.PosDesejada_P1 = np.array([[np.int64(-500 + Rx * math.cos(w*elapsed_time))],
                                            [np.int64( 000 + Ry * math.sin(w*elapsed_time))],
                                            [-np.pi/2 - w*elapsed_time]])
            self.PosDesejada_P2 = np.array([[np.int64( 000 + Rx * math.cos(w*elapsed_time))],
                                            [np.int64( 000 + Ry * math.sin(w*elapsed_time))],
                                            [-np.pi/2 - w*elapsed_time]])
            self.PosDesejada_P3 = np.array([[np.int64( 500 + Rx * math.cos(w*elapsed_time))],
                                            [np.int64( 000 + Ry * math.sin(w*elapsed_time))],
                                            [-np.pi/2 - w*elapsed_time]])
            
            if 2*T == int(elapsed_time):
                self.Var_TesteMecanico = False

            # if simulacao == 1:
            Campo_Virtual = self.Comando_DesenhaTudo(self.PosDesejada_P1, self.Cor_Jogador_1, self.PosDesejada_P2, self.Cor_Jogador_2, self.PosDesejada_P3, self.Cor_Jogador_3,
                                                    self.Posicao_Oponente_1, self.Posicao_Oponente_2, self.Posicao_Oponente_3, self.Cor_Oponente, 
                                                    self.Posicao_Bola, self.Cor_Bola)

            cv2.imshow("Visão da Associação", Campo_Virtual)
            cv2.waitKey(self.Var_FPS)  # Está em 25 milissegundos = 40 fps
            if (cv2.getWindowProperty("Visão da Associação", cv2.WND_PROP_VISIBLE) < 1):
                break
            # else:
            self.J1.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[0, 0:]
            self.J1.rBDP_pPos_Xd[0:, 0] = self.PosDesejada_P1[0:,0]
            self.J1.xtil()
            self.J1.autonivel()
            self.J1.baixonivel()

            self.J2.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[1, 0:]
            self.J2.rBDP_pPos_Xd[0:, 0] = self.Var_ParametrosJogo[6, 0]#self.PosDesejada_P2[0:,0]*-1
            self.J2.xtil()
            self.J2.autonivel()
            self.J2.baixonivel()

            self.J3.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[2, 0:]
            self.J3.rBDP_pPos_Xd[0:, 0] = self.PosDesejada_P3[0:,0]
            self.J3.xtil()
            self.J3.autonivel()
            self.J3.baixonivel()

            self.Acao_Jogo()
        
        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus('Partida Encerrada')
    
    def Comando_IniciarPartida(self):
        self.Var_Jogando = True
        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus("Partida Iniciada")

        while self.Var_Jogando == True:
            self.InicioCiclo = time.time()
            self.Obter_DadosJogo()

            self.J1.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[0, 0:]
            self.J1.rBDP_pPos_Xd[0:, 0] = self.Var_ParametrosJogo[6, 0:]
            self.J1.xtil()
            self.J1.autonivel()
            self.J1.baixonivel()

            self.J2.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[1, 0:]
            self.J2.rBDP_pPos_Xd[0:, 0] = self.Var_ParametrosJogo[6, 0:]
            self.J2.xtil()
            self.J2.autonivel()
            self.J2.baixonivel()

            self.J3.rBDP_pPos_X[0:, 0] = self.Var_ParametrosJogo[2, 0:]
            self.J3.rBDP_pPos_Xd[0:, 0] = self.Var_ParametrosJogo[6, 0:]
            self.J3.xtil()
            self.J3.autonivel()
            self.J3.baixonivel()

            # self.Acao_Jogo()

        self.Limpar_BarraDeStatus()
        self.Atualizar_BarrraDeStatus('Partida Encerrada')
    
    def Obter_DadosJogo(self):
        _, frames = self.Var_InformacoesCamera.read()
        frames = cv2.resize(cv2.medianBlur(frames, self.Var_MedianBlur), [640, 480])  # Aplica um filtro de mediana

        # Posição da bola em pixels
        self.Posicao_Bola = self.Comando_BuscarBola(frames, self.Var_MatrizCor[1][0:],100,200)        

        # Posição das cores da minha equipe e do oponente
        MinhaEquipe = self.Comando_BuscarPosicaoCor(frames, self.Var_MatrizCor[self.Var_CorMinhaEquipe][0:],150,300)
        Oponente = self.Comando_BuscarPosicaoCor_Opp(frames, self.Var_MatrizCor[self.Var_CorEquipeAdversaria][0:],150,300)

        # Posição das cores dos meus jogadores
        Centroide_P1_Cor_1 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[0][:6],50,150)
        Centroide_P2_Cor_1 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[1][:6],50,150)
        Centroide_P3_Cor_1 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[2][:6],50,150)

        Centroide_P1_Cor_2 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[0][6:],50,150)
        Centroide_P2_Cor_2 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[1][6:],50,150)
        Centroide_P3_Cor_2 = self.Comando_BuscarPosicaoCor(frames, self.CoresCamisas[2][6:],50,150)

        Centroide_Cor_P1 = self.Comando_AssociarCores(Centroide_P1_Cor_1,Centroide_P1_Cor_2)
        Centroide_Cor_P2 = self.Comando_AssociarCores(Centroide_P2_Cor_1,Centroide_P2_Cor_2)
        Centroide_Cor_P3 = self.Comando_AssociarCores(Centroide_P3_Cor_1,Centroide_P3_Cor_2)

        self.Postura_P1 = self.Comando_AssociarCores(MinhaEquipe,Centroide_Cor_P1)
        self.Postura_P2 = self.Comando_AssociarCores(MinhaEquipe,Centroide_Cor_P2)
        self.Postura_P3 = self.Comando_AssociarCores(MinhaEquipe,Centroide_Cor_P3)
        
        self.Postura_P1, self.Postura_P2, self.Postura_P3 = self.Comando_EncontraPostura(MinhaEquipe, Centroide_Cor_P1, Centroide_Cor_P2, Centroide_Cor_P3)

        self.Posicao_Oponente_1 = [Oponente[0][0], Oponente[0][1]]
        self.Posicao_Oponente_2 = [Oponente[1][0], Oponente[1][1]]
        self.Posicao_Oponente_3 = [Oponente[2][0], Oponente[2][1]]

        self.Cor_Jogador_1 = self.CorCamisa_BGR[0][:3]
        self.Cor_Jogador_2 = self.CorCamisa_BGR[1][:3]
        self.Cor_Jogador_3 = self.CorCamisa_BGR[2][:3]
        self.Cor_Oponente = self.Var_CorEquipeAdversaria_BGR
        self.Cor_Bola = (0, 165, 255)

        # if(len(self.Postura_P1) != 0):
        #     self.Var_ParametrosJogo[0, 0:] = np.array(self.Postura_P1).T
        #     self.Var_ParametrosJogo[0, 0] = self.Var_ParametrosJogo[0, 0] * -1
        # if(len(self.Postura_P2) != 0):
        #     self.Var_ParametrosJogo[1, 0:] = np.array(self.Postura_P2).T
        #     self.Var_ParametrosJogo[1, 0] = self.Var_ParametrosJogo[1, 0] * -1
        # if(len(self.Postura_P3) != 0):
        #     self.Var_ParametrosJogo[2, 0:] = np.array(self.Postura_P3).T
        #     self.Var_ParametrosJogo[2, 0] = self.Var_ParametrosJogo[2, 0] * -1
        # if(len(self.Posicao_Oponente_1) != 0):
        #     self.Var_ParametrosJogo[3, 0:2] = np.array(self.Posicao_Oponente_1).T
        #     self.Var_ParametrosJogo[3, 0] = self.Var_ParametrosJogo[3, 0] * -1
        # if(len(self.Posicao_Oponente_2) != 0):
        #     self.Var_ParametrosJogo[4, 0:2] = np.array(self.Posicao_Oponente_2).T
        #     self.Var_ParametrosJogo[4, 0] = self.Var_ParametrosJogo[4, 0] * -1
        # if(len(self.Posicao_Oponente_3) != 0):
        #     self.Var_ParametrosJogo[5, 0:2] = np.array(self.Posicao_Oponente_3).T
        #     self.Var_ParametrosJogo[5, 0] = self.Var_ParametrosJogo[5, 0] * -1
        # if(len(self.Posicao_Bola) != 0):
        #     self.Var_ParametrosJogo[6, 0:2] = self.Posicao_Bola.T
        #     self.Var_ParametrosJogo[6, 0] = self.Var_ParametrosJogo[6, 0] * -1

    def Camando_CriaMascara(self,quadro,vetor_limites):
        # Cria a mascara apartir do vetor de limites em HSV
        CorHSV = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)
        LimiteCorInferior = np.array([vetor_limites[0], vetor_limites[2], vetor_limites[4]])
        LimiteCorSuperior = np.array([vetor_limites[1], vetor_limites[3], vetor_limites[5]])
        MascaraCor = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        MascaraCor = cv2.dilate(MascaraCor, self.Var_Kernel, iterations=1)
        MascaraCor = cv2.medianBlur(MascaraCor, self.Var_MedianBlur+4)
        return MascaraCor

    def Comando_BuscarBola(self, quadro, vetor_limites, AreaMinima=100, AreaMaxima=200):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        Area_Atual = 0
        Posicao_Bola = np.ones((3, 1))
        
        MascaraCor = self.Camando_CriaMascara(quadro,vetor_limites)

        # CorHSV = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)
        # LimiteCorInferior = np.array([vetor_limites[0], vetor_limites[2], vetor_limites[4]])
        # LimiteCorSuperior = np.array([vetor_limites[1], vetor_limites[3], vetor_limites[5]])

        # CorHSV = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        # CorHSV = cv2.dilate(CorHSV, self.Var_Kernel, iterations=1)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        # # CorHSV = cv2.morphologyEx(CorHSV, cv2.MORPH_OPEN, self.Var_ElementoEstruturante)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur

        Contornos, _ = cv2.findContours(MascaraCor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Tamanho_Contornos = len(Contornos)

        if Tamanho_Contornos > 0:
            for i in range(Tamanho_Contornos):
                tupla = Contornos[i]
                M = cv2.moments(tupla)
                try:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    x = np.array([cx, cy])
                    Area = cv2.contourArea(tupla)

                    if (AreaMinima < Area) and (Area < AreaMaxima) and (Area > Area_Atual):
                        Posicao_Bola[0][0] = x[0]
                        Posicao_Bola[1][0] = x[1]
                        Area_Atual = Area
                except:
                    pass

            Posicao_Bola = self.Var_MatrizTransfPerspectiva @ Posicao_Bola
            return Posicao_Bola[0:2, 0:]
        else:
            Posicao_Bola = []
            return Posicao_Bola

    def Comando_BuscarPosicaoCor(self, quadro, vetor_limites, AreaMinima=200, AreaMaxima=500):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        PosicaoCor = []
        PosicaoCorBGR = np.ones((3, 1))

        CorHSV = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)
        LimiteCorInferior = np.array([vetor_limites[0], vetor_limites[2], vetor_limites[4]])
        LimiteCorSuperior = np.array([vetor_limites[1], vetor_limites[3], vetor_limites[5]])

        CorHSV = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        CorHSV = cv2.dilate(CorHSV, self.Var_Kernel, iterations=1)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        # PosicaoCor = cv2.morphologyEx(PosicaoCor, cv2.MORPH_OPEN, Kernel)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur

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
                        PosicaoCor.append(x[0:2, 0:])
                except:
                    pass
        else:
            PosicaoCor = []
        return PosicaoCor

    def Comando_BuscarPosicaoCor_Opp(self, quadro, vetor_limites, AreaMinima=200, AreaMaxima=500):
        # Encontra as posições de todos os objetos da cor pré-determinada na imagem segmentada.
        PosicaoCor_Opp = []
        PosicaoCorBGR = np.ones((3, 1))

        CorHSV = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)
        LimiteCorInferior = np.array([vetor_limites[0], vetor_limites[2], vetor_limites[4]])
        LimiteCorSuperior = np.array([vetor_limites[1], vetor_limites[3], vetor_limites[5]])

        CorHSV = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        CorHSV = cv2.dilate(CorHSV, self.Var_Kernel, iterations=1)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur
        # PosicaoCor_Opp = cv2.morphologyEx(PosicaoCor_Opp, cv2.MORPH_OPEN, Kernel)  # testar cv2.MORPH_CLOSE e usar filtro cv2.medianblur

        MascaraCor = self.Camando_CriaMascara(quadro,vetor_limites)

        contornos, _ = cv2.findContours(MascaraCor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Tamanho_Contornos = len(contornos)
        VectorFinal = []

        if Tamanho_Contornos > 0:
            VectorArea = []
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
                        PosicaoCor_Opp.append(x[0:2, 0:])
                        VectorArea.append(Area)
                except:
                    pass

            Vector_Array = np.array(VectorArea)
            Vector_Index = Vector_Array.argsort()[-3:][::-1]
            for E in Vector_Index:
                VectorFinal.append(PosicaoCor_Opp[E])

        if len(VectorFinal) == 3:
            return VectorFinal
        elif len(VectorFinal) == 2:
            VectorFinal.append(np.array([250, 685]))
            return VectorFinal
        elif len(VectorFinal) == 1:
            VectorFinal.append(np.array([230, 685]))
            VectorFinal.append(np.array([250, 685]))
            return VectorFinal
        elif len(VectorFinal) == 0:
            VectorFinal.append(np.array([200, 685]))
            VectorFinal.append(np.array([250, 685]))
            VectorFinal.append(np.array([300, 685]))
            return VectorFinal

    def Comando_CalcDistance(self,point1, point2):
        return np.linalg.norm(np.array(point2) - np.array(point1))

    def Comando_CalcCenter(self,point1, point2):
        return tuple((np.array(point1) + np.array(point2)) / 2)

    def Comando_AssociarCores(self,VetorCor1,VetorCor2):
        # Obtem a posição das duas cores de jogadores mais proximas
        Centroide_Cor = []

        # Lista de posições (x, y) dos objetos
        object_positions = list(VetorCor1)
        for col in range(np.shape(VetorCor2)[0]):
            object_positions.append(VetorCor2[col])       

        # Número de objetos para combinar
        num_to_combine = 2

        # Calcula todas as combinações de objetos mais próximos
        closest_combinations = list(itertools.combinations(object_positions, num_to_combine))

        # Ordena as combinações com base na distância entre os objetos
        closest_combinations.sort(key=lambda combo: self.Comando_CalcDistance(combo[0], combo[1]))

        # Imprime as combinações mais próximas e seus centros
        for combo in closest_combinations:
            combo_distance = self.Comando_CalcDistance(combo[0], combo[1])
            combo_center = self.Comando_CalcCenter(combo[0], combo[1])
            if combo_distance < 80:
                Centroide_Cor.append(combo_center)
                print(f"Combination: {combo}, Distance: {combo_distance:.2f}, Center: {combo_center}")
        
        return Centroide_Cor

    def Comando_EncontraPostura(self, Posicao_Cor_Time, Posicao_Camisetas_Jogador_1, Posicao_Camisetas_Jogador_2, Posicao_Camisetas_Jogador_3):
        Postura_Jogador_1 = self.Comando_AssociarCamisetaUnica(Posicao_Cor_Time, Posicao_Camisetas_Jogador_1)
        Postura_Jogador_2 = self.Comando_AssociarCamisetaUnica(Posicao_Cor_Time, Posicao_Camisetas_Jogador_2)
        Postura_Jogador_3 = self.Comando_AssociarCamisetaUnica(Posicao_Cor_Time, Posicao_Camisetas_Jogador_3)
            
        return Postura_Jogador_1, Postura_Jogador_2, Postura_Jogador_3
        
    def Comando_AssociarCamisetaUnica(self, Posicao_Cor_Time, Posicao_Camisetas_Jogador, Distancia_Maxima = 80):
        # A função deve receber posição transformada pela matriz de transformação de perspectiva.
        Posicao_Possivel = []
        Lista_Distancias = []
        Angulos = []

        NumeroJogadores = np.shape(Posicao_Cor_Time)[0]  # Número de jogadores
        NumeroCamisetas = np.shape(Posicao_Camisetas_Jogador)[0]  # Número de camisetas
        if (NumeroJogadores > 0) and (NumeroCamisetas > 0):
            for k in range(NumeroJogadores):
                Distancias = []
                for i in range(NumeroCamisetas):
                    Distancias.append(dist(Posicao_Cor_Time[k][0:], Posicao_Camisetas_Jogador[i][0:]))
                Lista_Distancias.append(min(Distancias))  # Contém todas as distâncias possíveis
                IndiceMenorDistancia = np.argmin(Distancias)  # Pega o índice da menor distância
                Posicao_Possivel.append(np.mean(np.array([Posicao_Cor_Time[k][0:], Posicao_Camisetas_Jogador[IndiceMenorDistancia][0:]]), axis=0))  # Média das colunas
                VetorDiferenca = np.array(Posicao_Camisetas_Jogador[IndiceMenorDistancia][0:]) - np.array(Posicao_Cor_Time[k][0:])
                if VetorDiferenca[1] > 0:
                    Angulos.append(-np.arccos(np.dot(VetorDiferenca.T/np.linalg.norm(VetorDiferenca.T), np.array([1, 0]))))
                else:
                    Angulos.append(np.arccos(np.dot(VetorDiferenca.T/np.linalg.norm(VetorDiferenca.T), np.array([1, 0]))))

            # Condição para caso não haja a captura de todas as camisetas do time
            if np.min(Lista_Distancias) < Distancia_Maxima:
                IndiceMenorDistancia2 = np.argmin(np.array(Lista_Distancias))
                PosicaoFinalJogador = Posicao_Possivel[IndiceMenorDistancia2][0:]
                Orientacao = Angulos[IndiceMenorDistancia2]
                Postura_Jogador = [PosicaoFinalJogador[0], PosicaoFinalJogador[1], Orientacao]
            else:
                Postura_Jogador = []
        else:
            Postura_Jogador = []

        return Postura_Jogador
    
    def Comando_EncerrarPartida(self):
        self.Var_Jogando = False
    
    # Função para visualizar a câmera em uma thread
    def Comando_VisualizarCamera(self):
        while True:
            _, Quadros = self.Var_InformacoesCamera.read()
            Quadros = cv2.resize(cv2.medianBlur(Quadros, self.Var_MedianBlur), [640, 480]) # Aplica um filtro de mediana

            cv2.imshow("Visao Camera", Quadros)
            tecla = cv2.waitKey(self.Var_FPS)
            if (cv2.getWindowProperty("Visao Camera", cv2.WND_PROP_VISIBLE) < 1):
                break

    # Função para visualizar a segmentação em uma thread
    def Comando_VisualizarSegmentacao(self):
        while True:
            _, Quadros = self.Var_InformacoesCamera.read()
            Quadros = cv2.resize(cv2.medianBlur(Quadros, self.Var_MedianBlur), [640, 480]) # Aplica um filtro de mediana

        
            # Inicializar uma máscara vazia
            MascaraTotal = np.zeros(Quadros.shape[:2], dtype=np.uint8)
            CorHSV = cv2.cvtColor(Quadros, cv2.COLOR_BGR2HSV)
            MatrizCores = [None] * 7

            # Aplicar o filtro de cor para cada cor calibrada e realizar a combinação lógica "OR"
            for Id, Dados in enumerate(self.Var_MatrizCor):
                LimiteCorInferior = np.array([Dados[0], Dados[2], Dados[4]])
                LimiteCorSuperior = np.array([Dados[1], Dados[3], Dados[5]])
                MascaraCor = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
                MascaraCor = cv2.dilate(MascaraCor, self.Var_Kernel, iterations=1)
                MatrizCores[Id] = cv2.bitwise_and(Quadros, Quadros, mask=MascaraCor)

            AplicacaoCor = MatrizCores[0]
            for i in range(1, 7):
                AplicacaoCor = cv2.bitwise_or(AplicacaoCor, MatrizCores[i])

            AplicacaoCor = cv2.resize(AplicacaoCor, (400, 300))
            ConversaoRGB = cv2.cvtColor(AplicacaoCor, cv2.COLOR_BGR2RGB)
            
            cv2.imshow("Visao Segmentacao", ConversaoRGB)
            tecla = cv2.waitKey(self.Var_FPS)
            if (cv2.getWindowProperty("Visao Segmentacao", cv2.WND_PROP_VISIBLE) < 1):
                break
    
    def Comando_VisualizarAssociacao(self):
        while True:
            Campo_Virtual = self.Comando_DesenhaTudo(self.Postura_P1, self.Cor_Jogador_1, self.Postura_P2, self.Cor_Jogador_2, self.Postura_P3, self.Cor_Jogador_3,
                                                    self.Posicao_Oponente_1, self.Posicao_Oponente_2, self.Posicao_Oponente_3, self.Cor_Oponente, 
                                                    self.Posicao_Bola, self.Cor_Bola)

            cv2.imshow("Visao Associacao", Campo_Virtual)
            cv2.waitKey(self.Var_FPS) # Está em 25 milisegundos = 40 fps
            if (cv2.getWindowProperty("Visao Associacao", cv2.WND_PROP_VISIBLE) < 1):
                break
        # while True:
        #     elementos = [
        #         {"tipo": "seta", "X": self.Postura_P1[0], "Y": self.Postura_P1[1], "cor": self.Cor_Jogador_1, "orientacao": self.Postura_P1[2]},
        #         {"tipo": "seta", "X": self.Postura_P2[0], "Y": self.Postura_P2[1], "cor": self.Cor_Jogador_2, "orientacao": self.Postura_P2[2]},
        #         {"tipo": "seta", "X": self.Postura_P3[0], "Y": self.Postura_P3[1], "cor": self.Cor_Jogador_3, "orientacao": self.Postura_P3[2]},
        #         {"tipo": "circulo", "X": self.Posicao_Oponente_1[0], "Y": self.Posicao_Oponente_1[1], "cor": self.Cor_Oponente},
        #         {"tipo": "circulo", "X": self.Posicao_Oponente_2[0], "Y": self.Posicao_Oponente_2[1], "cor": self.Cor_Oponente},
        #         {"tipo": "circulo", "X": self.Posicao_Oponente_3[0], "Y": self.Posicao_Oponente_3[1], "cor": self.Cor_Oponente},
        #         {"tipo": "bola", "X": self.Posicao_Bola[0], "Y": self.Posicao_Bola[1], "cor": self.Cor_Bola},
        #     ]

        #     Campo_Virtual = self.Comando_DesenhaTudo(elementos)

        #     cv2.imshow("Visao Associacao", Campo_Virtual)
        #     cv2.waitKey(self.Var_FPS) # Está em 25 milisegundos = 40 fps
        #     if (cv2.getWindowProperty("Visao Associacao", cv2.WND_PROP_VISIBLE) < 1):
        #         break

    
    # # Função genérica para desenhar setas, círculos e bolas
    # def Comando_DesenhaElemento(self, Campo_Virtual, tipo, X, Y, **kwargs):
    #     X = X + 900
    #     Y = Y + 750
    #     coordenadas_centro = (int(X), int(Y))
    #     espessura = 10        
    #     if tipo == "seta":
    #         orientacao = kwargs.get("orientacao", 0)
    #         comprimento = kwargs.get("comprimento", 60)
    #         end_point = (int(X + comprimento * np.cos(-orientacao)), int(Y + comprimento * np.sin(-orientacao)))
    #         cv2.arrowedLine(Campo_Virtual, coordenadas_centro, end_point, kwargs.get("cor", (0, 255, 0)), espessura, cv2.LINE_AA, tipLength=0.2)
    #     elif tipo == "circulo":
    #         raio = kwargs.get("raio", 20)
    #         cv2.circle(Campo_Virtual, coordenadas_centro, raio, kwargs.get("cor", (255, 255, 0)), espessura, cv2.LINE_AA)
    #     elif tipo == "bola":
    #         raio = kwargs.get("raio", 15)
    #         cv2.circle(Campo_Virtual, coordenadas_centro, raio, kwargs.get("cor", (0, 255, 255)), espessura, cv2.LINE_AA)

    # # Função para desenhar robôs do time e robôs adversários
    # def Comando_DesenhaTudo(self, elementos):
    #     Campo_Virtual = self.ImagemCampo_px.copy()
        
    #     for elemento in elementos:
    #         tipo = elemento.get("tipo", None)
    #         if tipo:
    #             X = elemento.get("X", 0)
    #             Y = elemento.get("Y", 0)
    #             cor = elemento.get("cor", None)
    #             if cor is None:
    #                 raise ValueError(f"Cor não especificada para o elemento {tipo}.")
                
    #             if tipo == "seta":
    #                 orientacao = elemento.get("orientacao", 0)
    #                 comprimento = elemento.get("comprimento", 60)
    #                 self.Comando_DesenhaElemento(Campo_Virtual, "seta", X, Y, orientacao=orientacao, comprimento=comprimento, cor=cor)
    #             elif tipo == "circulo":
    #                 raio = elemento.get("raio", 20)
    #                 self.Comando_DesenhaElemento(Campo_Virtual, "circulo", X, Y, raio=raio, cor=cor)
    #             elif tipo == "bola":
    #                 raio = elemento.get("raio", 15)
    #                 self.Comando_DesenhaElemento(Campo_Virtual, "bola", X, Y, raio=raio, cor=cor)
    #             else:
    #                 raise ValueError(f"Tipo de elemento não reconhecido: {tipo}")
        
    #     Campo_Virtual = cv2.resize(Campo_Virtual, (384, 288))
    #     return Campo_Virtual


    def Comando_DesenhaSeta(self, Campo_Virtual, X, Y, Orientacao, Cor=(0, 255, 0), Comprimento=60):
        X = X + 900
        Y = Y + 750
        end_point = (int(X + Comprimento * np.cos(-Orientacao)), int(Y + Comprimento * np.sin(-Orientacao)))
        start_point = (int(X), int(Y))
        espessura = 10
        cv2.arrowedLine(Campo_Virtual, start_point, end_point, Cor, espessura, cv2.LINE_AA, tipLength=0.2)

    # Função para desenhar oponentes como círculos
    def Comando_DesenhaCirculoOponente(self, Campo_Virtual, X, Y, Cor=(255, 255, 0), Raio=20):
        X = X + 900
        Y = Y + 750
        coordenadas_centro = (int(X), int(Y))
        espessura = 10
        cv2.circle(Campo_Virtual, coordenadas_centro, Raio, Cor, espessura, cv2.LINE_AA)

    # Função para desenhar a bola
    def Comando_DesenhaBola(self, Campo_Virtual, X, Y, Cor=(0, 255, 255), Raio=15):
        X = X + 900
        Y = Y + 750
        coordenadas_centro = (int(X), int(Y))
        espessura = 20
        cv2.circle(Campo_Virtual, coordenadas_centro, Raio, Cor, espessura, cv2.LINE_AA)
    
    # Função para desenhar robôs do time e robôs adversários
    def Comando_DesenhaTudo(self, Posicao_Jogador_1, Cor_1, Posicao_Jogador_2, Cor_2, Posicao_Jogador_3, Cor_3, 
                                Posicao_Adversario_1, Posicao_Adversario_2, Posicao_Adversario_3, Cor_Adversario, 
                                Posicao_Bola, Cor_Bola):    
        Campo_Virtual = self.ImagemCampo_px.copy()
        
        if len(Posicao_Jogador_1) == 3:
            self.Comando_DesenhaSeta(Campo_Virtual, Posicao_Jogador_1[0], Posicao_Jogador_1[1], Posicao_Jogador_1[2], Cor_1)
        if len(Posicao_Jogador_2) == 3:
            self.Comando_DesenhaSeta(Campo_Virtual, Posicao_Jogador_2[0], Posicao_Jogador_2[1], Posicao_Jogador_2[2], Cor_2)
        if len(Posicao_Jogador_3) == 3:
            self.Comando_DesenhaSeta(Campo_Virtual, Posicao_Jogador_3[0], Posicao_Jogador_3[1], Posicao_Jogador_3[2], Cor_3)
        if len(Posicao_Adversario_1) == 2:
            self.Comando_DesenhaCirculoOponente(Campo_Virtual, Posicao_Adversario_1[0], Posicao_Adversario_1[1], Cor_Adversario)
        if len(Posicao_Adversario_2) == 2:
            self.Comando_DesenhaCirculoOponente(Campo_Virtual, Posicao_Adversario_2[0], Posicao_Adversario_2[1], Cor_Adversario)
        if len(Posicao_Adversario_3) == 2:
            self.Comando_DesenhaCirculoOponente(Campo_Virtual, Posicao_Adversario_3[0], Posicao_Adversario_3[1], Cor_Adversario)
        if len(Posicao_Bola) == 2:
            self.Comando_DesenhaBola(Campo_Virtual, Posicao_Bola[0], Posicao_Bola[1], Cor_Bola)
        Campo_Virtual = cv2.resize(Campo_Virtual, (384, 288))
        return Campo_Virtual

    def Acao_Jogo(self):
        print('1: ', self.J1.rBDP_pSC_PWM[0], self.J1.rBDP_pSC_PWM[1], '2: ', self.J2.rBDP_pSC_PWM[0], self.J2.rBDP_pSC_PWM[1], '3: ', self.J3.rBDP_pSC_PWM[0], self.J3.rBDP_pSC_PWM[1])
        
        try:
            self.pEsp.write([1, 2, int(self.J1.rBDP_pSC_PWM[0, 0]), int(self.J1.rBDP_pSC_PWM[1, 0]), int(self.J2.rBDP_pSC_PWM[0, 0]), int(self.J2.rBDP_pSC_PWM[1, 0]), int(self.J3.rBDP_pSC_PWM[0, 0]), int(self.J3.rBDP_pSC_PWM[1, 0]), 3, 10])
            EndCycle = time.time()
            TempoVerificacao = EndCycle - self.InicioCiclo
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus('Frequência de Amostragem: %f' % TempoVerificacao)
        except:
            EndCycle = time.time()
            TempoVerificacao = EndCycle - self.InicioCiclo
            self.Limpar_BarraDeStatus()
            self.Atualizar_BarrraDeStatus('Atenção cominicação não Foi iniciada => Frequência de Amostragem: %f' % TempoVerificacao)

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
            self.pEsp.close()
        except Exception as e:
            print(f"Erro ao encerrar a comunicação: {str(e)}")
        
        self.Janela.destroy()

    # Encerra a janela
    def Comando_Parar(self):
        try:
            self.Janela.destroy()
        except Exception as e:
            print(f"Erro ao encerrar a janela: {str(e)}")

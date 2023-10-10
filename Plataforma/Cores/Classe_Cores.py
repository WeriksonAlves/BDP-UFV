'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Script destinado para funções relacionadas à calibragem de cores.

Melhorias: Consertar o vermelho e implementar a segmentação completa
'''

# Importação das bibliotecas
from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
import os

# Definição da classe ColorsWindow para a janela de calibração de cores
class JanelaCores(object):
    # Inicialização dos atributos da classe JanelaCalibracaoCores com valores recebidos como parâmetros
    def __init__(self, Kernel, MedianBlur, MatrizCores, InformacoesCamera, FPS):
        # Variáveis principais:
        self.Var_MedianBlur = MedianBlur
        self.Var_Kernel = Kernel
        self.Var_MatrizCores = MatrizCores
        self.Var_InformacoesCamera = InformacoesCamera
        self.Var_FPS = FPS
        self.Var_Cor = 7  # Cor padrão é cinza
        self.Var_TodasCores = {"Vermelho": IntVar(),"Laranja": IntVar(),"Amarelo": IntVar(),"Verde": IntVar(),"Ciano": IntVar(),"Azul": IntVar(),"Magenta": IntVar(),"Total": IntVar()}
        self.PastaAtual = os.path.dirname(__file__)

        # Executa as funções
        self.Criar_Janela()
        self.Criar_CheckButton()
        self.Criar_TextoInformacao()
        self.Criar_Botao()
        self.Criar_Escala()
    
    # Criação e configuração da janela principal de calibração de cores e da barra de status na parte inferior da janela
    def Criar_Janela(self):
        self.Janela = Toplevel()
        self.Janela.title("Calibrar cores")
        self.Janela.minsize(1380, 700)
        self.Janela.maxsize(1380, 700)
        self.Janela.configure(bg='#229A00')

        self.BarraStatus = Label(self.Janela,
                               text='Instruções: \nSelecionar uma cor \nExibir imagem \nCalibrar a cor desejada \nSalvar calibração',
                               bd=1, relief=SUNKEN, anchor=CENTER)
        self.BarraStatus.pack(side=BOTTOM, fill=X)

    # Função para limpar a barra de status
    def Limpar_BarrraStatus(self):
        self.BarraStatus.config(text="")
        self.BarraStatus.update_idletasks()

    # Função para atualizar a barra de status com um texto específico
    def Atualizar_BarrraStatus(self, texto):
        self.BarraStatus.config(text=texto)
        self.BarraStatus.update_idletasks()

    # Criação das checkbuttons para cada cor disponível
    # Cada checkbutton representa uma cor diferente, e ao ser selecionado, mostra os sliders de calibração
    # Cada cor selecionada é associada a uma matriz de valores de calibração (matiz, saturação e luminosidade)
    def Criar_CheckButton(self):
        Chebut_Vermelho = Checkbutton(self.Janela, text="Vermelho", bg="red", variable=self.Var_TodasCores["Vermelho"], command=lambda: self.Comando_ApenasUmaCor("Vermelho", 0))
        Chebut_Vermelho.place(height=30, width=120, x=0, y=0)

        Chebut_Laranja = Checkbutton(self.Janela, text="Laranja", bg="orange", variable=self.Var_TodasCores["Laranja"], command=lambda: self.Comando_ApenasUmaCor("Laranja", 1))
        Chebut_Laranja.place(height=30, width=120, x=120, y=0)

        Chebut_Amarelo = Checkbutton(self.Janela, text="Amarelo", bg="yellow", variable=self.Var_TodasCores["Amarelo"], command=lambda: self.Comando_ApenasUmaCor("Amarelo", 2))
        Chebut_Amarelo.place(height=30, width=120, x=240, y=0)

        Chebut_Verde = Checkbutton(self.Janela, text="Verde", bg="green", variable=self.Var_TodasCores["Verde"], command=lambda: self.Comando_ApenasUmaCor("Verde", 3))
        Chebut_Verde.place(height=30, width=120, x=360, y=0)

        Chebut_Ciano = Checkbutton(self.Janela, text="Ciano", bg="cyan", variable=self.Var_TodasCores["Ciano"], command=lambda: self.Comando_ApenasUmaCor("Ciano", 4))
        Chebut_Ciano.place(height=30, width=120, x=480, y=0)

        Chebut_Azul = Checkbutton(self.Janela, text="Azul", bg="blue", variable=self.Var_TodasCores["Azul"], command=lambda: self.Comando_ApenasUmaCor("Azul", 5))
        Chebut_Azul.place(height=30, width=120, x=600, y=0)

        Chebut_Magenta = Checkbutton(self.Janela, text="Magenta", bg="magenta", variable=self.Var_TodasCores["Magenta"], command=lambda: self.Comando_ApenasUmaCor("Magenta", 6))
        Chebut_Magenta.place(height=30, width=120, x=720, y=0)

        Chebut_Cinza = Checkbutton(self.Janela, text="Total", bg="gray", variable=self.Var_TodasCores["Total"], command=lambda: self.Comando_ApenasUmaCor("Total",7))
        Chebut_Cinza.place(height=30, width=120, x=840, y=0)

    # Criação dos textos informativos na janela
    def Criar_TextoInformacao(self):
        Txt_Matriz = Label(self.Janela, text="Matriz", bg='#229A00')
        Txt_Matriz.place(height=30, width=50, x=170, y=80)

        Txt_Saturacao = Label(self.Janela, text="Saturação", bg='#229A00')
        Txt_Saturacao.place(height=30, width=60, x=435, y=80)

        Txt_Luminosidade = Label(self.Janela, text="Luminosidade", bg='#229A00')
        Txt_Luminosidade.place(height=30, width=80, x=710, y=80)

        Txt_CampoSegmentado = Label(self.Janela, text="Campo Segmentado", bg='#229A00')
        Txt_CampoSegmentado.place(height=20, width=120, x=10, y=120)

        self.Txt_Rotulo = Label(self.Janela)
        self.Txt_Rotulo.place(height=480, width=1280, x=50, y=140)

    # Criação dos botões para carregar, exibir e salvar a calibração de cores
    def Criar_Botao(self):
        But_CarregarCalibragem = Button(self.Janela, text="Carregar Calibração", command=self.Comando_CarregarTxt)
        But_CarregarCalibragem.place(height=30, width=150, x=5, y=30)

        But_ExibirImagem = Button(self.Janela, text="Exibir Imagem", command=lambda: self.Comando_HSV())
        But_ExibirImagem.place(height=30, width=150, x=5, y=60)

        But_SalvarCalibracao = Button(self.Janela, text="Salvar Calibração", command=self.Comando_SalvarTxt)
        But_SalvarCalibracao.place(height=30, width=150, x=5, y=90)

    # Criação das barras deslizantes (sliders) para calibração das cores
    # Os sliders permitem ajustar os valores de matiz, saturação e luminosidade para cada cor selecionada
    def Criar_Escala(self):
        self.VarM1 = IntVar()
        self.Sca_M1 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM1, bg='#229A00')
        self.Sca_M1.place(height=70, width=190, x=235, y=30)

        self.VarM2 = IntVar()
        self.Sca_M2 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM2, bg='#229A00')
        self.Sca_M2.place(height=70, width=190, x=235, y=70)

        self.VarM3 = IntVar()
        self.Sca_S1 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM3, bg='#229A00')
        self.Sca_S1.place(height=70, width=190, x=505, y=30)

        self.VarM4 = IntVar()
        self.Sca_S2 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM4, bg='#229A00')
        self.Sca_S2.place(height=70, width=190, x=505, y=70)

        self.VarM5 = IntVar()
        self.Sca_B1 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM5, bg='#229A00')
        self.Sca_B1.place(height=70, width=190, x=805, y=30)

        self.VarM6 = IntVar()
        self.Sca_B2 = Scale(self.Janela, from_=0, to=255, orient="horizontal", variable=self.VarM6, bg='#229A00')
        self.Sca_B2.place(height=70, width=190, x=805, y=70)

    # Função para desmarcar todas as checkbuttons
    # Função para desmarcar todas as checkbuttons
    def Comando_DesmarcarTodas(self):
        for cor in self.Var_TodasCores:
            self.Var_TodasCores[cor].set(False)

    # Funções para selecionar apenas uma cor de cada vez e exibir seus valores de calibração nos sliders
    # As funções ativam a checkbutton correspondente e atualizam os sliders com os valores da cor selecionada
    def Comando_ApenasUmaCor(self, Cor, ID):
        self.Comando_DesmarcarTodas()
        self.Var_TodasCores[Cor].set(True)
        self.Var_Cor = ID

        if 0 <= self.Var_Cor <= 6:
            VetorCor = self.Var_MatrizCores[self.Var_Cor]

            self.Sca_M1.set(VetorCor[0])
            self.Sca_M2.set(VetorCor[1])
            self.Sca_S1.set(VetorCor[2])
            self.Sca_S2.set(VetorCor[3])
            self.Sca_B1.set(VetorCor[4])
            self.Sca_B2.set(VetorCor[5])

    # Função para aplicar o filtro de cores HSV na imagem da câmera e exibir o resultado.
    # O filtro é aplicado de acordo com os valores de calibração definidos nos sliders.
    def Comando_HSV(self):
        try:
            _, self.Var_Frames = self.Var_InformacoesCamera.read()
            self.Var_Frames = cv2.medianBlur(self.Var_Frames, self.Var_MedianBlur)
            self.Var_Frames = cv2.resize(self.Var_Frames, [640, 480])

            if 0 <= self.Var_Cor <= 6:
                self.Comando_IdentificarCor(self.Var_Frames)

                self.Var_CorHSV = cv2.cvtColor(self.Var_Frames, cv2.COLOR_BGR2HSV)
                self.Var_LimiteCorInferior = np.array([self.VarM1.get(), self.VarM3.get(), self.VarM5.get()])
                self.Var_LimiteCorSuperior = np.array([self.VarM2.get(), self.VarM4.get(), self.VarM6.get()])
                self.Var_MascaraCor = cv2.inRange(self.Var_CorHSV, self.Var_LimiteCorInferior, self.Var_LimiteCorSuperior)
                self.Var_MascaraCor = cv2.dilate(self.Var_MascaraCor, self.Var_Kernel, iterations=1)
                self.Var_MascaraCor = cv2.medianBlur(self.Var_MascaraCor, self.Var_MedianBlur+4)

                # Colocar aqui o  findcontorns
                                
                self.Var_AplicacaoCor = cv2.bitwise_and(self.Var_Frames, self.Var_Frames, mask=self.Var_MascaraCor)

            elif self.Var_Cor == 7:
                # Inicializar uma máscara vazia
                self.Var_MascaraTotal = np.zeros(self.Var_Frames.shape[:2], dtype=np.uint8)
                self.Var_CorHSV = cv2.cvtColor(self.Var_Frames, cv2.COLOR_BGR2HSV)
                MatrizCores = [None] * 7

                # Aplicar o filtro de cor para cada cor calibrada e realizar a combinação lógica "OR"
                for Id, Dados in enumerate(self.Var_MatrizCores):
                    self.Var_LimiteCorInferior = np.array([Dados[0], Dados[2], Dados[4]])
                    self.Var_LimiteCorSuperior = np.array([Dados[1], Dados[3], Dados[5]])
                    self.Var_MascaraCor = cv2.inRange(self.Var_CorHSV, self.Var_LimiteCorInferior, self.Var_LimiteCorSuperior)
                    self.Var_MascaraCor = cv2.dilate(self.Var_MascaraCor, self.Var_Kernel, iterations=1)  
                    self.Var_MascaraCor = cv2.medianBlur(self.Var_MascaraCor, self.Var_MedianBlur+4)              
                    MatrizCores[Id] = cv2.bitwise_and(self.Var_Frames, self.Var_Frames, mask=self.Var_MascaraCor)

                self.Var_AplicacaoCor = MatrizCores[0]
                for i in range(1, 7):
                    self.Var_AplicacaoCor = cv2.bitwise_or(self.Var_AplicacaoCor, MatrizCores[i])


            else:
                self.Limpar_BarrraStatus()
                self.Atualizar_BarrraStatus("Selecione uma cor")

            self.Var_ConcatenarH = np.concatenate((self.Var_Frames, self.Var_AplicacaoCor), axis=1)
            self.Var_ConversaoRGB = cv2.cvtColor(self.Var_ConcatenarH, cv2.COLOR_BGR2RGB)

            self.Var_Imagem = ImageTk.PhotoImage(Image.fromarray(self.Var_ConversaoRGB))
            self.Txt_Rotulo.configure(image=self.Var_Imagem)
            self.Txt_Rotulo.after(self.Var_FPS, self.Comando_HSV)

        except Exception as e:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus(f"Erro ao processar a imagem: {str(e)}")

    # Função para identificar objetos de uma cor calibrada na imagem da câmera.
    # A cor é filtrada na imagem usando os valores de calibração, e os contornos dos objetos são encontrados.
    def Comando_IdentificarCor(self, Frame):
        CorHSV = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)
        LimiteCorInferior = np.array([self.Var_MatrizCores[self.Var_Cor][0], self.Var_MatrizCores[self.Var_Cor][2], self.Var_MatrizCores[self.Var_Cor][4]])
        LimiteCorSuperior = np.array([self.Var_MatrizCores[self.Var_Cor][1], self.Var_MatrizCores[self.Var_Cor][3], self.Var_MatrizCores[self.Var_Cor][5]])
        MascaraCor = cv2.inRange(CorHSV, LimiteCorInferior, LimiteCorSuperior)
        MascaraCor = cv2.dilate(MascaraCor, self.Var_Kernel, iterations=1)
        self.Contornos, _ = cv2.findContours(MascaraCor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Colocari isto em cima e apagar esta função

        self.Limpar_BarrraStatus()
        self.Atualizar_BarrraStatus("Número de itens identificados: %d." % len(self.Contornos))

    # Função para carregar os valores de calibração da cor a partir de um arquivo de texto.
    # Os valores são carregados na matriz de calibração.
    def Comando_CarregarTxt(self):
        try:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus("Carregando Calibração")
            self.Var_MatrizCores = np.loadtxt(os.path.join(self.PastaAtual, 'MatrizHSV.txt'))
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus("Calibragem carregada.")
        except FileNotFoundError:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus("Arquivo não encontrado. Faça uma nova calibração.")
        except Exception as e:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus(f"Erro ao carregar calibração: {str(e)}")

    # Função para salvar os valores de calibração da cor atual em um arquivo de texto. Os valores são salvos na matriz de calibração com base na cor selecionada.
    def Comando_SalvarTxt(self):
        try:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus("Salvando calibração da cor.")
            Num = self.Var_Cor + 1
            self.Atualizar_BarrraStatus(f"Número de itens identificados: {len(self.Contornos)}.\nCalibragem da cor {Num} salva.")
            self.Var_MatrizCores[self.Var_Cor] = [self.VarM1.get(), self.VarM2.get(), self.VarM3.get(), self.VarM4.get(), self.VarM5.get(), self.VarM6.get()]
            np.savetxt(os.path.join(self.PastaAtual, 'MatrizHSV.txt'), self.Var_MatrizCores, newline='\n')
            self.Var_Cor = 7
        except Exception as e:
            self.Limpar_BarrraStatus()
            self.Atualizar_BarrraStatus(f"Erro ao salvar calibração: {str(e)}")

    # Função para iniciar o loop da janela principal e manter o programa em execução.
    def Comando_Iniciar(self):
        try:
            self.Janela.mainloop()
        except Exception as e:
            print(f"Erro ao executar a janela\nErro: {str(e)}")

    # Função para encerrar a janela principal e finalizar o programa.
    def Comando_Parar(self):
        try:
            self.Janela.quit()
        except Exception as e:
            print(f"Erro ao parar a janela\nErro: {str(e)}")
'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções realcionada a calibragem do campo.
'''

# Importação das bibliotecas
from tkinter import*
import cv2
import numpy as np
import os

# Cria a janela responsável pelas configurações da câmera
class JanelaCampo(object):
    def __init__(self, InformacoesCamera, FPS):
        # Variáveis principais:
        self.Var_InformacoesCamera = InformacoesCamera
        self.Var_FPS = FPS

        self.Pasta_Atual = os.path.dirname(__file__)
        self.Var_Alvo = np.ones((3, 1))
        self.Var_Pontos_Validacao = np.ones((3, 1))
        self.Imagem_Campo_mm = cv2.imread(os.path.join(self.Pasta_Atual, 'Campo_mm.png'))
        self.Imagem_Campo_px = cv2.imread(os.path.join(self.Pasta_Atual, 'Campo_px.png'))
        self.OK = False

        # Executa as funções
        self.Criar_Janela()
        self.Criar_Botoes()

    # Cria e configura a sub-janela
    def Criar_Janela(self):
        self.Janela = Toplevel()
        self.Janela.title("Calibrar Campo")
        self.Janela.minsize(300, 500)
        self.Janela.maxsize(300, 500)
        self.Janela.configure(bg='#229A00')

        self.Barra_Status = Label(self.Janela, text="Instruções:\nCapturar e recortar a imagem\nCorrelacionar os pontos\nSalvar calibração",
                                bd=1, relief=SUNKEN, anchor=CENTER)
        self.Barra_Status.pack(side=BOTTOM, fill=X)

    # Limpa a barra de status
    def Limpar_Barrra_Status(self):
        self.Barra_Status.config(text="")
        self.Barra_Status.update_idletasks()
        
    # Sobrescreve a barra de status
    def Atualizar_BarrraStatus(self, texto):
        self.Barra_Status.config(text=texto)
        self.Barra_Status.update_idletasks()

    # Cria os botões na janela
    def Criar_Botoes(self):
        But_CarregarCalibracao = Button(self.Janela, text="Carregar Calibração", command=self.Comando_CarregarTxt)
        But_CarregarCalibracao.place(height=50, width=200, x=50, y=10)

        But_CapturarImagem = Button(self.Janela, text="Capturar Imagem", command=self.Comando_CapturarImagem)
        But_CapturarImagem.place(height=50, width=200, x=50, y=70)

        But_CorrelacionarPontos = Button(self.Janela, text="Correlacionar Pontos", command=self.Comando_CorrelacionarPontos)
        But_CorrelacionarPontos.place(height=50, width=200, x=50, y=130)

        But_ValidarPontos = Button(self.Janela, text="Validar Pontos", command=self.Comando_ValidarPontos)
        But_ValidarPontos.place(height=50, width=200, x=50, y=190)

        But_SalvarCalibracao = Button(self.Janela, text="Salvar Calibração", command=self.Comando_SalvarCalibracao)
        But_SalvarCalibracao.place(height=50, width=200, x=50, y=250)

    # Carrega a calibração do campo
    def Comando_CarregarTxt(self):
        try:
            self.Var_Matriz_Transformacao_Perspectiva = np.loadtxt(os.path.join(self.Pasta_Atual, 'MatrizTransformação.txt'))
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus("Calibração carregada")
        except FileNotFoundError:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus("Arquivo de calibração não encontrado. Faça uma nova calibração.")
        except Exception as e:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus(f"Erro ao carregar a calibração: {str(e)}")

    # Captura a imagem atual
    def Comando_CapturarImagem(self):
        self.Limpar_Barrra_Status()
        self.Atualizar_BarrraStatus("Capturando imagem do campo")
        try:
            _, self.Var_Quadros = self.Var_InformacoesCamera.read()
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus("Imagem capturada")
        except Exception as e:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus(f"Erro ao capturar a imagem: {str(e)}")

    # Obtem a matriz de transformação de perspectiva do campo
    def Comando_CorrelacionarPontos(self):
        self.Limpar_Barrra_Status()
        self.Atualizar_BarrraStatus("Correlacionando pontos")

        WF = 750
        WA = 600
        HF = 650
        HA = 350
        Pontos_Reais = np.array([[-WF,0,WF,WF,0,-WF,-WA,WA,WA,-WA],[-HF,-HF,-HF,HF,HF,HF,-HA,-HA,HA,HA],[1,1,1,1,1,1,1,1,1,1]])

        if (np.size(self.Var_Alvo,1) > 1):
            self.Var_Alvo = self.Var_Alvo[0:, :1]

        try:
            while True:
                Quadro = cv2.resize(self.Var_Quadros,(640,480))
                Imagem_Campo = cv2.resize(self.Imagem_Campo_mm,(640,480))
                Concatenar_Imagens = np.concatenate((Imagem_Campo, Quadro), axis=1)

                self.Limpar_Barrra_Status()
                self.Atualizar_BarrraStatus(f"Correlacionando o ponto {np.size(self.Var_Alvo,1)}.")
        
                if (np.size(self.Var_Alvo,1) == 11):
                    self.Var_Matriz_Transformacao_Perspectiva = Pontos_Reais @ np.linalg.pinv(self.Var_Alvo[0:, 1:])
                    break
                
                cv2.imshow('Capturar pontos', Concatenar_Imagens)
                cv2.setMouseCallback('Capturar pontos', self.Comando_CorrelacionarPontos_Mouse)
                cv2.waitKey(self.Var_FPS)

                if cv2.getWindowProperty('Capturar pontos', cv2.WND_PROP_VISIBLE) < 1:
                    break
        except Exception as e:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus(f"Erro ao correlacionar pontos: {str(e)}")

        self.Limpar_Barrra_Status()
        self.Atualizar_BarrraStatus("Matriz de transformação obtida.")
        cv2.destroyAllWindows()

    # Função para o evento de clique do mouse durante a correlação de pontos
    def Comando_CorrelacionarPontos_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            Ponto = np.array([[x-640],[y],[1]])
            self.Var_Alvo = np.concatenate((self.Var_Alvo,Ponto),1) 
        elif event == cv2.EVENT_RBUTTONDOWN:
            if np.size(self.Var_Alvo,1) > 1:
                self.Var_Alvo = self.Var_Alvo[0:, 0:-1]

    # Valida a calibração dos pontos
    def Comando_ValidarPontos(self):
        self.Limpar_Barrra_Status()
        self.Atualizar_BarrraStatus("Validando calibração")

        # Redimensiona a imagem da câmera e a imagem de referência para exibir na tela
        self.Img_Quadro = cv2.resize(self.Var_Quadros, (640, 480))
        Imagem_Preview = cv2.resize(self.Imagem_Campo_px, (640, 480))
        self.Var_Imagem_Concatenada = np.concatenate((Imagem_Preview, self.Img_Quadro), axis=1)

        while True:
            # Exibe a imagem para validar os pontos
            cv2.imshow('Validação dos Pontos', self.Var_Imagem_Concatenada)
            cv2.setMouseCallback('Validação dos Pontos', self.Comando_ValidarPontos_Mouse)
            cv2.waitKey(self.Var_FPS)

            # Verifica se a janela de validação está fechada
            if cv2.getWindowProperty('Validação dos Pontos', cv2.WND_PROP_VISIBLE) < 1:
                break

        # Se a validação for bem-sucedida, define a flag de calibração como True
        if self.OK == True:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus("Calibração validada")
                        
    # Função para o evento de clique do mouse durante a validação dos pontos
    def Comando_ValidarPontos_Mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.Var_Pontos_Validacao[0, 0] = x - 640
            self.Var_Pontos_Validacao[1, 0] = y 

            try:
                # Aplica a transformação de perspectiva nos pontos de validação
                AP = self.Var_Matriz_Transformacao_Perspectiva @ self.Var_Pontos_Validacao + np.array([[900], [750], [0]])

                # Desenha um círculo vermelho nos pontos de validação na imagem de referência
                self.Imagem_Validacao = self.Imagem_Campo_px.copy()
                cv2.circle(self.Imagem_Validacao, (int(AP[0, 0]), int(AP[1, 0])), 15, (255, 0, 0), 10)

                # Atualiza a imagem exibida na tela com os pontos de validação marcados
                Imagem_Campo = cv2.resize(self.Imagem_Validacao, (640, 480))
                self.Var_Imagem_Concatenada = np.concatenate((Imagem_Campo, self.Img_Quadro), axis=1)

                # Define a flag de calibração como True, indicando que a validação foi realizada com sucesso
                self.OK = True
            except:
                # Caso ocorra algum erro na validação, exibe mensagem de erro
                self.Limpar_Barrra_Status()
                self.Atualizar_BarrraStatus('Carregue ou faça uma calibração.')

    # Função para salvar a matriz de transformação de perspectiva em um arquivo
    def Comando_SalvarCalibracao(self):
        self.Limpar_Barrra_Status()
        self.Atualizar_BarrraStatus("Salvando calibração")

        try:
            np.savetxt(os.path.join(self.Pasta_Atual, 'MatrizTransformação.txt'), self.Var_Matriz_Transformacao_Perspectiva, newline='\n')
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus("Calibração salva")
        except Exception as e:
            self.Limpar_Barrra_Status()
            self.Atualizar_BarrraStatus(f"Erro ao salvar a calibração: {str(e)}")

    # Função para executar o loop da janela
    def Comando_Iniciar(self):
        try:
            self.Janela.mainloop()
        except:
            pass

    # Função para encerrar a janela
    def Comando_Parar(self):
        try:
            # Liberar recursos e fechar janela do OpenCV ao parar a execução da janela
            cv2.destroyAllWindows()
            self.Janela.quit()
        except:
            pass
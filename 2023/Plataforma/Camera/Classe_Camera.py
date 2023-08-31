'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
Programadores: Mateus Souza e Werikson Alves
:::::::::::::::::::::::::::::::::::::::::::::::::::

Scrip destinado para funções relacionadas à camera.
'''

# Importando bibliotecas necessárias
from tkinter import *
from tkinter import ttk
import cv2
import threading

# Classe para a janela responsável pelas configurações da câmera
class JanelaCamera(object):
    def __init__(self, CameraOn, MedianBlur, FPS):
        # Variáveis principais:
        self.Var_CameraOn = CameraOn 
        self.Var_MedianBlur = MedianBlur
        self.Var_FPS = FPS
        self.Var_PreviewOn = False 
        self.PreviewThread = None
        
        # Executa as funções para criar e configurar a janela
        self.Criar_Janela()
        self.Criar_Menu()
        self.Janela.protocol("WM_DELETE_WINDOW", self.Ao_Fechar_Janela)  # Adiciona tratamento para o fechamento da janela

    # Cria e configura a janela
    def Criar_Janela(self):
        self.Janela = Toplevel()
        self.Janela.title("Configuração da câmera")
        self.Janela.minsize(300, 500)
        self.Janela.maxsize(300, 500)
        self.Janela.configure(bg='#229A00')

        Lab_FPS = Label(self.Janela, text="FPS:")
        Lab_FPS.place(x=50, y=60)

        Lab_Medianblur = Label(self.Janela, text="MedianBlur:")
        Lab_Medianblur.place(x=130, y=60)
        
        self.StatusBar = Label(self.Janela, text="Instruções:\nSelecionar câmera\nConectar câmera\nVisualizar o preview",
                               bd=1, relief=SUNKEN, anchor=CENTER)
        self.StatusBar.pack(side=BOTTOM, fill=X)

    # Limpa a barra de status
    def Limpar_StatusBar(self):
        try:
            self.StatusBar.config(text="")
            self.StatusBar.update_idletasks() 
        except TclError:
            pass

    # Atualiza a barra de status com um texto específico
    def Definir_StatusBar(self, texto):
        try:
            self.StatusBar.config(text=texto)
            self.StatusBar.update_idletasks()
        except TclError:
            pass

    # Cria o menu de opções da janela atual
    def Criar_Menu(self):        
        self.Var_CameraList = self.Obter_Cameras_disponiveis()
        self.Var_SelectCamera = StringVar(value=self.Var_CameraList[0])
        self.Var_ChosenCamera = ttk.Combobox(self.Janela, state='readonly', textvariable=self.Var_SelectCamera, values=self.Var_CameraList, justify='center')
        self.Var_ChosenCamera.place(height=20, width=200, x=50, y=10)
        self.Var_SelectCamera.trace('w', self.Comando_ObterIndiceCamera)

        self.FPS = StringVar(value=str(self.Var_FPS))        
        Ent_FPS = Entry(self.Janela, textvariable=self.FPS)
        Ent_FPS.place(height=20,width=40, x=80, y=60)

        self.MedianBlur = StringVar(value=str(self.Var_MedianBlur))
        Ent_Medianblur = Entry(self.Janela, textvariable=self.MedianBlur)
        Ent_Medianblur.place(height=20,width=40, x=210, y=60)

        But_ConnectCamera = Button(self.Janela, text="Conectar", command=self.Comando_ConectarCamera)
        But_ConnectCamera.place(height=50, width=200, x=50, y=100)

        But_DisconnectCamera = Button(self.Janela, text="Desconectar", command=self.Comando_DesconectarCamera)
        But_DisconnectCamera.place(height=50, width=200, x=50, y=160)

        But_OpenPreview = Button(self.Janela, text="Abrir Preview", command=self.Alternar_Preview)
        But_OpenPreview.place(height=50, width=200, x=50, y=220)
    
    # Obtém a lista de câmeras disponíveis no sistema
    def Obter_Cameras_disponiveis(self):
        cameras = []
        for i in range(10):  # Verificar até 10 possíveis câmeras (pode ajustar esse número conforme necessário)
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                _, _ = cap.read()
                camera_name = f"{i}: Camera {i}"
                cameras.append(camera_name)
                cap.release()
        return cameras

    # Obtém o índice da câmera selecionada
    def Comando_ObterIndiceCamera(self, *arg):
        self.Var_CameraMode = int(self.Var_CameraList[self.Var_ChosenCamera.current()][0])
        if self.Var_CameraOn:
            self.Var_CameraInformation.release()
            self.Var_CameraOn = False

    # Conecta a câmera
    def Comando_ConectarCamera(self):
        # Obtem os valores inseridos nas caixas de entrada
        self.Var_FPS = int(self.FPS.get())
        self.Var_MedianBlur = int(self.MedianBlur.get())        

        if not self.Var_CameraOn:
            self.Limpar_StatusBar()
            self.Definir_StatusBar("Conectando a câmera")
            try:
                self.Var_CameraInformation = cv2.VideoCapture(self.Var_CameraMode, cv2.CAP_DSHOW)
                self.Var_CameraOn, _ = self.Var_CameraInformation.read() 
                self.Limpar_StatusBar()
                self.Definir_StatusBar("Câmera conectada com sucesso. Verifique o Preview.")
            except cv2.error as e:  # Captura exceção específica do OpenCV
                self.Limpar_StatusBar()
                self.Definir_StatusBar(f"Falha na conexão da câmera\nErro: {str(e)}")
            except Exception as e:
                self.Limpar_StatusBar()
                self.Definir_StatusBar(f"Outro erro ocorreu\nErro: {str(e)}")
        else:
            self.Limpar_StatusBar()            
            self.Definir_StatusBar("A câmera já está conectada. Verifique o Preview.")

    # Desconecta a câmera
    def Comando_DesconectarCamera(self):
        if self.Var_CameraOn:
            self.Limpar_StatusBar()
            self.Definir_StatusBar("Desconectando a câmera")
            try:
                self.Var_CameraInformation.release()
                self.Var_CameraOn = False       
                self.Limpar_StatusBar()
                self.Definir_StatusBar("Câmera desconectada com sucesso")
            except cv2.error as e:  # Captura exceção específica do OpenCV
                self.Limpar_StatusBar()
                self.Definir_StatusBar(f"Falha na desconexão da câmera\nErro: {str(e)}")
            except Exception as e:
                self.Limpar_StatusBar()
                self.Definir_StatusBar(f"Outro erro ocorreu\nErro: {str(e)}")
        else:
            self.Limpar_StatusBar()
            self.Definir_StatusBar("A câmera já está desconectada")

    # Abre o preview da câmera
    def Comando_AbrirPreview(self):
        try:
            self.Limpar_StatusBar()
            self.Definir_StatusBar("Visualizando na janela Preview.")

            while True:
                _, self.Var_Frames = self.Var_CameraInformation.read()
                self.Var_Frames = cv2.medianBlur(self.Var_Frames, self.Var_MedianBlur)
                cv2.imshow("Preview", self.Var_Frames)
                cv2.waitKey(self.Var_FPS)

                self.Var_PreviewOn = True
                
                if cv2.getWindowProperty("Preview", cv2.WND_PROP_VISIBLE) < 1:
                    self.Limpar_StatusBar()
                    self.Definir_StatusBar("Sistema de visão conectado\nVá para calibração de cores")
                    self.Var_PreviewOn = False
                    break
            # cv2.destroyAllWindows()
        except cv2.error as e:  # Captura exceção específica do OpenCV
            self.Limpar_StatusBar()
            self.Definir_StatusBar(f"Erro ao abrir o preview\nErro: {str(e)}")
        except Exception as e:
            self.Limpar_StatusBar()
            self.Definir_StatusBar(f"Outro erro ocorreu\nErro: {str(e)}")

    def Alternar_Preview(self):
        if self.Var_PreviewOn:
            self.Fechar_Preview()  # Fecha a janela de visualização se estiver aberta
        else:
            self.Abrir_Preview()  # Abre a janela de visualização se estiver fechada

    def Abrir_Preview(self):
        if self.Var_CameraOn and not self.Var_PreviewOn:
            self.PreviewThread = threading.Thread(target=self.Comando_AbrirPreview)
            self.PreviewThread.start()

    def Fechar_Preview(self):
        if self.Var_PreviewOn:
            self.Var_PreviewOn = False  # Sinaliza para o loop da visualização encerrar
            self.PreviewThread.join()  # Aguarda o encerramento do thread de visualização
            cv2.destroyAllWindows()  # Fecha a janela de visualização do preview

    def Ao_Fechar_Janela(self):
        self.Fechar_Preview()  # Fecha a janela de visualização, se estiver aberta
        self.Janela.destroy()  # Fecha a janela principal

    # Executa o loop da janela 
    def Comando_Iniciar(self):
        try:
            self.Janela.mainloop()
        except Exception as e:
            print(f"Erro ao executar a janela\nErro: {str(e)}")

    # Encerra a janela
    def Comando_Encerrar(self):
        try:
            if self.Var_CameraOn:
                self.Var_CameraInformation.release()
            self.Janela.quit()
        except Exception as e:
            print(f"Erro ao parar a janela\nErro: {str(e)}")
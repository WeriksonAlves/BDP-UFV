'''
:::::::::::::::::::::::::::::::::::::::::::::::::::
:Programadores: Mateus Souza e Werikson Alves   :
:Data de início: 01/05/2022 - Data de término: ?? :
:::::::::::::::::::::::::::::::::::::::::::::::::::

PLATAFORMA BDP 2023

Conjunto de janelas para as informações do sistema
Através de um conjunto de botões será possível selecionar 
as janelas que serão abertas e cada uma será correspondente às
etapas de calibração, ajuste, comunicação e jogo.
'''

from tkinter import*
import sys
from Interface_Camera import*
from Interface_Calibra_Cor import*
from Interface_Calibra_Campo import*

#from Camera_Funcs import*
import cv2
import threading

class Menu_Principal(object):
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = Tk() #Cria a janela
        self.root.title("PLATAFORMA BDP 2023") #Titulo da janela
        self.root.geometry('300x500') # Tamanho da janela
        self.root.configure(bg='green') # Cor de fundo da janela
        self.create_status_bar() # Cria a notas de rodapé
        self.create_menu_button() # Menu inicial do sistema
        self.check = False
    
    # Cria a notas de rodapé
    def create_status_bar(self): 
        self.status = Label(self.root,
                               text="Página Geral do Sistema",
                               bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
    
    # Limpa a nota de rodapé
    def clear_status_bar(self): 
        self.status.config(text="")
        self.status.update_idletasks() 
    
    # Atualiza a nota de rodapé
    def set_status_bar(self, texto): 
        self.status.config(text=texto)
        self.status.update_idletasks()       

    def create_menu_button(self): # Menu inicial do sistema
        # Abre a janela de configurações da camera
        check_cam = Button(self.root, text= "Câmera", command = lambda: Menu_Camera()) 
        check_cam.place(height=50, width=200, x=50, y=10)

        # Abre a janela de calibração de cores
        check_cal_cor = Button(self.root, text= "Calibrar Cores", command = lambda: Menu_Calibra_Cor())
        check_cal_cor.place(height=50, width=200, x=50, y=70)

        # Abre a janela de calibração de campo
        check_cal_cam = Button(self.root, text= "Calibrar Campo", command = lambda: Menu_Calibra_Campo())
        check_cal_cam.place(height=50, width=200, x=50, y=130)

        # Abre a janela de configurações da partida
        check_hab_par = Button(self.root, text= "Habilitar Partida")
        check_hab_par.place(height=50, width=200, x=50, y=190)

        #Encerra o software
        btn_sair = Button(self.root, text= "Encerrar o programa", bg='grey', activebackground='red', command=self.finaliza_software)
        btn_sair.place(height=50, width=200, x=50, y=250)

    def finaliza_software(self):
        self.root.quit()       
    
    def execute(self):
        self.root.mainloop()

#..............................................................................................................
#Colocar isto no programa principal 

def main(args):
    app_proc = Menu_Principal()
    app_proc.execute()
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv))

#                           PLATAFORMA BDP 2022
#
# Conjunto de abas que permite ao usuario ter acesso às  informações do sistema através da interface gráfica. 

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
                            
        self.root = Tk()
        self.root.title("PLATAFORMA BDP 2022")
        self.root.geometry('300x500')
        self.root.configure(bg='green')
        self.create_status_bar()
        self.create_menu_button()
         
    def create_status_bar(self):
        self.status = Label(self.root,
                               text="Página Geral do Sistema",
                               bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
    
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       

    def create_menu_button(self):
        check_cam = Button(self.root, text= "Câmera", command = Menu_Camera)
        check_cam.place(height=50, width=200, x=50, y=10)

        check_cal_cor = Button(self.root, text= "Calibrar Cores", command = Menu_Calibra_Cor)
        check_cal_cor.place(height=50, width=200, x=50, y=70)

        check_cal_cam = Button(self.root, text= "Calibrar Campo", command = Menu_Calibra_Campo)
        check_cal_cam.place(height=50, width=200, x=50, y=130)

        check_hab_par = Button(self.root, text= "Habilitar Partida")
        check_hab_par.place(height=50, width=200, x=50, y=190)

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

#                           PLATAFORMA BDP 2022
#
# Conjunto de abas que permite ao usuario ter acesso às  informações do sistema através da interface gráfica. 

from tkinter import*
import sys
from Funcao_Camera import*


class myApp(object):
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = Tk()
        self.root.title("PLATAFORMA BDP 2022")
        self.root.geometry('800x600')
        self.create_menu_bar()
        self.create_canvas_area()
        self.create_status_bar()
         
         
    def create_status_bar(self):
        self.status = Label(self.root,
                               text="Werikson: Atualmente trabalhando na aba camera!",
                               bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
    
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
    
    def create_menu_bar(self):           
        menubar = Menu(self.root)

        #Termina
        terminamenu = Menu(menubar, tearoff=0)
        terminamenu.add_command(label="Exit", command=self.finaliza_software)
        menubar.add_cascade(label="Sair", menu=terminamenu)

        #Câmera 
        cameramenu = Menu(menubar, tearoff=0)
        cameramenu.add_command(label="Conectar", command=self.mnu_about)
        cameramenu.add_command(label="Iniciar Captura", command=self.mnu_about)
        cameramenu.add_command(label="Abrir Preview", command=self.mnu_about)
        menubar.add_cascade(label="Câmera", menu=cameramenu)
         
        comunicacaoomenu = Menu(menubar, tearoff=0)
        comunicacaoomenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Comunicação", menu=comunicacaoomenu)
        
        calibracaomenu = Menu(menubar, tearoff=0)
        calibracaomenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Calibração", menu=calibracaomenu)
        
        campomenu = Menu(menubar, tearoff=0)
        campomenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Campo", menu=campomenu)
        
        partidamenu = Menu(menubar, tearoff=0)
        partidamenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Partida", menu=partidamenu)
        
        testepwmmenu = Menu(menubar, tearoff=0)
        testepwmmenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="TestePMW", menu=testepwmmenu)
         
        self.root.config(menu=menubar)
    
    def create_canvas_area(self):
        pass
    
  
    def finaliza_software(self):
        self.root.quit()       
     
         
    def mnu_about(self):
        pass
  
     
    def execute(self):
        self.root.mainloop()
#Colocar isto no programa principal 

def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv))

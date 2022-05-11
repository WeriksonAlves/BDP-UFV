
from tkinter import*
import sys

#from Camera_Funcs import*
import cv2
import threading

class myApp(object):
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = Tk()
        self.root.title("PLATAFORMA BDP 2022")
        self.root.geometry('800x600')
        self.create_check_bar()
        self.entry_cal()

 
         
         
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
    
    def create_check_bar(self):           
        check_verm = Checkbutton(self.root, text= "Vermelho", bg= "red")
        check_verm.place(height=50, width=100, x=0, y=(0))

        check_lar = Checkbutton(self.root, text= "Laranja",bg= "orange")
        check_lar.place(height=50, width=100, x=100, y=(0))

        check_amar = Checkbutton(self.root, text= "Amarelo",bg= "yellow")
        check_amar.place(height=50, width=100, x=200, y=(0))

        check_verd = Checkbutton(self.root, text= "Verde",bg= "green")
        check_verd.place(height=50, width=100, x=300, y=(0))

        check_ciano = Checkbutton(self.root, text= "Ciano",bg= "cyan")
        check_ciano.place(height=50, width=100, x=400, y=(0))

        check_azul = Checkbutton(self.root, text= "Azul",bg= "blue")
        check_azul.place(height=50, width=100, x=500, y=(0))

        check_mag = Checkbutton(self.root, text= "Magenta",bg= "magenta" )
        check_mag.place(height=50, width=100, x=600, y=(0))

        check_tot =  Checkbutton(self.root, text= "Total",bg= "gray")
        check_tot.place(height=50, width=100, x=700, y=(0))
    def entry_cal(self):
        set_entry_m1 = Entry(self.root)
        set_entry_m1.place(height=30, width=50, x=20, y=(100))
        set_entry_s1 = Entry(self.root)
        set_entry_s1.place(height=30, width=50, x=20, y=(150))


    def finaliza_software(self):
        self.root.quit()       
     
    def execute(self):
        self.root.mainloop()
#Colocar isto no programa principal 

def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv))

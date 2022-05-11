
from tkinter import*
import sys

#from Camera_Funcs import*
import cv2
import threading

class myApp(object):
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = Tk()
        self.root.title("Calibrar Cores")
        self.root.geometry('940x600')
        self.create_check_bar()
        self.entry_cal()
        self.escalas()
        self.create_text()
        self.create_buttons()
         
    def create_text(self):
        text_1 = Label(self.root,text="Matriz")
        text_1.place(height=30, width=50, x=180, y=(60))
        text_2 = Label(self.root,text="Saturação")
        text_2.place(height=30, width=60, x=470, y=(60))
        text_3 = Label(self.root,text="Luminosidade")
        text_3.place(height=30, width=80, x=750, y=(60))
        text_4 = Label(self.root,text="Campo Segmentado:")
        text_4.place(height=20, width=120, x=15, y=(270))
    
    def create_buttons(self):
        Select_pixels = Button(self.root, text= "Selecionar Pixels")
        Select_pixels.place(height=40, width=150, x=20, y=(200))

        Save_cal = Button(self.root, text= "Selecionar Pixels")
        Save_cal.place(height=40, width=150, x=180, y=(200))
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
    
    def create_check_bar(self):           
        check_verm = Checkbutton(self.root, text= "Vermelho", bg= "red")
        check_verm.place(height=50, width=120, x=0, y=(0))

        check_lar = Checkbutton(self.root, text= "Laranja",bg= "orange")
        check_lar.place(height=50, width=120, x=120, y=(0))

        check_amar = Checkbutton(self.root, text= "Amarelo",bg= "yellow")
        check_amar.place(height=50, width=120, x=240, y=(0))

        check_verd = Checkbutton(self.root, text= "Verde",bg= "green")
        check_verd.place(height=50, width=120, x=360, y=(0))

        check_ciano = Checkbutton(self.root, text= "Ciano",bg= "cyan")
        check_ciano.place(height=50, width=120, x=480, y=(0))

        check_azul = Checkbutton(self.root, text= "Azul",bg= "blue")
        check_azul.place(height=50, width=120, x=600, y=(0))

        check_mag = Checkbutton(self.root, text= "Magenta",bg= "magenta" )
        check_mag.place(height=50, width=120, x=720, y=(0))

        check_tot =  Checkbutton(self.root, text= "Total",bg= "gray")
        check_tot.place(height=50, width=120, x=820, y=(0))
    
    def entry_cal(self):
        set_entry_m1 = Entry(self.root)
        set_entry_m1.place(height=30, width=50, x=40, y=(100))
        set_entry_s1 = Entry(self.root)
        set_entry_s1.place(height=30, width=50, x=40, y=(130))

        set_entry_m2 = Entry(self.root)
        set_entry_m2.place(height=30, width=50, x=330, y=(100))
        set_entry_s2 = Entry(self.root)
        set_entry_s2.place(height=30, width=50, x=330, y=(130))

        set_entry_m3 = Entry(self.root)
        set_entry_m3.place(height=30, width=50, x=620, y=(100))
        set_entry_s3 = Entry(self.root)
        set_entry_s3.place(height=30, width=50, x=620, y=(130))

    def escalas(self):
        escal_m1 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_m1.place(height=70, width=200, x=110, y=(85))

        escal_m2 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_m2.place(height=70, width=200, x=110, y=(120))

        escal_s1 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_s1.place(height=70, width=200, x=400, y=(85))

        escal_s2 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_s2.place(height=70, width=200, x=400, y=(120))

        escal_s3 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_s3.place(height=70, width=200, x=690, y=(85))

        escal_s3 = Scale(self.root, from_ = 1, to = 200, orient = "horizontal")
        escal_s3.place(height=70, width=200, x=690, y=(120))

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

#                           Menu da Câmera
#
# Conjunto de abas relacionadas a câmera.

from tkinter import*
import tkinter as tk
import sys
import cv2
import threading
from BDPsystem import*
class Menu_Camera(object):
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root_camera = Toplevel()
        self.root_camera.title("Câmera")
        self.root_camera.geometry('300x500')
        self.root_camera.configure(bg='green')
        self.create_menu_button()
        self.create_status_bar()
        self.execute()
        

    def create_status_bar(self):
        self.status = tk.Label(self.root_camera,
                               text="Iniciando o sistema câmera",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
 
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
 
    def create_menu_button(self):           
        btn_con = Button(self.root_camera, text= "Conectar", command = self.Camconectar)
        btn_con.place(height=50, width=200, x=50, y=10)

        btn_abr_pre = Button(self.root_camera, text= "Abrir Preview", command = lambda: threading.Thread(target=self.Campreview).start())
        btn_abr_pre.place(height=50, width=200, x=50, y=70)
 
    def Camconectar(self):
        #Para opção webcam n = 0, para realsense n = 2. Conferir gerenciador de dispositivos
        self.tipo_camera = 0
        Menu_Principal.teste = 10

        #self.cam = cv2.VideoCapture(tipo_camera)
        self.cam = cv2.VideoCapture(self.tipo_camera, cv2.CAP_DSHOW)#corrigi bug ao fechar aplicação

    
    def Campreview(self):
        while True:
            self.ret, self.frame = self.cam.read() # retorna True ou False para a camera
            print(type(self.cam))
            if not self.ret:
                print("Câmera desativada")
                break
            cv2.imshow("preview", self.frame)
            k = cv2.waitKey(25) #40 fps
            if (cv2.getWindowProperty("preview", cv2.WND_PROP_VISIBLE) <1):
                break
        #cam2 = self.cam
        #cam2.release()  #Desliga a camera
        cv2.destroyAllWindows()
    
    def execute(self):
        self.root_camera.protocol("WM_DELETE_WINDOW", self.a)
        self.root_camera.mainloop()

    def a(self):
        print("A")
        self.root_camera.withdraw()
        


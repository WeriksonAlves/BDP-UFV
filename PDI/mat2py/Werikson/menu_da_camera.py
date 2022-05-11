#                           Menu da Câmera
#
# Conjunto de abas relacionadas a câmera.

from tkinter import*
import tkinter as tk
import sys
import cv2
import threading

class mycamera(object):
     
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = tk.Tk()
        self.root.title("Câmera")
        self.root.geometry('300x500')
        self.root.configure(bg='green')
        self.create_menu_button()
 
        self.create_status_bar()
         
    def create_status_bar(self):
        self.status = tk.Label(self.root,
                               text="",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
 
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
 
    def create_menu_button(self):           
        btn_con = Button(self.root, text= "Conectar", command = self.Camconectar)
        btn_con.place(height=50, width=200, x=50, y=10)

        btn_abr_pre = Button(self.root, text= "Abrir Preview", command = lambda: threading.Thread(target=self.Campreview).start())
        btn_abr_pre.place(height=50, width=200, x=50, y=70)
 
    def Camconectar(self):
        #Para opção webcam n = 0, para realsense n = 2. Conferir gerenciador de dispositivos
        tipo_camera = 0

        #self.cam = cv2.VideoCapture(tipo_camera)
        self.cam = cv2.VideoCapture(tipo_camera, cv2.CAP_DSHOW)#corrigi bug ao fechar aplicação
        

    def Campreview(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("Câmera desativada")
                break
            cv2.imshow("preview", frame)
            k = cv2.waitKey(1)
            if (cv2.getWindowProperty("preview", cv2.WND_PROP_VISIBLE) <1):
                break
        cam2 = self.cam
        #cam2.release()  #Desliga a camera
        cv2.destroyAllWindows()
  
     
    def execute(self):
        self.root.mainloop()


#.mainTk.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#{fileheader}

 
import tkinter as tk
import sys
 

class myApp(object):
     
    def __init__(self, **kw):
        #insira toda a inicialização aqui
                            
        self.root = tk.Tk()
        self.root.title("Titulo da janela da aplicação")
        self.root.geometry('800x600')
        self.create_menu_bar()
        self.create_canvas_area()
        self.create_status_bar()
         
         
    def create_status_bar(self):
        self.status = tk.Label(self.root,
                               text="Welcome to myApp",
                               bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
 
    def clear_status_bar(self):
        self.status.config(text="")
        self.status.update_idletasks() 
         
    def set_status_bar(self, texto):
        self.status.config(text=texto)
        self.status.update_idletasks()       
 
    def create_menu_bar(self):           
        menubar = tk.Menu(self.root)
         
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.finaliza_software)
        
        
        menubar.add_cascade(label="File", menu=filemenu)
         
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.mnu_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
         
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
'''
def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 

if __name__ == '__main__':
    sys.exit(main(sys.argv))
'''
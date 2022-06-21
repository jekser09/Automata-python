from Automatas import *
from tkinter import *

class Ventana():
    def __init__(self):
        self.__raiz=Tk()
        self.__raiz.title("Teoria de la computacion")
        self.__raiz.resizable(False, False)
        self.__raiz.geometry("700x400")
        self.__frame=Frame(bg="#577615",bd=4,relief="solid")
        self.__frame.pack(fill="both",expand="True")
        automata=Automatas()
        
        Label(self.__frame,bg="#577615",text="Automatas AFD",fg="Black",font=("Comic Sans MS",25)).grid(row=0,column=0,columnspan=3,ipadx=221,pady=10)
        Label(self.__frame,bg="#577615",text="Cadena:",fg="Black",font=("Comic Sans MS",15)).grid(row=1,column=0,sticky=E)
        Entry(self.__frame,fg="Black",font=("Comic Sans MS",12),bg="#E6D375",relief="groove",justify=CENTER).grid(row=1,column=1,ipadx=40)
        Label(self.__frame,bg="#577615",text="A. Entero:",fg="Black",font=("Comic Sans MS",15)).grid(row=2,column=0,sticky=E)
        self.lblEntero=Label(self.__frame,bg="#3E5410",text="Analizando...",fg="Black",font=("Comic Sans MS",11),relief="sunken").grid(row=2,column=1,ipadx=123,pady=15)
        Label(self.__frame,bg="#577615",text="A. Real:",fg="Black",font=("Comic Sans MS",15)).grid(row=3,column=0,sticky=E)
        self.lblReal=Label(self.__frame,bg="#3E5410",text="Analizando...",fg="Black",font=("Comic Sans MS",11), relief="sunken").grid(row=3,column=1,ipadx=123,pady=15)
        Label(self.__frame,bg="#577615",text="A. Notacion C:",fg="Black",font=("Comic Sans MS",15)).grid(row=4,column=0,sticky=E)
        self.lblNotacion=Label(self.__frame,bg="#3E5410",text="Analizando...",fg="Black",font=("Comic Sans MS",11), relief="sunken").grid(row=4,column=1,ipadx=123,pady=15)
        Label(self.__frame,bg="#577615",text="A. Correo:",fg="Black",font=("Comic Sans MS",15)).grid(row=5,column=0,sticky=E)
        self.lblCorreo=Label(self.__frame,bg="#3E5410",text="Analizando...",fg="Black",font=("Comic Sans MS",11), relief="sunken").grid(row=5,column=1,ipadx=123,pady=15)
        Button(self.__frame,text="Comprobar").grid(row=3,column=2)



        self.__raiz.mainloop()
Ventana()
        
        
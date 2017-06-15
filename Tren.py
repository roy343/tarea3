import tkinter
from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading
import winsound
import random

class Tren:
    def __init__(self,num,ruta,hora,maq,vags):
        self.num=num
        self.ruta=ruta
        self.hora=hora
        self.maquna=maq
        self.vagones=vags
        self.head=None  
        self.tail=None
        self.largo=0
        
    def get_num(self):
        return self.num
    def set_num(self,num):
        self.num=num
        
    def get_ruta(self):
        return self.ruta
    def set_ruta(self,ruta):
        self.ruta=ruta
        
    def get_hora(self):
        return self.hora
    def set_hora(self,hora):
        self.hora=hora
        
    def get_maq(self):
        return self.maq
    def set_maq(self,maq):
        self.maq=maq

    def get_vag(self):
        return self.vag
    def set_vag(self,vag):
        self.vag=vag
            
class Maquina:
    def __init__(self,num,cap):
        self.num=num
        self.cap=cap   

class Vagon:
    def __init__(self,num,cant,next=None,prev=None):
        self.num=num
        self.cant=cant
        self.next=next
        self.prev=prev

def cargarImagen(nombre):
    ruta = os.path.join('Material',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

ventana = Tk()
ventana.title("Estación TEC")
ventana.minsize(1300,700)
ventana.resizable(width=NO,height=NO)

ventana1=tkinter.Canvas(ventana,width=1400,height=800,bg="white")
ventana1.place(x=0,y=0)

ventana2=tkinter.Canvas(ventana,width=1405,height=200,bg="gray")
ventana2.place(x=-5,y=500)

img=cargarImagen("0.gif")
tren = Label(ventana1,image=img,bg="white")
tren.place(x=100,y=100)
tren.image = img

#Dejo el thread desactivado para trabajar
'''def trenanimacion(): 
    i = 0
    try:
        while i < 2:
            img = cargarImagen(str(i)+".gif")
            tren.configure(image=img)
            tren.image = img
            i += 1
            if i == 2:
                i = 0
            time.sleep(0.21)
    except Exception as errtxt:
        print("Error en hilo")
def ver_trenanimacion():
    trent = Thread(target=trenanimacion, args=())
    trent.start()
ver_trenanimacion()'''
#############################################################3
clientes = 0
#Prototipo del reloj
'''hora = 12
minutos = 30

texth = str(hora)
lblhora = Label(ventana1, text= texth, bg="white").place(x=1250,y=0)
lbl = Label(ventana1, text= ":", bg="white").place(x=1270,y=0)
textm = str(minutos)
lblminutos = Label(ventana1, text= textm, bg="white").place(x=1280,y=0)

def hora():
    global hora
    global minutos
    try:
        while 1:
            if minutos == "00":
                minutos = 15
            elif minutos == 60:
                minutos = "00"
                hora += 1
                if hora == 24:
                    hora = 0
            else:
                minutos += 15
            texth = str(hora)
            lblhora.configure(text = texth)
            textm = str(minutos)
            lblminutos.configure(text = textm)
            time.sleep(2.0)      
    except Exception as errtxt:
        print("Error en hilo")
def ver_hora():
    horah = Thread(target=hora, args=())
    horah.start()
ver_hora()'''

def pasajeros():
    global clientes
    if clientes == 0:
        can = random.randint(1, 100)
        lblcan = Label(ventana2,text=str(can),bg="black",fg="white").place(x=218,y=30)
        clientes = 1
    else:
        return None

def vagones():
    ventana5 = Toplevel()
    ventana5.title("Administración de vagones")
    ventana5.minsize(200,200)
    ventana5.resizable(width=NO,height=NO)

    canvas3 = Canvas(ventana5,width=200,height=200,bg="white")
    canvas3.place(x=0,y=0)

    def vagon_automatico():
        ventana5.destroy()
        
        ventana6 = Toplevel()
        ventana6.title("Qué quieres hacer?")
        ventana6.minsize(200,200)
        ventana6.resizable(width=NO,height=NO)
    
        canvas4 = Canvas(ventana6,width=200,height=200,bg="white")
        canvas4.place(x=0,y=0)

        def posicion():
            ventana6.destroy()
   
        boton19 = Button(canvas4, command=posicion,text="      Llenar vagones      ", bg = "#000000", fg = "#FFFFFF").place(x=35,y=50)
        boton20 = Button(canvas4, command=posicion,text="      Quitar vagones      ", bg = "#000000", fg = "#FFFFFF").place(x=35,y=125)
    
    def vagon_manual():
        ventana5.destroy()
        
        ventana3 = Toplevel()
        ventana3.title("Añadir vagon de...")
        ventana3.minsize(200,200)
        ventana3.resizable(width=NO,height=NO)
    
        canvas = Canvas(ventana3,width=200,height=200,bg="white")
        canvas.place(x=0,y=0)

        def posicion():
            ventana3.destroy()

            ventana4 = Toplevel()
            ventana4.title("Posición")
            ventana4.minsize(200,200)
            ventana4.resizable(width=NO,height=NO)
    
            canvas2 = Canvas(ventana4,width=200,height=200,bg="white")
            canvas2.place(x=0,y=0)

            Label(canvas2,text="...O en la posición:",bg="white",fg="black").place(x=25,y=125)

            pos=Entry(canvas2,width=3).place(x=135,y=125)
        
            def posicion():
                ventana4.destroy()

            boton14 = Button(canvas2, command=posicion,text="      Al inicio      ", bg = "#000000", fg = "#FFFFFF").place(x=52,y=25)
            boton15 = Button(canvas2, command=posicion,text="      Al final      ", bg = "#000000", fg = "#FFFFFF").place(x=55,y=65)
            boton16 = Button(canvas2, command=posicion,text="Aceptar", bg = "#000000", fg = "#FFFFFF").place(x=70,y=165)
    
        boton11 = Button(canvas, command=posicion,text="      20 personas      ", bg = "#000000", fg = "#FFFFFF").place(x=50,y=31)
        boton12 = Button(canvas, command=posicion,text="      30 personas      ", bg = "#000000", fg = "#FFFFFF").place(x=50,y=87)
        boton13 = Button(canvas, command=posicion,text="      50 personas      ", bg = "#000000", fg = "#FFFFFF").place(x=50,y=143)

    boton17 = Button(canvas3, command=vagon_automatico, text="      Automático      ", bg = "#000000", fg = "#FFFFFF").place(x=45,y=50)
    boton18 = Button(canvas3, command=vagon_manual, text="      Manual      ", bg = "#000000", fg = "#FFFFFF").place(x=55,y=125)

#########################################################################
boton1 = Button(ventana2, text="      Iniciar Simulación      ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=5)
boton2 = Button(ventana2, text="        Rutas por horas        ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=35)
boton3 = Button(ventana2, command = pasajeros, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF").place(x=655,y=35)
boton4 = Button(ventana2, command = vagones, text="      Administración de vagones   ", bg = "#000000", fg = "#FFFFFF").place(x=655,y=5)
boton5 = Button(ventana2, text="          Salida de tren          ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=65)
boton6 = Button(ventana2, text="               Llegada de tren               ", bg = "#000000", fg = "#FFFFFF").place(x=655,y=65)

Label(ventana2,text="Hora de llegada/salida:",bg="black",fg="white").place(x=10,y=5)

Label(ventana2,text="Cantidad de personas que van a viajar:",bg="black",fg="white").place(x=10,y=30)


ventana.mainloop ()

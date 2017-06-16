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

def pasajeros():
    global clientes
    if clientes == 0:
        can = random.randint(1, 100)
        lblcan = Label(ventana2,text=str(can),bg="black",fg="white").place(x=218,y=30)
        clientes = 1
    else:
        return None

def vagones():
    ventana_vagones = Toplevel()
    ventana_vagones.title("Administración de vagones")
    ventana_vagones.minsize(200,200)
    ventana_vagones.resizable(width=NO,height=NO)

    canvas_vagones = Canvas(ventana_vagones,width=200,height=200,bg="white")
    canvas_vagones.place(x=0,y=0)

    def vagon_automatico():
        ventana_vagones.destroy()
        
        ventana_auto = Toplevel()
        ventana_auto.title("Qué quieres hacer?")
        ventana_auto.minsize(200,200)
        ventana_auto.resizable(width=NO,height=NO)
    
        canvas_auto = Canvas(ventana_auto,width=200,height=200,bg="white")
        canvas_auto.place(x=0,y=0)

        def llenar_auto():
            ventana_auto.destroy()

        def quitar_auto():
            ventana_auto.destroy()
   
        boton1 = Button(canvas_auto, command=llenar_auto,text="      Llenar vagones      ", bg = "#000000", fg = "#FFFFFF")
        boton1.place(x=35,y=50)
        boton2 = Button(canvas_auto, command=quitar_auto,text="      Quitar vagones      ", bg = "#000000", fg = "#FFFFFF")
        boton2.place(x=35,y=125)
    
    def vagon_manual():
        ventana_vagones.destroy()
        
        ventana_man = Toplevel()
        ventana_man.title("Añadir vagon de...")
        ventana_man.minsize(200,200)
        ventana_man.resizable(width=NO,height=NO)
    
        canvas_man = Canvas(ventana_man,width=200,height=200,bg="white")
        canvas_man.place(x=0,y=0)

        def posicion():
            ventana_man.destroy()

            ventana_pos = Toplevel()
            ventana_pos.title("Posición")
            ventana_pos.minsize(200,200)
            ventana_pos.resizable(width=NO,height=NO)
    
            canvas_pos = Canvas(ventana_pos,width=200,height=200,bg="white")
            canvas_pos.place(x=0,y=0)

            Label(canvas_pos,text="...O en la posición:",bg="white",fg="black").place(x=25,y=125)

            pos=Entry(canvas_pos,width=3).place(x=135,y=125)
        
            def colocar():
                ventana_pos.destroy()

            boton1 = Button(canvas_pos, command=colocar,text="      Al inicio      ", bg = "#000000", fg = "#FFFFFF")
            boton1.place(x=52,y=25)
            boton2 = Button(canvas_pos, command=colocar,text="      Al final      ", bg = "#000000", fg = "#FFFFFF")
            boton2.place(x=55,y=65)
            boton3 = Button(canvas_pos, command=colocar,text="Aceptar", bg = "#000000", fg = "#FFFFFF")
            boton3.place(x=70,y=165)
    
        boton1 = Button(canvas_man, command=posicion,text="      20 personas      ", bg = "#000000", fg = "#FFFFFF")
        boton1.place(x=50,y=31)
        boton2 = Button(canvas_man, command=posicion,text="      30 personas      ", bg = "#000000", fg = "#FFFFFF")
        boton2.place(x=50,y=87)
        boton3 = Button(canvas_man, command=posicion,text="      50 personas      ", bg = "#000000", fg = "#FFFFFF")
        boton3.place(x=50,y=143)

    boton1 = Button(canvas_vagones, command=vagon_automatico, text="      Automático      ", bg = "#000000", fg = "#FFFFFF")
    boton1.place(x=45,y=50)
    boton2 = Button(canvas_vagones, command=vagon_manual, text="      Manual      ", bg = "#000000", fg = "#FFFFFF")
    boton2.place(x=55,y=125)

#########################################################################
boton1 = Button(ventana2, text="      Iniciar Simulación      ", bg = "#000000", fg = "#FFFFFF")
boton1.place(x=505,y=5)
boton2 = Button(ventana2, text="        Rutas por horas        ", bg = "#000000", fg = "#FFFFFF")
boton2.place(x=505,y=35)
boton3 = Button(ventana2, command = pasajeros, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF")
boton3.place(x=655,y=35)
boton4 = Button(ventana2, command = vagones, text="      Administración de vagones   ", bg = "#000000", fg = "#FFFFFF")
boton4.place(x=655,y=5)
boton5 = Button(ventana2, text="          Salida de tren          ", bg = "#000000", fg = "#FFFFFF")
boton5.place(x=505,y=65)
boton6 = Button(ventana2, text="               Llegada de tren               ", bg = "#000000", fg = "#FFFFFF")
boton6.place(x=655,y=65)

Label(ventana2,text="Hora de llegada/salida:",bg="black",fg="white").place(x=10,y=5)
Label(ventana2,text="Cantidad de personas que van a viajar:",bg="black",fg="white").place(x=10,y=30)

ventana.mainloop ()

import tkinter
from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading
import winsound

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
    def get_num(self):
        return self.num
    def set_num(self,num):
        self.num=num

    def get_cap(self):
        return self.cap
    def set_cap(self,cap):
        self.cap=cap

class Vagon:
    def __init__(self,num,cant,next=None,prev=None):
        self.num=num
        self.cant=cant
        self.next=next
        self.prev=prev
    def get_num(self):
        return self.num
    def set_num(self,num):
        self.num=num

    def get_cant(self):
        return self.cant
    def set_cant(self,cant):
        self.cant=cant

ventana = Tk()
ventana.title("Estación TEC")
ventana.minsize(1400,900)
ventana.resizable(width=NO,height=NO)

ventana1=tkinter.Canvas(ventana,width=1400,height=800,bg="white")
ventana1.place(x=0,y=0)

ventana2=tkinter.Canvas(ventana,width=1405,height=200,bg="gray")
ventana2.place(x=-5,y=800)

boton1 = Button(ventana2, text="      Iniciar Simulación      ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=5)
boton2 = Button(ventana2, text="        Rutas por horas        ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=35)
boton3 = Button(ventana2, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF").place(x=655,y=35)
boton4 = Button(ventana2, text="      Administración de vagones   ", bg = "#000000", fg = "#FFFFFF").place(x=655,y=5)
boton5 = Button(ventana2, text="          Salida de tren          ", bg = "#000000", fg = "#FFFFFF").place(x=505,y=65)
boton6 = Button(ventana2, text="               Llegada de tren               ", bg = "#000000", fg = "#FFFFFF").place(x=655,y=65)
boton7 = Button(ventana2, text="   Llenar vagones   ", bg = "#000000", fg = "#FFFFFF").place(x=1245,y=5)
boton8 = Button(ventana2, text="   Añadir vagones  ", bg = "#000000", fg = "#FFFFFF").place(x=1245,y=35)
boton9 = Button(ventana2, text="   Quitar vagones  ", bg = "#000000", fg = "#FFFFFF").place(x=1245,y=65)
boton9 = Button(ventana2, text=" Salir de la estacion ", bg = "#000000", fg = "#FFFFFF").place(x=1125,y=5)

Label(ventana2,text="Hora de llegada/salida:",bg="black",fg="white").place(x=10,y=5)


Label(ventana2,text="Cantidad de pasajeros:",bg="black",fg="white").place(x=10,y=30)


ventana.mainloop ()

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
ventana.minsize(1000,650)
ventana.resizable(width=NO,height=NO)

ventana1=tkinter.Canvas(ventana,width=1700,height=900,bg="white")
ventana1.place(x=0,y=0)

boton1 = Button(ventana1, text="Iniciar Simulación", bg = "#000000", fg = "#FFFFFF").place(x=2,y=2)
boton2 = Button(ventana1, text="Rutas por horas", bg = "#000000", fg = "#FFFFFF").place(x=2,y=33)
boton3 = Button(ventana1, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF").place(x=2,y=63)
boton4 = Button(ventana1, text="Administración de vagones", bg = "#000000", fg = "#FFFFFF").place(x=2,y=93)
boton5 = Button(ventana1, text="Salida de tren", bg = "#000000", fg = "#FFFFFF").place(x=2,y=123)
boton6 = Button(ventana1, text="Llegada de tren", bg = "#000000", fg = "#FFFFFF").place(x=2,y=153)

ventana.mainloop ()

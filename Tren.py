import tkinter
from tkinter import *
from tkinter import messagebox
import os
import time
from threading import Thread
import threading
import winsound

ventana = Tk()
ventana.title("Estación TEC")
ventana.geometry("1700x900+50+50")
ventana.resizable(width=NO,height=NO)

ventana1=tkinter.Canvas(ventana,width=1700,height=900,bg="white")
ventana1.place(x=0,y=0)


boton1 = Button(ventana, text="Iniciar Simulación", bg = "#000000", fg = "#FFFFFF").place(x=2,y=2)
boton2 = Button(ventana, text="Rutas por horas", bg = "#000000", fg = "#FFFFFF").place(x=2,y=33)
boton3 = Button(ventana, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF").place(x=2,y=63)
boton4 = Button(ventana, text="Administración de vagones", bg = "#000000", fg = "#FFFFFF").place(x=2,y=93)
boton5 = Button(ventana, text="Salida de tren", bg = "#000000", fg = "#FFFFFF").place(x=2,y=123)
boton6 = Button(ventana, text="Llegada de tren", bg = "#000000", fg = "#FFFFFF").place(x=2,y=153)








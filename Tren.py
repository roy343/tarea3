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
        self.maquina=Maquina(num = maq, cap = 3)
        self.vagones=vags
        self.head=None  
        self.tail=None
        self.largo=0

    def get_vag(self):
        return self.vag
    def set_vag(self,vag):
        self.vag=vag

    def mostrar (self):
        print (self.maquina.num)
        nodo = self.head
        while nodo != None:
            print (nodo.num)
            nodo = nodo.next

    def agregar_inicio (self, num, cant):
        self.largo += 1
        if self.head == None: 
            self.head = Vagon (num = num, cant = cant)
            self.tail = self.head
        else:
            temp = Vagon (num = num, cant = cant)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def agregar_final (self, num, cant):
        self.largo += 1
        if self.head == None: 
            self.head = Vagon (num = num, cant = cant)
            self.tail = self.head
        else:
            temp = self.tail
            temp2 = Vagon (num = num, cant = cant)
            temp.next = temp2
            temp2.prev = temp
            self.tail = temp2

    def agregar_medio (self, pos, num, cant):
        if self.head == None:
            self.head = Vagon (num = num, cant = cant)
            self.tail = self.head
        elif self.head != None and pos == 1:
            temp = Vagon (num = num, cant = cant)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        else:
            i = 1
            temp = self.head
            while temp.next != None:
                i += 1
                if i == pos:
                    break
                temp = temp.next
            izq = temp.prev
            der = temp
            med = Vagon (num = num, cant = cant)
            if i == pos-1:
                der.next = med
                med.prev = der
                self.tail = med
            elif i == pos:
                izq = temp
                der = temp.next
                izq.next = med
                med.next = der
                der.prev = med
                med.prev = izq
            else:
                return 'Error'

    def quitar_vagones (self):
        self.head = None
        self.tail = None
        self.largo = 0

    def quitar_vagon (self, pos):
        temp = self.head
        if pos > self.largo:
            return 'Error'
        if pos == 1:
            self.head = temp.next
            self.largo -=1
        elif pos == self.largo:
            temp = self.tail
            temp2 = temp.prev
            self.tail = temp2
            temp2.next = None
            self.largo -=1
        else:
            i = 1
            while i != pos:
                temp = temp.next
                i += 1
            temp_1 = temp.prev
            temp_1.next = temp.next
            self.largo -=1

    #Falta llenar vagones automaticos, salir, llegar 
            
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
tren.place(x=650,y=100)
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

simulacion = False
clientes = 0

def info_Vagon(): 
    info = Toplevel()
    info.title("Informacion de los vagones")
    info.config(bg = "black")
    info.minsize(100,100)
    ventana.resizable(width=NO,height=NO)
    Label(info,text= "Vagon verde = 50 pasajeros",bg="black",fg="green").place(x=10,y=10)
    Label(info,text= "Vagon marron = 30 pasajeros",bg="black",fg="brown").place(x=10,y=40)
    Label(info,text= "Vagon gris = 20 pasajeros",bg= "black",fg="grey").place(x=10,y=70)
def pausa():
    pausa = True
def reloj():
    pausa = False
    while pausa == False:
        Label(ventana2,text= "HORA = 00:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 01:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 02:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 03:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 04:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 05:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 06:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 07:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 08:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 09:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 10:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 11:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 12:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 13:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 14:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 15:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 16:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 17:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 18:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 19:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 20:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 21:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 22:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        Label(ventana2,text= "HORA = 23:00",bg="black",fg="white").place(x=10,y=65)
        time.sleep(10)
        
def hilo_reloj():
    hilo = Thread(target = reloj,args=())
    hilo.start()
hilo_reloj()

def iniciar ():
    global simulacion
    simulacion = True

def pasajeros():
    global simulacion
    global clientes
    if simulacion == False:
        return None
    if clientes == 0:
        can = random.randint(1, 100)
        lblcan = Label(ventana2,text=str(can),bg="black",fg="white").place(x=218,y=30)
        clientes = 1
    else:
        return None

def vagones():
    global simulacion
    if simulacion == False:
        return None
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
   
        #boton1 = Button(canvas_auto, command=llenar_auto,text="      Llenar vagones      ", bg = "#000000", fg = "#FFFFFF")
        #boton1.place(x=35,y=50)
        boton2 = Button(canvas_auto, command=quitar_auto,text="      Quitar vagones      ", bg = "#000000", fg = "#FFFFFF")
        boton2.place(x=35,y=125)

    def vagon_manual():
        ventana_vagones.destroy()
        
        ventana_man = Toplevel()
        ventana_man.title("Qué quieres hacer?")
        ventana_man.minsize(200,200)
        ventana_man.resizable(width=NO,height=NO)
    
        canvas_man = Canvas(ventana_man,width=200,height=200,bg="white")
        canvas_man.place(x=0,y=0)

        def quitar_manual():
            ventana_man.destroy()
        
            ventana_qui = Toplevel()
            ventana_qui.title("Eliminar vagon")
            ventana_qui.minsize(200,200)
            ventana_qui.resizable(width=NO,height=NO)
    
            canvas_qui = Canvas(ventana_qui,width=200,height=200,bg="white")
            canvas_qui.place(x=0,y=0)

            Label(canvas_qui,text="Eliminar vagon en posición:",bg="white",fg="black").place(x=25,y=31)

            pos=Entry(canvas_qui,width=3).place(x=87,y=87)
        
            def quitar():
                ventana_qui.destroy()

            boton = Button(canvas_qui, command=quitar,text="Aceptar", bg = "#000000", fg = "#FFFFFF")
            boton.place(x=72,y=143)
            
        def agregar_manual():
            ventana_man.destroy()
        
            ventana_ag = Toplevel()
            ventana_ag.title("Añadir vagon de...")
            ventana_ag.minsize(200,200)
            ventana_ag.resizable(width=NO,height=NO)
    
            canvas_ag = Canvas(ventana_ag,width=200,height=200,bg="white")
            canvas_ag.place(x=0,y=0)

            def posicion():
                ventana_ag.destroy()
    
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
    
            boton1 = Button(canvas_ag, command=posicion,text="      20 personas      ", bg = "#000000", fg = "#FFFFFF")
            boton1.place(x=50,y=31)
            boton2 = Button(canvas_ag, command=posicion,text="      30 personas      ", bg = "#000000", fg = "#FFFFFF")
            boton2.place(x=50,y=87)
            boton3 = Button(canvas_ag, command=posicion,text="      50 personas      ", bg = "#000000", fg = "#FFFFFF")
            boton3.place(x=50,y=143)

        boton1 = Button(canvas_man, command=agregar_manual,text="      Agregar vagon      ", bg = "#000000", fg = "#FFFFFF")
        boton1.place(x=35,y=50)
        boton2 = Button(canvas_man, command=quitar_manual,text="      Quitar vagon      ", bg = "#000000", fg = "#FFFFFF")
        boton2.place(x=38,y=125)

    boton1 = Button(canvas_vagones, command=vagon_automatico, text="      Automático      ", bg = "#000000", fg = "#FFFFFF")
    boton1.place(x=45,y=50)
    boton2 = Button(canvas_vagones, command=vagon_manual, text="      Manual      ", bg = "#000000", fg = "#FFFFFF")
    boton2.place(x=55,y=125)

boton1 = Button(ventana2, command = iniciar,text="      Iniciar Simulación      ", bg = "#000000", fg = "#FFFFFF")
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
boton7 = Button(ventana2, command = pausa, text="                Pausar reloj                     ", bg = "#000000", fg = "#FFFFFF")#Agregue 2 botones nuevos
boton7.place(x=655,y=95)
boton8 = Button(ventana2, command = info_Vagon, text="                Info de Vagones             ", bg = "#000000", fg = "#FFFFFF")
boton8.place(x=655,y=125)

Label(ventana2,text="Hora de llegada/salida:",bg="black",fg="white").place(x=10,y=5)
Label(ventana2,text="Cantidad de personas que van a viajar:",bg="black",fg="white").place(x=10,y=30)

ventana.mainloop ()

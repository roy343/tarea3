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
        self.maquina=maq
        self.vagones=vags
        self.head=None  
        self.tail=None
        self.largo=0

    def get_vagones(self):
        return self.vagones
    def set_vagones(self,vags):
        self.vagones=vags

    def mostrar (self):
        print (self.maquina.num)
        nodo = self.head
        while nodo != None:
            print (nodo.num)
            nodo = nodo.next

    def agregar_inicio (self, vag):
        if self.largo == self.vagones:
            return None
        self.largo += 1
        if self.head == None: 
            self.head = vag
            self.head.estado = 'Ocupado'
            self.tail = self.head
        else:
            temp = vag
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            self.head.estado = 'Ocupado'

    def agregar_final (self, vag):
        if self.largo == self.vagones:
            return None
        self.largo += 1
        if self.head == None: 
            self.head = vag
            self.head.estado = 'Ocupado'
            self.tail = self.head
        else:
            temp = self.tail
            temp2 = vag
            temp.next = temp2
            temp2.prev = temp
            self.tail = temp2
            self.tail.estado = 'Ocupado'

    def agregar_medio (self, pos, vag):
        if self.largo == self.vagones:
            return None
        elif self.head == None and pos == 1:
            self.head = vag
            self.head.estado = 'Ocupado'
            self.tail = self.head
        elif self.head != None and pos == 1:
            temp = vag
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            self.head.estado = 'Ocupado'
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
            med = vag
            med.estado = 'Ocupado'
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
        if self.largo == 0:
            return None
        self.largo = 0
        temp = self.tail
        temp2 =  temp.prev
        while temp2 != None:
            temp.estado = 'Libre'
            temp.next = None
            temp = temp2
            temp2 = temp.prev
            temp.next.prev = None
        temp.next = None
        temp.prev = None
        self.head = None
        self.tail = None

    def quitar_vagon (self, pos):
        temp = self.head
        if pos > self.largo:
            return None
        if pos == 1 and pos == self.largo:
            temp.next = None
            temp.prev = None
            self.head = None
            self.tail = None
            return None
        elif pos == 1:
            temp2 = temp.next
            self.head = temp2
            self.largo -=1
            temp.next = None
            temp.estado = 'Libre'
            temp2.prev = None
            return None
        elif pos == self.largo:
            temp = self.tail
            temp2 = temp.prev
            self.tail = temp2
            temp2.next = None
            self.largo -=1
            temp.prev = None
            temp.estado = 'Libre'
            return None
        else:
            i = 1
            while i != pos:
                temp = temp.next
                i += 1
            temp_1 = temp.prev
            temp_1.next = temp.next
            self.largo -=1
            temp.next = None
            temp.prev = None
            temp.estado = 'Libre'

    def llenar(self):
        global x
        if self.largo > 0:
            return None
        while x > 0:
            if x > 30:
                self.agregar_final(v11)
                v11.estado = 'Ocupado'
                xb = 50
            elif x <= 30 and x > 20:
                self.agregar_final(v6)
                v6.estado = 'Ocupado'
                xb = 30
            else:
                self.agregar_final(v1)
                v1.estado = 'Ocupado'
                xb = 20
            x -= xb
x=71
    #Falta salir, llegar  
            
class Maquina:
    def __init__(self,num,cap):
        self.num=num
        self.cap=cap

class Vagon:
    def __init__(self,num,cant,estado,next=None,prev=None):
        self.num=num
        self.cant=cant
        self.estado=estado        
        self.next=next
        self.prev=prev

    def get_estado(self):
        return self.estado
    def set_estado(self,estado):
        self.estado=estado

m1 = 0
m2 = 0
m3 = 0
m4 = 0
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0
v10 = 0
v11 = 0
v12 = 0
v13 = 0
v14 = 0
v15 = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0

def sim():
    global m1 
    global m2 
    global m3 
    global m4 
    global v1 
    global v2 
    global v3 
    global v4 
    global v5 
    global v6 
    global v7
    global v8 
    global v9 
    global v10 
    global v11 
    global v12  
    global v13 
    global v14 
    global v15 
    global t1 
    global t2 
    global t3 
    global t4
    global t5 
    global t6 
    global t7 
    global t8
    with open('estacion.txt','r') as f:
        x = f.readlines()
        m1 = Maquina(int(x[0].replace('\n','')),int(x[1].replace('\n','')))
        m2 = Maquina(int(x[2].replace('\n','')),int(x[3].replace('\n','')))
        m3 = Maquina(int(x[4].replace('\n','')),int(x[5].replace('\n','')))
        m4 = Maquina(int(x[6].replace('\n','')),int(x[7].replace('\n','')))
        v1 = Vagon(int(x[8].replace('\n','')),int(x[9].replace('\n','')),x[10].replace('\n',''))
        v2 = Vagon(int(x[11].replace('\n','')),int(x[12].replace('\n','')),x[13].replace('\n',''))
        v3 = Vagon(int(x[14].replace('\n','')),int(x[15].replace('\n','')),x[16].replace('\n',''))
        v4 = Vagon(int(x[17].replace('\n','')),int(x[18].replace('\n','')),x[19].replace('\n',''))
        v5 = Vagon(int(x[20].replace('\n','')),int(x[21].replace('\n','')),x[22].replace('\n',''))
        v6 = Vagon(int(x[23].replace('\n','')),int(x[24].replace('\n','')),x[25].replace('\n',''))
        v7 = Vagon(int(x[26].replace('\n','')),int(x[27].replace('\n','')),x[28].replace('\n',''))
        v8 = Vagon(int(x[29].replace('\n','')),int(x[30].replace('\n','')),x[31].replace('\n',''))
        v9 = Vagon(int(x[32].replace('\n','')),int(x[33].replace('\n','')),x[34].replace('\n',''))
        v10 = Vagon(int(x[35].replace('\n','')),int(x[36].replace('\n','')),x[37].replace('\n',''))
        v11 = Vagon(int(x[38].replace('\n','')),int(x[39].replace('\n','')),x[40].replace('\n',''))
        v12 = Vagon(int(x[41].replace('\n','')),int(x[42].replace('\n','')),x[43].replace('\n',''))
        v13 = Vagon(int(x[44].replace('\n','')),int(x[45].replace('\n','')),x[46].replace('\n',''))
        v14 = Vagon(int(x[47].replace('\n','')),int(x[48].replace('\n','')),x[49].replace('\n',''))
        v15 = Vagon(int(x[50].replace('\n','')),int(x[51].replace('\n','')),x[52].replace('\n',''))
        t1 = Tren(int(x[53].replace('\n','')),x[54].replace('\n',''),x[55].replace('\n',''),m1,int(x[56].replace('\n','')))
        t2 = Tren(int(x[57].replace('\n','')),x[58].replace('\n',''),x[59].replace('\n',''),m2,int(x[60].replace('\n','')))
        t3 = Tren(int(x[61].replace('\n','')),x[62].replace('\n',''),x[63].replace('\n',''),m3,int(x[64].replace('\n','')))
        t4 = Tren(int(x[65].replace('\n','')),x[66].replace('\n',''),x[67].replace('\n',''),m4,int(x[68].replace('\n','')))
        t5 = Tren(int(x[69].replace('\n','')),x[70].replace('\n',''),x[61].replace('\n',''),m1,int(x[72].replace('\n','')))
        t6 = Tren(int(x[73].replace('\n','')),x[74].replace('\n',''),x[75].replace('\n',''),m2,int(x[76].replace('\n','')))
        t7 = Tren(int(x[77].replace('\n','')),x[78].replace('\n',''),x[79].replace('\n',''),m3,int(x[80].replace('\n','')))
        t8 = Tren(int(x[81].replace('\n','')),x[82].replace('\n',''),x[83].replace('\n',''),m4,int(x[84]))

def cargarImagen(nombre):
    ruta = os.path.join('Material',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

ventana = Tk()
ventana.title("Estación TEC")
ventana.minsize(1300,700)
ventana.resizable(width=NO,height=NO)

ventana1=tkinter.Canvas(ventana,width=1400,height=800,bg="blue")
ventana1.place(x=0,y=0)

#ESTACION = cargarImagen("Estacion.gif")
#Estacion = ventana1.create_image(650,100,image = ESTACION)

ventana2=tkinter.Canvas(ventana,width=1405,height=200,bg="gray")
ventana2.place(x=-5,y=500)

img=cargarImagen("0.gif")
tren = Label(ventana1,image=img,bg="blue")
tren.place(x=1800,y=225)
tren.image = img

vagon = Label(ventana1, image = '',bg="blue")
vagon.place(x=1800,y=295)
vagon.image = ''

vagon2 = Label(ventana1, image = '',bg="blue")
vagon2.place(x=1800,y=295)
vagon2.image = ''

vagon3 = Label(ventana1, image = '',bg="blue")
vagon3.place(x=1800,y=295)
vagon3.image = ''

#Dejo el thread desactivado para trabajar
def trenanimacion(): 
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

def vagon1animacion(): 
    i2 = 8
    try:
        while i2 < 15:
            img2 = cargarImagen(str(i2)+".gif")
            vagon.configure(image = img2)
            vagon.image = img2
            i2 += 1
            if i2 == 15:
                i2 = 8
            time.sleep(0.21)
    except Exception as errtxt:
        print("Error en hilo")
def ver_vagon1animacion():
    trent2 = Thread(target=vagon1animacion, args=())
    trent2.start()

def vagon2animacion(): 
    i3 = 16
    try:
        while i3 < 23:
            img3 = cargarImagen(str(i3)+".gif")
            vagon2.configure(image = img3)
            vagon2.image = img3
            i3 += 1
            if i3 == 23:
                i3 = 16
            time.sleep(0.21)
    except Exception as errtxt:
        print("Error en hilo")
def ver_vagon2animacion():
    trent3 = Thread(target=vagon2animacion, args=())
    trent3.start()

def vagon3animacion(): 
    i4 = 24
    try:
        while i4 < 31:
            img4 = cargarImagen(str(i4)+".gif")
            vagon3.configure(image = img4)
            vagon3.image = img4
            i4 += 1
            if i4 == 31:
                i4 = 24
            time.sleep(0.21)
    except Exception as errtxt:
        print("Error en hilo")
def ver_vagon3animacion():
    trent4 = Thread(target=vagon3animacion, args=())
    trent4.start()

simulacion = False
clientes = 0
pausa = True

def Llegada():
    quieto = False
    i5 = 0
    while quieto != True and i5 < 675:
        tren.place(x = str(i5),y = 225)
        vagon.place(x = str(i5-100),y = 295)
        vagon2.place(x = str(i5-400),y = 295)
        vagon3.place(x = str(i5-675),y = 295)
        i5 += 10
        time.sleep(0.1)
def iniciar_Llegada():
    Hiloprueba = Thread(target = Llegada, args=())
    Hiloprueba.start()
    
def Salida():
    moviendose = False
    i6 = 675
    while moviendose != True and i6 < 1800:
        tren.place(x = str(i6), y = 225)
        vagon.place(x = str(i6-100),y = 295)
        vagon2.place(x = str(i6-400),y = 295)
        vagon3.place(x = str(i6-675),y = 295)
        i6 += 10
        time.sleep(0.1)
    tren.place(x = 1800, y = 225)
    vagon.place(x = 1800,y = 295)
    vagon2.place(x = 1800,y = 295)
    vagon3.place(x = 1800,y = 295)
def iniciar_Salida():
    Hiloprueba2 = Thread(target = Salida, args = ())
    Hiloprueba2.start()
    
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
    global pausa
    if pausa == False:
        pausa = True
    else:
        pausa = False
        hilo_reloj()
    
v=StringVar()#define v como una variable de texto
Label(ventana2,textvariable=v,bg="black",fg="white").place(x=10,y=65)#Label principal

var1 = "Hora "
var2 = "0"
var3 = 0
var4 = ":"
var5 = 0
var6 = "0"

def reloj():#funcion de reloj
    global var1
    global var2
    global var3
    global var4
    global var5
    global pausa
    global tren
    while pausa == False:
        v.set(var1+var2+str(var3)+var4+str(var5)+var6)
        var5 += 1
        if var5 == 6:
            var5 = 0
            var3 += 1
            if var3 == 10 and var2 == "1":
                var3 = 0
                var2 = "2"
            elif var3 == 10 and var2 == "0":
                var3 = 0
                var2 = "1"
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 01:10":
            pausa = True
            tren_actual = t1
            tren.place(x=675,y=225)
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 04:10":
            pausa = True
            tren_actual = t2
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 07:10":
            pausa = True
            tren_actual = t3
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 10:10":
            pausa = True
            tren_actual = t4
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 13:10":
            pausa = True
            tren_actual = t5
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 16:10":
            pausa = True
            tren_actual = t6
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 19:10":
            pausa = True
            tren_actual = t7
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 22:10":
            pausa = True
            tren_actual = t8
        if var1+var2+str(var3)+var4+str(var5)+var6 == "Hora 24:00":
            var2 = "0"
            var5 = 0
            var3 = 0
        time.sleep(0.5)
def hilo_reloj():
    hilo = Thread(target = reloj,args=())
    hilo.start()

def iniciar ():
    global simulacion
    global pausa
    if simulacion == True:
        return None
    else:
        sim()
        simulacion = True
        pausa = False
        hilo_reloj()

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
   
        boton1 = Button(canvas_auto, command=llenar_auto,text="      Llenar vagones      ", bg = "#000000", fg = "#FFFFFF")
        boton1.place(x=35,y=50)
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
                #####################################estoy en esto
                ventana_ag.destroy()
    
                ventana_pos = Toplevel()
                ventana_pos.title("Posición")
                ventana_pos.minsize(200,200)
                ventana_pos.resizable(width=NO,height=NO)
    
                canvas_pos = Canvas(ventana_pos,width=200,height=200,bg="white")
                canvas_pos.place(x=0,y=0)

                Label(canvas_pos,text="...O en la posición:",bg="white",fg="black").place(x=25,y=125)

                pos=Entry(canvas_pos,width=3).place(x=135,y=125)

                def colocar_final():
                    global tren_actual
                    ventana_pos.destroy()
                    img = cargarImagen("8.gif")
                    if vagon.image == '':
                        vagon.config(image=img)
                        vagon.image=img
                        vagon.place(x=575,y=295)
                    elif vagon2.image == '':
                        vagon2.config(image=img)
                        vagon2.image=img
                        vagon2.place(x=275,y=295)
                    else:
                        vagon3.config(image=img)
                        vagon3.image=img
                        vagon3.place(x=0,y=295)

                def colocar_inicio():
                    global tren_actual
                    ventana_pos.destroy()
                    img = cargarImagen("8.gif")
                    if vagon.image == '':
                        vagon.config(image=img)
                        vagon.image=img
                        vagon.place(x=575,y=295)
                    elif vagon2.image == '':
                        vagon2 = vagon                        
                        vagon2.place(x=275,y=295)
                        vagon.config(image=img)
                        vagon.image=img
                        vagon.place(x=575,y=295)
                    else:
                        vag = vagon2
                        vagon3 = vag
                        vagon3.place(x=0,y=295)
                        vag = vagon
                        vagon2 = vag
                        vagon2.place(x=275,y=295)
                        vagon.config(image=img)
                        vagon.image=img
                        vagon.place(x=575,y=295)
                
                def colocar():
                    ventana_pos.destroy()

                boton1 = Button(canvas_pos, command=colocar_inicio,text="      Al inicio      ", bg = "#000000", fg = "#FFFFFF")
                boton1.place(x=52,y=25)
                boton2 = Button(canvas_pos, command=colocar_final,text="      Al final      ", bg = "#000000", fg = "#FFFFFF")
                boton2.place(x=55,y=65)
                boton3 = Button(canvas_pos, command=colocar,text="Aceptar", bg = "#000000", fg = "#FFFFFF")
                boton3.place(x=70,y=165)
                #################################
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
    
def rutas():
    if simulacion == True:
        rutas = Toplevel()
        rutas.title("Rutas por Hora")
        rutas.minsize(200,200)
        rutas.resizable(width=NO,height=NO)


        rlbl = Label(rutas,text="TEC - San Jose").place(x=60,y=0)
        rlbl2 = Label(rutas,text="Salida:             01:00        07:00     ").place(x=0,y=40)
        rlbl = Label(rutas,text="Llegada:         13:00        19:00    ").place(x=0,y=60)
        rlbl = Label(rutas,text="TEC - Alajuela").place(x=60,y=120)
        rlbl5 = Label(rutas,text="Salida:             04:00        10:00     ").place(x=0,y=160)
        rlbl6 = Label(rutas,text="Llegada:         17:00        22:00    ").place(x=0,y=180)

def llegada():
    if simulacion == True:
        tren.config(image='')
        tren.image=''
        vagon.config(image='')
        vagon.image=''
        vagon2.config(image='')
        vagon2.image=''
        vagon3.config(image='')
        vagon3.image=''
    else:
        return None

boton1 = Button(ventana2, command = iniciar,text="      Iniciar Simulación      ", bg = "#000000", fg = "#FFFFFF")
boton1.place(x=505,y=5)
boton2 = Button(ventana2, command = rutas, text="        Rutas por horas        ", bg = "#000000", fg = "#FFFFFF")
boton2.place(x=505,y=35)
boton3 = Button(ventana2, command = pasajeros, text="Estimación de demanda por ruta", bg = "#000000", fg = "#FFFFFF")
boton3.place(x=655,y=35)
boton4 = Button(ventana2, command = vagones, text="      Administración de vagones   ", bg = "#000000", fg = "#FFFFFF")
boton4.place(x=655,y=5)
boton5 = Button(ventana2, text="          Salida de tren          ", bg = "#000000", fg = "#FFFFFF")
boton5.place(x=505,y=65)
boton6 = Button(ventana2, command = llegada,text="               Llegada de tren               ", bg = "#000000", fg = "#FFFFFF")
boton6.place(x=655,y=65)
boton7 = Button(ventana2, command = pausa, text="                Pausar reloj                     ", bg = "#000000", fg = "#FFFFFF")#Agregue 2 botones nuevos
boton7.place(x=655,y=95)
boton8 = Button(ventana2, command = info_Vagon, text="                Info de Vagones             ", bg = "#000000", fg = "#FFFFFF")
boton8.place(x=655,y=125)
boton9 = Button(ventana2, command = iniciar_Llegada, text="                Llegada Pureba             ", bg = "#000000", fg = "#FFFFFF")
boton9.place(x=505,y=125)
boton9 = Button(ventana2, command = iniciar_Salida, text="                Salida Pureba             ", bg = "#000000", fg = "#FFFFFF")
boton9.place(x=505,y=155)
Label(ventana2,text="Hora de llegada/salida:",bg="black",fg="white").place(x=10,y=5)
Label(ventana2,text="Cantidad de personas que van a viajar:",bg="black",fg="white").place(x=10,y=30)

ventana.mainloop ()



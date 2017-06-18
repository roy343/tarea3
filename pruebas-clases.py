class Tren:
    def __init__(self,num,ruta,hora,maq,vags):
        self.num=num
        self.ruta=ruta
        self.hora=hora
        self.maquina=maq #Temporal
        self.vagones=vags
        self.head=None  
        self.tail=None
        self.largo=0

    def get_vag(self):
        return self.vag
    def set_vag(self,vag):
        self.vag=vag

    #################################

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

    ###################
            
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

###################################################

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

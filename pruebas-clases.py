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
    def __init__(self,num,cant,next=None,prev=None):
        self.num=num
        self.cant=cant
        self.next=next
        self.prev=prev


def main():

    file=open("archivo.txt","w")#Abre el archivo y deja que se pueda escribi en el 
    file.write("Maquina#2 \n7:30 a.m. \nTEC-San Jose")#Escribe en el archivo #el "\n" python lo lee como unn "enter"
    file.close()#Cierra el archivo(esto es necesario)
    file=open("archivo.txt","r")#Abre el archivo y deja escribir en el
    line=file.readlines()#Define a todo lo escrito en el texto como una lista "line"
    #Si en vez de "readlines" se pone "readline" solamente toma el primer reglon y define a las letras como los elementos de la lista
    print(line[0])#impirme el primer elemento de la lista, en este caso el primer reglon
    print(line[1])#impirme el segundo elemento de la lista, en este caso el segundo reglon
    print(line[2])#impirme el tercer elemento de la lista, en este caso el tercer reglon

main()#ejecuta la funcion

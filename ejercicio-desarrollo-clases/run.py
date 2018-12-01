from Archivo.archivo import Archivo_Leer, Escribir_Archivo
#clase estudiante
class Estudiante():
    #constructor y atributos
    def __init__(self, n, n1, n2, n3):
        self.nombre=n
        self.n1=n1
        self.n2=n2
        self.n3=n3

    #metodo que retorna el nombre
    def getNombre(self):
        return self.nombre

    #metodo que retorna el promedio
    def getPromedio(self):
        return (self.n1+self.n2+self.n3)/3


leer = Archivo_Leer() #objeto que abre el archivo que provee la información
escribir = Escribir_Archivo()#objeto que abre el archivo en donde se va a presentar la informacion

lista = leer.Leer_Lineas() #se crea una lista que almacene los datos del archivo de origen
lista = lista[1:5]#se limita el contenido de la misma
newLista = []#se crea una nueva lista para almacenar los valores separados

for line in lista: #for para recorrer la lista y speraralos con referecia del caracter '|' y agregarlos a la nueva lista
    line = line.split("|")
    newLista.append(line)

for line in newLista: #for que crea el objeto con las lineas de la lueva lista y los agrega el nuevo archivo.
    est = Estudiante(line[0], int(line[1]),int(line[2]),int(line[3]))
    escribir.Escribir(est)

#se cierra el objeto de leer y escribir archivo.
escribir.Cerrar()
leer.Cerrar()
import codecs
#clase que lee el archivo


class Archivo_Leer:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.txt", "r")#se abre el archivo especificando la ubicacion

    def Leer_Lineas(self):
        return self.archivo.readlines() #metodo para leer el contenido del archivo

    def Cerrar(self):
        self.archivo.close() #metodo para cerrar el archivo


#clase que escribe el archivo
class Escribir_Archivo:

    def __init__(self):
        self.archivo = codecs.open("data/resultados.txt","a")#se abre el archivo especificando la ubicacion

    def Escribir(self, est):
         self.archivo.write("%s. Promedio: %s \n" % (est.getNombre(), est.getPromedio()))#se escribe en el archivo dependiendo de los argumentos del metodo y el formato

    def Cerrar(self):
        self.archivo.close()#metodo para cerrar el archivo
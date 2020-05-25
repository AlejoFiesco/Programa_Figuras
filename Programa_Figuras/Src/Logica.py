from Esfera import Esfera
from Cilindro import Cilindro
from Cono import Cono
from Cono_mediante_cilindros import Cono_mediante_cilindro
from Cubo import Cubo

class Logica():

    def __init__(self,opc):
        if(opc == 1):
            print ("Ingrese el radio de la esfera")
            radio = float(input())
            self.fig = Esfera(radio)
        if(opc == 2):
            print ("Ingrese el radio de la base")
            radio = float(input())
            print ("Ingrese la altura del cilindro")
            h = float(input())
            self.fig = Cilindro(radio,h)
        if(opc == 3):
            print ("Ingrese el radio de la base")
            radio = float(input())
            print ("Ingrese la altura del cono")
            h = float(input())
            self.fig = Cono(radio, h)
        if(opc == 4):            
            print ("Ingrese el radio de la base")
            radio = float(input())
            print ("Ingrese la altura del cono")
            h = float(input())
            print ("Ingrese la cantidad de cilindros en que se va a dividir el cono")
            cant = int(input())
            self.fig = Cono_mediante_cilindro(radio, h, cant)
        if(opc == 5):
            print ("Ingrese la magnitud de una arista del cubo")    
            lado = float(input())
            self.fig = Cubo(lado)
        
    def mostrar_volumen(self):
        return (self.fig.obtener_volumen())

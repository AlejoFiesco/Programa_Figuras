from Figura import Figura

class Cilindro(Figura):

    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def obtener_volumen(self):
        return (3.141592*pow(self.radius,2)*self.height)        
from Figura import Figura

class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def obtener_volumen(self):
        return pow(self.lado,3)
from Figura import Figura

class Esfera(Figura):        

    def __init__(self,radio):
        self.radio = radio
        
    def obtener_volumen(self):
        return (3.141592*(4/3)*pow(self.radio,3))
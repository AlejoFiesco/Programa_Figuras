from Figura import Figura

class Cono(Figura):
    def __init__(self,radio,altura):
        self.radio = radio
        self.altura = altura

    def obtener_volumen(self):
        return (3.141592 * pow(self.radio , 2) * self.altura/3)    

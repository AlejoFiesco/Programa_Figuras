from Figura import Figura

class Cono_mediante_cilindro(Figura):

    def __init__(self,radio,altura,cantidad_cilindros):
        self.radio = radio
        self.altura = altura
        self.cantidad_cilindros = cantidad_cilindros

    def obtener_volumen(self):
        volumen_acumulado = 0
        radio_temp = self.radio
        for i in range(self.cantidad_cilindros):
            volumen_acumulado += (3.141592 * pow(radio_temp,2) * self.altura/self.cantidad_cilindros)
            radio_temp -= self.radio/self.cantidad_cilindros
        return volumen_acumulado


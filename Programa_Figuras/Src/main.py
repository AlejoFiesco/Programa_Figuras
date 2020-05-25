from Logica import Logica

print ("""Ingrese la figura de la cual va a calcular su volumen: 
1) Esfera
2) Cilindro
3) Cono de con formula
4) Cono mediante cálculo con cilindros
5) Cubo""")
opc = int(input())
log = Logica(opc)
print ("El volumen es "+str(log.mostrar_volumen())+" u^3")




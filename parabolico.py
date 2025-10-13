import math


#NIGGA
class Posicion:
    def __init__(self, x_inicial, y_inicial, velocidad, angulo, tiempo):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.velocidad = velocidad
        self.angulo = angulo
        self.tiempo = tiempo
    def altura(self):
        vy = self.velocidad*math.sin(self.angulo)
        y = self.y_inicial + vy*self.tiempo - 0.5*9.8*(self.tiempo**2)
        return y

p1 = Posicion(0, 1.5, 20, math.pi/4, 2)
print(p1.altura())
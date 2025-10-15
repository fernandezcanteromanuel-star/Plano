import math


#NIGGA
class Posicion:
    def __init__(self, x_inicial, y_inicial, velocidad, angulo):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.velocidad = velocidad
        self.angulo = angulo

    def altura(self, tiempo):
        global vy
        global y
        global tiempo_final
        vy = self.velocidad*math.sin(self.angulo)
        y = self.y_inicial + vy*tiempo - 0.5*9.8*(tiempo**2)
        tiempo_final = (-vy+math.sqrt(vy**2-4*(-4.9)*self.y_inicial))/(2*(-4.9))
        return y
   
    def alcance_max(self):
        global alcance_max
        alcance_max = vx*tiempo_final
        return alcance_max
    
    def alcance(self, tiempo):
        global vx
        vx = self.velocidad*math.cos(self.angulo)
        alcance = vx*tiempo
        if tiempo <= tiempo_final:
            return alcance
        else:
            alcance_max()
p1 = Posicion(0, 1.5, 20, math.pi/4)
print(p1.altura(2))

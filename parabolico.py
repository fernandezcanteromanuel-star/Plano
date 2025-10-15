import math


#NIGGA
class Posicion:
    def __init__(self, x_inicial, y_inicial, velocidad, angulo):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.velocidad = velocidad
        self.angulo = angulo
    
    #Cálculo de la altura en función del tiempo
    def altura(self, tiempo):
        #Glovales para los procesos
        global vy
        global y
        global tiempo_final

        #La velocidad en y cambia con el tiempo
        vy = self.velocidad*math.sin(self.angulo)

        #Posicion en el eje y por MRUA
        y = self.y_inicial + vy*tiempo - 0.5*9.8*(tiempo**2)

        #Definimos condiciones para un tiempo > 0
        if (-vy-math.sqrt(vy**2-4*(-4.9)*self.y_inicial))/(2*(-4.9)) > 0:
            tiempo_final = (-vy-math.sqrt(vy**2-4*(-4.9)*self.y_inicial))/(2*(-4.9))
        else:
            tiempo_final = (-vy+math.sqrt(vy**2-4*(-4.9)*self.y_inicial))/(2*(-4.9))

        #La altura después de determinado momento es fija=0
        if tiempo <= tiempo_final:
            return y
        else:
            return 0
        
    #Altura máxima calculando el tiempo en el que lo alcanza
    def altura_max(self):
        tiempo_altmax = vy/9.8
        y_max =  self.y_inicial + vy*tiempo_altmax - (4.9*tiempo_altmax)
        return y_max
    
    #Alcance máximo, solo depende del tiempo_final
    def alcance_max(self):
        global vx
        global alcance_max

        vx = self.velocidad*math.cos(self.angulo)
        alcance_max = vx*tiempo_final
        return alcance_max
    
    #Alcance con respecto al tiempo (Eje X)
    def alcance(self, tiempo):
        
        alcance = vx*tiempo
        if tiempo <= tiempo_final:
            return alcance
        else:
            return alcance_max()
    
    #El vector velocidad en todo momento
    def vector_velocidad(self, tiempo):
        if tiempo <= tiempo_final:
            return '{}i + {}j'.format(vx, (vy-9.8*tiempo))
        else:
            return '{}i + {}j'.format(vx, vy-9.8*tiempo_final)




p1 = Posicion(0, 1.5, 20, math.pi/4)
print(p1.altura(10))
print(p1.alcance_max())
print(p1.vector_velocidad(2))
print(p1.alcance(2))
print(p1.altura_max())


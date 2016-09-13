# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Protagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.figura = pilas.fisica.Circulo(self.x, self.y, 17)

#        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 1

        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, dinamica=False)

        self.figura.x= -200
        self.figura.y= 240


    def actualizar(self):
        velocidad = 10
        salto = 15
        self.x = self.figura.x
        self.y = self.figura.y

        if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
        elif self.pilas.control.izquierda:
            self.figura.velocidad_x = -velocidad
        else:
            self.figura.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

mapa = pilas.actores.MapaTiled('D:\curso\Tiled\prueba.tmx')

pilas.actores.vincular(Protagonista)
p = pilas.actores.Protagonista()


pilas.ejecutar()

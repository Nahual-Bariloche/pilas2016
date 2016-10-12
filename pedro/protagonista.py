import pilasengine

class Protagonista(pilasengine.actores.Actor):

    vidas = 3

    def iniciar(self):
        self.puntaje = pilas.actores.Puntaje(texto=str(self.vidas), x=200, y=200)
        self.imagen = "aceituna.png"
        self.figura = self.pilas.fisica.Circulo(self.x, self.y, 17,
            friccion=0, restitucion=0)

        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2

        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)

    def actualizar(self):
        velocidad = 10
        salto = 15
        self.x = self.figura.x
        self.y = self.figura.y

        if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
            self.rotacion -= velocidad
        elif self.pilas.control.izquierda:
            self.figura.velocidad_x = -velocidad
            self.rotacion += velocidad
        else:
            self.figura.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20
        
        if self.esta_pisando_el_suelo():
            self.imagen = "aceituna.png"
        else:
            self.imagen = "aceituna_risa.png"

        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

    def perder_vida(self):
        self.vidas -= 1
        self.puntaje.actualizar(str(self.vidas))
        if(self.vidas == 0):
            self.eliminar()
            self.pilas.actores.Texto('GAME OVER')
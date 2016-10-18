import pilasengine

class Protagonista(pilasengine.actores.Actor):

    vidas = 5

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.figura = pilas.fisica.Circulo(self.x, self.y, 17, friccion= 0, restitucion= 0)

        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 4

        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor = True, dinamica=False)

    def actualizar(self):
        velocidad = 10
        salto = 17
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

        if self.esta_pisando_el_suelo():
            self.imagen ="aceituna.png"
        else:
            self.imagen="aceituna_risa.png"
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

    def restar_vidas(self):
        self.vidas = self.vidas -1
        puntaje.reducir()
        if self.vidas == 0:
            self.eliminar()
            texto = pilas.actores.Texto("Game Over")

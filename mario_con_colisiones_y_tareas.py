import pilasengine
import random


pilas = pilasengine.iniciar()
#pilas.depurador.definir_modos(fisica=True)

pilas.reiniciar_si_cambia(__file__)

class Protagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.figura = pilas.fisica.Circulo(self.x, self.y, 17,
            friccion=0, restitucion=0)

        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2

        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)

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



def agregar_caja():
    caja = pilas.actores.Caja(x = random.randint(-300, 300), y = random.randint(0, 300))
    pilas.tareas.agregar(4, caja.eliminar)
    
def colisiona_con_bomba(actor, bomba):
    bomba.explotar()
    actor.eliminar()

def agregar_bombas(actor):
    bombas = pilas.actores.Bomba()*5
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

mapa = pilas.actores.MapaTiled('plataformas.tmx', densidad=0,
            restitucion=0, friccion=0, amortiguacion=0)

pilas.actores.vincular(Protagonista)
protagonista = pilas.actores.Protagonista()
   
segundos = 3
agregando_cajas = pilas.tareas.siempre(segundos, agregar_caja)
pilas.tareas.agregar(3, agregar_bombas, protagonista)



pilas.ejecutar()

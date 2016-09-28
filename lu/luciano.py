import pilasengine
import random

def iniciar_juego():
    pilas.escenas.Normal()
    actor = pilas.actores.Aceituna()
    actor.decir("Bienvenido al juego")

pilas = pilasengine.iniciar()
#pilas.depurador.definir_modos(fisica=True)

pilas.reiniciar_si_cambia(__file__)

class Protagonista(pilasengine.actores.Actor):

    vidas = 3

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.figura = pilas.fisica.Circulo(self.x, self.y, 17,
            friccion=0, restitucion=0)

        self.figura._rotacion = True
        self.figura.escala_de_gravedad = 1

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

    def perder_vida(self):
        self.vidas = self.vidas - 1
        if(self.vidas==0):
            self.eliminar()       
        

def agregar_caja():
    caja = pilas.actores.Caja(x = random.randint(-300, 300), y = random.randint(0, 300))
    pilas.tareas.agregar(4, caja.eliminar)
    
def colisiona_con_bomba(actor, bomba):
    bomba.explotar()
    actor.perder_vida()
    
def agregar_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=100   
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregara_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=140 
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregaras_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=180
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregarasa_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=220
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregarasas_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=260 
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregarasasa_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=60 
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

def agregarasasas_bombas(actor):
    bombas = pilas.actores.Bomba(x = 100, y=-300)*1
    bombas.y=-200    
    bombas.x=20 
    pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

mapa = pilas.actores.MapaTiled('untitled.tmx')
    
pilas.actores.vincular(Protagonista)
protagonista = pilas.actores.Protagonista()
   
segundos = 3
agregando_cajas = pilas.tareas.siempre(segundos, agregar_caja)
pilas.tareas.agregar(3, agregar_bombas, protagonista)

pilas.tareas.agregar(3, agregara_bombas, protagonista)

pilas.tareas.agregar(3, agregaras_bombas, protagonista)

pilas.tareas.agregar(3, agregarasa_bombas, protagonista)

pilas.tareas.agregar(3, agregarasas_bombas, protagonista)

pilas.tareas.agregar(3, agregarasasa_bombas, protagonista)

pilas.tareas.agregar(3, agregarasasas_bombas, protagonista)

pilas.ejecutar()

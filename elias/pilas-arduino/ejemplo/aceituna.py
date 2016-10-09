import pilasengine
import random
from protagonista import Protagonista
import arduino_pilas

pilas = pilasengine.iniciar()

#pilas.depurador.definir_modos(fisica=True)
pilas.reiniciar_si_cambia(__file__)
arduino_pilas.iniciar_arduino();

def agregar_caja():
    caja = pilas.actores.Caja(x = random.randint(-300, 300), y = random.randint(0, 300))
    pilas.tareas.agregar(4, caja.eliminar)
    
def colisiona_con_bomba(actor, bomba):
    bomba.explotar()
    actor.perder_vida()

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

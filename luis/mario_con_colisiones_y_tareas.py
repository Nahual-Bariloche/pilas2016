import pilasengine
import random
import protagonista

pilas = pilasengine.iniciar()
#pilas.depurador.definir_modos(fisica=True)

pilas.reiniciar_si_cambia(__file__)

# vidas = 5


def agregar_caja():
    caja = pilas.actores.Caja(x = random.randint(-300, 300), y = random.randint(0, 300))
    pilas.tareas.agregar(4, caja.eliminar)
    
def colisiona_con_bomba(actor, bomba):
    bomba.explotar()
#    actor.eliminar()
    actor.restar_vida()

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

puntaje=pilas.actores.Puntaje(texto="5",x=200, y=200)



pilas.ejecutar()

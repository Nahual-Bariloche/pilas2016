import pilasengine
import inicio

pilas = pilasengine.iniciar()
#pilas.reiniciar_si_cambia(__file__)

def colisiona_con_bomba(actor, bomba):
    bomba.explotar()
    actor.perder_vida()
    if(actor.vidas == 0):
        pilas.actores.Texto('GAME OVER')
        pilas.tareas.agregar(5, pilas.escenas.Inicio)

pilas.escenas.vincular(Inicio)

pilas.escenas.Inicio()


pilas.ejecutar()

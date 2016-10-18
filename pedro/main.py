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

inicio = pilas.escenas.Inicio()

def llega_a_puerta(actor, puerta):
    pilas.actores.Texto('Felicitaciones, pasaste de nivel')
    inicio.juego.pasar_nivel()



pilas.ejecutar()

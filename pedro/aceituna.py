import pilasengine
import inicio

pilas = pilasengine.iniciar()
#pilas.reiniciar_si_cambia(__file__)

pilas.escenas.vincular(Inicio)

pilas.escenas.Inicio()


pilas.ejecutar()

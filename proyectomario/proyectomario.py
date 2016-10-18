import pilasengine

import random

import protagonista

pilas = pilasengine.iniciar(alto=495, ancho=396)

mapa = pilas.actores.MapaTiled("D:\\curso\\pilas2016\\proyectomario\\mapamario.tmx")


def agregar_caja():
        caja = pilas.actores.Caja(x = random.randint(-300,300), y = random.randint(0,300))
        pilas.tareas.agregar(4, caja.eliminar)

def colisiona_con_bomba(actor, bomba):
        bomba.explotar()
        actor.restar_vidas()

def agregar_bombas(actor):
        bombas = pilas.actores.Bomba()*5
        pilas.colisiones.agregar(actor,bombas,colisiona_con_bomba)

pilas.actores.vincular(Protagonista)
protagonista = pilas.actores.Protagonista()

puntaje = pilas.actores.Puntaje(texto=protagonista.vidas, x = 150, y = 200)

segundos = 3
agragando_cajas = pilas.tareas.siempre(segundos, agregar_caja)
pilas.tareas.agregar(3, agregar_bombas, protagonista)


pilas.ejecutar()
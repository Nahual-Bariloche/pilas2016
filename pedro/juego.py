import pilasengine
import random
import protagonista

class Juego(pilasengine.escenas.Escena):

    def iniciar(self):
        puntaje = self.pilas.actores.Puntaje(texto='3', x=200, y=200)
        self.mapa = self.pilas.actores.MapaTiled('plataformas.tmx', densidad=0, restitucion=0, friccion=0, amortiguacion=0)
        self.pilas.actores.vincular(Protagonista)
        self.protagonista = self.pilas.actores.Protagonista()
        segundos = 3
        agregando_cajas = self.pilas.tareas.siempre(segundos, self.agregar_caja)
        self.pilas.tareas.agregar(3, self.agregar_bombas, self.protagonista)
        

    def agregar_caja(self):
        caja = self.pilas.actores.Caja(x = random.randint(-300, 300), y = random.randint(0, 300))
        self.pilas.tareas.agregar(4, caja.eliminar)
        
    def agregar_bombas(self, actor):
        bombas = self.pilas.actores.Bomba()*5
        self.pilas.colisiones.agregar(actor, bombas, colisiona_con_bomba)

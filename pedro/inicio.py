import pilasengine
import juego

class Inicio(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = self.pilas.fondos.Volley()
        self.pilas.actores.Menu(
                [
                    ('iniciar juego', self.iniciar_juego),
                    ('salir', self.salir_del_juego),
                ])
        
        pass

    def ejecutar(self):
        pass

    def iniciar_juego(self):
        self.pilas.escenas.vincular(Juego)
        self.pilas.escenas.Juego()

    def salir_del_juego(self):
        print("Adios...")
        self.pilas.terminar()
        
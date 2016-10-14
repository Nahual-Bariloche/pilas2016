# -*- coding: utf-8
import pilasengine
from arduino_pilas import SensorDigital, iniciar_arduino, ActuadorDigital
from pilasengine.actores.actor import Actor

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.blanco)

class SuperRayo(Actor):
    
    def iniciar(self):
        self.esta_habilitado = False
        self.tiempo_inhabilitacion = 600
        self.boton = SensorDigital(pin=7)
        self.luz_de_carga = ActuadorDigital(pin=3)
        self.luz_de_listo = ActuadorDigital(pin=4)
        self.x = 0
        self.y = 0
        self.imagen = "invisible.png"
        self.se_disparo_rayo = False
        self.luz_de_carga.enceder()
        
    def actualizar(self):
        if(self.tiempo_inhabilitacion > 1):
            self.tiempo_inhabilitacion-=1
        else:
            self.luz_de_carga.apagar()
            self.luz_de_listo.enceder()
            self.esta_habilitado = True
                    
        if(self.esta_habilitado and self.boton.esta_encendido()):
            self.se_disparo_rayo = True
        
    def disparado(self):
        if(self.se_disparo_rayo):
            self.esta_habilitado = False
            self.tiempo_inhabilitacion = 600
            self.se_disparo_rayo = False
            self.luz_de_carga.enceder()
            self.luz_de_listo.apagar()
            return True
        else:
            return False
    
class AceitunaEnemiga(pilasengine.actores.Aceituna):

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-200, 200)
        self.y = 290
        self.velocidad = pilas.azar(10, 40) / 10.0

    def actualizar(self):
        self.rotacion += 10
        self.y -= self.velocidad
        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

fondo = pilas.fondos.Galaxia(dy= -5)
iniciar_arduino();
enemigos = pilas.actores.Grupo()
rayo = SuperRayo(pilas)

def crear_enemigo():
    actor = AceitunaEnemiga(pilas)
    enemigos.agregar(actor)    
            
def chequear_rayo():
    if(rayo.disparado()):
        for un_enemigo in enemigos:
            un_enemigo.eliminar()

pilas.tareas.siempre(0.5, crear_enemigo)
pilas.tareas.siempre(0.1, chequear_rayo)

nave = pilas.actores.NaveRoja(y=-200)
nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
nave.definir_enemigos(enemigos, puntaje.aumentar)

pilas.colisiones.agregar(nave, enemigos, nave.eliminar)

pilas.avisar(u"Pulsá los direccionales del teclado o espacio para disparar.")
pilas.ejecutar()

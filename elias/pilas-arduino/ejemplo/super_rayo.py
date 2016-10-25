# -*- coding: utf-8
import pilasengine
from pilasengine.actores.actor import Actor
from pilasengine.actores.nave_roja import NaveRoja
from pilasengine import colores
from pilas_arduino.arduino_pilas import SensorDigital, ActuadorDigital,\
    iniciar_arduino

pilas = pilasengine.iniciar()
puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.blanco)


class NaveRayo(NaveRoja):
    def iniciar(self, *k, **kw):
        NaveRoja.iniciar(self, *k, **kw)
        self.cantidad_de_carga = 10
        self.demora_carga = 120
        self.carga_rayo = self.pilas.actores.Energia(y=200)
        self.carga_rayo.progreso = 100
        self.super_rayo = SuperRayo(self.pilas)
        
    def intenta_disparar(self):
        if(self.cantidad_de_carga>0):
            super(NaveRayo,self).intenta_disparar()
           
    def crear_disparo(self):
        NaveRoja.crear_disparo(self)
        self.cantidad_de_carga-=1
        self.carga_rayo.progreso -= 10
            
    def actualizar(self):
        NaveRoja.actualizar(self)
        if(self.demora_carga==0):
            self.demora_carga=120
            self.carga_rayo.progreso = 100
            self.cantidad_de_carga = 10
                    
        if(self.cantidad_de_carga==0):
            self.demora_carga-=1
            
        self.chequear_rayo()   
    
    def chequear_rayo(self):
        if(self.super_rayo.esta_habilitado):
            self.carga_rayo.color_relleno = colores.verde
            self.carga_rayo.pintar_imagen()
        if(self.super_rayo.disparado()):
            self.carga_rayo.color_relleno = colores.amarillo
            self.carga_rayo.pintar_imagen()
            explosion=pilas.actores.Explosion()
            explosion.escala = 10            
            for un_enemigo in enemigos:
                un_enemigo.eliminar()
                if self.cuando_elimina_enemigo:
                    self.cuando_elimina_enemigo()                
        
class SuperRayo(Actor):
    
    def iniciar(self):
        self.esta_habilitado = False
        self.tiempo_inhabilitacion = 600
        self.boton = SensorDigital(pin=2)
        self.luz_de_carga = ActuadorDigital(pin=10)
        self.luz_de_carga2 = ActuadorDigital(pin=11)
        self.luz_de_listo = ActuadorDigital(pin=9)
        self.x = 0
        self.y = 0
        self.imagen = "invisible.png"
        self.se_disparo_rayo = False
        self.luz_de_carga.enceder()
        self.luz_de_carga2.enceder()
        self.luz_de_listo.apagar()
        self.tiempo_chequeo = 10
        
    def actualizar(self):
        if(self.tiempo_inhabilitacion > 1):
            self.tiempo_inhabilitacion-=1
        else:
            if(self.esta_habilitado == False):
                self.luz_de_carga.apagar()
                self.luz_de_carga2.apagar()    
                self.luz_de_listo.enceder()                
                self.esta_habilitado = True
                    
        if(self.esta_habilitado and self.esta_presionado()):
            self.se_disparo_rayo = True
            
    def esta_presionado(self):
        self.tiempo_chequeo-=1
        if(self.tiempo_chequeo<1):
            self.tiempo_chequeo = 10
            return self.boton.esta_encendido()                 
        return 0
        
    def disparado(self):
        if(self.se_disparo_rayo):
            self.esta_habilitado = False
            self.tiempo_inhabilitacion = 600
            self.se_disparo_rayo = False
            self.luz_de_carga.enceder()
            self.luz_de_carga2.enceder()
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
arduino =iniciar_arduino();
enemigos = pilas.actores.Grupo()

def crear_enemigo():
    actor = AceitunaEnemiga(pilas)
    enemigos.agregar(actor)    
           
pilas.tareas.siempre(0.5, crear_enemigo)

nave = NaveRayo(pilas,y=-200)
nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
nave.definir_enemigos(enemigos, puntaje.aumentar)
pilas.colisiones.agregar(nave, enemigos, nave.eliminar)

pilas.avisar(u"Pulsá los direccionales del teclado o espacio para disparar.")
pilas.ejecutar()

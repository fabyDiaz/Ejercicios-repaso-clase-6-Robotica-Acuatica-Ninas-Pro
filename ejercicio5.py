# Arranque suave (rampa)
# Clase 04 · velocidades y aceleraciones
# Qué observar: la velocidad sube de a poco antes de la marcha de crucero.

import time
from robot_interface import robot_connect

rov = robot_connect.start()

def avanzar_controlado(vel=0.5, dur=2.0, rampa=10):
    
    for i in range(1, rampa + 1):
        rov.set_surge(vel * i / rampa)  # sube de a poco (arranque suave)
        time.sleep(0.05)
    
    time.sleep(dur)                      # mantiene la velocidad de crucero
    rov.stop()                           # siempre al final

avanzar_controlado(vel=0.5, dur=2.0)
robot_connect.stop()

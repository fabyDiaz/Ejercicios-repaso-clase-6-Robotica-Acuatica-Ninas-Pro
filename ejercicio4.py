# Control de profundidad
# Clase 03 · leer, comparar y ajustar

import time
from robot_interface import robot_connect

rov = robot_connect.start()

profundidad_objetivo = 3
tolerancia = 0.5
ganancia = 0.3

while True:
    prof_actual = rov.get_depth()
    error = profundidad_objetivo - prof_actual  # positivo = falta bajar
    if abs(error) > tolerancia:
        rov.set_heave(-ganancia * error)        # heave negativo = baja
        time.sleep(0.1)
    else:
        rov.stop()
        break                                   # llegamos al objetivo

print(f"Profundidad alcanzada: {rov.get_depth():.2f} m")
robot_connect.stop()
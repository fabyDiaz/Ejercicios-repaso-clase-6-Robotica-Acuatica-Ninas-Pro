#Mantener la profundidad
# Clase 04 · bucle de control con for
# Qué observar: el ROV busca 2 m y mantiene esa profundidad mientras dura el bucle.

import time
from robot_interface import robot_connect

rov = robot_connect.start()

objetivo_z = 2.0
margen = 0.5

for paso in range(300):
    actual_z = rov.get_depth()
    error_z = objetivo_z - actual_z
    if abs(error_z) > margen:
        rov.set_heave(-error_z * 0.3)
    else:
        rov.set_heave(0.0)
    time.sleep(0.1)
    if paso % 50 == 0:
        print(f"t={paso * 0.1:.1f}s | prof: {actual_z:.2f} m | error: {error_z:.2f} m")

rov.stop()  # detener al terminar el bucle
robot_connect.stop()
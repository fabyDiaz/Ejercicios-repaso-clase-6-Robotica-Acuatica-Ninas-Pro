#Avanza y gira
import time
from robot_interface import robot_connect

rov = robot_connect.start()

# 1. Avanzar
rov.set_surge(0.5)
time.sleep(3)
rov.stop()

# 2. Girar a la izquierda
rov.set_yaw(0.3)
time.sleep(3)
rov.stop()

pos = rov.get_position()
print(f"Posición: x={pos['x']:.2f} y={pos['y']:.2f} rumbo={rov.get_yaw():.0f}°")
robot_connect.stop()
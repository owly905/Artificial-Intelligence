from py4j.java_gateway import JavaGateway
import math

# Hilfsfunktion zur Formatierung der Zeit und der Koordinaten des Ufos
def format_flight_data(sim):
    return "{0:5.1f} s: [{1:6.1f} {2:6.1f} {3:5.1f}] ".format(
    sim.getTime(), sim.getX(), sim.getY(), sim.getZ())

# Initialisierung des Gateways zur Java-Ufo-Simulation
gateway = JavaGateway()

# In der folgenden Zeile definieren wir eine Referenz auf die Simulation.
sim = gateway.entry_point
sim.reset()

# Oeffnen einer View, die immer on Top angezeigt wird.
# Die Skalierung ist 10 m pro Pixel.
sim.openViewWindow(False, True, 10)

# Ziele des Ufos einzeichnen
sim.addDestination(20.0, 20.0)

# Doppelte Simulationsgeschwindigkeit
sim.setSpeedup(2)

# Meldung auf die Konsole ausgeben und auf Eingabe warten
input("Press return to start...")

# Der folgende Code fliegt das Ufo zur Position (20, 20, 0).

# Das Ufo fliegt senkrecht nach oben mit 10 km/h.
print(format_flight_data(sim) + "takeoff with 10 km/h to alt 10 m...")
sim.setI(90)
sim.requestDeltaV(10)

# Wenn die Hoehe 8m erreicht ist, bremst das Ufo auf 1 km/h.
while sim.getZ() < 8:
    pass
print(format_flight_data(sim) + "...slow down to 1 km/h... ")
sim.requestDeltaV(-9)
    
# Wenn die Hoehe 9.95m erreicht ist, stoppt das Ufo und richtet sich horizontal aus.
while sim.getZ() < 9.95:
    pass
print(format_flight_data(sim) + "...stop and turn horizontal")
sim.requestDeltaV(-1)
sim.setI(0)

# Weiter geht es in Richtung 45 Grad. Die zu fliegende Distanz ist dist.
sim.setD(45)
dist = sim.getDist() + math.sqrt(20 * 20 + 20 * 20)
    
# Das Ufo beschleunigt auf 15 km/h.
print(format_flight_data(sim) + "go " + str(45) + " deg with 15 km/h...")
sim.requestDeltaV(15)
    
# Wenn der Abstand zum Ziel 4m ist, bremst das Ufo auf 1 km/h.
while dist - sim.getDist() > 4:
    pass
print(format_flight_data(sim) + "...slow down to 1 km/h... ")
sim.requestDeltaV(-14)
    
# Wenn der Abstand zum Ziel 0.05m ist, stoppt das Ufo.
while dist - sim.getDist() > 0.05:
    pass
print(format_flight_data(sim) + "...stop")
sim.requestDeltaV(-1)
    
# Das Ufo fliegt senkrecht nach unten mit 10 km/h.
print(format_flight_data(sim) + "landing with 10 km/h")
sim.setI(-90)
sim.requestDeltaV(10)
    
# Wenn die Hoehe 3m erreicht, bremst das Ufo auf 1 km/h.
while sim.getZ() > 3:
    pass
print(format_flight_data(sim) + "...slow down to 1 km/h...")
sim.requestDeltaV(-9)
    
# Das Ufo ist gelandet, wenn die Hoehe kleiner gleich 0 ist.
while sim.getZ() > 0:
    pass
print(format_flight_data(sim) + "...happily landed")

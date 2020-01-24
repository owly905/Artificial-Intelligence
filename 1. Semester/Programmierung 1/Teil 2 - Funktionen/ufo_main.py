from py4j.java_gateway import JavaGateway
from ufo_autopilot import flight_distance
from ufo_autopilot import fly_to

# Initialisierung des Gateways zur Java-Ufo-Simulation
gateway = JavaGateway()

# In der folgenden Zeile definieren wir eine Referenz auf die Simulation.
sim = gateway.entry_point
sim.reset()

# Oeffnen einer View, die immer on Top angezeigt wird.
# Die Skalierung ist 10 m pro Pixel.
sim.openViewWindow(False, True, 10)

# Hier Konsoleingabe des Ziels x, y und der Flughöhe z ergaenzen
sim.addDestination(x, y)

# Simulationsgeschwindigkeit setzen
sim.setSpeedup(10)

# Meldung auf die Konsole ausgeben und auf Eingabe warten
input("Press return to start...")

# Hier Konsolausgabe der zu fliegenden Distanz ergaenzen

# Fliege das Ufo zum Ziel
fly_to(sim, x, y, z)

# Hier Konsolausgabe der tatsächlich geflogenen Distanz ergaenzen

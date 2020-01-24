def fly_to(sim, x, y, z):
    takeoff(sim, z)
    cruise(sim, x, y)
    landing(sim)

def takeoff(sim, z):
    # Das Ufo fliegt senkrecht nach oben mit 10 km/h.
    sim.setI(90)
    sim.requestDeltaV(10)

    # Rechtzeitig vor dem Erreichen der Zielhoehe, bremst das Ufo auf 1 km/h.
    while sim.getZ() < z - 2:
        pass
    sim.requestDeltaV(-9)
    
    # Wenn das Ufo ganz nahe dran ist, stoppt es und richtet sich horizontal aus.
    while sim.getZ() < z - 0.05:
        pass
    sim.requestDeltaV(-1)
    sim.setI(0)

def cruise(sim, x, y):
    # Das Ufo ist in der aktuellen Position gestartet.
    fro_x = sim.getX()
    fro_y = sim.getY()

    # Weiter geht es in Richtung Ziel. Die zu fliegende Distanz ist dist.
    sim.setD(int(angle(fro_x, fro_y, x, y)))
    dist = sim.getDist() + distance(fro_x, fro_y, x, y)
    
    # Das Ufo beschleunigt auf 15 km/h.
    sim.requestDeltaV(15)
    
    # Wenn der Abstand zum Ziel 4m ist, bremst das Ufo auf 1 km/h.
    while dist - sim.getDist() > 4:
        pass
    sim.requestDeltaV(-14)

    # Wenn der Abstand zum Ziel 0.05m ist, stoppt das Ufo.
    while dist - sim.getDist() > 0.05:
        pass
    sim.requestDeltaV(-1)

def landing(sim):
    # Das Ufo fliegt senkrecht nach unten mit 10 km/h.
    sim.setI(-90)
    sim.requestDeltaV(10)
    
    # Wenn die Hoehe 3m erreicht, bremst das Ufo auf 1 km/h.
    while sim.getZ() > 3:
        pass
    sim.requestDeltaV(-9)
    
    # Das Ufo ist gelandet, wenn die Hoehe kleiner gleich 0 ist.
    while sim.getZ() > 0:
        pass
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

    # Kurz vor dem Ziel richten wir das Ufo genau aus.
    fro_x = sim.getX()
    fro_y = sim.getY()
    sim.setD(int(angle(fro_x, fro_y, x, y)))
    dist = sim.getDist() + distance(fro_x, fro_y, x, y)

    # Wenn der Abstand zum Ziel 0.05m ist, stoppt das Ufo.
    while dist - sim.getDist() > 0.05:
        pass
    sim.requestDeltaV(-1)
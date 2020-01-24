from copy import deepcopy
import random
import tkinter as tk

anz_zeilen = 6
anz_spalten = 7
sf = [ ['_','_','_','_','_','_','_'], 
       ['_','_','_','_','_','_','_'], 
       ['_','_','_','_','_','_','_'], 
       ['_','_','_','_','_','_','_'],
       ['_','_','_','_','_','_','_'], 
       ['_','_','_','_','_','_','_'] ]
dran = 'A'
gewonnen = None

def setze(spalte):
    global dran
    if spalte < 0 or spalte >= anz_spalten or sf[0][spalte] != '_':
        return
    for i in range(anz_zeilen):
        if sf[anz_zeilen - i - 1][spalte] == '_':
            sf[anz_zeilen - i - 1][spalte] = dran
            if dran == 'A':
                dran = 'B'
            else:
                dran = 'A'
            return

def finde_reihe():
    for i in range(anz_zeilen):
        for j in range(anz_spalten):
            if sf[i][j] != '_':
                # Ueberpruefe, ob es eine Reihe nach rechts gibt 
                if j + 3 < anz_spalten and sf[i][j] == sf[i][j+1] == sf[i][j+2] == sf[i][j+3]:
                    return [(i,j), (i,j+1), (i,j+2), (i,j+3)]

                # Ueberpruefe, ob es eine Reihe nach rechts unten gibt 
                if i + 3 < anz_zeilen and j + 3 < anz_spalten and sf[i][j] == sf[i+1][j+1] == sf[i+2][j+2] == sf[i+3][j+3]:
                    return [(i,j), (i+1,j+1), (i+2,j+2), (i+3,j+3)]

                # Ueberpruefe, ob es eine Reihe nach unten gibt 
                if i + 3 < anz_zeilen and sf[i][j] == sf[i+1][j] == sf[i+2][j] == sf[i+3][j]:
                    return [(i,j), (i+1,j), (i+2,j), (i+3,j)]

                # Ueberpruefe, ob es eine Reihe nach links unten gibt 
                if i - 3 < anz_zeilen and j + 3 < anz_spalten and sf[i][j] == sf[i-1][j+1] == sf[i-2][j+2] == sf[i-3][j+3]:
                    return [(i,j), (i-1,j+1), (i-2,j+2), (i-3,j+3)]

def random_spalte():
    return random.randint(0, 6)

def zug(spalte):
    global gewonnen
    if dran == 'A':
        setze(spalte)
        root.title("Blau, Clicke auf eine Spalte")
    elif dran == 'B':
        setze(spalte)
        root.title("Rot, Clicke auf eine Spalte")
    
    gewonnen = finde_reihe()

    # Farbwechsel der Buttons
    for i in range(anz_zeilen):
        for j in range(anz_spalten):
            if sf[i][j] == 'A':
                buttons[i][j].configure(bg="red")
            elif sf[i][j] == 'B':
                buttons[i][j].configure(bg="blue")
            else:
                buttons[i][j].configure(bg="white")

    # Falls gewonnen, Vierer mit X markieren und Kommandos zuruecksetzen, damit nicht mehr
    # gesetzt werden kann
    if gewonnen != None:
        for k in range(4):
            buttons[gewonnen[k][0]][gewonnen[k][1]].configure(text='X')
        for i in range(anz_zeilen):
            for j in range(anz_spalten):
                buttons[i][j].configure(command="")
        if dran == 'A':
            root.title("Blau hat gewonnen")
        elif dran == 'B':
            root.title("Rot hat gewonnen")

root = tk.Tk()
buttons = deepcopy(sf)
commands = [lambda :zug(0), lambda :zug(1), lambda :zug(2), lambda :zug(3), lambda :zug(4), lambda :zug(5), lambda :zug(6)]
for i in range(anz_zeilen):
    for j in range(anz_spalten):
        buttons[i][j] = tk.Button(bg="white", width=5, height=2, command=commands[j])
        buttons[i][j].grid(row=i, column=j, padx=1, pady=1)

root.title("Rot, Clicke auf eine Spalte")
root.mainloop()
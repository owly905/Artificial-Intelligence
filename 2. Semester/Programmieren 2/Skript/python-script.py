'''
    Gemeinsamkeiten und Unterschied zwischen Python und Java:
	- Keine implizite Typisierung!
	- Verschiedenes: Syntax von Anweisungen, Operatoren, Kommentare
	- Funktionen
	- Blöcke
	- Kontrollfluss: if, while, for
    - Ausgabe auf Console
'''

def summe(a, b, c):
    ''' Liefert die Summe von a, b und c '''
    return a + b + c

def ggT(x, y):
    ''' Liefert den grössten gemeinsamen Teiler von x und y '''
    while x > 0:
        if x < y:
            x, y = y, x
        x -= y
    return y

wert1, wert2, wert3 = 10, 20, 30

print('Summe: ', summe(wert1, wert2, wert3))
print('ggT(', wert1, ', ', wert2, ') =', ggT(wert1, wert2))
import math

# 1.
n = int(input("Ganze Zahl n > 0: "))
fib_k = 1
fib_k_minus_1 = 0
i = 2

while i <= n:
   temp = fib_k
   fib_k = fib_k + fib_k_minus_1
   fib_k_minus_1 = temp
   i = i + 1

print("Fibonaccizahl fib(" + str(n) + ") = " + str(fib_k))

# 2.
n = int(input("Ganze Zahl n > 0: "))
folge = 1
abstand = 1
i = 1

while i < n:
   folge = folge + abstand
   abstand = abstand + 1
   i = i + 1

print("Das " + str(n) + "-te Glied der Zahlenfolge: " + str(folge))

# 3.
n = int(input("Wie oft soll der Frosch springen? "))
distanz = 0.0
sprung = 1.0

while n > 0:
    distanz = distanz + sprung
    print(" + " + str(sprung), end="")
    sprung = sprung / 2
    n = n - 1

print(" = " + str(distanz))

# 4.
n = int(input("Ganze Zahl n > 0: "))
summe = 0
i = 1

while True:
   summe = summe + i
   i = i + 1
   if not (i <= n):
      break

print("Summe der Zahlen von 1 bis " + str(n) + ": " + str(summe))

# 5.
a = int(input("Ganze Zahl a >= 0: "))
n = int(input("Ganze Zahl n >= 0: "))
r = 1
while n > 0:
    if n % 2 == 0:
        a = a * a
        n = n / 2
    else:
        r = r * a
        n = n - 1
print("a**n = " + str(r))

# 6.
l = 0
r = 1.5
fl = l ** 3 - 1.8 * l ** 2 - 1.2 * l + 1.6
fr = r ** 3 - 1.8 * r ** 2 - 1.2 * r + 1.6

if l < r and fl * fr < 0:
    while r - l > 0.0001:
        x = (l + r) / 2
        fx = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

        if fl * fx < 0:
            r = x
            fr = fx
        else:
            l = x
            fl = fx
    print((l + r) / 2)

# 7.
n = int(input("Ganze Zahl n > 0: "))
summe = 0

for i in range(1, n + 1):
   summe = summe + i

print("Summe der Zahlen von 1 bis " + str(n) + ": " + str(summe))

# 8.
n = int(input("Ganze Zahl n > 0: "))
fak = 1

for i in range (1, n+1):
   fak = fak * i

print("Fakultät von " + str(n) + ": " + str(fak))

# 9.
n = int(input("Ganze Zahl n > 0: "))
folge = 1
abstand = 1

for i in range(1, n):
   folge = folge + abstand
   abstand = abstand + 1

print("Das " + str(n) + "-te Glied der Zahlenfolge: " + str(folge))

# 10.
n = int(input("Ganze Zahl n >= 2: "))
i = 3

while i < n and n % i != 0:
    i = i + 2
if i == n:
    print("Die Zahl n ist eine Primzahl.")
else:
    print("Die Zahl n ist keine Primzahl.")

# oder 

n = int(input("Ganze Zahl n >= 2: "))
i = 3

for i in range(3, n):
    if n % i == 0:
        break
if i == n - 1:
    print("Die Zahl n ist eine Primzahl.")
else:
    print("Die Zahl n ist keine Primzahl.")

# 11.
n = int(input("Zweierpotenz n: "))
i = n
while i > 0:
    ausgabe = ""
    for j in range(0, i):
        ausgabe = ausgabe + "*"
    print(ausgabe)
    i = i // 2

# oder

import itertools

n = int(input("Zweierpotenz n: "))
i = n
while i > 0:
    print("".join(itertools.repeat("*", i)))
    i = i // 2

# 12.
n = int(input("Zweierpotenz n: "))
i = n
while i > 1:
    ausgabe = ""
    for j in range(0, i//2):
        ausgabe = ausgabe + "*"
    for j in range(i//2, n - i//2):
        ausgabe = ausgabe + " "
    for j in range(n - i//2, n):
        ausgabe = ausgabe + "*"
    print(ausgabe)
    i = i // 2
i = 2
while i <= n:
    ausgabe = ""
    for j in range(0, i//2):
        ausgabe = ausgabe + "*"
    for j in range(i//2, n - i//2):
        ausgabe = ausgabe + " "
    for j in range(n - i//2, n):
        ausgabe = ausgabe + "*"
    print(ausgabe)
    i = i * 2
# 1.
def third_char(s):
    t = ""
    i = 2
    while i < len(s):
        t = t + s[i] 
        i = i + 3
    return t

print(third_char("Python!"))
print(third_char("P"))

# 2.
def modulo(a, b):
    while a >= b:
        a = a - b
    return a

print(modulo(11, 3))
print(modulo(12, 3))
print(modulo(3, 11))

# 3.
def max_three(a, b, c):
    if a >= b:
        if a >= c:
            max = a
        else:
            max = c
    else:
        if b >= c:
            max = b
        else:
            max = c
    return max

print(max_three(5, -1, 10))
print(max_three(1, 1, 1))
print(max_three(8, 7, 6))

# 4.
def inc_second(hours, minutes, seconds):
    if seconds == 59:
        seconds = 0
        if minutes == 59:
            minutes = 0
            if hours == 23:
                hours = 0
            else:
                hours += 1
        else:
            minutes += 1
    else:
        seconds += 1
    return (hours, minutes, seconds)

print(inc_second(23, 59, 59))
print(inc_second(10, 10, 10))

# 5.
def is_prefix(s, t):
    if len(s) > len(t):
        return False
    for i in range(0, len(s)):
        if s[i] != t[i]:
            return False
    return True

def is_substring(s, t):
    for i in range(0, len(t)):
        if len(s) > len(t[i:]):
            return False
        if is_prefix(s, t[i:]):
            return True
    return False

print(is_substring("terhas", "Osterhase"))
print(is_substring("Oster", "Osterhase"))
print(is_substring("hase", "Osterhase"))
print(is_substring("stern", "Osterhase"))
print(is_substring("sterhasen", "Osterhase"))
print(is_substring("", "Osterhase"))

# 6.
def zafo(k):
    if k == 1:
        return 1
    else:
        return k - 1 + zafo(k - 1)

print(zafo(1))
print(zafo(4))
print(zafo(7))

# 7.
def count_char(s, c):
    if s == "":
        return 0
    elif s[0] == c[0]:
        return count_char(s[1:], c) + 1
    else:
        return count_char(s[1:], c)

print(count_char("reittier", "r"))
print(count_char("", "r"))
print(count_char("rrrrrr", "r"))

# 9.
# with open("punkte.csv", "r") as fhi:
#     with open("noten.txt", "w") as fho:
#         print("Matrikel   A1   A2   A3   A4   A5   A6   A7   A8 Punkte Note", file=fho)

#         for line in fhi:
#             punkte = line.split(";")
#             summe = 0
#             print(punkte[0].rjust(8, " "), end=" ", file=fho)

#             for i in range(1,9):
#                 summe = summe + float(punkte[i])
#                 print(str(float(punkte[i])).rjust(4, " "), end=" ", file=fho)

#             print(str(summe).rjust(6, " "), end=" ", file=fho)
#             # Die Notenzuordnung fehlt. Jede/r kriegt eine 1.0.
#             print("1.0".rjust(4, " "), file=fho)

# 10. 
# SyntaxError: name 'w' is assigned to before global declaration
# SyntaxError: name 'w' is used prior to global declaration

# 11.
# tom und maja sind Tiere
# maja und tom sind auch Insekten
# maja ist eine Biene

# 12.
# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111
# Die Funktion gibt alle Binärwörter der Länge 4 aus.
a = int(input("gora pierwszego ulamka "))
b = int(input("dol pierwszego ulamka "))
c = int(input("gora drugiego ulamka "))
d = int(input("dul drugiego ulamka "))
x, y = b, d 
iloczyn = x * y
while y > 0:
    x, y = y, x % y
nww = iloczyn // x 
e = (nww // b) * a 
t = (nww // d) * c 
g = e + t
print (f" {a} / {b} +  {c}/{d} = {e}/{nww} + {t}/{nww} = {g}/{nww}")
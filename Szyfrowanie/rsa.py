#PRE
# from math import gcd
# print(gcd(20,15))

# 1. Wybór dużych liczb pierwszych
p = 11
q = 13
print(p,q)

# 2. Obliczenie n=p*q i funkcji Eulera F=(p-1)*(q-1)
n = p * q
F = (p - 1) * (q - 1)
print(n)
print(F)

# 3. Generujemy klucz publiczny e taki że, NWD(e,F)=1
from math import gcd
for i in range(2,F):
    if gcd(i,F) == 1:
        e = i
        break
print(e, n)

# 4. Generujemy klucz prywatny d taki, że (d*e) % F = 1 
for j in range(2,F):
    if ((j*e) % F) == 1:
        d = j
        break
print(d,n)


# Przykład działania RSA
# m - moja wiadomość - message
# c = m**e % n (szyfrogram - cypher - wiadomość zaszyfrowana)
# t = c**d % n (tekst jawny czyli nasza wiadomość - text (message))

m = input()
cipher = ""
for i in m:
    cipher += chr((ord(i)**e)%n)
print(cipher)

tekst=""
for j in cipher:
    tekst += chr((ord(j)**d)%n)
print(tekst)

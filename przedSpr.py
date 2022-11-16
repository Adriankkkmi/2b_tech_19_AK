# print(11%4)

# jak wyodbyć 
# ostatnie 2 cyfry z liczby, 
# albo cyfrę setek?
# n = 12345
# print((n%1000)//100)

# pierwiastek

# from math import sqrt
# print(sqrt(576))
# print(576**(1/2))
# print(8**(1/3))

# ifyyyyy

# == >= <= > < != - operatory porównań

# pętla z liczbami 3-cyfrowymi 
# podzielnymi przez
# 13 i niepodzielnymi przez 4

# for i in range(100,1000):
#     if i % 13 == 0 and i % 4 >= 1: 
#         print(i, end=" ")

# łącznie warunków

# a, b, c, d = 3 , 5, 7, 9
# # if a < b < c < d:
# if a < b and b < c and c < d:
#     print("Eppure si move")

# n = 24
# suma = 0
# ilosc = 0
# for i in range(1,25):
#     if n % i == 0:
#         print(i)
#         suma = suma + i
#         ilosc = ilosc + 1
        
# print("suma", suma)
# print("ilosc", ilosc)


# Zad 1 - Medium - Oblicz sumę k początkowych liczb  trzycyfrowych
# 100 + 101 + 102 + 103 ...
# we: 4
# wy: 406 (100+101+102+103)

# k = 3
# suma = 0
# ilosc = 0
# for i in range(100,1000):
#     suma = suma+i
#     ilosc = ilosc + 1
#     if ilosc == k:
#         break
# print(suma)


# k = 4
# suma = 0
# for i in range(100,100+k):
#     suma = suma+i
# print(suma)

# Zad 2 - Hard - Oblicz sumę n początkowych wyrazów ciągu fibonacciego
# # 1 + 2 + 3 + 5 + 8 + 13 ....

# n = int(input())
# a, b = 0, 1
# suma = 0
# for i in range(n):
#     a, b = b, a+b
#     suma = suma + b
# print(suma)

# Zad 3 - Hard - Spradź czy liczba wpisana przez usera jest doskonała
# doskonała to taka, która jest równa sumie swoich dzielników bez niej samej

n = 496
suma = 0
for i in range(1,n):
    if n % i == 0:
        suma = suma + i
        
if suma == n:
    print("TAK")
else:
    print("NIE")


# Zad 4 - Medium - Oblicz sumę liczb dwucyfrowych parzystych podzielnych przez 7
# Sprawa oczywista :)
#zad1 
# suma = 0
# a = int(input())
# for i in range(a):
#   b = int(input())
#   suma += i
# print( suma )

#zad2
# n = int(input())
# for i in range (2, n ):
#   if n % i == 0 :
#     print("lizcba nie jest pierwsza ")
#     exit(0)
# print("liczba jest pierwsza")

#zad3
# suma = 0
# a = int(input())
# for i in range( 1, a):
#   if a % i == 0 
#   suma += i 
# if suma == a :
#   print("tak")
# else:
#   print ("nie")

# zad 4 
# a, b = int(input()), int(input())
# while a != b :
#   if a > b : a = a - b 
#   if b > a : b = b - a 
# if a == 1:
#   print ("TAK")
# else: 
#   print ("nie")

#zad 5 
# m = int(input())
# lista = ""
# for i in range(10,20):
#     x = i
#     y = m
#     while y != x:
#         if x > y : x = x - y
#         if y > x : y = y - x
#     if x == 1:
#         lista += f"{i}\n"
# print(lista)

# zad 5 dwie wersje
# X = int(input("P))
# for Y in range(10,20):
#     x = X
#     y = Y
#     while x != y:
#         if x > y:
#             x -= y
#         else:
#             y -= x
#     if x == 1:
#         print(Y)

#zad 6
# a, b = int(input()), int(input())
# for i in range(min(a,b), 1, -1):
#     if a % i == 0 and b % i == 0:
#         a, b = a // i, b // i
# print(f"{a}/{b}")

#zad7
# a, b = int(input()), int(input())
# cal = a // b
# a -= cal * b
# for i in range(a, 1, -1):
#     if a % i == 0 and b % i == 0:
#         a, b = a / i, b / i
# print(f"{cal}  {int(a)}/{int(b)}")


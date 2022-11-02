# PRE
# print(list(range(2, 8,1 )))
# print(list(range(1, 8,)))
# print(list(range(8, 1 , -1 )))

# pętla liczb dwucyfrowych od 10 do 21
# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# pętla liczb dwucyfrowych malejąco (step ujemny)
# pętla liczb dwucyfrowych malejąco (step dodatni)
# pętla liczb 3-cyfrowych podzielnych przez 20


# for i in range(3,10):
#   print (i)

# for n in range(10, 22):
#   print (n)

# for n in range (15, 32, 2): 
#   print (n)

# for n in range (10, 100, 1 ):
#   print (109-n)
  
# for n in range (100,1000, 20):
#   print (n end = "-")



# # Zad 1
# n = int(input())
# for n in range (n):
#   print (n**3 + 3, end =" " )

# # Zad 2 
# for n in range (100, 1000, 15):
#   print (n, end=" ")

# for n in range (100, 1000,):
#   if n % 15 ==0 
#  print (n, end=" ")


# Zad 3
# print("zadanie 3")
# p = int(input("podaj liczbę"))
# for n in range(1, p+1 ):
#   if p % n == 0: 
#     print (n)

# Zad 4 
# suma = 0 
# for n in range(10, 100):
#   suma += n 
# print (suma)

# Zad 5 

# n = int(input("W ile gramy "))
# suma = ((n+1)*n) // 2

# for i in range(n-1):
#   a = int(input())
#   suma = suma - a
# print (suma)


# Zad 6

# for n in range(1, n + n ):

#   print(n)




# napisz pętle sumującą liczby dwu cyfrowe parzyste 
# suma = 0
# for n in range (10, 100, 2):
#   suma += n 
# print ("suma parzystych liczb dwucyfrowych ", suma)


# zad 6 
n = int(input("podaj liczby  "))
a = 0
b = 1 
for i in range(n):
  a, b = b, a + b  
print (b)

# #1 sprawdzanie czy liczba jest 1 

n = int(input())
for i in range (2, n ):
  if n % i == 0 :
    print("lizcba nie jest pierwsza ")
    exit(0)
print("liczba jest pierwsza")85



#2. generowanie liczb 1 

n = int(input("do jakiej liczby pierwszej "))
for i in range(2, n+1 ):
  flaga = True
  for j in range(2, i ):
    if i % j == 0 :
      flaga = False
      break
  if flaga: 
    print ( i, end = " ")
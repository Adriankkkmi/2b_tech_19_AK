# # #1 sprawdzanie czy liczba jest 1 

# n = int(input())
# for i in range (2, n ):
#   if n % i == 0 :
#     print("lizcba nie jest pierwsza ")
#     exit(0)
# print("liczba jest pierwsza")85



# #2. generowanie liczb 1 

# n = int(input("do jakiej liczby pierwszej "))
# for i in range(2, n+1 ):
#   flaga = True
#   for j in range(2, i ):
#     if i % j == 0 :
#       flaga = False
#       break
#   if flaga: 
#     print ( i, end = " ")



# 3 ggenerowanie liczb pierwszych ( pierwsze n liczb pierwszych )

p = int(input("Podaj od ilu mam szukać liczb pierwszych: \n"))
i = 2 
liczbik = 0
while 1:
    flaga = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            flaga = False
            break
    if flaga == True:
        print(i, end=" ")
      licznik += 1
    if licznik == p:
      break
    else: 
      i = i+1
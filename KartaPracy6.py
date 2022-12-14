# Zad 1 

# a,b,c = int(input()), int(input()), int(input())
# if b - a == c - b :
#   print("arytmetyczny")
# if b*2 > a and c*2 > b:
#   print ("geometryczny")
# if a <b <c :
#   print ("rosnący")
# if a>b>c :
#   print ("malejący")

# Zad 2 
# suma = 0
# for i in range (100, 1000):
#  if  i % 8 == 0 and   i % 16 != 0 :
#     suma += i 
# print (suma)

# Zad 3 
# ilosc = 0 
# for i in range(10, 100 ):
#   cd = i//10
#   cj = i % 10 
#   if cd >= 2 * cj:
#     ilosc += 1 
# print ( ilosc )

# # Zad 4 
# ilosc = 0 
# for i in range (10, 100 ):
#   cd = i // 10 
#   cj = i % 10 
#   if cd*2 > cj:
#    ilosc += 1
# print (ilosc)

# zad 5
# suma = 0 
# for i in range (100, 1000 ):
#   cs = i // 100 
#   cd = (i % 100) // 10 
#   cj = i % 10
#   if cs > cd > cj:
#     suma += 1
# print ( suma )

# zad 6
suma = 0
a = int(input())
for i in range (10, 100  ):
  
  if i % 19 == 0 :
    suma += i
print ( suma )  
# #Zad 1 
# a,b,c = int(input()), int(input()), int(input())
# for i in range (0, 10):
#    if a +2  >= b and b +2  >= c and c -2 <b : 
#     print ( "ok" )
# else:
#   print("nie")

# # proba zad 1 
# a,b,c = int(input()), int(input()), int(input())
# for i in range (0, 10):
#    if a%1000 == a >b and b %100 == b > c and c % 10 == c<b :
#     print ( "ok" )
# else:
#   print("nie")

  
#Zad 2 
suma = 0
a = int(input("ile ułamków"))
for i in range(1, a+1):
  x = int(input( "góra ułamka "))
  y = int(input("dół ułamka " ))
  suma = suma + x/y 
print ( suma )

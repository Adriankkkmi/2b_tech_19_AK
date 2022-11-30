# NWD 
# a = int(input())
# b = int(input())
# while a != b :
#   if a > b : a = a - b 
#   if b > a : b = b - a 
# print (a)


# euklides modulo
# a = int(input())
# b = int(input())
# while b>0:
#   a, b = b, a%b 
#   print (a)



# # NWW - odej omwanie
# a = int(input())
# b = int(input())
# c = a * b 
# while a != b :
#     if a > b : a = a - b 
#     if b > a : b = b - a 
#     print ("NWD ", a) 
#     break
# d = c / a  
# print ("NWW", d)\


a = int(input())
b = int(input())
while b>0:
  a, b = b, a%b 
NWD = a 
print(a)
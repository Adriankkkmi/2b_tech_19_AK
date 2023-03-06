# napisy (stringi) są "prawie listami"

# s = input()
# print(s)

# for x in s:
#     print(x)

# for i in range(len(s)):
#     print(s[i])

# L = [5, 7, 1, 4]
# print(s, L)
# L.sort()
# print(s, L)
# s.sort() -> to nie działa, błąd
# print(s, L)

# konwersja lista <-> napis (list(), join())

# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# s = "".join(L)
# print(s, L)

# sprawdz czy napis jest palindromem

s = input()
L = list(s)
R = L.copy()
R.reverse()
if L == R:
    print("TAK")
else:
    print("NIE")

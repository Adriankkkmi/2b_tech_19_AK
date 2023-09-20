W = "AAAAABBCCCCDDDEEEEEEEFGGGH" # 5A2B4C3D7EF3G
W += "."
ilosc = 1
H = ""
for i in range(len(W)-1):
    if W[i] == W[i+1]:
        ilosc += 1
    else:
        if ilosc > 1:
            H += str(ilosc)
        H += W[i]
        ilosc = 1
print(H)

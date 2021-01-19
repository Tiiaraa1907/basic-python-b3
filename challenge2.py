def lingkaran(r):
    luas = 22/7*(r**2)
    keliling= 2*22/7*r

    return luas,keliling

r=int(input("r= "))
print(lingkaran(r))

print("{:.2f}" .format(lingkaran(r)))
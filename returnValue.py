# def my_function(x):
#     return 5 * x

# print(my_function(3)) 
# print(my_function(5)) 
# print(my_function(9))

def rectangle(p,l):
    luas=p*l
    keliling=2*p + 2*l
    return luas, keliling

p = int(input("panjang = "))
l = int(input("lebar = "))

print(rectangle(p,l))
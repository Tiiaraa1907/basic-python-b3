# print(10<8)
# print(10>8)
# print(10==8)
# print(10!=8)


#untuk membuat comment, bisa diblok terus ctrl+/(slash)

a=int(input("input the number: "))
b=int(input("input the number: "))
if(a%2==0 and b%2!=0):
    print("{} is even number and {} is odd number" .format(a,b))
elif(a%2!=0 and b%2==0):
     print("{} is odd number and {} is even number" .format(a,b))
else :
    print("Undefined")


# NOTED!
# not is mean not same, if we type not 10, it's mean not 10
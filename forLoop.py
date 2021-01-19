fruits = ["apple" , "mango"]

for x in fruits :
    print(x)


#show the number of data
tnoData = len(fruits)
for i in range(tnoData):
    print(fruits[i])

add=3
for j in range(add):
    fruits.append(input("add the fruits: "))


print(fruits)
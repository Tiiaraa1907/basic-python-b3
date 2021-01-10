number="The number is 5"
numberList=["The", "number", "is" ,"5"]

print(number)
print(numberList)

# #to add the string
# #before
print(numberList)

# #after
numberList.append("guys!!!")
print(numberList)

#looping
for x in numberList:
    print(x)


for x in range(0,len(numberList)):
    print(x)

result = ""
for x in range(0,len(numberList)):
    result +=numberList[x]+ " "
    print(result)
cust=int(input("The number of customer = "))
i=1
while i<=cust:
    name=input("Name = ")
    age= int(input("Age = "))
    print("Customer {} is {} , {} years old." .format(i,name,age))
    print("\n")
    i+=1
   
  
class Person(object):
    def __init__(self, name, idnumber):    
        self.name = name 
        self.idnumber = idnumber 
    def display(self): 
        print(self.name) 
        print(self.idnumber)

class Employee( Person ):            
    def __init__(self, name, idnumber, salary, post): 
        self.salary = salary 
        self.post = post 

        Person.__init__(self, name, idnumber)  
    def display2(self): 
        print(self.name) 
        print(self.idnumber)
        print(self.salary) 
        print(self.post)

a = Employee('Kim', 990654, 990876, "Mira")  
a.display()
print("==============")
a.display2()
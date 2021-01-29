class Person:
    def __init__(self,name,age,namaLawan):
        self.name = name
        self.age = age
        self.namaLawan = namaLawan
    
    def sapa(self):
        print("Hallo namaku "+self.name)
        print("Nama kamu siapa ?")
    
    def salamkenal(self):
        print("Salam kenal "+self.namaLawan)
        print("Senang bertemu denganmu. sampai jumpa kembali")
# import module
# p1 = module.Person("Tiara",17,"Ara")
# p1.sapa()
# p1.salamkenal()

# p1 = Person("Tiara",17)
# p2 = Person("Ara",18)
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)
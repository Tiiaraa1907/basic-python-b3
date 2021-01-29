class Biodata:
    def __init__(self,name,age,alamat,hoby,phone):
        self.name = name
        self.age = age
        self.alamat = alamat
        self.hoby = hoby
        self.phone = phone
    
    def display(self):
        print("Perkenalkan namaku {} umur ku {} tahun, aku menetap di {}. di {} aku sering bermain {}.".format(self.name,self.age,self.alamat,self.alamat,self.hoby))
        print("Salam kenal kamu!")
        print("phone : "+self.phone)

nama = input("Namamu : ")
umur = input("Umurmu : ")
alamat = input("Alamatmu : ")
hoby = input("Hobymu : ")
phone = input("Phonemu : ")

bio = Biodata(nama,umur,alamat,hoby,phone)
bio.display()
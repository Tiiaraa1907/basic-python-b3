f=open("file.txt","a")
f.write("\nTiara")
f.close()

# f=open("file.txt","w")
# f.write("Tambah text")
# f.close()

f=open("file.txt","r")
# print(f.read())
# print(f.read(1))
print(f.readlines())


x=f.readlines()
print(x)
print(x[0])

#w menindih/mengganti
#a menambahkan
#r membaca
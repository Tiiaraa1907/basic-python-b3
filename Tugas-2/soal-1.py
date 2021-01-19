print("Selamat Datang!")
print("---Menu---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar") 

nama=["Tiara", "Ara"]
noTelp=["088230588835","082244738256"]

iinput = int(input("Pilih menu : "))
i=0
if(iinput == 1):
    print("Daftar Kontak : ")
    while i<=1:
        print("Nama : {}" .format(nama[i]))
        print("No. Telepon : {}" .format(noTelp[i]))
        i+=1

elif(iinput==2):
    nama.append(input("Nama : "))
    noTelp.append(input("No. Telepon : "))
    print("Kontak berhasil ditambahkan")
    print("Nama : {}" .format(nama[i]))
    print("No. Telepon : {}" .format(noTelp[i]))

elif(iinput==3):
    print("Program selesai, sampai jumpa!")
else:
    print("Menu tidak tersedia")

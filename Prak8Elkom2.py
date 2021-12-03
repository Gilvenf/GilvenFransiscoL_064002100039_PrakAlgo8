print("PROGRAM MENGHITUNG JUMLAH RANGE")
angka1=int(input("Masukkan Angka Pertama: "))
angka2=int(input("Masukkan Angka Kedua: "))
jumlah_range=0
for i in range(angka1,angka2+1):
    jumlah_range+=i
    print(i)
print(jumlah_range)
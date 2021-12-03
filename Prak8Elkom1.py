print("PROGRAM MEMUNCULKAN KARAKTER INDEX GANJIL")
kata=input("Masukkan Sebuah Kata:")
hkata=""
for i in range(len(kata)):
    if i %2==1:
        hkata+=kata[i]
print(hkata)
#1. Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia 
#tersebut berdasarkan kriteria berikut: 
#• 0 - 12 tahun: Anak-anak 
#• 13 - 17 tahun: Remaja 
#• 18 - 59 tahun: Dewasa 
#• 60 tahun ke atas: lansia

# ELIF = else if statement
usia = int(input("Masukkan usia: "))

if usia >= 0 and usia <= 12:
    print("masuk: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("masuk: Remaja")
elif usia >= 18 and usia <= 59:
    print("masuk: Dewasa")
else:
    print("masuk: Lansia")
print("end")


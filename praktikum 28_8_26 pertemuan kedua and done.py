# string itu kata dan ada petiknya " , dan variabel itu tempat atau perwakilan
#iteger itu angka bulat 123
#float itu desimal 1,2 / 1,3 sbg
#biner or boolean itu true false

#ATURAN PENULISAN, tdk boleh spasi, tdk diawali angka, pakai camelcase

#SESI 2 latihan soal, belum TUGASS

# tipe data: Angka desimal berkomanya (float)
y = 21.5
print (y) 

# tipe data: kalimat biasa dengan petik (string)
z = "Huda"
print (z)

#tipe data: biner (boolean) true or false
a = True
print (a)

#nice one and good 
#kemudian masuk ke tugas

nama = "\nMuhammad Nur Huda"      # string -> pakai tanda kutip
umur = 18              # umur dalam bentuk integer
berat = 100              # berat dalam bentuk float

print("data : ",nama,umur,berat) 
print("- bertipe ", type(nama), type(umur), type(berat))

#Ubah data string menjadi integer

angka_string = "123" 
angka_float = 45.67 
angka_integer = 89

# 1. Konversi angka_string menjadi integer 
data_int = int(angka_string)
print("data = ", data_int, ",type = ", type(data_int)) 

# 2. Konversi angka_float menjadi integer
data_int2 = int(angka_float)
print("data = ", data_int2, ",type = ", type(data_int2))

# 3. Konversi angka_integer menjadi string
data_str = str(angka_integer)
print("data = ", data_str, ",type = ", type(data_str))

angka= int(input("imputlah usia:") )
print("data ",angka,",type = ",type(angka))

angka= float(input("imputlah tinggi badan (cm): ") )
print("data ",angka,",type = ",type(angka))

nama = input("imputlah nama: ") 
print("data ",nama,",type =",type(nama)) 
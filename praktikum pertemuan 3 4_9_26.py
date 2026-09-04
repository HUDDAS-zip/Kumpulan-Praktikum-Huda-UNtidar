#konfersi celcius ke satuan lainnya
 
celcius = float(input('Masukan suhu dalam celcius : ')) 
print("suhu adalah", celcius, "Celcius") 

#konversi ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur") 

# fahrenheit 
fahrenheit = ((9/5) * celcius) + 32 
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit") 
 
# kelvin 
kelvin = celcius + 273 
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")


# setiap hasil dari operasi komperasi adalah boolean  
# >,<,>=,<=,==,!=,is,is not 
# Tapi karena pada soal 1 kita hanya menggunakan > dan < maka kita akan membahasnya pada lingkup ini saja.
a = 10
b = 8

# lebih besar dari > 
print("lebih besar dari (>)") 
hasil = a > 3 
print(a,'>',b,'=',hasil) 
hasil = b > 3 
print(b,'>',3,'=',hasil) 
hasil = b > 2 
print(b,'>',2,'=',hasil) 
 
# kurang dari < 
print("kurang dari (<)") 
hasil = a < 3 
print(a,'<',b,'=',hasil) 
hasil = b < 3 
print(b,'<',3,'=',hasil) 
hasil = b < 2 
print(b,'<',2,'=',hasil)


#test
#operasi aritmatika 
#menjawab soal dari 1. Diberikan sebuah bangunan dengan nilai berikut
#• Panjang = 12 
#• Lebar = 5 
#• Tinggi = 8

#a. Hitunglah luas, volume dan keliling dari bangunan tersebut! 
#tinggi adalah 8, panjang adalah 12, lebar adalah 5

# volume bangunan tersebut 
a= 12
b= 5
c= 8
total = a * b * c
print(a,'*',b,'*',c,'=',total) 

#Luas bangunan tersebut
total2 = 2 * (a * b + a * c + b * c)
print(2 ,'*' ,'(',a ,'*' ,b ,'+' ,a ,'*' ,c ,'+' ,b ,'*' ,c ,')', '=', total2)

# Keliling bangunan tersebut
total3 = 4 * (a + b + c)
print(4 ,'*' ,'(',a ,'+' ,b ,'+' ,c ,')', '=', total3)

#b. Apakah luas bangunan tersebut lebih luas dari 50?
 
hasil = total2 > 50
print((2 ,'*' ,'(',a ,'*' ,b ,'+' ,a ,'*' ,c ,'+' ,b ,'*' ,c ,')', '=', total2), '>', 50, '=', hasil)

#c. Apakah volume tersebut bernilai 480? 
hasil = total == 480
print((a ,'*' ,b ,'*' ,c ,')', '=', total), '==', 480, '=', hasil)

#d. Jawab pertanyaan di atas menggunakan program
print('sudah dijawab di atas')
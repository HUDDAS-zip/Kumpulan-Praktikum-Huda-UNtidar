#hai
kartu = 'aktif'
saldo = 100000
saldoTarik = int(input("masukkan Jumlah Tarik"))

if kartu == 'aktif':
    if saldoTarik <= saldo:
        if saldoTarik >= 50000:
            saldo = saldo - saldoTarik
            print(f"penarikan bisa mase, saldo yg ditarik: Rp {saldoTarik}")
            print(f"sisa saldo anda adalah: Rp {saldo}")
        else:
            print("gak iso mas, kurang narik e")
    else:
        print ("saldo kurank mas")
else:
    print("status kartu kadaluarsa")

#nested while
i = 1
while i <=3:
    j = 1
    while j <= 6:
        print ("hidoep TIF")
        j = j + 1
        print ("\n")
        i = i + 1

        
#for in while 
# sesi = 1
# while sesi <= 2:
#     print (f"ini sesi ke = {sesi} :")

# for anteran in range (1, 4):
#     print (f"sedang ngelayani nomor: {anteran}")

# sesi = sesi + 1
# print ("selesai")
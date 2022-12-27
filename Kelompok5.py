from bangun_datar import *
from bangun_ruang import *

while True :
    print('''\nAPLIKASI MENGHITUNG LUAS BANGUN DATAR DAN RUANG
KELOMPOK 5
1. Menghitung luas bangun datar
2. Menghitung luas bangun ruang
0. Quit''')
    opt = int(input('\nPilih : '))
    if opt == 1 :
        while True :
            print('''\nMENGHITUNG LUAS BANGUN DATAR
1. persegi
2. persegi panjang
3. segitiga
4. lingkaran
5. jajar genjang
6. belah ketupat
7. layang layang 
8. trapesium
0. Quit''')
            opt = int(input('\nPilih : '))
            if opt == 1 :
                sisi = int(input('\nMasukan panjang sisi : '))
                luas = luas_persegi(sisi)
                print('Luas persegi adalah : ',luas)
            elif opt == 2 :
                panjang = int(input('\nMasukan panjang : '))
                lebar = int(input('Masukan Lebar : '))
                luas = luas_persegi_panjang(panjang,lebar)
                print('Luas persegi panjang adalah : ',luas)
            elif opt == 3 :
                tinggi = int(input('Masukan tinggi : '))
                alas = int(input('Masukan alas   : '))
                luas = luas_segitiga(tinggi,alas)
                print('\nLuas segitiga adalah ',luas)
            elif opt == 4 :
                ruas = int(input('\nMasukan jari-jari lingkaran : '))
                luas = luas_lingkaran(ruas)
                print('Luas lingkaran adalah %0.2f '%luas)
            elif opt == 0 :
                quit = input('\nApakah anda ingin keluar? (y/n) :')
                if quit == 'y' :
                    print('Terima kasih telah menggunakan program ini'.upper())
                    break
    elif opt == 2 :
            while True :
                print('''\nMENGHITUNG LUAS BANGUN RUANG
1. Balok
2. Kubus
3. Kerucut
4. Prisma
5. Limas
6. Tabung
7. Bola
0. Quit''')
                opt = int(input('\nPilih : '))
                if opt == 1 :
                    panjang = int(input('\nMasukan panjang : '))
                    lebar = int(input('Masukan Lebar : '))
                    tinggi = int(input('Masukan tinggi : '))
                    luas = luas_balok(panjang,lebar,tinggi)
                    print('Luas Balok adalah ',luas)
                elif opt == 2:
                    pass
                elif opt == 3:
                    pass
                elif opt == 4:
                    pass
                elif opt == 5:
                    pass
                elif opt == 6:
                    pass
                elif opt == 7:
                    pass
                elif opt == 8:
                    pass
                elif opt == 0:
                    quit = input('\nApakah anda ingin keluar? (y/n) :')
                    if quit == 'y':
                        print('Terima kasih telah menggunakan program ini'.upper())
                        break
    elif opt == 0 :
        quit = input('\nApakah anda ingin keluar? (y/n) :')
        if quit == 'y' :
            print('Terima kasih telah menggunakan program ini'.upper())
            break    
    else:
        print('ERROR - MOHON MASUKAN NOMOR YANG TERDAPAT DI MENU')
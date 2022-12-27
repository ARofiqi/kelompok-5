from tugas.bangun_datar import *
from tugas.bangun_ruang import *

while True :
    print('\nAPLIKASI MENGHITUNG LUAS BANGUN DATAR DAN RUANG')
    print('KELOMPOK 5')
    print('''\n1. Menghitung luas bangun datar
2. Menghitung luas bangun ruang
3. Quit''')

    opt = int(input('\nMasukan nomor : '))

    if opt == 1 :
        while True :
            print('\nMENGHITUNG LUAS BANGUN DATAR')
            print('''\n1. Menghitung luas persegi
2. Menghitung luas persegi panjang
3. Menghitung luas segitiga
4. Menghitung luas lingkaran
5. Quit''')

            opt = int(input('\nPilih nomor rumus luas bangun datar : '))

            if opt == 1 :
                luas = luas_persegi(sisi=int(input('\nMasukan panjang sisi : ')))
                print('Luas persegi adalah : ',luas)
                

            elif opt == 2 :
                luas = luas_persegi_panjang(
                    panjang=int(input('\nMasukan panjang : ')),
                    lebar=int(input('Masukan Lebar : '))
                )
                print('Luas persegi panjang adalah : ',luas)
                

            elif opt == 3 :
                luas = luas_segitiga(
                    alas=int(input('\nMasukan alas   : ')),
                    tinggi=int(input('Masukan tinggi : '))
                )
                print('\nLuas segitiga adalah : ',luas)
                

            elif opt == 4 :
                luas = luas_lingkaran(ruas=int(input('\nMasukan jari-jari lingkaran : ')),)
                print('Luas lingkaran adalah %0.2f: '%luas)
                

            elif opt == 5 :
                quit = input('\nApakah anda ingin keluar? (y/n) :')
                if quit == 'y' :
                    print('Terima kasih telah menggunakan program ini'.upper())
                    break
                else : continue

    elif opt == 2 :
        luas = luas_balok(
            panjang=int(input('\nMasukan panjang : ')),
            lebar=int(input('Masukan Lebar : ')),
            tinggi=int(input('Masukan tinggi : '))
        )
        print('Luas persegi panjang adalah : ',luas)

    elif opt == 3 :
        quit = input('\nApakah anda ingin keluar? (y/n) :')
        if quit == 'y' :
            print('Terima kasih telah menggunakan program ini'.upper())
            break
        else : continue
    
    else :
        print('ERROR - MOHON MASUKAN NOMOR YANG TERDAPAT DI MENU')



import math

def CetakJudul():
    Title01 = 'Cetak Judul Dari Function'
    Title02 = 'Function ini dipanggil dari main program'
    print(Title01)
    print(Title02)

def HitungLuasPersegi():
    print('\nMenghitung Luas Persegi Dari Function')
    Panjang = 10
    Lebar = 4
    Luas = Panjang * Lebar
    print('Luar Persegi Panjang  = %2.2f2'%Luas)

def HitungLuasLingkaran():
    print('\nMenghitung Luas Lingkaran Dari Function')
    r = input('Masukkan JariJari =')
    HitungLuasLingkaran = math.pi * float(r) * float(r)
    print('Luas Lingkaran = %5.2f'% HitungLuasLingkaran)


Judul01 = 'Cetak Judul Tanpa Function'
Judul02 = 'Judul02 Dicetak disini'
print(Judul01)
print(Judul02)
print('\n')
CetakJudul()
HitungLuasPersegi()
HitungLuasLingkaran()    

    
            
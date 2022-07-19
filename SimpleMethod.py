import math

class SimpleMethod:

    def CetakJudul():
        Title01 = 'Cetak Judul dari class method'
        Title02 = 'Method ini dipanggil dari main program'
        print(Title01)
        print(Title02)

    def HitungLuasPersegi():
        print('\nMenghitung Luas Persegi Dari Method')
        Panjang = 10
        Lebar = 4
        Luas = Panjang * Lebar
        print('Luar Persegi Panjang  = %2.2f2'%Luas)

    def HitungLuasLingkaran(self):
        print('\nMenghitung Luas Lingkaran Dari Function')
        r = input('Masukkan JariJari =')
        HitungLuasLingkaran = math.pi * float(r) * float(r)
        print('Luas Lingkaran = %5.2f'% HitungLuasLingkaran)


Judul01 = 'Cetak Judul Tanpa Class Method'
Judul02 = 'Judul02 Dicetak disini'
print(Judul01)
print(Judul02)
print('\n')
myMethod = SimpleMethod()
myMethod.CetakJudul()
myMethod.HitungLuasPersegi()
myMethod.HitungLuasLingkaran()


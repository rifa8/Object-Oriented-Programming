# tulis solusi code disini
class BangunDatar:
    def luas(self):
        pass

    def keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return self.sisi * 4

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi_miring = ((self.alas ** 2) + (self.tinggi ** 2)) ** 0.5

    def luas(self):
        return self.alas * self.tinggi * 0.5

    def keliling(self):
        return self.alas + self.tinggi + self.sisi_miring

class Persegi_panjang(BangunDatar):
    def __init__(self, lebar, panjang):
        self.lebar = lebar
        self.panjang = panjang

    def luas(self):
        return self.lebar * self.panjang

    def keliling(self):
        return 2 * (self.lebar + self.panjang)

persegi = Persegi(4)
segitiga = Segitiga(3, 4)
persegi_panjang = Persegi_panjang(7, 8)

print(f'Luas\nPersegi : {persegi.luas()}\nSegitiga : {segitiga.luas()}\nPersegi Panjang : {persegi_panjang.luas()}\nKeliling\nPersegi : {persegi.keliling()}\nSegitiga : {segitiga.keliling()}\nPersegi Panjang : {persegi_panjang.keliling()}')

# tulis solusi code disini
class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, tinggi, lebar, panjang):
        self.tinggi = tinggi
        self.lebar = lebar
        self.panjang = panjang

    def volume(self):
        return self.tinggi * self.lebar * self.panjang

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
        self.pi = 22/7

    def volume(self):
        return self.pi * (self.jari_jari ** 2) *self.tinggi

kubus = Kubus(10)
balok = Balok(3,6,10)
tabung = Tabung(7,10)

print(f'Volume\nKubus : {kubus.volume()}\nBalok : {balok.volume()}\nTabung : {tabung.volume()}')

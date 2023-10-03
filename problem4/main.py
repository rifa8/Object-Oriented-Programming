# tulis solusi code disini
class Ongkir:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = ''.join(filter(str.isdigit, berat))
        self.harga_standar = 5000

    def volume_barang(self):
        return self.panjang * self.lebar * self.tinggi

    def harga_ongkir(self):
        volume = self.volume_barang()
        pembulatan_berat = round(int(self.berat))
        if volume >= 50 or pembulatan_berat == 1:
            return self.harga_standar
        else:
            return None

data_barang = Ongkir(5,2,4,'1 kg')

print(f'Harga : Rp {data_barang.harga_ongkir()}')

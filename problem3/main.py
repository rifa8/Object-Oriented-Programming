# tulis solusi code disini
class Kalkulator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def penjumlahan(self):
        return self.num1 + self.num2

    def pengurangan(self):
        return self.num1 - self.num2

    def perkalian(self):
        return self.num1 * self.num2

    def pembagian(self):
        return self.num1 / self.num2

tambah = Kalkulator(3,4)
kurang = Kalkulator(15,4)
kali = Kalkulator(10,10)
bagi = Kalkulator(12,3)

print(f'Penjumlahan : {tambah.penjumlahan()}\nPengurangan : {kurang.pengurangan()}\nPerkalian : {kali.perkalian()}\nPembagian : {bagi.pembagian()}')

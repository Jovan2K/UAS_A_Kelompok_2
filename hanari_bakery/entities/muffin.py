
from entities.produk import Produk
from interfaces.pengembang import Pengembang
from interfaces.topping import Topping

class Muffin(Produk, Pengembang, Topping):
    def pengadonan(self):
        print(f"{self.nama}: Mengaduk bahan muffin...")

    def pengembangan(self):
        print(f"{self.nama}: Muffin dibiarkan mengembang 45 menit...")

    def pemanggangan(self):
        print(f"{self.nama}: Dipanggang 25 menit di suhu 175°C.")

    def tambah_topping(self):
        print(f"{self.nama}: Menambahkan topping kacang/krim.")

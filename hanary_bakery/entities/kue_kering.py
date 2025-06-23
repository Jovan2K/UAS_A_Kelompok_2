from entities.produk import Produk
from interfaces.topping import Topping

class KueKering(Produk, Topping):
    def pengadonan(self):
        print(f"{self.nama}: Campur tepung, telur, mentega...")

    def pemanggangan(self):
        print(f"{self.nama}: Kue kering dipanggang 20 menit.")

    def tambah_topping(self):
        print(f"{self.nama}: Topping coklat ditambahkan.")

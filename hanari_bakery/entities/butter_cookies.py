
from entities.produk import Produk
from interfaces.topping import Topping

class ButterCookies(Produk, Topping):
    def pengadonan(self):
        print(f"{self.nama}: Mengocok mentega dan gula...")

    def pemanggangan(self):
        print(f"{self.nama}: Dipanggang 15 menit di suhu 160°C.")

    def tambah_topping(self):
        print(f"{self.nama}: Menambahkan topping gula halus.")

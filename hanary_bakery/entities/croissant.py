from entities.produk import Produk
from interfaces.pengembang import Pengembang

class Croissant(Produk, Pengembang):
    def pengadonan(self):
        print(f"{self.nama}: Proses pengadonan croissant dimulai...")

    def pengembangan(self):
        print(f"{self.nama}: Adonan mengembang selama 1 jam...")

    def pemanggangan(self):
        print(f"{self.nama}: Dipanggang selama 20 menit pada 180°C.")

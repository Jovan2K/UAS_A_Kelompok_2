from entities.produk import Produk
from interfaces.pengembang import Pengembang

class RotiManis(Produk, Pengembang):
    def pengadonan(self):
        print(f"{self.nama}: Adonan roti manis sedang diuleni...")

    def pengembangan(self):
        print(f"{self.nama}: Mengembang selama 1.5 jam.")

    def pemanggangan(self):
        print(f"{self.nama}: Roti manis dipanggang selama 30 menit.")


from abc import ABC, abstractmethod
from tabulate import tabulate

class Produk(ABC):
    def __init__(self, nama, kode, bahan_baku: dict, biaya_produksi, harga_jual):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def tampilkan_data(self):
        print(f"\n[INFO PRODUK: {self.nama}]")
        print(f"Kode Produk     : {self.kode}")
        print(f"Biaya Produksi  : Rp{self.biaya_produksi}")
        print(f"Harga Jual      : Rp{self.harga_jual}")
        print("Bahan Baku:")
        table = [[bahan, jumlah] for bahan, jumlah in self.bahan_baku.items()]
        print(tabulate(table, headers=["Bahan", "Jumlah"], tablefmt="grid"))

    def kalkulasi_biaya_produksi(self, jumlah_pcs):
        return self.biaya_produksi * jumlah_pcs

    def kalkulasi_harga_jual(self, jumlah_pcs):
        return self.harga_jual * jumlah_pcs

    @abstractmethod
    def pengadonan(self):
        pass

    @abstractmethod
    def pemanggangan(self):
        pass

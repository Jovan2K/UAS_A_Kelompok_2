
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.factory import buat_produk
from repository.produk_repo import tambah_produk, tampilkan_semua_produk, pilih_produk
from services.estimasi_service import hitung_estimasi_profit
from services.produksi_service import simulasi_produksi

def tampilkan_menu():
    print("\n=== SISTEM INFORMASI PRODUKSI HANARI BAKERY ===")
    print("1. Tambah Produk Baru")
    print("2. Tampilkan Semua Produk")
    print("3. Kalkulasi Estimasi Profit")
    print("4. Simulasi Proses Produksi")
    print("5. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            produk_baru = buat_produk()
            if produk_baru:
                tambah_produk(produk_baru)

        elif pilihan == "2":
            tampilkan_semua_produk()

        elif pilihan == "3":
            produk = pilih_produk()
            if produk:
                try:
                    jumlah = int(input("Masukkan jumlah pcs: "))
                    hitung_estimasi_profit(produk, jumlah)
                except ValueError:
                    print("Jumlah harus angka!")

        elif pilihan == "4":
            produk = pilih_produk()
            if produk:
                simulasi_produksi(produk)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem Hanari Bakery.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()

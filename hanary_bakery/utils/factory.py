
from entities.croissant import Croissant
from entities.muffin import Muffin
from entities.roti_manis import RotiManis
from entities.kue_kering import KueKering
from entities.butter_cookies import ButterCookies

def buat_produk():
    try:
        print("\nPilih jenis produk:")
        print("1. Croissant")
        print("2. Muffin")
        print("3. Roti Manis")
        print("4. Kue Kering")
        print("5. Butter Cookies")

        pilihan = input("Masukkan pilihan (1-5): ").strip()

        class_map = {
            "1": Croissant,
            "2": Muffin,
            "3": RotiManis,
            "4": KueKering,
            "5": ButterCookies,
        }

        cls = class_map.get(pilihan)
        if not cls:
            print("Pilihan tidak valid.")
            return None

        nama = input("Nama produk: ").strip()
        kode = input("Kode produk: ").strip()

        bahan_baku = {}
        print("Masukkan bahan baku (ketik 'selesai' untuk berhenti):")
        while True:
            bahan = input("  - Nama bahan: ").strip()
            if bahan.lower() == "selesai":
                break
            try:
                jumlah = float(input(f"    Jumlah {bahan}: "))
                bahan_baku[bahan] = jumlah
            except ValueError:
                print("Jumlah harus berupa angka!")

        biaya = float(input("Biaya produksi per pcs (Rp): "))
        harga = float(input("Harga jual per pcs (Rp): "))

        return cls(nama, kode, bahan_baku, biaya, harga)

    except Exception as e:
        print(f"Terjadi kesalahan saat membuat produk: {e}")
        return None

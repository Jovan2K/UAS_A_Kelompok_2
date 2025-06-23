from entities.croissant import Croissant
from entities.muffin import Muffin
from entities.roti_manis import RotiManis
from entities.kue_kering import KueKering
from entities.butter_cookies import ButterCookies

def buat_produk():
    try:
        print("\nPilih jenis produk:")
        print("1. Roti Manis")
        print("2. Croissant")
        print("3. Roti Kering")

        pilihan = input("Masukkan pilihan (1-3): ").strip()

        if pilihan == "1":
            cls = RotiManis
        elif pilihan == "2":
            cls = Croissant
        elif pilihan == "3":
            print("\n-- Roti Kering --")
            print("1. Butter Cookies")
            print("2. Muffin")
            sub_pilihan = input("Pilih sub-jenis roti kering (1-2): ").strip()
            if sub_pilihan == "1":
                cls = ButterCookies
            elif sub_pilihan == "2":
                cls = Muffin
            else:
                print("Sub-pilihan tidak valid.")
                return None
        else:
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

        biaya = float(input("Biaya produksi (Rp): "))
        jumlah_produksi = int(input("Jumlah produksi: "))
        harga = float(input("Harga jual per pcs (Rp): "))

        return cls(nama, kode, bahan_baku, biaya, jumlah_produksi, harga)

    except Exception as e:
        print(f"Terjadi kesalahan saat membuat produk: {e}")
        return None

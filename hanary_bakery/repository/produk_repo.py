
produk_list = []

def tambah_produk(produk):
    produk_list.append(produk)
    print(f"\nProduk '{produk.nama}' berhasil ditambahkan!\n")

def tampilkan_semua_produk():
    if not produk_list:
        print("\nBelum ada produk yang tersedia.\n")
    else:
        print("\n[DAFTAR PRODUK]")
        for idx, p in enumerate(produk_list):
            print(f"\nProduk #{idx + 1}")
            p.tampilkan_data()

def pilih_produk():
    tampilkan_semua_produk()
    if not produk_list:
        return None
    try:
        index = int(input("\nPilih nomor produk: ")) - 1
        return produk_list[index]
    except (IndexError, ValueError):
        print("Pilihan tidak valid.")
        return None

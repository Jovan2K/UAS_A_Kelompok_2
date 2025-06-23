
from interfaces.pengembang import Pengembang
from interfaces.topping import Topping

def simulasi_produksi(produk):
    print("\n[SIMULASI PRODUKSI]")
    produk.pengadonan()

    if isinstance(produk, Pengembang):
        produk.pengembangan()

    produk.pemanggangan()

    if isinstance(produk, Topping):
        produk.tambah_topping()

    print("[PROSES SELESAI]\n")

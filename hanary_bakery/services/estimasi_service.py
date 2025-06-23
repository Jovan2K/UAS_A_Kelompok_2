
def hitung_estimasi_profit(produk, jumlah_pcs):
    biaya = produk.kalkulasi_biaya_produksi(jumlah_pcs)
    pendapatan = produk.kalkulasi_harga_jual(jumlah_pcs)
    profit = pendapatan - biaya

    print(f"\n[ESTIMASI PROFIT]")
    print(f"Jumlah: {jumlah_pcs} pcs")
    print(f"Biaya Produksi: Rp{biaya}")
    print(f"Harga Jual: Rp{pendapatan}")
    print(f"Estimasi Profit: Rp{profit}\n")

from entities.roti_manis import RotiManis
from entities.butter_cookies import ButterCookies
from entities.croissant import Croissant
from entities.kue_kering import KueKering
from entities.muffin import Muffin
from data import produk_list

#mockup masbro 
produk_list.append(
    RotiManis(
        nama="Roti Manis Coklat",
        kode="RM001",
        bahan_baku={"Tepung": "500g", "Gula": "100g", "Coklat": "150g", "Ragi": "5g"},
        biaya_produksi=3000,
        jumlah_produksi=100,
        harga_jual=5000
    )
)

produk_list.append(
    ButterCookies(
        nama="Butter Cookies Vanilla",
        kode="BC001",
        bahan_baku={"Tepung": "300g", "Butter": "200g", "Vanilla": "50g"},
        biaya_produksi=2500,
        jumlah_produksi=80,
        harga_jual=4000
    )
)

produk_list.append(
    Croissant(
        nama="Croissant Keju",
        kode="CR001",
        bahan_baku={"Tepung": "600", "Butter": "300", "Keju": "100"},
        biaya_produksi=4500,
        jumlah_produksi=60,
        harga_jual=7000
    )
)

produk_list.append(
    KueKering(
        nama="Kue Kering Kacang",
        kode="KK001",
        bahan_baku={"Tepung": "400", "Kacang": "200", "Gula": "100"},
        biaya_produksi=2000,
        jumlah_produksi=120,
        harga_jual=3500
    )
)

produk_list.append(
    Muffin(
        nama="Muffin Coklat",
        kode="MF001",
        bahan_baku={"Tepung": "350", "Coklat": "150", "Telur": "2"},
        biaya_produksi=3200,
        jumlah_produksi=90,
        harga_jual=5500
    )
)


from entities.roti_manis import RotiManis
from entities.butter_cookies import ButterCookies
from entities.croissant import Croissant
from entities.kue_kering import KueKering
from entities.muffin import Muffin
from data import produk_list

#mockup masbro 
produk_list.append(
    RotiManis(
        nama="Roti Manis Susu",
        kode="RM001",
        bahan_baku={
            "Tepung Cakra": "400 ",
            "Tepung Segitiga": "100 ",
            "Ragi Instan": "10 ",
            "Gula Pasir": "100 ",
            "Kuning Telur": "3 ",
            "Susu Cair": "250",
            "Mentega": "110 ",
            "Garam": "½"
        },
        biaya_produksi=2000,
        jumlah_produksi=20,
        harga_jual=4000
    )
)

produk_list.append(
    ButterCookies(
        nama="Croissant",
        kode="CR001",
        bahan_baku={
            "Tepung Terigu": "525 ",
            "Air": "250",
            "Susu Cair": "125",
            "Gula Pasir": "62 ",
            "Ragi Instan": "8 ",
            "Garam": "¼",
            "Mentega Tawar": "315 ",
            "Kuning Telur": "1 "
        },
        biaya_produksi=5000,
        jumlah_produksi=12,
        harga_jual=7000
    )
)

produk_list.append(
    Croissant(
        nama="Butter Cookies",
        kode="BC001",
        bahan_baku={
            "Mentega Tawar": "100 ",
            "Gula Halus": "55 ",
            "Kuning Telur": "20 ",
            "Vanilla Extract": "½",
            "Tepung Serbaguna": "125 ",
            "Garam": "¼",
            "Chocco Chips": "100 "
        },
        biaya_produksi=2200,
        jumlah_produksi=15,
        harga_jual=3500
    )
)

produk_list.append(
    Muffin(
        nama="Muffin",
        kode="MF001",
        bahan_baku={
            "Tepung Terigu": "250 ",
            "Gula Pasir": "150 ",
            "Garam": "½",
            "Baking Powder": "2",
            "Susu Cair": "150",
            "Telur Ayam": "2 ",
            "Margarin Cair": "150 ",
            "Vanili": "1"
        },
        biaya_produksi=2100,
        jumlah_produksi=15,
        harga_jual=3000
    )
)


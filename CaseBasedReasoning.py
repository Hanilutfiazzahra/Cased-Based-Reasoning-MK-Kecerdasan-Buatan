import pandas as pd

# Membaca data restoran dari file Excel
dataset_restoran = pd.read_excel("restoran.xlsx")

# Menampilkan beberapa data awal
print("DATA RESTORAN")
print(dataset_restoran.head())


## Fungsi keanggotaan fuzzy untuk variabel pelayanan dan harga
# Servis rendah
def servis_rendah(nilai):

    if nilai <= 40:
        return 1

    elif 40 < nilai < 60:
        return (60 - nilai) / 20

    else:
        return 0

#Servis cukup
def servis_cukup(nilai):

    if 40 < nilai < 60:
        return (nilai - 40) / 20

    elif 60 <= nilai < 80:
        return (80 - nilai) / 20

    else:
        return 0

# Servis memuaskan
def servis_memuaskan(nilai):

    if nilai <= 60:
        return 0

    elif 60 < nilai < 80:
        return (nilai - 60) / 20

    elif 80 <= nilai <= 100:
        return (nilai - 80) / 20

    else:
        return 1


#F Fungsi keanggotaan fuzzy untuk variabel harga
# Harga ekonomis
def harga_ekonomis(nilai):

    if nilai <= 20000:
        return 1

    elif 20000 < nilai < 30000:
        return (30000 - nilai) / 10000

    else:
        return 0

# Harga standar
def harga_standar(nilai):

    if 25000 < nilai < 40000:
        return (nilai - 25000) / 15000

    elif 40000 <= nilai < 55000:
        return (55000 - nilai) / 15000

    else:
        return 0

# Harga premium
def harga_premium(nilai):

    if nilai <= 40000:
        return 0

    elif 40000 < nilai < 55000:
        return (nilai - 40000) / 15000

    else:
        return 1

# Menyimpan seluruh hasil perhitungan fuzzy
daftar_hasil = []


# Looping data restoran 
for nomor, data in dataset_restoran.iterrows():

    kode_restoran = data['id Pelanggan']

    nilai_servis = data['Pelayanan']

    nilai_harga = data['harga']

    # Fuzzification servis
    servis_low = servis_rendah(nilai_servis)

    servis_mid = servis_cukup(nilai_servis)

    servis_high = servis_memuaskan(nilai_servis)

    # Fuzzification harga
    harga_low = harga_ekonomis(nilai_harga)

    harga_mid = harga_standar(nilai_harga)

    harga_high = harga_premium(nilai_harga)

    # Inferensi
    rule_fuzzy = []

    rule_fuzzy.append((min(servis_low, harga_low), 60))

    rule_fuzzy.append((min(servis_low, harga_mid), 30))

    rule_fuzzy.append((min(servis_low, harga_high), 20))

    rule_fuzzy.append((min(servis_mid, harga_low), 70))

    rule_fuzzy.append((min(servis_mid, harga_mid), 60))

    rule_fuzzy.append((min(servis_mid, harga_high), 30))

    rule_fuzzy.append((min(servis_high, harga_low), 90))

    rule_fuzzy.append((min(servis_high, harga_mid), 70))

    rule_fuzzy.append((min(servis_high, harga_high), 50))

    # Deffuzifikasi m
    total_atas = 0

    total_bawah = 0

    for alpha, output in rule_fuzzy:

        total_atas += alpha * output

        total_bawah += alpha

    if total_bawah == 0:
        skor_akhir = 0

    else:
        skor_akhir = total_atas / total_bawah

    # Menyimpan hasil

    daftar_hasil.append([

        kode_restoran,

        nilai_servis,

        nilai_harga,

        round(skor_akhir, 2)
    ])


tabel_hasil = pd.DataFrame(

    daftar_hasil,

    columns=[
        'ID Restoran',
        'Pelayanan',
        'Harga',
        'Skor Fuzzy'
    ]
)

tabel_hasil = tabel_hasil.sort_values(

    by='Skor Fuzzy',
    ascending=False
)

# Mengambil 5 restoran terbaik
rekomendasi_restoran = tabel_hasil.head(5)

print("\n5 RESTORAN TERBAIK")
print(rekomendasi_restoran)

rekomendasi_restoran.to_excel(

    "peringkat.xlsx",
    index=False
)

print("\nFile peringkat.xlsx berhasil dibuat")
# Tugas 6 Studi Kasus dengan Python

| | |
|---|---|
| **Nama** | Abdul Vaiz Vahry Iskandar |
| **NPM** | G1A025063 |
| **Program Studi** | Teknik Informatika |
| **Universitas** | Universitas Bengkulu |

Repositori ini berisi 6 studi kasus. Setiap studi kasus ada di folder sendiri dan hanya terdiri dari **1 file Python** (`main.py`). Semua program hanya memakai library bawaan Python, jadi **tidak perlu install apa pun**.

## Struktur Folder

```
stdui/
├── README.md
├── 01_data_analytics_ai/main.py
├── 02_hpc_infrastructure/main.py
├── 03_gis_career/main.py
├── 04_machine_learning/main.py
├── 05_hci_data_visualization/main.py
└── 06_deforestation_satellite_ai/main.py
```

## Cara Menjalankan

Pastikan Python 3.8 atau lebih baru sudah terpasang, lalu jalankan dari folder utama:

```bash
python 01_data_analytics_ai/main.py
python 02_hpc_infrastructure/main.py
python 03_gis_career/main.py
python 04_machine_learning/main.py
python 05_hci_data_visualization/main.py
python 06_deforestation_satellite_ai/main.py
```

---

## 1. Make Sense of Data with Analytics and AI

**Folder:** `01_data_analytics_ai`

**Kasus:** Menganalisis data penjualan 6 bulan sebuah UMKM kopi di Bengkulu.

**Yang dilakukan program:**
1. Menghitung statistik deskriptif (total, rata-rata, median, standar deviasi).
2. Mencari insight: produk terlaris, persentase pertumbuhan, dan bulan terbaik.
3. Memprediksi penjualan bulan berikutnya dengan **regresi linear** sebagai bentuk AI sederhana.
4. Memberi rekomendasi otomatis (tambah stok, promosi, atau pertahankan strategi).

**Konsep:** analisis data, statistik, regresi linear, pengambilan keputusan berbasis data.

---

## 2. Bridging Global Infrastructure to Address Local Challenges in HPC

**Folder:** `02_hpc_infrastructure`

**Kasus:** Simulasi Monte Carlo untuk memperkirakan risiko banjir di 6 kecamatan Kota Bengkulu, berdasarkan curah hujan dan kapasitas drainase.

**Yang dilakukan program:**
1. Menjalankan 3 juta simulasi curah hujan acak per wilayah.
2. Menghitung peluang banjir dan memberi status TINGGI / SEDANG / RENDAH.
3. Membandingkan waktu komputasi **serial** (1 core) dengan **paralel** (`multiprocessing`, banyak core).
4. Menampilkan **speedup**, yaitu seberapa cepat komputasi paralel dibanding serial.

**Konsep:** komputasi paralel, Monte Carlo, speedup. Ini konsep dasar HPC yang dipakai untuk menyelesaikan masalah lokal seperti banjir.

---

## 3. Career and Competition in Industrial Era with GIS

**Folder:** `03_gis_career`

**Kasus:** Mencari lowongan kerja bidang GIS yang paling dekat dari Universitas Bengkulu.

**Yang dilakukan program:**
1. Menyimpan data lowongan beserta koordinat lokasinya (latitude, longitude).
2. Menghitung jarak sebenarnya di permukaan bumi dengan **rumus Haversine**.
3. Menentukan arah mata angin dari kampus ke lokasi kerja.
4. Menyaring lowongan dalam radius 10 km.
5. Memberi rekomendasi lowongan terbaik berdasarkan gaji dan jarak, lengkap dengan link Google Maps.

**Konsep:** data spasial, koordinat geografis, perhitungan jarak, analisis lokasi.

> Catatan: nama perusahaan dan koordinat lowongan adalah data contoh (fiktif).

---

## 4. Introduction to Machine Learning

**Folder:** `04_machine_learning`

**Kasus:** Memprediksi apakah mahasiswa akan lulus **tepat waktu** atau **terlambat** berdasarkan IPK, persentase kehadiran, dan jam belajar per minggu.

**Yang dilakukan program:**
1. Membagi data menjadi data latih (70%) dan data uji (30%).
2. Melakukan normalisasi data (min-max scaling).
3. Membuat algoritma **K-Nearest Neighbors (KNN)** dari nol tanpa library.
4. Menguji akurasi model dengan nilai K = 1, 3, dan 5.
5. Memprediksi kelulusan untuk data mahasiswa baru.

**Konsep:** supervised learning, klasifikasi, jarak Euclidean, train/test split, akurasi.

---

## 5. Human-Computer Interaction & Data Visualization

**Folder:** `05_hci_data_visualization`

**Kasus:** Aplikasi dashboard nilai mahasiswa berbasis menu interaktif di terminal.

**Fitur:**
- `[1]` Tabel nilai beserta huruf mutu dan rata-rata
- `[2]` Grafik batang horizontal, nilai di bawah 65 diberi tanda "perlu perbaikan"
- `[3]` Distribusi huruf mutu (A sampai E)
- `[4]` Tambah atau ubah nilai
- `[5]` Hapus nilai, dengan konfirmasi sebelum menghapus
- `[0]` Keluar

**Prinsip HCI yang diterapkan:**
- **Menu yang jelas dan konsisten**, sehingga pengguna tahu apa saja yang bisa dilakukan.
- **Umpan balik (feedback)** dengan pesan `[OK]` saat berhasil dan `[!]` saat terjadi kesalahan.
- **Validasi input**, sehingga nilai harus berupa angka 0 sampai 100 dan nama tidak boleh kosong.
- **Pencegahan kesalahan**, dengan konfirmasi `y/n` sebelum data dihapus.

**Konsep:** desain interaksi, usability, visualisasi data.

---

## 6. Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

**Folder:** `06_deforestation_satellite_ai`

**Kasus:** Mendeteksi hutan yang hilang dari citra satelit, lalu menebak penyebabnya.

**Yang dilakukan program:**
1. Membuat simulasi citra satelit 20x20 piksel (1 piksel = 30 m x 30 m, seperti Landsat) untuk waktu **sebelum** dan **sesudah**.
2. Menghitung indeks vegetasi **NDVI = (NIR - Red) / (NIR + Red)**.
3. Menandai piksel sebagai *alert* jika NDVI turun lebih dari 0.3.
4. Menggabungkan piksel alert yang bersebelahan menjadi satu area dengan algoritma **flood fill**.
5. Mengekstrak fitur tiap area: luas (ha), kerapatan bentuk, rasio panjang/lebar, dan NDVI.
6. Mengklasifikasikan penyebab deforestasi dengan **AI berbasis aturan (rule-based)**:

| Penyebab | Ciri-ciri |
|---|---|
| Pembangunan Jalan | Area memanjang seperti garis |
| Kebakaran Hutan | NDVI sangat rendah (lahan gosong) |
| Perkebunan/Pertanian | Area luas dan berbentuk kotak teratur |
| Pembalakan Liar | Petak kecil di tengah hutan |

**Konsep:** penginderaan jauh (remote sensing), NDVI, deteksi perubahan, ekstraksi fitur, klasifikasi.

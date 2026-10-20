"""
Studi Kasus 1: Make Sense of Data with Analytics and AI
Kasus: Analisis data penjualan UMKM kopi di Bengkulu dan prediksi penjualan bulan berikutnya.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

import statistics

# Data penjualan (dalam jumlah cup) selama 6 bulan
penjualan = {
    "Kopi Robusta": [120, 135, 150, 160, 172, 185],
    "Kopi Susu":    [200, 210, 205, 230, 245, 260],
    "Teh Tarik":    [90, 85, 95, 88, 92, 90],
    "Coklat":       [60, 70, 65, 80, 85, 95],
}
bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"]


def regresi_linear(y):
    """Mencari garis y = a + b*x dengan metode kuadrat terkecil."""
    x = list(range(1, len(y) + 1))
    rata_x = statistics.mean(x)
    rata_y = statistics.mean(y)
    b = sum((xi - rata_x) * (yi - rata_y) for xi, yi in zip(x, y)) / sum((xi - rata_x) ** 2 for xi in x)
    a = rata_y - b * rata_x
    return a, b


print("=" * 60)
print("ANALISIS DATA PENJUALAN UMKM KOPI BENGKULU")
print("=" * 60)

# 1. Statistik deskriptif
print("\n[1] Statistik Deskriptif")
print(f"{'Produk':<14}{'Total':>7}{'Rata2':>8}{'Median':>8}{'Std':>7}")
for produk, data in penjualan.items():
    print(f"{produk:<14}{sum(data):>7}{statistics.mean(data):>8.1f}"
          f"{statistics.median(data):>8.1f}{statistics.stdev(data):>7.1f}")

# 2. Insight: produk terlaris dan pertumbuhan
print("\n[2] Insight")
terlaris = max(penjualan, key=lambda p: sum(penjualan[p]))
print(f"- Produk terlaris : {terlaris}")
for produk, data in penjualan.items():
    growth = (data[-1] - data[0]) / data[0] * 100
    print(f"- Pertumbuhan {produk:<13}: {growth:6.1f}% (Jan -> Jun)")

total_bulanan = [sum(p[i] for p in penjualan.values()) for i in range(len(bulan))]
bulan_terbaik = bulan[total_bulanan.index(max(total_bulanan))]
print(f"- Bulan dengan penjualan tertinggi: {bulan_terbaik} ({max(total_bulanan)} cup)")

# 3. AI sederhana: prediksi bulan Juli dengan regresi linear
print("\n[3] Prediksi Penjualan Bulan Juli (Regresi Linear)")
for produk, data in penjualan.items():
    a, b = regresi_linear(data)
    prediksi = a + b * (len(data) + 1)
    tren = "naik" if b > 1 else "turun" if b < -1 else "stabil"
    print(f"- {produk:<13}: {prediksi:6.0f} cup (tren {tren}, {b:+.1f}/bulan)")

# 4. Rekomendasi otomatis berdasarkan data
print("\n[4] Rekomendasi")
for produk, data in penjualan.items():
    _, b = regresi_linear(data)
    if b > 5:
        print(f"- {produk}: tambah stok bahan baku, permintaan terus naik.")
    elif b < 1:
        print(f"- {produk}: perlu promosi agar penjualan meningkat.")
    else:
        print(f"- {produk}: pertahankan strategi saat ini.")

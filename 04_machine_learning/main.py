"""
Studi Kasus 4: Introduction to Machine Learning
Kasus: Memprediksi mahasiswa lulus tepat waktu atau tidak
       menggunakan algoritma K-Nearest Neighbors (KNN) dari nol.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

import math
import random

# Data contoh: [IPK, persentase kehadiran, jam belajar per minggu], label
DATA = [
    ([3.8, 95, 20], "Tepat"), ([3.5, 90, 15], "Tepat"), ([3.2, 85, 12], "Tepat"),
    ([3.6, 92, 18], "Tepat"), ([3.0, 80, 10], "Tepat"), ([3.9, 98, 25], "Tepat"),
    ([3.4, 88, 14], "Tepat"), ([3.1, 82, 11], "Tepat"), ([3.7, 94, 16], "Tepat"),
    ([2.5, 60, 5], "Terlambat"), ([2.8, 70, 6], "Terlambat"), ([2.2, 55, 3], "Terlambat"),
    ([2.9, 72, 8], "Terlambat"), ([2.4, 65, 4], "Terlambat"), ([2.7, 68, 7], "Terlambat"),
    ([2.0, 50, 2], "Terlambat"), ([2.6, 75, 6], "Terlambat"), ([3.0, 65, 5], "Terlambat"),
]


def normalisasi(data):
    """Min-max scaling agar semua fitur bernilai 0-1."""
    kolom = list(zip(*[x for x, _ in data]))
    batas = [(min(k), max(k)) for k in kolom]
    return batas


def skala(x, batas):
    return [(v - lo) / (hi - lo) for v, (lo, hi) in zip(x, batas)]


def jarak_euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_prediksi(data_latih, x, batas, k=3):
    x = skala(x, batas)
    tetangga = sorted(data_latih, key=lambda d: jarak_euclidean(skala(d[0], batas), x))[:k]
    label = [lbl for _, lbl in tetangga]
    return max(set(label), key=label.count)


print("=" * 60)
print("PREDIKSI KELULUSAN MAHASISWA DENGAN KNN")
print("=" * 60)

# 1. Bagi data latih (70%) dan data uji (30%)
random.seed(42)
data = DATA[:]
random.shuffle(data)
batas_bagi = int(len(data) * 0.7)
latih, uji = data[:batas_bagi], data[batas_bagi:]
batas = normalisasi(latih)
print(f"Data latih: {len(latih)} | Data uji: {len(uji)}\n")

# 2. Evaluasi model dengan beberapa nilai K
for k in [1, 3, 5]:
    benar = sum(knn_prediksi(latih, x, batas, k) == y for x, y in uji)
    print(f"K = {k} -> Akurasi: {benar / len(uji) * 100:.1f}%")

# 3. Detail prediksi data uji (K=3)
print("\nDetail prediksi (K=3):")
print(f"{'IPK':>5}{'Hadir':>7}{'Jam':>5}  {'Aktual':<10}{'Prediksi':<10}")
for x, y in uji:
    p = knn_prediksi(latih, x, batas, 3)
    print(f"{x[0]:>5}{x[1]:>6}%{x[2]:>5}  {y:<10}{p:<10}{'OK' if p == y else 'SALAH'}")

# 4. Prediksi data mahasiswa baru
print("\nPrediksi mahasiswa baru:")
mahasiswa_baru = [[3.3, 87, 13], [2.6, 62, 4], [3.0, 78, 9]]
for m in mahasiswa_baru:
    print(f"- IPK {m[0]}, hadir {m[1]}%, belajar {m[2]} jam/minggu -> {knn_prediksi(DATA, m, normalisasi(DATA), 3)}")

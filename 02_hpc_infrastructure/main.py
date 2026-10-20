"""
Studi Kasus 2: Bridging Global Infrastructure to Address Local Challenges in HPC
Kasus: Simulasi Monte Carlo risiko banjir di kecamatan Kota Bengkulu.
       Dibandingkan cara serial (1 core) dengan paralel (banyak core),
       seperti konsep High Performance Computing.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

import multiprocessing as mp
import random
import time

# Data contoh: rata-rata curah hujan harian (mm) dan kapasitas drainase (mm)
WILAYAH = {
    "Gading Cempaka": (45, 70),
    "Ratu Agung":     (50, 65),
    "Teluk Segara":   (55, 60),
    "Selebar":        (40, 75),
    "Muara Bangkahulu": (52, 62),
    "Sungai Serut":   (58, 58),
}
JUMLAH_SIMULASI = 3_000_000


def simulasi_banjir(args):
    """Menghitung peluang banjir: berapa kali hujan acak melebihi kapasitas drainase."""
    nama, rata_hujan, kapasitas, n, seed = args
    rng = random.Random(seed)
    banjir = 0
    for _ in range(n):
        hujan = rng.expovariate(1 / rata_hujan)  # curah hujan acak
        if hujan > kapasitas:
            banjir += 1
    return nama, banjir / n * 100


def buat_tugas():
    return [(nama, h, k, JUMLAH_SIMULASI, i) for i, (nama, (h, k)) in enumerate(WILAYAH.items())]


if __name__ == "__main__":
    print("=" * 60)
    print("SIMULASI RISIKO BANJIR KOTA BENGKULU (SERIAL vs PARALEL)")
    print("=" * 60)
    print(f"Jumlah core CPU tersedia : {mp.cpu_count()}")
    print(f"Simulasi per wilayah     : {JUMLAH_SIMULASI:,}\n")

    # 1. Serial: dikerjakan satu per satu
    mulai = time.perf_counter()
    hasil_serial = [simulasi_banjir(t) for t in buat_tugas()]
    waktu_serial = time.perf_counter() - mulai

    # 2. Paralel: dibagi ke beberapa core sekaligus
    mulai = time.perf_counter()
    with mp.Pool() as pool:
        hasil_paralel = pool.map(simulasi_banjir, buat_tugas())
    waktu_paralel = time.perf_counter() - mulai

    print(f"{'Wilayah':<18}{'Peluang Banjir':>15}  Status")
    for nama, peluang in sorted(hasil_paralel, key=lambda x: -x[1]):
        status = "TINGGI" if peluang > 30 else "SEDANG" if peluang > 20 else "RENDAH"
        print(f"{nama:<18}{peluang:>14.2f}%  {status}")

    print("\nPerbandingan Waktu Komputasi")
    print(f"- Serial  : {waktu_serial:.2f} detik")
    print(f"- Paralel : {waktu_paralel:.2f} detik")
    print(f"- Speedup : {waktu_serial / waktu_paralel:.2f}x lebih cepat")
    print(f"- Hasil serial dan paralel sama: {hasil_serial == hasil_paralel}")

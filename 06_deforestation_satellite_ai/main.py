"""
Studi Kasus 6: Attributing Direct Drivers to Deforestation Alerts
               with Satellite Imagery and AI
Kasus: Mendeteksi area hutan yang hilang dari citra satelit (simulasi)
       menggunakan NDVI, lalu menebak penyebabnya (driver) dengan
       klasifikasi berbasis aturan.

NDVI = (NIR - Red) / (NIR + Red)
Nilai NDVI tinggi (> 0.6) = vegetasi lebat, rendah (< 0.3) = lahan terbuka.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

import random

random.seed(7)
UKURAN = 20  # citra 20 x 20 piksel (1 piksel = 30 m x 30 m, seperti Landsat)


def ndvi(nir, red):
    return (nir - red) / (nir + red)


def citra_hutan():
    """Citra awal: seluruh area adalah hutan lebat (NIR tinggi, Red rendah)."""
    return [[(random.uniform(0.45, 0.55), random.uniform(0.04, 0.08)) for _ in range(UKURAN)]
            for _ in range(UKURAN)]


def ubah_area(citra, baris, kolom, nir, red):
    for r in baris:
        for c in kolom:
            citra[r][c] = (nir + random.uniform(-0.02, 0.02), red + random.uniform(-0.01, 0.01))


# 1. Buat citra sebelum dan sesudah
sebelum = citra_hutan()
sesudah = [baris[:] for baris in sebelum]
ubah_area(sesudah, range(2, 9), range(2, 10), 0.25, 0.12)      # kotak besar & rapi -> perkebunan
ubah_area(sesudah, range(12, 18), range(13, 19), 0.12, 0.10)   # area gosong -> kebakaran
ubah_area(sesudah, [15], range(1, 7), 0.25, 0.15)              # garis panjang -> jalan
ubah_area(sesudah, range(11, 13), range(9, 11), 0.22, 0.12)    # petak kecil -> pembalakan

# 2. Hitung perubahan NDVI dan tandai piksel alert
AMBANG = 0.3
alert = [[ndvi(*sebelum[r][c]) - ndvi(*sesudah[r][c]) > AMBANG for c in range(UKURAN)]
         for r in range(UKURAN)]


def kelompokkan(alert):
    """Menggabungkan piksel alert yang bersebelahan menjadi satu area (flood fill)."""
    dikunjungi, area = set(), []
    for r in range(UKURAN):
        for c in range(UKURAN):
            if alert[r][c] and (r, c) not in dikunjungi:
                tumpukan, piksel = [(r, c)], []
                dikunjungi.add((r, c))
                while tumpukan:
                    y, x = tumpukan.pop()
                    piksel.append((y, x))
                    for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                        if 0 <= ny < UKURAN and 0 <= nx < UKURAN and alert[ny][nx] and (ny, nx) not in dikunjungi:
                            dikunjungi.add((ny, nx))
                            tumpukan.append((ny, nx))
                area.append(piksel)
    return area


def ekstrak_fitur(piksel):
    ys, xs = [p[0] for p in piksel], [p[1] for p in piksel]
    tinggi, lebar = max(ys) - min(ys) + 1, max(xs) - min(xs) + 1
    return {
        "luas_ha": len(piksel) * 0.09,                          # 30 m x 30 m = 0.09 ha
        "kerapatan": len(piksel) / (tinggi * lebar),           # 1.0 = bentuk kotak rapi
        "rasio": max(tinggi, lebar) / min(tinggi, lebar),      # tinggi = memanjang
        "ndvi": sum(ndvi(*sesudah[y][x]) for y, x in piksel) / len(piksel),
        "pusat": (sum(ys) // len(ys), sum(xs) // len(xs)),
    }


def tebak_driver(f):
    """Klasifikasi penyebab deforestasi berbasis aturan (rule-based AI)."""
    if f["rasio"] >= 4:
        return "Pembangunan Jalan", "area memanjang seperti garis"
    if f["ndvi"] < 0.15:
        return "Kebakaran Hutan", "NDVI sangat rendah (lahan gosong)"
    if f["luas_ha"] >= 3 and f["kerapatan"] > 0.9:
        return "Perkebunan/Pertanian", "area luas berbentuk kotak teratur"
    return "Pembalakan Liar", "petak kecil di tengah hutan"


# 3. Tampilkan peta alert
print("=" * 64)
print("DETEKSI & ATRIBUSI PENYEBAB DEFORESTASI DARI CITRA SATELIT")
print("=" * 64)
print("Peta perubahan (. = hutan, X = alert deforestasi):\n")
for baris in alert:
    print("   " + " ".join("X" if a else "." for a in baris))

# 4. Analisis tiap area alert
area_alert = kelompokkan(alert)
print(f"\nDitemukan {len(area_alert)} area alert:\n")
print(f"{'No':<4}{'Lokasi':<10}{'Luas':>8}{'NDVI':>7}  {'Penyebab':<22}Alasan")
total = 0
for i, piksel in enumerate(area_alert, 1):
    f = ekstrak_fitur(piksel)
    driver, alasan = tebak_driver(f)
    total += f["luas_ha"]
    print(f"{i:<4}{str(f['pusat']):<10}{f['luas_ha']:>5.2f} ha{f['ndvi']:>7.2f}  {driver:<22}{alasan}")

print(f"\nTotal hutan hilang: {total:.2f} ha dari {UKURAN * UKURAN * 0.09:.0f} ha area pantauan")

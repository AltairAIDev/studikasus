"""
Studi Kasus 3: Career and Competition in Industrial Era with GIS
Kasus: Mencari lowongan kerja terdekat dari Universitas Bengkulu
       menggunakan koordinat (latitude, longitude) dan rumus Haversine.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

import math

# Titik awal: Universitas Bengkulu (perkiraan koordinat)
ASAL = ("Universitas Bengkulu", -3.7590, 102.2730)

# Data contoh lowongan kerja (nama perusahaan fiktif)
LOWONGAN = [
    {"perusahaan": "PT Data Nusantara",   "posisi": "GIS Analyst",       "lat": -3.7928, "lon": 102.2608, "gaji": 6_000_000},
    {"perusahaan": "CV Peta Raflesia",    "posisi": "Surveyor Pemetaan", "lat": -3.8004, "lon": 102.2655, "gaji": 4_500_000},
    {"perusahaan": "PT Sawit Hijau",      "posisi": "Remote Sensing",    "lat": -3.4520, "lon": 102.5430, "gaji": 7_000_000},
    {"perusahaan": "Dinas Tata Ruang",    "posisi": "Staf Data Spasial", "lat": -3.7955, "lon": 102.2520, "gaji": 5_000_000},
    {"perusahaan": "PT Tambang Bengkulu", "posisi": "Drone Mapper",      "lat": -3.9000, "lon": 102.3500, "gaji": 6_500_000},
    {"perusahaan": "Startup GeoTech",     "posisi": "Web GIS Developer", "lat": -3.7700, "lon": 102.2800, "gaji": 8_000_000},
]


def haversine(lat1, lon1, lat2, lon2):
    """Menghitung jarak dua titik di permukaan bumi (km)."""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(a))


def arah_mata_angin(lat1, lon1, lat2, lon2):
    sudut = math.degrees(math.atan2(lon2 - lon1, lat2 - lat1)) % 360
    arah = ["Utara", "Timur Laut", "Timur", "Tenggara", "Selatan", "Barat Daya", "Barat", "Barat Laut"]
    return arah[round(sudut / 45) % 8]


print("=" * 70)
print("PEMETAAN LOWONGAN KERJA BIDANG GIS DI SEKITAR BENGKULU")
print("=" * 70)
print(f"Titik asal: {ASAL[0]} ({ASAL[1]}, {ASAL[2]})\n")

# Hitung jarak dan skor tiap lowongan
for l in LOWONGAN:
    l["jarak"] = haversine(ASAL[1], ASAL[2], l["lat"], l["lon"])
    l["arah"] = arah_mata_angin(ASAL[1], ASAL[2], l["lat"], l["lon"])
    # Skor: gaji makin tinggi makin baik, jarak makin jauh makin buruk
    l["skor"] = l["gaji"] / 1_000_000 - l["jarak"] * 0.1

print(f"{'Perusahaan':<21}{'Posisi':<19}{'Jarak':>9}  {'Arah':<11}{'Gaji':>12}")
for l in sorted(LOWONGAN, key=lambda x: x["jarak"]):
    print(f"{l['perusahaan']:<21}{l['posisi']:<19}{l['jarak']:>6.2f} km  {l['arah']:<11}Rp{l['gaji']:>10,}")

# Filter lowongan dalam radius tertentu
RADIUS = 10
print(f"\nLowongan dalam radius {RADIUS} km:")
for l in LOWONGAN:
    if l["jarak"] <= RADIUS:
        print(f"- {l['perusahaan']} ({l['posisi']})")

terbaik = max(LOWONGAN, key=lambda x: x["skor"])
print(f"\nRekomendasi terbaik (gaji vs jarak): {terbaik['posisi']} di {terbaik['perusahaan']}")
print(f"Lihat di peta: https://www.google.com/maps?q={terbaik['lat']},{terbaik['lon']}")

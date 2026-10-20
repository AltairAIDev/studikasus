"""
Studi Kasus 5: Human-Computer Interaction & Data Visualization
Kasus: Aplikasi menu interaktif di terminal untuk mengelola dan
       memvisualisasikan nilai mahasiswa dalam bentuk grafik batang.
       Prinsip HCI yang diterapkan: menu jelas, umpan balik, validasi input,
       dan pencegahan kesalahan.

Nama : Abdul Vaiz Vahry Iskandar
NPM  : G1A025063
"""

nilai = {
    "Algoritma": 85,
    "Basis Data": 78,
    "Jaringan": 65,
    "Kalkulus": 55,
    "Pemrograman Web": 92,
}


def huruf_mutu(n):
    if n >= 85: return "A"
    if n >= 75: return "B"
    if n >= 65: return "C"
    if n >= 50: return "D"
    return "E"


def tampilkan_tabel():
    print(f"\n{'No':<4}{'Mata Kuliah':<18}{'Nilai':>6}{'Mutu':>6}")
    print("-" * 34)
    for i, (mk, n) in enumerate(nilai.items(), 1):
        print(f"{i:<4}{mk:<18}{n:>6}{huruf_mutu(n):>6}")
    if nilai:
        print("-" * 34)
        print(f"{'Rata-rata':<22}{sum(nilai.values()) / len(nilai):>6.1f}")


def grafik_batang():
    """Visualisasi horizontal bar chart dengan karakter teks."""
    print("\nGrafik Nilai Mahasiswa (skala 0-100, 1 '#' = 2 poin)")
    for mk, n in sorted(nilai.items(), key=lambda x: -x[1]):
        bar = "#" * (n // 2)
        tanda = "  <- perlu perbaikan" if n < 65 else ""
        print(f"{mk:<16}|{bar:<50}| {n}{tanda}")


def distribusi_mutu():
    print("\nDistribusi Huruf Mutu")
    for h in "ABCDE":
        jumlah = sum(1 for n in nilai.values() if huruf_mutu(n) == h)
        print(f"{h} | {'*' * jumlah} ({jumlah})")


def tambah_nilai():
    mk = input("Nama mata kuliah : ").strip()
    if not mk:
        print("[!] Nama mata kuliah tidak boleh kosong.")
        return
    try:
        n = int(input("Nilai (0-100)    : "))
    except ValueError:
        print("[!] Nilai harus berupa angka.")
        return
    if not 0 <= n <= 100:
        print("[!] Nilai harus di antara 0 dan 100.")
        return
    nilai[mk] = n
    print(f"[OK] {mk} dengan nilai {n} berhasil disimpan.")


def hapus_nilai():
    mk = input("Mata kuliah yang dihapus: ").strip()
    if mk not in nilai:
        print("[!] Mata kuliah tidak ditemukan.")
        return
    if input(f"Yakin hapus '{mk}'? (y/n): ").lower() == "y":
        del nilai[mk]
        print("[OK] Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


MENU = {
    "1": ("Lihat tabel nilai", tampilkan_tabel),
    "2": ("Lihat grafik batang", grafik_batang),
    "3": ("Lihat distribusi huruf mutu", distribusi_mutu),
    "4": ("Tambah / ubah nilai", tambah_nilai),
    "5": ("Hapus nilai", hapus_nilai),
}

while True:
    print("\n" + "=" * 40)
    print("  DASHBOARD NILAI MAHASISWA")
    print("=" * 40)
    for kode, (judul, _) in MENU.items():
        print(f"  [{kode}] {judul}")
    print("  [0] Keluar")
    pilihan = input("Pilih menu: ").strip()

    if pilihan == "0":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    elif pilihan in MENU:
        MENU[pilihan][1]()
    else:
        print("[!] Pilihan tidak valid, masukkan angka 0-5.")

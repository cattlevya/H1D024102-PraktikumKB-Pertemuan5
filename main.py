# Sistem Pakar Diagnosa Penyakit THT

# 1. Knowledge Base — Database Penyakit & Gejala
# Struktur: "Nama Penyakit": {"gejala": [...], "solusi": "..."}
database_penyakit = {
    "Tonsilitis": {
        "gejala": ["G37", "G12", "G5", "G27", "G6", "G21"],
        "solusi": "Gunakan pereda nyeri (seperti ibuprofen), istirahat cukup, dan konsultasi ke dokter THT jika berlanjut untuk pertimbangan antibiotik."
    },
    "Sinusitis Maksilaris": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
        "solusi": "Irigasi hidung dengan larutan saline, kompres hangat di area pipi, dan minum banyak air putih. Segera temui dokter."
    },
    "Sinusitis Frontalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
        "solusi": "Irigasi hidung, perbanyak istirahat untuk memulihkan sistem imun, dan konsultasikan dengan dokter THT."
    },
    "Sinusitis Edmoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
        "solusi": "Gunakan pelega pernapasan atau obat semprot hidung (maks 3 hari). Konsultasikan selalu dengan dokter."
    },
    "Sinusitis Sfenoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
        "solusi": "Segera periksakan ke dokter THT karena lokasi infeksi yang lebih dalam di belakang rongga hidung berisiko tinggi."
    },
    "Abses Peritonsiler": {
        "gejala": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
        "solusi": "Kondisi darurat THT! Segera kunjungi IGD atau dokter THT untuk prosedur drainase nanah dan antibiotik dosis tinggi."
    },
    "Faringitis": {
        "gejala": ["G37", "G5", "G6", "G7", "G15"],
        "solusi": "Banyak minum air hangat, kumur air garam, hindari makanan pedas dan rokok."
    },
    "Kanker Laring": {
        "gejala": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
        "solusi": "Peringatan serius. Harus segera berkonsultasi ke spesialis onkologi THT untuk deteksi klinis berupa biopsi."
    },
    "Deviasi Septum": {
        "gejala": ["G37", "G17", "G20", "G8", "G18", "G25"],
        "solusi": "Jika keluhan mengganggu (sering infeksi/sesak nafas), pertimbangkan tindakan operatif (septoplasti) oleh dokter bedah THT."
    },
    "Laringitis": {
        "gejala": ["G37", "G5", "G15", "G16", "G32"],
        "solusi": "Istirahatkan suara total (vocal rest), hidrasi yang baik, dan hindari paparan asap rokok atau debu."
    },
    "Kanker Leher & Kepala": {
        "gejala": ["G5", "G22", "G8", "G28", "G3", "G11"],
        "solusi": "Kasus ini harus segera dirujuk ke Rumah Sakit besar yang memiliki Departemen Bedah Onkologi dan THT."
    },
    "Otitis Media Akut": {
        "gejala": ["G37", "G20", "G35", "G31"],
        "solusi": "Jangan memasang air atau cotton bud ke telinga dalam. Segera minta antibiotik tetes telinga dengan resep dokter."
    },
    "Contact Ulcers": {
        "gejala": ["G5", "G2"],
        "solusi": "Sering disebabkan oleh asam lambung naik atau trauma suara. Hindari berdehem keras dan evaluasi gaya hidup sehat."
    },
    "Abses Parafaringeal": {
        "gejala": ["G5", "G16"],
        "solusi": "Sangat berbahaya jika menyumbat saluran nafas. Segera datang ke UGD terdekat untuk membebaskan jalur nafas dan operasi drainase."
    },
    "Barotitis Media": {
        "gejala": ["G12", "G20"],
        "solusi": "Lakukan manuver valsava ringan saat perubahan tekanan udara. Jika gendang telinga nyeri persisten, periksakan THT."
    },
    "Kanker Nafasoring": {
        "gejala": ["G17", "G8"],
        "solusi": "Ada kemungkinan nama aslinya 'Kanker Nasofaring'. Butuh Nasoendoskopi rutin di dokter THT."
    },
    "Kanker Tonsil": {
        "gejala": ["G6", "G29"],
        "solusi": "Pemeriksaan langsung serta biopsi amandel diwajibkan bila curiga arah keganasan (tumor/kanker)."
    },
    "Neuronitis Vestibularis": {
        "gejala": ["G35", "G24"],
        "solusi": "Bed rest saat serangan. Konsumsi obat penekan vestibular resep dokter jika pusing tidak tertahankan."
    },
    "Meniere": {
        "gejala": ["G20", "G35", "G14", "G4"],
        "solusi": "Diet rendah garam (sodium restrict), minimalisir kafein, dan obat khusus vertigo dari THT akan sangat membantu."
    },
    "Tumor Syaraf Pendengaran": {
        "gejala": ["G12", "G34", "G23"],
        "solusi": "Penyakit di area neuroma akustik. Disarankan periksa MRI kepala dan konsultasi bedah saraf beserta THT."
    },
    "Kanker Leher Metastatik": {
        "gejala": ["G29"],
        "solusi": "Perlu investigasi lebih lanjut darimana asal tumor primernya. Diperlukan tindakan Biopsi Jarum Halus (FNAB)."
    },
    "Osteosklerosis": {
        "gejala": ["G34", "G9"],
        "solusi": "Kelainan tulang pendengaran kaku (Otosklerosis). Opsi solutif: Alat bantu dengar atau operasi Stapedektomi."
    },
    "Vertigo Postular": {
        "gejala": ["G24"],
        "solusi": "Hindari gerakan kepala mendadak terutama pada saat tidur/bangun. Bisa pulih dengan Manuver Epley bersama dokter."
    }
}

# 2. Daftar Semua Gejala Untuk Pertanyaan
# Struktur: (kode_gejala, teks_pertanyaan)
semua_gejala = [
    ("G1", "Apakah Anda bernafas secara abnormal (berbunyi atau tidak teratur)?"),
    ("G2", "Apakah suara Anda menjadi lebih serak dari biasanya?"),
    ("G3", "Apakah terdapat perubahan warna, tekstur, atau bentuk pada kulit Anda?"),
    ("G4", "Apakah telinga Anda terasa penuh atau tersumbat?"),
    ("G5", "Apakah Anda merasa nyeri pada saat berbicara atau menelan?"),
    ("G6", "Apakah tenggorokan Anda terasa nyeri?"),
    ("G7", "Apakah bagian leher Anda terasa nyeri?"),
    ("G8", "Apakah Anda mengalami pendarahan hidung (mimisan)?"),
    ("G9", "Apakah telinga bagian dalam Anda sering berdenging (tinnitus)?"),
    ("G10", "Apakah air liur Anda terus-menerus menetes (sulit ditelan)?"),
    ("G11", "Apakah terjadi perubahan atau pergeseran pada pita suara Anda saat berbicara?"),
    ("G12", "Apakah Anda merasa sakit kepala secara signifikan?"),
    ("G13", "Apakah terdapat atau terasa nyeri di pinggir area hidung?"),
    ("G14", "Apakah Anda mengalami serangan vertigo atau rasa berputar mendadak?"),
    ("G15", "Apakah Anda merasakan adanya pembengkakan pada kelenjar getah bening?"),
    ("G16", "Apakah leher Anda terlihat bengkak secara fisik?"),
    ("G17", "Apakah hidung Anda terasa tersumbat sehingga sulit bernafas?"),
    ("G18", "Apakah Anda memiliki riwayat atau gejala infeksi pada rongga sinus?"),
    ("G19", "Apakah berat badan Anda turun mendadak tanpa sebab makanan yang jelas?"),
    ("G20", "Apakah Anda merasa nyeri mendalam pada telinga?"),
    ("G21", "Apakah selaput lendir (mukosa) di hidung atau tenggorokan tampak memerah?"),
    ("G22", "Apakah Anda merasakan ada benjolan di leher (Benjolan leher)?"),
    ("G23", "Apakah tubuh terasa tak seimbang saat melakukan perpindahan posisi/berdiri?"),
    ("G24", "Apakah bola mata Anda bergerak dengan sendirinya (nistagmus)?"),
    ("G25", "Apakah Anda merasakan nyeri pada area dan otot wajah?"),
    ("G26", "Apakah area dahi bagian atas mata Anda terasa sakit?"),
    ("G27", "Apakah Anda mengalami batuk secara berkala atau intens?"),
    ("G28", "Apakah ada jaringan tidak wajar yang tumbuh di dalam kawasan mulut?"),
    ("G29", "Apakah terdapat pembengkakan benjolan di leher Anda (Benjolan dileher)?"),
    ("G30", "Apakah Anda merasa nyeri di sela-sela antara area mata Anda?"),
    ("G31", "Apakah ada dugaan radang pada dinding gendang telinga Anda?"),
    ("G32", "Apakah dalam rongga tenggorokan Anda terasa sangat gatal?"),
    ("G33", "Apakah hidung Anda terus-menerus meler atau ingusan?"),
    ("G34", "Apakah telinga Anda mengalami tuli atau penurunan fungsi pendengaran yang ekstrim?"),
    ("G35", "Apakah Anda merasa sensasi mual dan ingin muntah?"),
    ("G36", "Apakah badan Anda selalu merasa sangat letih dan dan lesu dalam beraktivitas?"),
    ("G37", "Apakah Anda sedang mengalami demam atau peningkatan panas tubuh?")
]

# 3. Working Memory — Menyimpan Gejala yang Dialami Pengguna
gejala_pasien = []

# 4. Fungsi Tanya Gejala
def tanya_gejala(kode_gejala, teks_pertanyaan):
    """Menampilkan pertanyaan dan menyimpan jawaban ke working memory."""
    while True:
        jawaban = input(f"[{kode_gejala}] {teks_pertanyaan} (y/t): ").lower().strip()
        if jawaban in ('y', 't'):
            break
        print("  ⚠ Masukkan 'y' untuk Ya atau 't' untuk Tidak.")
    if jawaban == 'y':
        gejala_pasien.append(kode_gejala)

# 5. Mesin Inferensi — Forward Chaining
def jalankan_diagnosa():
    """Mencocokkan gejala pasien dengan knowledge base untuk mendiagnosa penyakit THT."""
    hasil_diagnosa = []

    for penyakit, data in database_penyakit.items():
        gejala_penyakit = data["gejala"]
        # Hitung berapa gejala yang cocok dari pasien
        gejala_cocok = [g for g in gejala_penyakit if g in gejala_pasien]
        jumlah_cocok = len(gejala_cocok)
        jumlah_total = len(gejala_penyakit)

        # Penyakit terdeteksi jika semua gejala kunci penyakit tersebut terpenuhi tubuh pasien
        if jumlah_cocok == jumlah_total:
            persentase = 100.0
            hasil_diagnosa.append((penyakit, data["solusi"], persentase, gejala_cocok))
        # Penyakit kemungkinan jika sebagian besar gejala terpenuhi (>= 50%)
        elif jumlah_cocok > 0 and (jumlah_cocok / jumlah_total) >= 0.5:
            persentase = round((jumlah_cocok / jumlah_total) * 100, 1)
            hasil_diagnosa.append((penyakit, data["solusi"], persentase, gejala_cocok))

    return hasil_diagnosa

# 6. Fungsi Menampilkan Hasil Diagnosa
def tampilkan_hasil(hasil_diagnosa):
    """Menampilkan hasil diagnosa penyakit THT beserta solusinya."""
    print("\n" + "=" * 60)
    print("            HASIL DIAGNOSA PENYAKIT THT")
    print("=" * 60)

    if not hasil_diagnosa:
        print("\n  Tidak ditemukan penyakit yang cocok berdasarkan")
        print("     kombinasi gejala yang Anda masukkan.")
        print("\n  Saran: Pastikan jawaban Anda akurat atau hubungi")
        print("     Klinik Dokter THT terdekat untuk pengecekan fisik langsung.\n")
    else:
        # Urutkan secara descending berdasarkan tingkat persentase kesesuaian tertinggi
        hasil_diagnosa.sort(key=lambda x: x[2], reverse=True)
        for i, (penyakit, solusi, persentase, gejala_cocok) in enumerate(hasil_diagnosa, 1):
            status = "TERDETEKSI" if persentase == 100.0 else "KEMUNGKINAN"
            print(f"\n  [{i}] {status}: {penyakit}")
            print(f"      Tingkat Kesesuaian : {persentase}%")
            print(f"      Gejala Cocok       : {', '.join(gejala_cocok)}")
            print(f"      Solusi             : {solusi}")

    print("\n" + "=" * 60)

# 7. Fungsi Utama — Main Program
def main():
    print("=" * 60)
    print("      SISTEM PAKAR DIAGNOSA PENYAKIT THT (KONSOL)")
    print("=" * 60)
    print("\n  Instruksi: Jawablah rentetan pertanyaan gejala di bawah ini")
    print("  Ketik 'y' untuk Ya  |  Ketik 't' untuk Tidak\n")
    print("-" * 60)

    # Tanyakan semua unit gejala list kepada pengguna sistem
    for kode, teks in semua_gejala:
        tanya_gejala(kode, teks)

    print("-" * 60)
    print("\nMemulai proses analisis inferensi gejala...\n")

    # Mengeksekusi mesin inferensi algoritma
    hasil = jalankan_diagnosa()

    # Menampilkan hasil evaluasi dari diagnosa
    tampilkan_hasil(hasil)

    # Print out summary log gejala pasien dari working memory
    if gejala_pasien:
        print("Summary Gejala Terpilih yang Anda Dialami:")
        for g in gejala_pasien:
            print(f"     -> {g}")
        print()

# Pemanggilan program utama
if __name__ == "__main__":
    main()

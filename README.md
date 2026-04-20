# H1D024102-PraktikumKB-Pertemuan5

Pengumpulan tugas praktikum Kecerdasan Buatan pertemuan 5.

## Sistem Pakar Diagnosa Penyakit THT

Program ini merupakan implementasi sistem pakar (Expert System) berbasis Python menggunakan metode **Forward Chaining** untuk mendiagnosa penyakit pada THT (Telinga, Hidung, Tenggorokan) berdasarkan gejala yang dimasukkan oleh pengguna. Gaya bahasa, arsitektur, dan logika program ini mengadaptasi dari tugas sistem pakar diagnostik pada pertemuan-pertemuan sebelumnya (Pertemuan 4).

---

### 1. Knowledge Base (Basis Pengetahuan)

Knowledge base didefinisikan menggunakan struktur data **Dictionary** pada kode program `main.py`. Setiap penyakit THT memiliki daftar gejala spesifik beserta rekomendasi solusi penanganannya.

Program ini memiliki **23 jenis penyakit THT** yang dapat dideteksi berdasarkan tabel data studi kasus:

Struktur penyimpanan menggunakan Dictionary nested:
```python
database_penyakit = {
    "Nama Penyakit": {
        "gejala": ["G1", "G2", ...],
        "solusi": "Deskripsi solusi penanganan medis"
    }
}
```

---

### 2. Daftar Gejala (Pertanyaan)

Seluruh gejala yang diajukan kepada pengguna didefinisikan dalam bentuk list of tuple `semua_gejala`. Terdapat **37 gejala THT** (G1 hingga G37) yang akan ditanyakan secara berurutan menyesuaikan dengan data studi kasus.

Setiap elemen tuple berisi:
- **Kode gejala** (contoh: G1, G37) — digunakan sebagai key untuk pencocokan dengan knowledge base.
- **Teks pertanyaan** — pertanyaan medis yang ditampilkan ke pengguna dalam bahasa Indonesia.

---

### 3. Working Memory

Working memory dideklarasikan berupa list kosong `gejala_pasien = []`. List ini berfungsi untuk menyimpan kode gejala yang dijawab "Ya" oleh responden/pengguna selama sesi pengajuan diagnosa berlangsung.

---

### 4. Fungsi Tanya Gejala

Fungsi `tanya_gejala()` bertugas menampilkan pertanyaan kepada pengguna dan memasukkan kode gejala ke dalam working memory jika pengguna merespon `'y'`. Fungsi ini juga menangani validasi input iteratif agar hanya menerima string jawaban `'y'` atau `'t'`.

---

### 5. Mesin Inferensi (Forward Chaining)

Mesin inferensi diimplementasikan secara dinamis pada fungsi `jalankan_diagnosa()`. Proses pengambilan keputusan (inferensi) bekerja sebagai berikut:

1. Program mengiterasi komparasi silang seluruh penyakit di knowledge base.
2. Untuk setiap penyakit, program menghitung jumlah total gejala pasien yang cocok dengan manifestasi gejala mutlak di working memory.
3. Jika **semua gejala** terpenuhi → penyakit berstatus **TERDETEKSI** (100% kesesuaian).
4. Jika **sebagian gejala dominan** terpenuhi (≥ 50%) → penyakit di-skor sebagai **KEMUNGKINAN** dengan menampilkan nilai persentase kedekatannya.
5. Jika tidak ada gejala yang cocok signifikan → penyakit **tidak dilis/tidak terdeteksi**.

---

### 6. Output Hasil Diagnosa

Fungsi `tampilkan_hasil()` menampilkan log hasil akhir diagnosa yang meliputi:
- **Status deteksi** — `TERDETEKSI` atau `KEMUNGKINAN`.
- **Nama penyakit** — jenis penyakit THT yang diderita.
- **Tingkat kesesuaian** — persentase kecocokan rekam gejala pasien `(n Terpenuhi / n Total) * 100%`.
- **Gejala yang cocok** — daftar rawatan kode gejala yang bersinggungan langsung.
- **Solusi singkat** — rekomendasi tindakan lanjutan terkait rujukan medis atau penanganan pertama yang dimasukkan dari dictionary penyakit.

---

### 7. Cara Menjalankan Program

Aplikasi ini dibangun menggunakan antarmuka Command Line Interface (Console).

```bash
# Buka terminal dan masuk ke direktori Pertemuan 5
cd "Pertemuan 5"

# Jalankan Sistem Pakar Diagnosa Penyakit THT
python main.py
```

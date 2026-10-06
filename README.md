# pemograman-berorientasi-objek-pertemuan-7

Repository Praktikum Pemrograman Berorientasi Obyek (PBO) — **Modul 7: Abstract Class, Abstract Method, dan Interface** (*Project Based Learning + Agile Sprint Framework*).

---

## 👤 Identitas Mahasiswa & Akademik

- **Nama Mahasiswa** : Ahmad Yasar Maulana Dais
- **NRP** : 3125522018
- **Program Studi** : D3 Teknik Informatika
- **Kampus** : Politeknik Elektronika Negeri Surabaya (PENS) - PSDKU Sumenep (2026)
- **Mata Kuliah** : Praktikum Pemrograman Berorientasi Obyek (PBO)
- **Dosen Pengampu** : Nirwana Haidar Hari, S.Pd., M.Kom.
- **Topik Proyek** : AutoRent System — Sprint 7: Abstraction, Abstract Method, Interface & Polymorphism

---

## 📌 Deskripsi & Capaian Pembelajaran Modul 7

Pada praktikum Modul 7 ini, proyek **AutoRent System** hasil P6 direfaktor secara arsitektural menuju tahapan **Abstraction**:
1. **Abstract Class**: Mendeklarasikan Superclass `Kendaraan` dan `Person` sebagai `abstract class` guna mencegah instansiasi objek konseptual secara langsung (`new Kendaraan()` / `new Person()`).
2. **Abstract Method**: Mendefinisikan method abstrak (`hitungEstimasiBiaya()`, `tampilkanSpesifikasi()`, `getTipeKendaraan()`, `tampilkanProfil()`, `hitungKompensasi()`) yang wajib diimplementasikan oleh seluruh subclass konkret (`Mobil`, `Motor`, `Minibus`, `Pelanggan`, `Pegawai`).
3. **Interface Realization**:
   - `DapatDilacak`: Kontrak telematika GPS IoT yang diimplementasikan secara lintas hierarki oleh armada (`Mobil`, `Motor`, `Minibus`) dan petugas lapangan (`Pegawai`).
   - `Perawatan`: Kontrak standarisasi pemeliharaan berkala dan uji kelaikan jalan armada.
   - `Cetakable`: Kontrak standarisasi pencetakan format dokumen resmi (kuitansi transaksi, kartu member digital, dan slip gaji pegawai).
4. **Dynamic Polymorphism**: Pembuktian *Dynamic Method Dispatch* via *Superclass Abstract Reference* dan *Interface Reference*.
5. **Heterogeneous Collection**: Pemrosesan koleksi heterogen bertipe superclass abstrak dan interface (`List<Cetakable>`, `DapatDilacak[]`).

---

## 🏗️ Struktur Arsitektur & UML Class Diagram

```
                     +----------------------------------+
                     |      <<abstract>> Kendaraan      |
                     +----------------------------------+
                     | - nomorPlat: String              |
                     | - merk, model: String            |
                     | - tarifPerHari: double           |
                     | - mesin: Mesin (◆ Komposisi)     |
                     +----------------------------------+
                     | + <<abstract>> hitungEstimasi()  |
                     | + <<abstract>> tampilkanSpesif() |
                     | + hitungEstimasi(durasi, diskon) |
                     +----------------------------------+
                                      △
                                      │ Generalization (extends)
               ┌──────────────────────┼──────────────────────┐
               │                      │                      │
    +--------------------+ +--------------------+ +--------------------+
    |       Mobil        | |       Motor        | |      Minibus       |
    +--------------------+ +--------------------+ +--------------------+
    | - tipeTransmisi    | | - jenisMotor       | | - jumlahKursi      |
    | - fasilitasAC      | | - bagasiHelm       | | - noIzinTrayek     |
    +--------------------+ +--------------------+ +--------------------+
               ┆                      ┆                      ┆
               ┆ implements           ┆ implements           ┆ implements
               └──────────────────────┼──────────────────────┘
                                      ▼
                       +──────────────────────────────+
                       |   <<interface>> DapatDilacak |
                       +──────────────────────────────+
                       | + getLokasi(): String        |
                       | + perbaruiLokasi(koor, area) |
                       | + getStatusGPS(): String     |
                       | + default pingTelematika()   |
                       +──────────────────────────────+
                                      ▲
                                      ┆ implements (Lintas Hierarki!)
                                      │
    +--------------------+            │            +--------------------+
    |<<abstract>> Person |            │            |      Pegawai       |
    +--------------------+            │            +--------------------+
    | - id, nama, email  |            │            | - NIK: String      |
    +--------------------+            │            | - posisiJabatan    |
    | + <<abs>> profil() |            │            | - gajiPokok        |
    | + <<abs>> kompen() |            │            +--------------------+
    +--------------------+            │                      ▲
               △                      │                      │ extends
               └──────────────────────┴──────────────────────┘
               │
    +--------------------+            +──────────────────────────────+
    |     Pelanggan      | ┆implements|   <<interface>> Cetakable    |
    +--------------------+───────────>+──────────────────────────────+
    | - nomorKTP         |            | + formatCetakDokumen()       |
    | - saldoDeposit     |            | + generateRingkasan()        |
    +--------------------+            +──────────────────────────────+
                                                      ▲
    +────────────────────+               ┆ implements │
    |   GarasiArmada     |               └────────────┼─────────────────┐
    | (◇ Agregasi Armada)|                            │                 │
    +────────────────────+                            │                 │
    +────────────────────+            +──────────────────────────────+  │
    |   TransaksiSewa    |───────────>|        DetailItemBiaya       |  │
    | (Asosiasi & Cetak) | (◆ Kompos) |       (Komposisi Rincian)    |  │
    +────────────────────+            +──────────────────────────────+  │
               :                                                        │
               :..> KuitansiPrinter (Service Dependency) <──────────────┘
               :..> LayananNotifikasi (Service Gateway)
```

---

## 📂 Struktur Direktori Repositori

```
pemograman-berorientasi-objek-pertemuan-7/
├── .gitignore
├── README.md
├── Laporan_Praktikum_PBO_Modul_7_AutoRent.docx  (Laporan Lengkap Praktikum Format Word)
├── Laporan_Praktikum_PBO_Modul_7_AutoRent.pdf   (Laporan Lengkap Praktikum Format PDF, 39 Halaman)
├── P7_3125522018_Ahmad Yasar Maulana Dais/      (Folder Pengumpulan Resmi Sesuai Modul 7)
│   ├── README.pdf                               (Dokumen Ringkasan Sprint Tepat 3 Halaman)
│   └── src/                                     (17 File Java Source Code)
│       ├── DapatDilacak.java
│       ├── Perawatan.java
│       ├── Cetakable.java
│       ├── Person.java
│       ├── Kendaraan.java
│       ├── Mobil.java
│       ├── Motor.java
│       ├── Minibus.java
│       ├── Pelanggan.java
│       ├── Pegawai.java
│       ├── Mesin.java
│       ├── DetailItemBiaya.java
│       ├── GarasiArmada.java
│       ├── TransaksiSewa.java
│       ├── KuitansiPrinter.java
│       ├── LayananNotifikasi.java
│       └── Main.java
└── src/                                         (Source Code Aktif Workspace)
```

---

## 🚀 Cara Kompilasi & Menjalankan Program

### 1. Kompilasi Seluruh Source Code
```bash
javac -encoding UTF-8 -d bin src/*.java
```

### 2. Eksekusi Test Suite Driver
```bash
java -cp bin Main
```

---

## ✅ Ketercapaian Definition of Done (100% SUKSES)
- [x] Menggunakan proyek hasil P6 sebagai basis refactoring
- [x] Audit desain dan alasan penggunaan abstraksi tersedia
- [x] Minimal 1 abstract class yang relevan dibuat (`Kendaraan` & `Person`)
- [x] Minimal 1 abstract method dibuat (`hitungEstimasiBiaya`, `tampilkanSpesifikasi`, dll)
- [x] Minimal 2 subclass konkret mengimplementasikan abstract method (5 Subclass)
- [x] Minimal 1 interface dibuat (`DapatDilacak`, `Perawatan`, `Cetakable`)
- [x] Minimal 2 class mengimplementasikan interface yang relevan
- [x] Polymorphism melalui superclass dan interface dapat dibuktikan
- [x] Class diagram diperbarui dan konsisten dengan kode
- [x] Program berhasil dikompilasi (0 error) dan dijalankan
- [x] Minimal 4 skenario pengujian tersedia (8 Fase Pengujian Selesai)
- [x] Fitur proyek sebelumnya (P1–P6) tetap berjalan normal
- [x] Sprint Backlog diperbarui (SB-01 s/d SB-07)
- [x] Sprint Review tersedia (7/7 item terverifikasi)
- [x] Sprint Retrospective tersedia lengkap

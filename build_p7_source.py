import os
import shutil

src_dir = "src"
sub_src_dir = os.path.join("P7_3125522018_Ahmad Yasar Maulana Dais", "src")
os.makedirs(src_dir, exist_ok=True)
os.makedirs(sub_src_dir, exist_ok=True)

# 1. DapatDilacak.java
dapat_dilacak_code = """/**
 * Interface DapatDilacak
 * 
 * Mendefinisikan kontrak perilaku telematika dan pelacakan posisi GPS IoT untuk seluruh
 * entitas armada maupun petugas operasional di ekosistem AutoRent System.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public interface DapatDilacak {

    /**
     * Mengambil informasi nama area atau lokasi terkini objek.
     * 
     * @return String representasi lokasi
     */
    String getLokasi();

    /**
     * Memperbarui titik koordinat dan nama area lokasi objek.
     * 
     * @param koordinatBaru format koordinat GPS (contoh: "-7.0051, 113.8604")
     * @param namaArea nama wilayah atau pos pantau
     */
    void perbaruiLokasi(String koordinatBaru, String namaArea);

    /**
     * Mengecek status operasional modul GPS telematika.
     * 
     * @return String status konektivitas GPS
     */
    String getStatusGPS();

    /**
     * Default method (fitur modern Java 8+) untuk mengirimkan sinyal ping telematika standar.
     * Menunjukkan bahwa interface modern dapat memiliki implementasi default tanpa merusak implementor.
     * 
     * @return status pengiriman sinyal ping telematika
     */
    default String kirimSinyalPingTelematika() {
        return "Ping IoT GPS berhasil dikirimkan ke server AutoRent Telematics Central Gateway.";
    }
}
"""

# 2. Perawatan.java
perawatan_code = """/**
 * Interface Perawatan
 * 
 * Mendefinisikan kontrak standar pemeliharaan teknis, jadwal servis berkala,
 * dan uji kelayakan operasional armada rental kendaraan.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public interface Perawatan {

    /**
     * Menjalankan prosedur servis berkala sesuai standar operasional teknis masing-masing armada.
     */
    void lakukanServis();

    /**
     * Memeriksa apakah unit armada memenuhi standar kelayakan jalan raya yang aman bagi penyewa.
     * 
     * @return true jika layak beroperasi, false jika membutuhkan perbaikan mendesak
     */
    boolean cekKelayakanOperasional();

    /**
     * Mengambil informasi jadwal servis berkala berikutnya berdasarkan jarak tempuh atau waktu.
     * 
     * @return String estimasi jadwal servis berikutnya
     */
    String getJadwalServisBerikutnya();
}
"""

# 3. Cetakable.java
cetakable_code = """/**
 * Interface Cetakable
 * 
 * Mendefinisikan kontrak formal bagi seluruh entitas sistem yang dapat digenerate
 * menjadi dokumen cetak resmi (Kuitansi Transaksi, Kartu Member, Slip Gaji Pegawai).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public interface Cetakable {

    /**
     * Menghasilkan representasi dokumen cetak resmi dengan format teks terstruktur.
     * 
     * @return String format dokumen cetak
     */
    String formatCetakDokumen();

    /**
     * Menghasilkan teks ringkasan satu baris yang informatif untuk logging dan audit.
     * 
     * @return String ringkasan dokumen
     */
    String generateRingkasan();
}
"""

# 4. Person.java
person_code = """import java.util.regex.Pattern;

/**
 * Abstract Class Person (Superclass Abstraksi Entitas Manusia)
 * 
 * Kelas abstrak yang merepresentasikan konsep umum manusia dalam sistem AutoRent.
 * Person tidak dapat diinstansiasi secara langsung menggunakan keyword new,
 * melainkan berfungsi sebagai landasan pewarisan atribut identitas dan kontrak perilaku
 * bagi entitas konkrit seperti Pelanggan dan Pegawai.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public abstract class Person {
    private String id;
    private String nama;
    private String nomorTelepon;
    private String alamat;
    private String email;

    private static final Pattern PHONE_PATTERN = Pattern.compile("^08[0-9]{8,11}$");
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");

    /**
     * Konstruktor default Person.
     */
    public Person() {
        this.id = "PRS-UNKNOWN";
        this.nama = "Tanpa Nama";
        this.nomorTelepon = "081234567890";
        this.alamat = "Belum Diatur";
        this.email = "user@autorent.com";
    }

    /**
     * Konstruktor berparameter dengan validasi defensif terintegrasi.
     * 
     * @param id Identifier unik entitas
     * @param nama Nama lengkap
     * @param nomorTelepon Nomor telepon aktif (format 08xxxxxxxx)
     * @param alamat Alamat domisili lengkap
     * @param email Alamat surat elektronik valid
     */
    public Person(String id, String nama, String nomorTelepon, String alamat, String email) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("ID Person tidak boleh kosong.");
        }
        if (nama == null || nama.trim().length() < 2) {
            throw new IllegalArgumentException("Nama person minimal terdiri dari 2 karakter.");
        }
        if (nomorTelepon == null || !PHONE_PATTERN.matcher(nomorTelepon.trim()).matches()) {
            throw new IllegalArgumentException("Nomor telepon tidak valid! Format: 08xxxxxxxx (10-13 digit angka). Input: " + nomorTelepon);
        }
        if (alamat == null || alamat.trim().isEmpty()) {
            throw new IllegalArgumentException("Alamat tidak boleh kosong.");
        }
        if (email == null || !EMAIL_PATTERN.matcher(email.trim()).matches()) {
            throw new IllegalArgumentException("Format email tidak valid! Input: " + email);
        }

        this.id = id.trim().toUpperCase();
        this.nama = nama.trim();
        this.nomorTelepon = nomorTelepon.trim();
        this.alamat = alamat.trim();
        this.email = email.trim().toLowerCase();
    }

    // --- Getter dan Setter dengan Validasi Defensif ---

    public String getId() {
        return id;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        if (nama == null || nama.trim().length() < 2) {
            throw new IllegalArgumentException("Nama person minimal terdiri dari 2 karakter.");
        }
        this.nama = nama.trim();
    }

    public String getNomorTelepon() {
        return nomorTelepon;
    }

    public void setNomorTelepon(String nomorTelepon) {
        if (nomorTelepon == null || !PHONE_PATTERN.matcher(nomorTelepon.trim()).matches()) {
            throw new IllegalArgumentException("Nomor telepon tidak valid! Input: " + nomorTelepon);
        }
        this.nomorTelepon = nomorTelepon.trim();
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        if (alamat == null || alamat.trim().isEmpty()) {
            throw new IllegalArgumentException("Alamat tidak boleh kosong.");
        }
        this.alamat = alamat.trim();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        if (email == null || !EMAIL_PATTERN.matcher(email.trim()).matches()) {
            throw new IllegalArgumentException("Format email tidak valid! Input: " + email);
        }
        this.email = email.trim().toLowerCase();
    }

    // --- Abstract Methods (Kontrak Wajib Subclass) ---

    /**
     * Menampilkan profil lengkap entitas person sesuai format spesifik peran masing-masing.
     * Seluruh subclass konkret wajib mengimplementasikan method ini.
     */
    public abstract void tampilkanProfil();

    /**
     * Mengambil deskripsi peran dan wewenang aktor dalam sistem AutoRent.
     * 
     * @return String deskripsi peran
     */
    public abstract String getDeskripsiPeran();

    /**
     * Menghitung nilai kompensasi finansial (insentif bagi pegawai, atau reward loyalti bagi pelanggan).
     * 
     * @return double nilai kompensasi / reward
     */
    public abstract double hitungKompensasi();

    @Override
    public String toString() {
        return String.format("[%s] %s | Telp: %s | Email: %s", id, nama, nomorTelepon, email);
    }
}
"""

# 5. Kendaraan.java
kendaraan_code = """import java.util.regex.Pattern;

/**
 * Abstract Class Kendaraan (Superclass Abstraksi Armada Sewa)
 * 
 * Kelas abstrak yang merepresentasikan konsep umum armada kendaraan bermotor pada AutoRent.
 * Kendaraan tidak dapat diinstansiasi secara langsung menggunakan keyword new Kendaraan(),
 * karena konsep kendaraan di dunia nyata adalah abstraksi umum.
 * Subclass konkret (Mobil, Motor, Minibus) wajib mengimplementasikan seluruh abstract method.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public abstract class Kendaraan {
    private String nomorPlat;
    private String merk;
    private String model;
    private int tahunProduksi;
    private double tarifPerHari;
    private boolean statusTersedia;
    private Mesin mesin; // Komposisi ketat
    private int totalKaliDisewa;
    private int totalJarakTempuhKm;

    private static final Pattern PLAT_PATTERN = Pattern.compile("^[A-Z]{1,2}\\\\s[0-9]{1,4}\\\\s[A-Z]{1,3}$");

    /**
     * Konstruktor default Kendaraan.
     */
    public Kendaraan() {
        this.nomorPlat = "M 1000 XX";
        this.merk = "Generic";
        this.model = "Standard";
        this.tahunProduksi = 2020;
        this.tarifPerHari = 100000.0;
        this.statusTersedia = true;
        this.mesin = new Mesin("ENG-DEF-001", 1000, "Bensin");
        this.totalKaliDisewa = 0;
        this.totalJarakTempuhKm = 0;
    }

    /**
     * Konstruktor berparameter lengkap dengan validasi defensif dan inisialisasi komposisi Mesin.
     * 
     * @param nomorPlat Nomor registrasi kendaraan (format: [A-Z]{1,2} [0-9]{1,4} [A-Z]{1,3})
     * @param merk Pabrikan kendaraan
     * @param model Model seri kendaraan
     * @param tahunProduksi Tahun perakitan (2000 - 2026)
     * @param tarifPerHari Tarif sewa dasar per hari (positif)
     * @param nomorRangkaMesin Nomor seri mesin untuk komposisi
     * @param kapasitasCC Kapasitas silinder mesin dalam CC
     * @param tipeBahanBakar Jenis bahan bakar mesin
     */
    public Kendaraan(String nomorPlat, String merk, String model, int tahunProduksi, double tarifPerHari,
                     String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar) {
        if (nomorPlat == null || !PLAT_PATTERN.matcher(nomorPlat.trim().toUpperCase()).matches()) {
            throw new IllegalArgumentException("Nomor Plat tidak valid! Format: 'M 1234 AB'. Input: " + nomorPlat);
        }
        if (merk == null || merk.trim().isEmpty()) {
            throw new IllegalArgumentException("Merk kendaraan tidak boleh kosong.");
        }
        if (model == null || model.trim().isEmpty()) {
            throw new IllegalArgumentException("Model kendaraan tidak boleh kosong.");
        }
        if (tahunProduksi < 2000 || tahunProduksi > 2026) {
            throw new IllegalArgumentException("Tahun produksi tidak valid! Rentang: 2000 - 2026. Input: " + tahunProduksi);
        }
        if (tarifPerHari <= 0) {
            throw new IllegalArgumentException("Tarif sewa per hari harus lebih besar dari Rp 0.");
        }

        this.nomorPlat = nomorPlat.trim().toUpperCase();
        this.merk = merk.trim();
        this.model = model.trim();
        this.tahunProduksi = tahunProduksi;
        this.tarifPerHari = tarifPerHari;
        this.statusTersedia = true;
        this.mesin = new Mesin(nomorRangkaMesin, kapasitasCC, tipeBahanBakar);
        this.totalKaliDisewa = 0;
        this.totalJarakTempuhKm = 0;
    }

    // --- Getter dan Setter ---

    public String getNomorPlat() {
        return nomorPlat;
    }

    public void setNomorPlat(String nomorPlat) {
        if (nomorPlat == null || !PLAT_PATTERN.matcher(nomorPlat.trim().toUpperCase()).matches()) {
            throw new IllegalArgumentException("Nomor Plat tidak valid! Input: " + nomorPlat);
        }
        this.nomorPlat = nomorPlat.trim().toUpperCase();
    }

    public String getMerk() {
        return merk;
    }

    public void setMerk(String merk) {
        if (merk == null || merk.trim().isEmpty()) {
            throw new IllegalArgumentException("Merk tidak boleh kosong.");
        }
        this.merk = merk.trim();
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        if (model == null || model.trim().isEmpty()) {
            throw new IllegalArgumentException("Model tidak boleh kosong.");
        }
        this.model = model.trim();
    }

    public int getTahunProduksi() {
        return tahunProduksi;
    }

    public void setTahunProduksi(int tahunProduksi) {
        if (tahunProduksi < 2000 || tahunProduksi > 2026) {
            throw new IllegalArgumentException("Tahun produksi tidak valid! Input: " + tahunProduksi);
        }
        this.tahunProduksi = tahunProduksi;
    }

    public double getTarifPerHari() {
        return tarifPerHari;
    }

    public void setTarifPerHari(double tarifPerHari) {
        if (tarifPerHari <= 0) {
            throw new IllegalArgumentException("Tarif per hari harus positif.");
        }
        this.tarifPerHari = tarifPerHari;
    }

    public boolean isStatusTersedia() {
        return statusTersedia;
    }

    public void setStatusKetersediaan(boolean statusTersedia) {
        this.statusTersedia = statusTersedia;
    }

    public Mesin getMesin() {
        return mesin;
    }

    public int getTotalKaliDisewa() {
        return totalKaliDisewa;
    }

    public int getTotalJarakTempuhKm() {
        return totalJarakTempuhKm;
    }

    // --- Manajemen Siklus Hidup Kendaraan ---

    public void catatPenyewaan(int kmBertambah) {
        if (kmBertambah < 0) {
            throw new IllegalArgumentException("Kilometer pemakaian tidak boleh bernilai negatif.");
        }
        this.statusTersedia = false;
        this.totalKaliDisewa++;
        this.totalJarakTempuhKm += kmBertambah;
        this.mesin.kurangiKesehatanOli(kmBertambah);
    }

    public void selesaikanPenyewaan() {
        this.statusTersedia = true;
    }

    public void servisMesinKendaraan() {
        this.mesin.gantiOliMesin();
    }

    // --- Abstract Methods (Wajib Diimplementasikan Subclass) ---

    /**
     * Menghitung estimasi total biaya sewa dasar berdasarkan durasi hari pemakaian.
     * Logika diskon durasi dan surcharge spesifik diimplementasikan pada masing-masing Subclass.
     * 
     * @param durasiHari Durasi sewa dalam hari (>= 1)
     * @return double total biaya sewa dasar terhitung
     */
    public abstract double hitungEstimasiBiaya(int durasiHari);

    /**
     * Menampilkan spesifikasi teknis dan fasilitas unik armada ke konsol.
     */
    public abstract void tampilkanSpesifikasi();

    /**
     * Mengambil kategori/tipe armada kendaraan.
     * 
     * @return String kategori kendaraan
     */
    public abstract String getTipeKendaraan();

    // --- Method Overloading (Compile-Time Polymorphism) ---

    /**
     * Overload 1: Menghitung estimasi biaya sewa dengan potongan diskon promosi persentase.
     * 
     * @param durasiHari durasi sewa dalam hari
     * @param diskonPersen persentase diskon promo (0 - 50%)
     * @return double total biaya setelah diskon
     */
    public double hitungEstimasiBiaya(int durasiHari, double diskonPersen) {
        if (diskonPersen < 0 || diskonPersen > 50.0) {
            throw new IllegalArgumentException("Persentase diskon promo harus berada dalam rentang 0% - 50%. Input: " + diskonPersen);
        }
        double biayaDasar = this.hitungEstimasiBiaya(durasiHari); // Dynamic dispatch ke abstract method
        double potongan = biayaDasar * (diskonPersen / 100.0);
        return biayaDasar - potongan;
    }

    /**
     * Overload 2: Menghitung estimasi biaya sewa dengan opsi layanan supir profesional.
     * 
     * @param durasiHari durasi sewa dalam hari
     * @param includeLayananSupir flag opsi supir
     * @param tarifSupirPerHari tarif jasa supir harian
     * @return double total biaya sewa + supir
     */
    public double hitungEstimasiBiaya(int durasiHari, boolean includeLayananSupir, double tarifSupirPerHari) {
        double biayaDasar = this.hitungEstimasiBiaya(durasiHari);
        if (includeLayananSupir) {
            if (tarifSupirPerHari <= 0) {
                throw new IllegalArgumentException("Tarif layanan supir harus bernilai positif.");
            }
            return biayaDasar + (tarifSupirPerHari * durasiHari);
        }
        return biayaDasar;
    }

    @Override
    public String toString() {
        return String.format("[%s] %s %s (%d) | Rp %,.2f/hari | Status: %s | Total Sewa: %d kali",
                nomorPlat, merk, model, tahunProduksi, tarifPerHari,
                (statusTersedia ? "TERSEDIA" : "DISEWA"), totalKaliDisewa);
    }
}
"""

# 6. Mobil.java
mobil_code = """/**
 * Concrete Subclass Mobil (Turunan dari Kendaraan)
 * 
 * Mengimplementasikan abstract method dari Kendaraan dan merealisasikan interface
 * DapatDilacak, Perawatan, dan Cetakable.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Mobil extends Kendaraan implements DapatDilacak, Perawatan, Cetakable {
    private String tipeTransmisi; // "Manual" atau "Automatic"
    private int kapasitasPenumpang;
    private boolean fasilitasAC;
    private String lokasiTerkiniGPS;
    private String koordinatGPS;
    private boolean statusGPSAktif;
    private String tanggalServisTerakhir;

    public Mobil(String nomorPlat, String merk, String model, int tahunProduksi, double tarifPerHari,
                 String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar,
                 String tipeTransmisi, int kapasitasPenumpang, boolean fasilitasAC) {
        super(nomorPlat, merk, model, tahunProduksi, tarifPerHari, nomorRangkaMesin, kapasitasCC, tipeBahanBakar);

        if (tipeTransmisi == null || (!tipeTransmisi.equalsIgnoreCase("Manual") && !tipeTransmisi.equalsIgnoreCase("Automatic"))) {
            throw new IllegalArgumentException("Tipe transmisi mobil harus bernilai 'Manual' atau 'Automatic'. Input: " + tipeTransmisi);
        }
        if (kapasitasPenumpang < 2 || kapasitasPenumpang > 10) {
            throw new IllegalArgumentException("Kapasitas penumpang mobil harus dalam rentang 2 - 10 orang. Input: " + kapasitasPenumpang);
        }

        this.tipeTransmisi = tipeTransmisi;
        this.kapasitasPenumpang = kapasitasPenumpang;
        this.fasilitasAC = fasilitasAC;
        this.lokasiTerkiniGPS = "Garasi Utama PENS Sumenep";
        this.koordinatGPS = "-7.0051, 113.8604";
        this.statusGPSAktif = true;
        this.tanggalServisTerakhir = "2026-03-01";
    }

    public String getTipeTransmisi() {
        return tipeTransmisi;
    }

    public int getKapasitasPenumpang() {
        return kapasitasPenumpang;
    }

    public boolean isFasilitasAC() {
        return fasilitasAC;
    }

    public void pasangAksesoris(String namaAksesoris, double biayaTambahan) {
        if (biayaTambahan < 0) {
            throw new IllegalArgumentException("Biaya aksesoris tidak boleh negatif.");
        }
        System.out.println(String.format("  [Aksesoris Mobil %s] Berhasil memasang '%s' (Biaya Tambahan: Rp %,.2f)",
                getNomorPlat(), namaAksesoris, biayaTambahan));
    }

    // --- Implementasi Abstract Methods dari Kendaraan ---

    @Override
    public double hitungEstimasiBiaya(int durasiHari) {
        if (durasiHari <= 0) {
            throw new IllegalArgumentException("Durasi hari sewa mobil minimal 1 hari.");
        }
        double subtotal = getTarifPerHari() * durasiHari;
        // Kebijakan diskon Mobil: > 7 hari diskon 10%, > 3 hari diskon 5%
        if (durasiHari > 7) {
            subtotal *= 0.90;
        } else if (durasiHari > 3) {
            subtotal *= 0.95;
        }
        return subtotal;
    }

    @Override
    public void tampilkanSpesifikasi() {
        System.out.println("  ================ SPESIFIKASI MOBIL ================");
        System.out.println(String.format("  Nomor Plat   : %s", getNomorPlat()));
        System.out.println(String.format("  Merk/Model   : %s %s (%d)", getMerk(), getModel(), getTahunProduksi()));
        System.out.println(String.format("  Kategori     : %s", getTipeKendaraan()));
        System.out.println(String.format("  Tarif Sewa   : Rp %,.2f / hari", getTarifPerHari()));
        System.out.println(String.format("  Transmisi    : %s | Kapasitas: %d Penumpang", tipeTransmisi, kapasitasPenumpang));
        System.out.println(String.format("  Fasilitas AC : %s", fasilitasAC ? "Dingin Dual-Zone" : "Tidak Tersedia"));
        System.out.println(String.format("  Posisi GPS   : %s (%s)", lokasiTerkiniGPS, koordinatGPS));
        System.out.println(String.format("  Mesin        : %d CC [%s] | Oli: %d%% | Status: %s",
                getMesin().getKapasitasCC(), getMesin().getTipeBahanBakar(),
                getMesin().getIndikatorKesehatanOliPersen(),
                (isStatusTersedia() ? "SIAP DISEWA" : "SEDANG BEROPERASI")));
        System.out.println("  ====================================================");
    }

    @Override
    public String getTipeKendaraan() {
        return "Mobil Penumpang";
    }

    // --- Realisasi Interface DapatDilacak ---

    @Override
    public String getLokasi() {
        return String.format("%s [Koordinat: %s, Status GPS: %s]",
                lokasiTerkiniGPS, koordinatGPS, (statusGPSAktif ? "ONLINE" : "OFFLINE"));
    }

    @Override
    public void perbaruiLokasi(String koordinatBaru, String namaArea) {
        if (koordinatBaru == null || namaArea == null) {
            throw new IllegalArgumentException("Data koordinat dan nama area tidak boleh kosong.");
        }
        this.koordinatGPS = koordinatBaru.trim();
        this.lokasiTerkiniGPS = namaArea.trim();
        System.out.println(String.format("  [GPS UPDATE] Mobil %s kini terpantau di: %s (%s)",
                getNomorPlat(), this.lokasiTerkiniGPS, this.koordinatGPS));
    }

    @Override
    public String getStatusGPS() {
        return statusGPSAktif ? "AKTIF - Terkoneksi 8 Satelit GPS" : "NONAKTIF - Sinyal Terputus";
    }

    // --- Realisasi Interface Perawatan ---

    @Override
    public void lakukanServis() {
        System.out.println(String.format("  [SERVIS MOBIL] Menjalankan SOP Servis Berkala untuk Unit %s (%s %s)...",
                getNomorPlat(), getMerk(), getModel()));
        System.out.println("  -> Penggantian Oli Mesin Sintetis & Filter Oli.");
        System.out.println("  -> Pengecekan Sistem Transmisi " + tipeTransmisi + " & Minyak Rem.");
        System.out.println("  -> Rotasi & Spooring-Balancing 4 Roda.");
        System.out.println("  -> Pembersihan Evaporator Filter AC & Pengisian Freon.");
        servisMesinKendaraan();
        this.tanggalServisTerakhir = "2026-10-05";
        System.out.println("  [SUKSES] Servis Mobil selesai! Seluruh indikator mekanikal kembali prima.");
    }

    @Override
    public boolean cekKelayakanOperasional() {
        return getMesin().getIndikatorKesehatanOliPersen() >= 40 && isStatusTersedia();
    }

    @Override
    public String getJadwalServisBerikutnya() {
        return String.format("Servis berikutnya: Maksimal jarak tempuh %d km atau tanggal 2026-12-05 (Terakhir: %s)",
                getTotalJarakTempuhKm() + 5000, tanggalServisTerakhir);
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("====================================================\\n");
        sb.append("           LEMBAR SPESIFIKASI ARMADA MOBIL          \\n");
        sb.append("====================================================\\n");
        sb.append(String.format("Plat Nomor    : %s\\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Kapasitas     : %d Orang | Transmisi: %s\\n", kapasitasPenumpang, tipeTransmisi));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MOBIL [%s] %s %s - %d Pax - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), kapasitasPenumpang, getTarifPerHari());
    }
}
"""

# 7. Motor.java
motor_code = """/**
 * Concrete Subclass Motor (Turunan dari Kendaraan)
 * 
 * Mengimplementasikan abstract method dari Kendaraan dan merealisasikan interface
 * DapatDilacak, Perawatan, dan Cetakable.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Motor extends Kendaraan implements DapatDilacak, Perawatan, Cetakable {
    private String jenisMotor; // "Matic", "Sport", "Bebek"
    private int kapasitasBagasiHelm; // kapasitas penyimpanan helm (1 atau 2)
    private boolean tersediaJasHujan;
    private String lokasiTerkiniGPS;
    private String koordinatGPS;
    private boolean statusGPSAktif;
    private String tanggalServisTerakhir;

    public Motor(String nomorPlat, String merk, String model, int tahunProduksi, double tarifPerHari,
                 String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar,
                 String jenisMotor, int kapasitasBagasiHelm, boolean tersediaJasHujan) {
        super(nomorPlat, merk, model, tahunProduksi, tarifPerHari, nomorRangkaMesin, kapasitasCC, tipeBahanBakar);

        if (jenisMotor == null || jenisMotor.trim().isEmpty()) {
            throw new IllegalArgumentException("Jenis motor tidak boleh kosong (contoh: Matic, Sport, Bebek).");
        }
        if (kapasitasBagasiHelm < 0 || kapasitasBagasiHelm > 3) {
            throw new IllegalArgumentException("Kapasitas bagasi helm tidak valid (0 - 3 helm). Input: " + kapasitasBagasiHelm);
        }

        this.jenisMotor = jenisMotor.trim();
        this.kapasitasBagasiHelm = kapasitasBagasiHelm;
        this.tersediaJasHujan = tersediaJasHujan;
        this.lokasiTerkiniGPS = "Garasi Shelter PENS Sumenep";
        this.koordinatGPS = "-7.0055, 113.8610";
        this.statusGPSAktif = true;
        this.tanggalServisTerakhir = "2026-03-05";
    }

    public String getJenisMotor() {
        return jenisMotor;
    }

    public int getKapasitasBagasiHelm() {
        return kapasitasBagasiHelm;
    }

    public boolean isTersediaJasHujan() {
        return tersediaJasHujan;
    }

    public void tambahFasilitasHelm(int jumlahHelm) {
        if (jumlahHelm <= 0) {
            throw new IllegalArgumentException("Jumlah helm tambahan minimal 1 unit.");
        }
        System.out.println(String.format("  [Fasilitas Motor %s] Tambahan %d unit Helm SNI steril disiapkan untuk penyewa.",
                getNomorPlat(), jumlahHelm));
    }

    // --- Implementasi Abstract Methods dari Kendaraan ---

    @Override
    public double hitungEstimasiBiaya(int durasiHari) {
        if (durasiHari <= 0) {
            throw new IllegalArgumentException("Durasi hari sewa motor minimal 1 hari.");
        }
        double subtotal = getTarifPerHari() * durasiHari;
        // Kebijakan tarif hemat motor: > 5 hari diskon spesial 12%, > 2 hari diskon 6%
        if (durasiHari > 5) {
            subtotal *= 0.88;
        } else if (durasiHari > 2) {
            subtotal *= 0.94;
        }
        return subtotal;
    }

    @Override
    public void tampilkanSpesifikasi() {
        System.out.println("  ================ SPESIFIKASI MOTOR ================");
        System.out.println(String.format("  Nomor Plat   : %s", getNomorPlat()));
        System.out.println(String.format("  Merk/Model   : %s %s (%d)", getMerk(), getModel(), getTahunProduksi()));
        System.out.println(String.format("  Kategori     : %s", getTipeKendaraan()));
        System.out.println(String.format("  Tarif Sewa   : Rp %,.2f / hari", getTarifPerHari()));
        System.out.println(String.format("  Jenis Motor  : %s | Bagasi Helm: %d unit", jenisMotor, kapasitasBagasiHelm));
        System.out.println(String.format("  Jas Hujan    : %s", tersediaJasHujan ? "Tersedia 2 Pasang (Steril)" : "Tidak Tersedia"));
        System.out.println(String.format("  Posisi GPS   : %s (%s)", lokasiTerkiniGPS, koordinatGPS));
        System.out.println(String.format("  Mesin        : %d CC [%s] | Oli: %d%% | Status: %s",
                getMesin().getKapasitasCC(), getMesin().getTipeBahanBakar(),
                getMesin().getIndikatorKesehatanOliPersen(),
                (isStatusTersedia() ? "SIAP DISEWA" : "SEDANG BEROPERASI")));
        System.out.println("  ====================================================");
    }

    @Override
    public String getTipeKendaraan() {
        return "Sepeda Motor";
    }

    // --- Realisasi Interface DapatDilacak ---

    @Override
    public String getLokasi() {
        return String.format("%s [Koordinat: %s, Status GPS: %s]",
                lokasiTerkiniGPS, koordinatGPS, (statusGPSAktif ? "ONLINE" : "OFFLINE"));
    }

    @Override
    public void perbaruiLokasi(String koordinatBaru, String namaArea) {
        if (koordinatBaru == null || namaArea == null) {
            throw new IllegalArgumentException("Data koordinat dan nama area tidak boleh kosong.");
        }
        this.koordinatGPS = koordinatBaru.trim();
        this.lokasiTerkiniGPS = namaArea.trim();
        System.out.println(String.format("  [GPS UPDATE] Motor %s kini terpantau di: %s (%s)",
                getNomorPlat(), this.lokasiTerkiniGPS, this.koordinatGPS));
    }

    @Override
    public String getStatusGPS() {
        return statusGPSAktif ? "AKTIF - Terkoneksi 6 Satelit IoT" : "NONAKTIF - Sinyal Terputus";
    }

    // --- Realisasi Interface Perawatan ---

    @Override
    public void lakukanServis() {
        System.out.println(String.format("  [SERVIS MOTOR] Menjalankan SOP Servis Berkala untuk Unit %s (%s %s)...",
                getNomorPlat(), getMerk(), getModel()));
        System.out.println("  -> Penggantian Oli Mesin & Oli Gardan (CVT/Rantai).");
        System.out.println("  -> Pembersihan Injektor/Karburator & Penggantian Busi.");
        System.out.println("  -> Penyetelan Kampas Rem Depan & Belakang.");
        System.out.println("  -> Pengecekan Tekanan Angin Ban Tubeless.");
        servisMesinKendaraan();
        this.tanggalServisTerakhir = "2026-10-05";
        System.out.println("  [SUKSES] Servis Sepeda Motor selesai! Seluruh komponen responsif.");
    }

    @Override
    public boolean cekKelayakanOperasional() {
        return getMesin().getIndikatorKesehatanOliPersen() >= 35 && isStatusTersedia();
    }

    @Override
    public String getJadwalServisBerikutnya() {
        return String.format("Servis berikutnya: Maksimal jarak tempuh %d km atau tanggal 2026-11-20 (Terakhir: %s)",
                getTotalJarakTempuhKm() + 2500, tanggalServisTerakhir);
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("====================================================\\n");
        sb.append("           LEMBAR SPESIFIKASI SEPEDA MOTOR          \\n");
        sb.append("====================================================\\n");
        sb.append(String.format("Plat Nomor    : %s\\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Jenis / CC    : %s | %d CC\\n", jenisMotor, getMesin().getKapasitasCC()));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MOTOR [%s] %s %s - %s - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), jenisMotor, getTarifPerHari());
    }
}
"""

# 8. Minibus.java
minibus_code = """/**
 * Concrete Subclass Minibus (Turunan dari Kendaraan)
 * 
 * Mengimplementasikan abstract method dari Kendaraan dan merealisasikan interface
 * DapatDilacak, Perawatan, dan Cetakable.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Minibus extends Kendaraan implements DapatDilacak, Perawatan, Cetakable {
    private int jumlahKursi;
    private boolean tersediaFasilitasHiburan; // Audio/Video Karaoke, TV
    private boolean tersediaBagasiAtas;
    private String nomorIzinTrayekPariwisata;
    private String lokasiTerkiniGPS;
    private String koordinatGPS;
    private boolean statusGPSAktif;
    private String tanggalServisTerakhir;

    public Minibus(String nomorPlat, String merk, String model, int tahunProduksi, double tarifPerHari,
                   String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar,
                   int jumlahKursi, boolean tersediaFasilitasHiburan, boolean tersediaBagasiAtas,
                   String nomorIzinTrayekPariwisata) {
        super(nomorPlat, merk, model, tahunProduksi, tarifPerHari, nomorRangkaMesin, kapasitasCC, tipeBahanBakar);

        if (jumlahKursi < 8 || jumlahKursi > 30) {
            throw new IllegalArgumentException("Jumlah kursi minibus travel harus dalam rentang 8 - 30 kursi. Input: " + jumlahKursi);
        }
        if (nomorIzinTrayekPariwisata == null || nomorIzinTrayekPariwisata.trim().isEmpty()) {
            throw new IllegalArgumentException("Nomor izin trayek pariwisata tidak boleh kosong.");
        }

        this.jumlahKursi = jumlahKursi;
        this.tersediaFasilitasHiburan = tersediaFasilitasHiburan;
        this.tersediaBagasiAtas = tersediaBagasiAtas;
        this.nomorIzinTrayekPariwisata = nomorIzinTrayekPariwisata.trim().toUpperCase();
        this.lokasiTerkiniGPS = "Pool Bus Komersial PENS Sumenep";
        this.koordinatGPS = "-7.0040, 113.8590";
        this.statusGPSAktif = true;
        this.tanggalServisTerakhir = "2026-02-28";
    }

    public int getJumlahKursi() {
        return jumlahKursi;
    }

    public boolean isTersediaFasilitasHiburan() {
        return tersediaFasilitasHiburan;
    }

    public boolean isTersediaBagasiAtas() {
        return tersediaBagasiAtas;
    }

    public String getNomorIzinTrayekPariwisata() {
        return nomorIzinTrayekPariwisata;
    }

    public void verifikasiIzinOperasional() {
        System.out.println(String.format("  [Dishub Verifikasi] Izin Trayek Pariwisata %s (%s) dinyatakan AKTIF dan RESMI.",
                nomorIzinTrayekPariwisata, getNomorPlat()));
    }

    // --- Implementasi Abstract Methods dari Kendaraan ---

    @Override
    public double hitungEstimasiBiaya(int durasiHari) {
        if (durasiHari <= 0) {
            throw new IllegalArgumentException("Durasi hari sewa minibus minimal 1 hari.");
        }
        double subtotal = getTarifPerHari() * durasiHari;
        // Kebijakan Minibus: Diskon paket rombongan > 5 hari diskon 8%, plus surcharge proteksi komersial
        if (durasiHari > 5) {
            subtotal *= 0.92;
        }
        double surchargeKomersial = 50000.0 * durasiHari; // Biaya pemeliharaan armada besar
        return subtotal + surchargeKomersial;
    }

    @Override
    public void tampilkanSpesifikasi() {
        System.out.println("  =============== SPESIFIKASI MINIBUS ===============");
        System.out.println(String.format("  Nomor Plat   : %s", getNomorPlat()));
        System.out.println(String.format("  Merk/Model   : %s %s (%d)", getMerk(), getModel(), getTahunProduksi()));
        System.out.println(String.format("  Kategori     : %s", getTipeKendaraan()));
        System.out.println(String.format("  Tarif Sewa   : Rp %,.2f / hari (Exclude Surcharge)", getTarifPerHari()));
        System.out.println(String.format("  Kapasitas    : %d Kursi Penumpang | Bagasi Atas: %s",
                jumlahKursi, (tersediaBagasiAtas ? "Tersedia Roof Rack" : "Internal Saja")));
        System.out.println(String.format("  Hiburan TV   : %s | Izin Dishub: %s",
                (tersediaFasilitasHiburan ? "Karaoke + TV LED" : "Standar Audio"), nomorIzinTrayekPariwisata));
        System.out.println(String.format("  Posisi GPS   : %s (%s)", lokasiTerkiniGPS, koordinatGPS));
        System.out.println(String.format("  Mesin Diesel : %d CC [%s] | Oli: %d%% | Status: %s",
                getMesin().getKapasitasCC(), getMesin().getTipeBahanBakar(),
                getMesin().getIndikatorKesehatanOliPersen(),
                (isStatusTersedia() ? "SIAP DISEWA" : "SEDANG BEROPERASI")));
        System.out.println("  ====================================================");
    }

    @Override
    public String getTipeKendaraan() {
        return "Minibus Komersial / Travel";
    }

    // --- Realisasi Interface DapatDilacak ---

    @Override
    public String getLokasi() {
        return String.format("%s [Koordinat: %s, Status GPS: %s]",
                lokasiTerkiniGPS, koordinatGPS, (statusGPSAktif ? "ONLINE" : "OFFLINE"));
    }

    @Override
    public void perbaruiLokasi(String koordinatBaru, String namaArea) {
        if (koordinatBaru == null || namaArea == null) {
            throw new IllegalArgumentException("Data koordinat dan nama area tidak boleh kosong.");
        }
        this.koordinatGPS = koordinatBaru.trim();
        this.lokasiTerkiniGPS = namaArea.trim();
        System.out.println(String.format("  [GPS UPDATE] Minibus %s kini terpantau di: %s (%s)",
                getNomorPlat(), this.lokasiTerkiniGPS, this.koordinatGPS));
    }

    @Override
    public String getStatusGPS() {
        return statusGPSAktif ? "AKTIF - Terkoneksi 10 Satelit Fleet Tracking" : "NONAKTIF - Sinyal Terputus";
    }

    // --- Realisasi Interface Perawatan ---

    @Override
    public void lakukanServis() {
        System.out.println(String.format("  [SERVIS MINIBUS] Menjalankan SOP Servis Berat Armada Komersial %s (%s %s)...",
                getNomorPlat(), getMerk(), getModel()));
        System.out.println("  -> Penggantian 8 Liter Oli Mesin Diesel Heavy Duty & Filter Solar.");
        System.out.println("  -> Pengecekan Sistem Pneumatik / Booster Rem Angin.");
        System.out.println("  -> Pemeriksaan Suspensi Daun / Per Keong Beban Berat.");
        System.out.println("  -> Uji Emisi Gas Buang & Uji Kelayakan Trayek Dishub.");
        servisMesinKendaraan();
        this.tanggalServisTerakhir = "2026-10-05";
        System.out.println("  [SUKSES] Servis Minibus selesai! Unit dinyatakan lolos inspeksi komersial.");
    }

    @Override
    public boolean cekKelayakanOperasional() {
        return getMesin().getIndikatorKesehatanOliPersen() >= 50 && isStatusTersedia();
    }

    @Override
    public String getJadwalServisBerikutnya() {
        return String.format("Servis berikutnya: Maksimal jarak tempuh %d km atau tanggal 2026-11-30 (Terakhir: %s)",
                getTotalJarakTempuhKm() + 4000, tanggalServisTerakhir);
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("====================================================\\n");
        sb.append("          LEMBAR SPESIFIKASI MINIBUS TRAVEL         \\n");
        sb.append("====================================================\\n");
        sb.append(String.format("Plat Nomor    : %s\\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Kapasitas     : %d Kursi | Izin: %s\\n", jumlahKursi, nomorIzinTrayekPariwisata));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MINIBUS [%s] %s %s - %d Kursi - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), jumlahKursi, getTarifPerHari());
    }
}
"""

# 9. Pelanggan.java
pelanggan_code = """import java.util.regex.Pattern;

/**
 * Concrete Subclass Pelanggan (Turunan dari Person)
 * 
 * Mengimplementasikan abstract method dari Person dan merealisasikan interface Cetakable.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Pelanggan extends Person implements Cetakable {
    private String nomorKTP;
    private double saldoDeposit;
    private int totalTransaksiSewa;
    private String kategoriMember; // "Reguler", "Silver", "Gold", "Platinum"

    private static final Pattern KTP_PATTERN = Pattern.compile("^[0-9]{16}$");

    public Pelanggan(String id, String nama, String nomorTelepon, String alamat, String email,
                     String nomorKTP, double saldoDepositAwal, String kategoriMember) {
        super(id, nama, nomorTelepon, alamat, email);

        if (nomorKTP == null || !KTP_PATTERN.matcher(nomorKTP.trim()).matches()) {
            throw new IllegalArgumentException("Nomor KTP harus terdiri dari tepat 16 digit angka! Input: " + nomorKTP);
        }
        if (saldoDepositAwal < 0) {
            throw new IllegalArgumentException("Saldo deposit awal tidak boleh negatif.");
        }
        if (kategoriMember == null || (!kategoriMember.equalsIgnoreCase("Reguler")
                && !kategoriMember.equalsIgnoreCase("Silver")
                && !kategoriMember.equalsIgnoreCase("Gold")
                && !kategoriMember.equalsIgnoreCase("Platinum"))) {
            throw new IllegalArgumentException("Kategori member harus bernilai 'Reguler', 'Silver', 'Gold', atau 'Platinum'. Input: " + kategoriMember);
        }

        this.nomorKTP = nomorKTP.trim();
        this.saldoDeposit = saldoDepositAwal;
        this.totalTransaksiSewa = 0;
        this.kategoriMember = kategoriMember.substring(0, 1).toUpperCase() + kategoriMember.substring(1).toLowerCase();
    }

    public String getNomorKTP() {
        return nomorKTP;
    }

    public double getSaldoDeposit() {
        return saldoDeposit;
    }

    public int getTotalTransaksiSewa() {
        return totalTransaksiSewa;
    }

    public String getKategoriMember() {
        return kategoriMember;
    }

    public void setKategoriMember(String kategoriMember) {
        if (kategoriMember == null || (!kategoriMember.equalsIgnoreCase("Reguler")
                && !kategoriMember.equalsIgnoreCase("Silver")
                && !kategoriMember.equalsIgnoreCase("Gold")
                && !kategoriMember.equalsIgnoreCase("Platinum"))) {
            throw new IllegalArgumentException("Kategori member tidak valid! Input: " + kategoriMember);
        }
        this.kategoriMember = kategoriMember.substring(0, 1).toUpperCase() + kategoriMember.substring(1).toLowerCase();
    }

    public double getDiskonMemberPersen() {
        switch (kategoriMember.toUpperCase()) {
            case "PLATINUM": return 15.0;
            case "GOLD": return 10.0;
            case "SILVER": return 5.0;
            default: return 0.0;
        }
    }

    // --- Method Overloading Tambah Deposit ---

    public void tambahDeposit(double nominal) {
        if (nominal <= 0) {
            throw new IllegalArgumentException("Nominal penambahan deposit tunai harus positif.");
        }
        this.saldoDeposit += nominal;
        System.out.println(String.format("  [Deposit Tunai] Berhasil top-up Rp %,.2f untuk Pelanggan %s. Total Saldo: Rp %,.2f",
                nominal, getNama(), this.saldoDeposit));
    }

    public void tambahDeposit(double nominal, String metodeTransfer, String referensiTransaksi) {
        if (nominal <= 0) {
            throw new IllegalArgumentException("Nominal deposit non-tunai harus positif.");
        }
        if (metodeTransfer == null || referensiTransaksi == null || referensiTransaksi.trim().isEmpty()) {
            throw new IllegalArgumentException("Metode pembayaran dan nomor referensi transaksi wajib disertakan.");
        }
        this.saldoDeposit += nominal;
        System.out.println(String.format("  [Deposit Digital - %s] Ref: %s | Top-up Rp %,.2f sukses untuk %s. Total Saldo: Rp %,.2f",
                metodeTransfer, referensiTransaksi, nominal, getNama(), this.saldoDeposit));
    }

    public void potongDeposit(double nominal) {
        if (nominal <= 0) {
            throw new IllegalArgumentException("Nominal pemotongan saldo deposit harus positif.");
        }
        if (nominal > this.saldoDeposit) {
            throw new IllegalStateException(String.format("Saldo deposit tidak mencukupi! Tersedia: Rp %,.2f, Dibutuhkan: Rp %,.2f",
                    this.saldoDeposit, nominal));
        }
        this.saldoDeposit -= nominal;
    }

    public void catatTransaksiSukses() {
        this.totalTransaksiSewa++;
        // Upgrade level otomatis berdasarkan akumulasi transaksi
        if (totalTransaksiSewa >= 10 && !kategoriMember.equalsIgnoreCase("Platinum")) {
            this.kategoriMember = "Platinum";
            System.out.println(String.format("  🎉 SELAMAT! Pelanggan %s resmi naik tingkat ke MEMBER PLATINUM!", getNama()));
        } else if (totalTransaksiSewa >= 5 && kategoriMember.equalsIgnoreCase("Reguler")) {
            this.kategoriMember = "Gold";
            System.out.println(String.format("  🎉 SELAMAT! Pelanggan %s resmi naik tingkat ke MEMBER GOLD!", getNama()));
        }
    }

    // --- Implementasi Abstract Methods dari Person ---

    @Override
    public void tampilkanProfil() {
        System.out.println("  =============== PROFIL PELANGGAN ===============");
        System.out.println(String.format("  ID / KTP     : %s / %s", getId(), nomorKTP));
        System.out.println(String.format("  Nama Lengkap : %s", getNama()));
        System.out.println(String.format("  Peran Sistem : %s", getDeskripsiPeran()));
        System.out.println(String.format("  Kontak       : Telp: %s | Email: %s", getNomorTelepon(), getEmail()));
        System.out.println(String.format("  Alamat       : %s", getAlamat()));
        System.out.println(String.format("  Status Member: %s (Diskon Hak: %.1f%%)", kategoriMember, getDiskonMemberPersen()));
        System.out.println(String.format("  Saldo Deposit: Rp %,.2f", saldoDeposit));
        System.out.println(String.format("  Total Sewa   : %d Transaksi Selesai", totalTransaksiSewa));
        System.out.println(String.format("  Reward Poin  : Rp %,.2f (Estimasi Cashback)", hitungKompensasi()));
        System.out.println("  =================================================");
    }

    @Override
    public String getDeskripsiPeran() {
        return "Pelanggan Terdaftar / Penyewa Armada AutoRent";
    }

    @Override
    public double hitungKompensasi() {
        // Pelanggan mendapatkan cashback reward loyalitas: 1.5% dari saldo deposit per kelipatan transaksi
        return (saldoDeposit * 0.015) + (totalTransaksiSewa * 25000.0);
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("====================================================\\n");
        sb.append("             KARTU MEMBER DIGITAL AUTORENT          \\n");
        sb.append("====================================================\\n");
        sb.append(String.format("ID Member     : %s\\n", getId()));
        sb.append(String.format("Nama Lengkap  : %s\\n", getNama()));
        sb.append(String.format("Tingkat Member: %s (Hak Diskon: %.0f%%)\\n", kategoriMember, getDiskonMemberPersen()));
        sb.append(String.format("Saldo Deposit : Rp %,.2f\\n", saldoDeposit));
        sb.append(String.format("Kontak        : %s\\n", getNomorTelepon()));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MEMBER [%s] %s (%s) - Saldo: Rp %,.0f",
                getId(), getNama(), kategoriMember, saldoDeposit);
    }
}
"""

# 10. Pegawai.java
pegawai_code = """/**
 * Concrete Subclass Pegawai (Turunan dari Person)
 * 
 * Mengimplementasikan abstract method dari Person dan merealisasikan interface
 * DapatDilacak dan Cetakable (Interface Realization Lintas Hierarki).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Pegawai extends Person implements DapatDilacak, Cetakable {
    private String nomorIndukKaryawan;
    private String posisiJabatan; // "Front-Office Admin", "Driver Lapangan", "Mekanik Armada", "Supervisor"
    private double gajiPokok;
    private int jumlahTransaksiDitangani;
    private double bonusPerTransaksi;
    private String lokasiTerkiniGPS;
    private String koordinatGPS;
    private boolean statusTugasAktif;

    public Pegawai(String id, String nama, String nomorTelepon, String alamat, String email,
                   String nomorIndukKaryawan, String posisiJabatan, double gajiPokok, double bonusPerTransaksi) {
        super(id, nama, nomorTelepon, alamat, email);

        if (nomorIndukKaryawan == null || nomorIndukKaryawan.trim().isEmpty()) {
            throw new IllegalArgumentException("NIK Pegawai tidak boleh kosong.");
        }
        if (posisiJabatan == null || posisiJabatan.trim().isEmpty()) {
            throw new IllegalArgumentException("Posisi jabatan tidak boleh kosong.");
        }
        if (gajiPokok < 0) {
            throw new IllegalArgumentException("Gaji pokok tidak boleh negatif.");
        }
        if (bonusPerTransaksi < 0) {
            throw new IllegalArgumentException("Bonus per transaksi tidak boleh negatif.");
        }

        this.nomorIndukKaryawan = nomorIndukKaryawan.trim().toUpperCase();
        this.posisiJabatan = posisiJabatan.trim();
        this.gajiPokok = gajiPokok;
        this.jumlahTransaksiDitangani = 0;
        this.bonusPerTransaksi = bonusPerTransaksi;
        this.lokasiTerkiniGPS = "Kantor Pusat Front-Office Sumenep";
        this.koordinatGPS = "-7.0050, 113.8600";
        this.statusTugasAktif = true;
    }

    public String getNomorIndukKaryawan() {
        return nomorIndukKaryawan;
    }

    public String getPosisiJabatan() {
        return posisiJabatan;
    }

    public void setPosisiJabatan(String posisiJabatan) {
        if (posisiJabatan == null || posisiJabatan.trim().isEmpty()) {
            throw new IllegalArgumentException("Posisi jabatan tidak boleh kosong.");
        }
        this.posisiJabatan = posisiJabatan.trim();
    }

    public double getGajiPokok() {
        return gajiPokok;
    }

    public void setGajiPokok(double gajiPokok) {
        if (gajiPokok < 0) {
            throw new IllegalArgumentException("Gaji pokok tidak boleh bernilai negatif.");
        }
        this.gajiPokok = gajiPokok;
    }

    public int getJumlahTransaksiDitangani() {
        return jumlahTransaksiDitangani;
    }

    public double getBonusPerTransaksi() {
        return bonusPerTransaksi;
    }

    // --- Method Overloading Catat Transaksi Ditangani ---

    public void catatTransaksiDitangani() {
        this.jumlahTransaksiDitangani++;
    }

    public void catatTransaksiDitangani(int batchTransaksi) {
        if (batchTransaksi <= 0) {
            throw new IllegalArgumentException("Jumlah batch transaksi minimal 1.");
        }
        this.jumlahTransaksiDitangani += batchTransaksi;
    }

    // --- Implementasi Abstract Methods dari Person ---

    @Override
    public void tampilkanProfil() {
        System.out.println("  ================ PROFIL PEGAWAI ================");
        System.out.println(String.format("  ID / NIK     : %s / %s", getId(), nomorIndukKaryawan));
        System.out.println(String.format("  Nama Lengkap : %s", getNama()));
        System.out.println(String.format("  Jabatan      : %s", posisiJabatan));
        System.out.println(String.format("  Peran Sistem : %s", getDeskripsiPeran()));
        System.out.println(String.format("  Kontak       : Telp: %s | Email: %s", getNomorTelepon(), getEmail()));
        System.out.println(String.format("  Lokasi Tugas : %s (%s)", lokasiTerkiniGPS, koordinatGPS));
        System.out.println(String.format("  Gaji Pokok   : Rp %,.2f", gajiPokok));
        System.out.println(String.format("  Beban Kerja  : %d Transaksi Sukses Ditangani", jumlahTransaksiDitangani));
        System.out.println(String.format("  Total Gaji   : Rp %,.2f (Termasuk Bonus)", hitungKompensasi()));
        System.out.println("  =================================================");
    }

    @Override
    public String getDeskripsiPeran() {
        return "Staf Operasional & Layanan Pelanggan AutoRent System";
    }

    @Override
    public double hitungKompensasi() {
        // Total penerimaan gaji = Gaji Pokok + (Transaksi ditangani * bonus)
        return gajiPokok + (jumlahTransaksiDitangani * bonusPerTransaksi);
    }

    // --- Realisasi Interface DapatDilacak ---

    @Override
    public String getLokasi() {
        return String.format("%s [Koordinat: %s, Status: %s]",
                lokasiTerkiniGPS, koordinatGPS, (statusTugasAktif ? "ON DUTY" : "OFF DUTY"));
    }

    @Override
    public void perbaruiLokasi(String koordinatBaru, String namaArea) {
        if (koordinatBaru == null || namaArea == null) {
            throw new IllegalArgumentException("Data koordinat dan nama area tugas tidak boleh kosong.");
        }
        this.koordinatGPS = koordinatBaru.trim();
        this.lokasiTerkiniGPS = namaArea.trim();
        System.out.println(String.format("  [PETUGAS GPS] Pegawai %s (%s) kini berada di: %s (%s)",
                getNama(), posisiJabatan, this.lokasiTerkiniGPS, this.koordinatGPS));
    }

    @Override
    public String getStatusGPS() {
        return statusTugasAktif ? "AKTIF - Terhubung Smart Tracker Petugas" : "NONAKTIF - Istirahat / Selesai Shift";
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("====================================================\\n");
        sb.append("             SLIP KOMPENSASI & GAJI PEGAWAI         \\n");
        sb.append("====================================================\\n");
        sb.append(String.format("NIK / ID      : %s / %s\\n", nomorIndukKaryawan, getId()));
        sb.append(String.format("Nama Pegawai  : %s\\n", getNama()));
        sb.append(String.format("Jabatan       : %s\\n", posisiJabatan));
        sb.append(String.format("Gaji Pokok    : Rp %,.2f\\n", gajiPokok));
        sb.append(String.format("Bonus Transaksi: Rp %,.2f (%d transaksi)\\n",
                jumlahTransaksiDitangani * bonusPerTransaksi, jumlahTransaksiDitangani));
        sb.append(String.format("TOTAL GAJI    : Rp %,.2f\\n", hitungKompensasi()));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("PEGAWAI [%s] %s (%s) - Total Gaji: Rp %,.0f",
                nomorIndukKaryawan, getNama(), posisiJabatan, hitungKompensasi());
    }
}
"""

# 11. Mesin.java
mesin_code = """/**
 * Class Mesin (Komponen Komposisi Kendaraan)
 * 
 * Merepresentasikan spesifikasi mekanikal dan status kesehatan mesin internal.
 * Memiliki relasi keterikatan siklus hidup yang kuat (Composition) dengan Kendaraan.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Mesin {
    private String nomorRangkaMesin;
    private int kapasitasCC;
    private String tipeBahanBakar;
    private boolean statusMesinMenyala;
    private int indikatorKesehatanOliPersen;

    public Mesin(String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar) {
        if (nomorRangkaMesin == null || nomorRangkaMesin.trim().isEmpty()) {
            throw new IllegalArgumentException("Nomor rangka mesin tidak boleh kosong.");
        }
        if (kapasitasCC < 50 || kapasitasCC > 10000) {
            throw new IllegalArgumentException("Kapasitas CC mesin tidak valid (50 - 10000 CC). Input: " + kapasitasCC);
        }
        if (tipeBahanBakar == null || tipeBahanBakar.trim().isEmpty()) {
            throw new IllegalArgumentException("Tipe bahan bakar tidak boleh kosong.");
        }

        this.nomorRangkaMesin = nomorRangkaMesin.trim().toUpperCase();
        this.kapasitasCC = kapasitasCC;
        this.tipeBahanBakar = tipeBahanBakar.trim();
        this.statusMesinMenyala = false;
        this.indikatorKesehatanOliPersen = 100;
    }

    public String getNomorRangkaMesin() {
        return nomorRangkaMesin;
    }

    public int getKapasitasCC() {
        return kapasitasCC;
    }

    public String getTipeBahanBakar() {
        return tipeBahanBakar;
    }

    public boolean isStatusMesinMenyala() {
        return statusMesinMenyala;
    }

    public int getIndikatorKesehatanOliPersen() {
        return indikatorKesehatanOliPersen;
    }

    public void nyalakanMesin() {
        this.statusMesinMenyala = true;
    }

    public void matikanMesin() {
        this.statusMesinMenyala = false;
    }

    public void gantiOliMesin() {
        this.indikatorKesehatanOliPersen = 100;
    }

    public void kurangiKesehatanOli(int km) {
        int penurunan = km / 100;
        this.indikatorKesehatanOliPersen = Math.max(5, this.indikatorKesehatanOliPersen - penurunan);
    }

    public String cekStatusMesin() {
        return String.format("Mesin %s (%d CC %s) | Status: %s | Kondisi Oli: %d%%",
                nomorRangkaMesin, kapasitasCC, tipeBahanBakar,
                (statusMesinMenyala ? "MENYALA" : "STANDBY"), indikatorKesehatanOliPersen);
    }
}
"""

# 12. DetailItemBiaya.java
detail_item_code = """/**
 * Class DetailItemBiaya (Komponen Komposisi Transaksi)
 * 
 * Merepresentasikan baris rincian komponen biaya dalam invoice / kuitansi transaksi.
 * Memiliki relasi Composition dengan TransaksiSewa.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class DetailItemBiaya {
    private String namaItem;
    private int jumlahQty;
    private double hargaSatuan;
    private double subtotalBiaya;

    public DetailItemBiaya(String namaItem, int jumlahQty, double hargaSatuan) {
        if (namaItem == null || namaItem.trim().isEmpty()) {
            throw new IllegalArgumentException("Nama item biaya tidak boleh kosong.");
        }
        if (jumlahQty <= 0) {
            throw new IllegalArgumentException("Kuantitas item biaya minimal 1.");
        }

        this.namaItem = namaItem.trim();
        this.jumlahQty = jumlahQty;
        this.hargaSatuan = hargaSatuan;
        this.subtotalBiaya = jumlahQty * hargaSatuan;
    }

    public String getNamaItem() {
        return namaItem;
    }

    public int getJumlahQty() {
        return jumlahQty;
    }

    public double getHargaSatuan() {
        return hargaSatuan;
    }

    public double getSubtotalBiaya() {
        return subtotalBiaya;
    }

    public String formatItemBiaya() {
        if (subtotalBiaya < 0) {
            return String.format("  - %-30s x %-2d @ -Rp %,10.2f = -Rp %,11.2f",
                    namaItem, jumlahQty, Math.abs(hargaSatuan), Math.abs(subtotalBiaya));
        }
        return String.format("  - %-30s x %-2d @ Rp %,11.2f = Rp %,12.2f",
                namaItem, jumlahQty, hargaSatuan, subtotalBiaya);
    }
}
"""

# 13. GarasiArmada.java
garasi_code = """import java.util.ArrayList;
import java.util.List;

/**
 * Class GarasiArmada (Agregasi Polimorfis Pool Kendaraan)
 * 
 * Mengelola koleksi heterogen armada kendaraan sewa berbasis tipe abstraksi Kendaraan.
 * Mengimplementasikan method overloading untuk pencarian armada yang fleksibel
 * serta eksekusi polimorfisme massal untuk pemeliharaan (Perawatan) dan telematika (DapatDilacak).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class GarasiArmada {
    private String namaGarasi;
    private String lokasiGarasi;
    private int kapasitasMaksimal;
    private ArrayList<Kendaraan> daftarArmada; // Agregasi Polimorfis

    public GarasiArmada(String namaGarasi, String lokasiGarasi, int kapasitasMaksimal) {
        if (namaGarasi == null || namaGarasi.trim().isEmpty()) {
            throw new IllegalArgumentException("Nama garasi tidak boleh kosong.");
        }
        if (lokasiGarasi == null || lokasiGarasi.trim().isEmpty()) {
            throw new IllegalArgumentException("Lokasi garasi tidak boleh kosong.");
        }
        if (kapasitasMaksimal <= 0) {
            throw new IllegalArgumentException("Kapasitas maksimal garasi harus positif.");
        }

        this.namaGarasi = namaGarasi.trim();
        this.lokasiGarasi = lokasiGarasi.trim();
        this.kapasitasMaksimal = kapasitasMaksimal;
        this.daftarArmada = new ArrayList<>();
    }

    public String getNamaGarasi() {
        return namaGarasi;
    }

    public String getLokasiGarasi() {
        return lokasiGarasi;
    }

    public int getKapasitasMaksimal() {
        return kapasitasMaksimal;
    }

    public ArrayList<Kendaraan> getDaftarArmada() {
        return daftarArmada;
    }

    public int getJumlahArmadaTersimpan() {
        return daftarArmada.size();
    }

    public void tambahKendaraan(Kendaraan kendaraan) {
        if (kendaraan == null) {
            throw new IllegalArgumentException("Objek kendaraan tidak boleh null.");
        }
        if (daftarArmada.size() >= kapasitasMaksimal) {
            throw new IllegalStateException("Garasi penuh! Tidak dapat menampung unit armada baru.");
        }
        for (Kendaraan k : daftarArmada) {
            if (k.getNomorPlat().equalsIgnoreCase(kendaraan.getNomorPlat())) {
                throw new IllegalArgumentException("Kendaraan dengan plat " + kendaraan.getNomorPlat() + " sudah terdaftar di garasi ini.");
            }
        }
        this.daftarArmada.add(kendaraan);
        System.out.println(String.format("  [GARASI ARMADA] Berhasil menambahkan %s [%s] ke %s.",
                kendaraan.getTipeKendaraan(), kendaraan.getNomorPlat(), this.namaGarasi));
    }

    public boolean hapusKendaraan(String nomorPlat) {
        if (nomorPlat == null) return false;
        return daftarArmada.removeIf(k -> k.getNomorPlat().equalsIgnoreCase(nomorPlat.trim()));
    }

    // --- Dynamic Binding / Polymorphic Display ---

    public void tampilkanSeluruhArmada() {
        System.out.println(String.format("\\n  === DAFTAR POOL ARMADA [%s - %s] (%d/%d Unit) ===",
                namaGarasi, lokasiGarasi, daftarArmada.size(), kapasitasMaksimal));
        if (daftarArmada.isEmpty()) {
            System.out.println("  (Garasi masih kosong)");
            return;
        }
        for (int i = 0; i < daftarArmada.size(); i++) {
            Kendaraan k = daftarArmada.get(i);
            System.out.println(String.format("  [%d] Tipe: %s", (i + 1), k.getTipeKendaraan()));
            k.tampilkanSpesifikasi(); // Dynamic Method Dispatch
        }
    }

    // --- Method Overloading Pencarian Armada ---

    public Kendaraan cariKendaraan(String nomorPlat) {
        if (nomorPlat == null || nomorPlat.trim().isEmpty()) {
            throw new IllegalArgumentException("Nomor plat pencarian tidak boleh kosong.");
        }
        for (Kendaraan k : daftarArmada) {
            if (k.getNomorPlat().equalsIgnoreCase(nomorPlat.trim())) {
                return k;
            }
        }
        return null;
    }

    public List<Kendaraan> cariKendaraan(String merk, String model) {
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.getMerk().equalsIgnoreCase(merk.trim()) && k.getModel().equalsIgnoreCase(model.trim())) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    public List<Kendaraan> cariKendaraan(double maxTarifPerHari) {
        if (maxTarifPerHari <= 0) {
            throw new IllegalArgumentException("Batas tarif pencarian harus positif.");
        }
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.getTarifPerHari() <= maxTarifPerHari) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    public List<Kendaraan> cariKendaraan(boolean statusTersedia) {
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.isStatusTersedia() == statusTersedia) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    // --- Interface Polymorphism Batch Processing ---

    /**
     * Menjalankan prosedur servis massal memanfaatkan interface Perawatan.
     */
    public void lakukanServisMasal() {
        System.out.println(String.format("\\n  === PROGRAM SERVIS PREVENTIF MASSAL GARASI [%s] ===", namaGarasi));
        int unitDiservis = 0;
        for (Kendaraan k : daftarArmada) {
            if (k instanceof Perawatan) {
                Perawatan p = (Perawatan) k;
                if (!p.cekKelayakanOperasional() || k.getMesin().getIndikatorKesehatanOliPersen() < 80) {
                    System.out.println(String.format("  -> Memproses Pemeliharaan Unit: %s [%s]", k.getMerk(), k.getNomorPlat()));
                    p.lakukanServis(); // Interface Dynamic Dispatch
                    unitDiservis++;
                }
            }
        }
        System.out.println(String.format("  [HASIL] Selesai melakukan servis preventif pada %d unit armada.\\n", unitDiservis));
    }

    /**
     * Memantau posisi seluruh armada memanfaatkan interface DapatDilacak.
     */
    public void pantauSeluruhPelacakGPS() {
        System.out.println(String.format("\\n  === MONITORING FLEET TELEMATICS GPS [%s] ===", namaGarasi));
        for (Kendaraan k : daftarArmada) {
            if (k instanceof DapatDilacak) {
                DapatDilacak pelacak = (DapatDilacak) k;
                System.out.println(String.format("  • [%s] %-15s : %s",
                        k.getNomorPlat(), k.getModel(), pelacak.getLokasi()));
            }
        }
    }

    public double hitungTotalNilaiArmada() {
        double total = 0;
        for (Kendaraan k : daftarArmada) {
            total += (k.getTarifPerHari() * 30.0); // Estimasi valuasi kapasitas sewa bulanan
        }
        return total;
    }
}
"""

# 14. TransaksiSewa.java
transaksi_code = """import java.util.ArrayList;

/**
 * Class TransaksiSewa (Sentral Orkestrasi Relasi & Eksekusi Polimorfisme)
 * 
 * Mengaitkan Pelanggan (Association), Pegawai (Association), Kendaraan (Polymorphic Association),
 * dan memiliki DetailItemBiaya (Composition).
 * Merealisasikan interface Cetakable untuk standarisasi format kuitansi resmi.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class TransaksiSewa implements Cetakable {
    private String kodeTransaksi;
    private Pelanggan pelanggan;
    private Pegawai pegawaiPetugas;
    private Kendaraan kendaraanDisewa; // Polymorphic Superclass Reference
    private int durasiHari;
    private double totalBiayaSewa;
    private double nominalDibayar;
    private boolean statusLunas;
    private boolean statusSelesai;
    private ArrayList<DetailItemBiaya> rincianBiaya; // Komposisi ketat

    public TransaksiSewa(String kodeTransaksi, Pelanggan pelanggan, Pegawai pegawaiPetugas,
                         Kendaraan kendaraanDisewa, int durasiHari) {
        if (kodeTransaksi == null || kodeTransaksi.trim().isEmpty()) {
            throw new IllegalArgumentException("Kode transaksi tidak boleh kosong.");
        }
        if (pelanggan == null) {
            throw new IllegalArgumentException("Pelanggan tidak boleh null.");
        }
        if (pegawaiPetugas == null) {
            throw new IllegalArgumentException("Pegawai petugas tidak boleh null.");
        }
        if (kendaraanDisewa == null) {
            throw new IllegalArgumentException("Kendaraan disewa tidak boleh null.");
        }
        if (!kendaraanDisewa.isStatusTersedia()) {
            throw new IllegalStateException("Kendaraan dengan plat " + kendaraanDisewa.getNomorPlat() + " sedang tidak tersedia untuk disewa.");
        }
        if (durasiHari <= 0) {
            throw new IllegalArgumentException("Durasi sewa minimal 1 hari.");
        }

        this.kodeTransaksi = kodeTransaksi.trim().toUpperCase();
        this.pelanggan = pelanggan;
        this.pegawaiPetugas = pegawaiPetugas;
        this.kendaraanDisewa = kendaraanDisewa;
        this.durasiHari = durasiHari;
        this.nominalDibayar = 0.0;
        this.statusLunas = false;
        this.statusSelesai = false;
        this.rincianBiaya = new ArrayList<>();

        // Hitung rincian biaya awal secara polimorfis
        kalkulasiKomponenBiayaAwal();
    }

    private void kalkulasiKomponenBiayaAwal() {
        this.rincianBiaya.clear();

        // 1. Biaya sewa dasar kendaraan (Dynamic Dispatch ke subclass terkait)
        double biayaDasar = kendaraanDisewa.hitungEstimasiBiaya(durasiHari);
        rincianBiaya.add(new DetailItemBiaya("Sewa " + kendaraanDisewa.getTipeKendaraan() + " (" + kendaraanDisewa.getModel() + ")",
                durasiHari, biayaDasar / durasiHari));

        // 2. Diskon Hak Member Pelanggan
        double diskonMemberPersen = pelanggan.getDiskonMemberPersen();
        if (diskonMemberPersen > 0) {
            double nominalDiskon = -(biayaDasar * (diskonMemberPersen / 100.0));
            rincianBiaya.add(new DetailItemBiaya("Diskon Member " + pelanggan.getKategoriMember() + " (" + diskonMemberPersen + "%)",
                    1, nominalDiskon));
        }

        // 3. Biaya Administrasi & Asuransi Standar
        rincianBiaya.add(new DetailItemBiaya("Administrasi & Asuransi All-Risk", 1, 35000.0));

        // Rekalkulasi Total Final
        this.totalBiayaSewa = 0.0;
        for (DetailItemBiaya item : rincianBiaya) {
            this.totalBiayaSewa += item.getSubtotalBiaya();
        }
    }

    public String getKodeTransaksi() {
        return kodeTransaksi;
    }

    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public Pegawai getPegawaiPetugas() {
        return pegawaiPetugas;
    }

    public Kendaraan getKendaraanDisewa() {
        return kendaraanDisewa;
    }

    public int getDurasiHari() {
        return durasiHari;
    }

    public double getTotalBiayaSewa() {
        return totalBiayaSewa;
    }

    public double getNominalDibayar() {
        return nominalDibayar;
    }

    public boolean isStatusLunas() {
        return statusLunas;
    }

    public boolean isStatusSelesai() {
        return statusSelesai;
    }

    public ArrayList<DetailItemBiaya> getRincianBiaya() {
        return rincianBiaya;
    }

    // --- Method Overloading Pembayaran ---

    public void prosesPembayaran(double nominalCash) {
        if (nominalCash <= 0) {
            throw new IllegalArgumentException("Nominal pembayaran cash harus positif.");
        }
        if (statusLunas) {
            throw new IllegalStateException("Transaksi " + kodeTransaksi + " sudah berstatus lunas.");
        }

        this.nominalDibayar += nominalCash;
        if (this.nominalDibayar >= this.totalBiayaSewa) {
            this.statusLunas = true;
            this.kendaraanDisewa.setStatusKetersediaan(false);
            this.pegawaiPetugas.catatTransaksiDitangani();
            double kembalian = this.nominalDibayar - this.totalBiayaSewa;
            System.out.println(String.format("  [BAYAR TUNAI] Transaksi %s LUNAS. Total: Rp %,.2f | Bayar: Rp %,.2f | Kembalian: Rp %,.2f",
                    kodeTransaksi, totalBiayaSewa, nominalDibayar, kembalian));
        } else {
            System.out.println(String.format("  [BAYAR TUNAI - DP] Transaksi %s Terbayar Rp %,.2f (Kurang: Rp %,.2f)",
                    kodeTransaksi, nominalDibayar, (totalBiayaSewa - nominalDibayar)));
        }
    }

    public void prosesPembayaran(double nominal, String metodeDigital, String refTransaksi) {
        if (nominal <= 0) {
            throw new IllegalArgumentException("Nominal pembayaran non-tunai harus positif.");
        }
        if (metodeDigital == null || refTransaksi == null || refTransaksi.trim().isEmpty()) {
            throw new IllegalArgumentException("Metode digital dan referensi transaksi wajib disertakan.");
        }
        if (statusLunas) {
            throw new IllegalStateException("Transaksi " + kodeTransaksi + " sudah berstatus lunas.");
        }

        this.nominalDibayar += nominal;
        if (this.nominalDibayar >= this.totalBiayaSewa) {
            this.statusLunas = true;
            this.kendaraanDisewa.setStatusKetersediaan(false);
            this.pegawaiPetugas.catatTransaksiDitangani();
            System.out.println(String.format("  [BAYAR DIGITAL - %s] Ref: %s | Transaksi %s LUNAS! Total: Rp %,.2f",
                    metodeDigital, refTransaksi, kodeTransaksi, totalBiayaSewa));
        } else {
            System.out.println(String.format("  [BAYAR DIGITAL - %s] Ref: %s | Terbayar Rp %,.2f (Sisa: Rp %,.2f)",
                    metodeDigital, refTransaksi, nominalDibayar, (totalBiayaSewa - nominalDibayar)));
        }
    }

    public void selesaikanTransaksi(int kmPemakaian, int keterlambatanHari) {
        if (!statusLunas) {
            throw new IllegalStateException("Transaksi tidak dapat diselesaikan karena belum lunas.");
        }
        if (statusSelesai) {
            throw new IllegalStateException("Transaksi sudah diselesaikan sebelumnya.");
        }
        if (keterlambatanHari < 0) {
            throw new IllegalArgumentException("Keterlambatan hari tidak boleh bernilai negatif.");
        }

        if (keterlambatanHari > 0) {
            double tarifDendaPerHari = kendaraanDisewa.getTarifPerHari() * 1.5;
            double dendaTotal = tarifDendaPerHari * keterlambatanHari;
            rincianBiaya.add(new DetailItemBiaya("Denda Keterlambatan (" + keterlambatanHari + " Hari)",
                    keterlambatanHari, tarifDendaPerHari));
            this.totalBiayaSewa += dendaTotal;
            System.out.println(String.format("  [DENDA KETERLAMBATAN] Terlambat %d hari. Denda tambahan: Rp %,.2f",
                    keterlambatanHari, dendaTotal));
        }

        this.kendaraanDisewa.catatPenyewaan(kmPemakaian);
        this.kendaraanDisewa.selesaikanPenyewaan();
        this.pelanggan.catatTransaksiSukses();
        this.statusSelesai = true;

        System.out.println(String.format("  [PENGEMBALIAN SUKSES] Armada %s [%s] telah dikembalikan ke pool garasi. Status: READY.",
                kendaraanDisewa.getModel(), kendaraanDisewa.getNomorPlat()));
    }

    // --- Realisasi Interface Cetakable ---

    @Override
    public String formatCetakDokumen() {
        StringBuilder sb = new StringBuilder();
        sb.append("================================================================\\n");
        sb.append("                  AUTORENT SYSTEM - RESMI                       \\n");
        sb.append("               BUKTI KUITANSI TRANSAKSI SEWA                    \\n");
        sb.append("================================================================\\n");
        sb.append(String.format("Kode Transaksi  : %-20s Status: %s\\n", kodeTransaksi, (statusLunas ? "LUNAS" : "BELUM LUNAS")));
        sb.append(String.format("Pelanggan       : %s (ID: %s | Member: %s)\\n",
                pelanggan.getNama(), pelanggan.getId(), pelanggan.getKategoriMember()));
        sb.append(String.format("Petugas CS      : %s (NIK: %s)\\n",
                pegawaiPetugas.getNama(), pegawaiPetugas.getNomorIndukKaryawan()));
        sb.append(String.format("Unit Armada     : %s [%s] - %s\\n",
                kendaraanDisewa.getModel(), kendaraanDisewa.getNomorPlat(), kendaraanDisewa.getTipeKendaraan()));
        sb.append(String.format("Durasi Sewa     : %d Hari\\n", durasiHari));
        sb.append("----------------------------------------------------------------\\n");
        sb.append("RINCIAN BIAYA :\\n");
        for (DetailItemBiaya item : rincianBiaya) {
            sb.append(item.formatItemBiaya()).append("\\n");
        }
        sb.append("----------------------------------------------------------------\\n");
        sb.append(String.format("TOTAL TAGIHAN   : Rp %,15.2f\\n", totalBiayaSewa));
        sb.append(String.format("TOTAL DIBAYAR   : Rp %,15.2f\\n", nominalDibayar));
        sb.append(String.format("STATUS SELESAI  : %s\\n", (statusSelesai ? "SELESAI / UNIT KEMBALI" : "AKTIF DALAM MASA SEWA")));
        sb.append("================================================================\\n");
        sb.append("    Terima kasih telah mempercayakan perjalanan Anda bersama    \\n");
        sb.append("                     AutoRent PENS Sumenep                      \\n");
        sb.append("================================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("TRX [%s] %s -> %s (%s) - Total: Rp %,.0f | Status: %s",
                kodeTransaksi, pelanggan.getNama(), kendaraanDisewa.getModel(),
                kendaraanDisewa.getNomorPlat(), totalBiayaSewa, (statusLunas ? "LUNAS" : "PENDING"));
    }
}
"""

# 15. KuitansiPrinter.java
kuitansi_code = """/**
 * Class KuitansiPrinter (Service Utility Dependency & Interface Consumer)
 * 
 * Bertanggung jawab mencetak kuitansi transaksi dan mencetak entitas apa pun
 * yang merealisasikan interface Cetakable (Interface-Based Polymorphic Printing).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class KuitansiPrinter {
    private String namaPercetakan;
    private String nomorIzin;

    public KuitansiPrinter(String namaPercetakan, String nomorIzin) {
        this.namaPercetakan = namaPercetakan;
        this.nomorIzin = nomorIzin;
    }

    public void cetakKuitansiTransaksi(TransaksiSewa transaksi) {
        if (transaksi == null) {
            System.out.println("  [ERROR] Objek transaksi sewa tidak valid!");
            return;
        }
        System.out.println(transaksi.formatCetakDokumen());
    }

    /**
     * Membuktikan pemanggilan polimorfisme berbasis interface Cetakable.
     * Dapat mencetak TransaksiSewa, Pelanggan (Kartu Member), Pegawai (Slip Gaji),
     * maupun Kendaraan (Lembar Spesifikasi).
     * 
     * @param dokumen Objek implementor interface Cetakable
     */
    public void cetakDokumenResmi(Cetakable dokumen) {
        if (dokumen == null) {
            System.out.println("  [ERROR] Dokumen cetakable tidak boleh null!");
            return;
        }
        System.out.println(String.format("  [PRINTER UTILITY: %s (Izin: %s)]", namaPercetakan, nomorIzin));
        System.out.println(dokumen.formatCetakDokumen());
        System.out.println();
    }
}
"""

# 16. LayananNotifikasi.java
notifikasi_code = """/**
 * Class LayananNotifikasi (Service Gateway Dependency)
 * 
 * Bertanggung jawab mengirimkan notifikasi multi-kanal (SMS, WhatsApp, Email)
 * kepada entitas Person secara polimorfis, serta mengirimkan telemetry alert ke objek DapatDilacak.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class LayananNotifikasi {
    private String namaProviderGateway;

    public LayananNotifikasi(String namaProviderGateway) {
        this.namaProviderGateway = namaProviderGateway;
    }

    public void kirimNotifikasiSewa(Person penerima, String pesan) {
        if (penerima == null) return;
        System.out.println(String.format("  [NOTIFIKASI GATEWAY - %s] Dikirim ke %s (%s - %s) -> \\"%s\\"",
                namaProviderGateway, penerima.getNama(), penerima.getNomorTelepon(), penerima.getEmail(), pesan));
    }

    public void kirimNotifikasiServis(Person penanggungJawab, String platKendaraan, String statusServis) {
        if (penanggungJawab == null) return;
        System.out.println(String.format("  [MAINTENANCE ALERT] Ke Staf %s [%s] -> Armada %s : %s",
                penanggungJawab.getNama(), penanggungJawab.getNomorTelepon(), platKendaraan, statusServis));
    }

    public void kirimPeringatanGPS(DapatDilacak target, String pesanPeringatan) {
        if (target == null) return;
        System.out.println(String.format("  [GPS TELEMATICS ALERT via %s] Lokasi: %s | Peringatan: %s",
                namaProviderGateway, target.getLokasi(), pesanPeringatan));
    }
}
"""

# 17. Main.java
main_code = """import java.util.ArrayList;
import java.util.List;

/**
 * Driver & Test Suite Utama (Main.java)
 * 
 * Menguji dan mendemonstrasikan secara komprehensif seluruh capaian pembelajaran Modul 7:
 * 1. Audit & Pembuktian Larangan Instansiasi Abstract Class (Kendaraan & Person).
 * 2. Instansiasi Sukses Subclass Konkret (Mobil, Motor, Minibus, Pelanggan, Pegawai).
 * 3. Dynamic Method Dispatch via Superclass Abstract Reference (Abstract Method Polymorphism).
 * 4. Interface Polymorphism (DapatDilacak, Perawatan, Cetakable) lintas hierarki.
 * 5. Heterogeneous Collection Processing (Array & ArrayList polimorfis superclass & interface).
 * 6. Method Overloading & Defensive Programming Verification.
 * 7. End-to-End Business Integration (Agregasi Garasi, Transaksi, Komposisi Mesin, Dependency).
 * 8. Evaluasi Definition of Done & Sprint 7 Completion.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Main {

    public static void main(String[] args) {
        cetakHeaderUtama();

        // =========================================================================
        // FASE 1: AUDIT & PEMBUKTIAN LARANGAN INSTANSIASI ABSTRACT CLASS
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 1: AUDIT & PEMBUKTIAN LARANGAN INSTANSIASI ABSTRACT CLASS               |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Pada Modul 7, superclass Kendaraan dan Person dideklarasikan sebagai 'abstract'.");
        System.out.println("  Artinya, kode berikut TIDAK BOLEH dikompilasi oleh Java Compiler:");
        System.out.println("    // Kendaraan k = new Kendaraan(...); // COMPILE ERROR: Kendaraan is abstract");
        System.out.println("    // Person p = new Person(...);       // COMPILE ERROR: Person is abstract");
        System.out.println("  [VERIFIKASI DESAIN] Abstraction menjamin entitas umum tidak dapat diinstansiasi langsung.");
        System.out.println("  Hanya subclass konkrit yang dapat diinstansiasi di Heap Memory.\\n");

        // =========================================================================
        // FASE 2: INSTANSIASI OBJEK SUBCLASS KONKRET
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 2: INSTANSIASI SUBCLASS KONKRET & VALIDASI KONSTRUKTOR DEFENSIVE        |");
        System.out.println("+------------------------------------------------------------------------------+");

        // Subclass Kendaraan
        Mobil mobilAvanza = new Mobil("M 1001 HA", "Toyota", "Avanza Veloz", 2023, 400000.0,
                "ENG-TOY-AVZ-001", 1500, "Bensin Pertamax", "Automatic", 7, true);

        Motor motorNmax = new Motor("M 2002 HB", "Yamaha", "NMAX 155 Connected", 2024, 150000.0,
                "ENG-YAM-NMX-002", 155, "Bensin Pertamax", "Matic", 2, true);

        Minibus minibusHiace = new Minibus("M 3003 HC", "Toyota", "HiAce Premio Luxury", 2023, 1100000.0,
                "ENG-TOY-HIC-003", 2800, "Diesel Dexlite", 14, true, true, "TRAYEK-PARIWISATA-JATIM-9988");

        // Subclass Person
        Pelanggan pelangganBudi = new Pelanggan("PLG-001", "Budi Pratama", "081234567890",
                "Jl. Trunojoyo No. 45, Sumenep", "budi.pratama@gmail.com",
                "3529012345670001", 500000.0, "Gold");

        Pegawai pegawaiSiti = new Pegawai("PGW-101", "Siti Aminah", "081987654321",
                "Jl. KH. Agus Salim No. 12, Sumenep", "siti.aminah@autorent.com",
                "NIK-2026-004", "Front-Office CS & Fleet Officer", 3500000.0, 50000.0);

        System.out.println("  [OK] Berhasil menginstansiasi objek Mobil    : " + mobilAvanza.getModel() + " [" + mobilAvanza.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Motor    : " + motorNmax.getModel() + " [" + motorNmax.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Minibus  : " + minibusHiace.getModel() + " [" + minibusHiace.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Pelanggan: " + pelangganBudi.getNama() + " [" + pelangganBudi.getId() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Pegawai  : " + pegawaiSiti.getNama() + " [" + pegawaiSiti.getNomorIndukKaryawan() + "]\\n");

        // =========================================================================
        // FASE 3: POLYMORPHISM VIA SUPERCLASS ABSTRACT REFERENCE (DYNAMIC METHOD DISPATCH)
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 3: PENGUJIAN POLYMORPHISM VIA SUPERCLASS ABSTRACT REFERENCE             |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Memanggil abstract method melalui reference Superclass Abstract (Upcasting):\\n");

        // Polymorphic reference Kendaraan
        Kendaraan refK1 = mobilAvanza;
        Kendaraan refK2 = motorNmax;
        Kendaraan refK3 = minibusHiace;

        System.out.println("  >>> [1] Pemanggilan refK1.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Mobil):");
        refK1.tampilkanSpesifikasi();

        System.out.println("  >>> [2] Pemanggilan refK2.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Motor):");
        refK2.tampilkanSpesifikasi();

        System.out.println("  >>> [3] Pemanggilan refK3.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Minibus):");
        refK3.tampilkanSpesifikasi();

        System.out.println("  >>> [4] Pemanggilan Abstract Method hitungEstimasiBiaya(5 hari) secara Polimorfis:");
        System.out.println(String.format("      * Estimasi Mobil 5 Hari   : Rp %,.2f (Diskon Durasi 5%%)", refK1.hitungEstimasiBiaya(5)));
        System.out.println(String.format("      * Estimasi Motor 5 Hari   : Rp %,.2f (Diskon Hemat 6%%)", refK2.hitungEstimasiBiaya(5)));
        System.out.println(String.format("      * Estimasi Minibus 5 Hari : Rp %,.2f (Termasuk Surcharge Komersial)", refK3.hitungEstimasiBiaya(5)));

        System.out.println("\\n  >>> [5] Pemanggilan Abstract Method Person via Polymorphic Reference:");
        Person refP1 = pelangganBudi;
        Person refP2 = pegawaiSiti;

        System.out.println("  [Profil via Person Ref 1]");
        refP1.tampilkanProfil();
        System.out.println("  [Profil via Person Ref 2]");
        refP2.tampilkanProfil();
        System.out.println();

        // =========================================================================
        // FASE 4: INTERFACE POLYMORPHISM LINTAS HIERARKI KELAS
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 4: PENGUJIAN INTERFACE POLYMORPHISM (LINTAS HIERARKI CLASS)             |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Interface DapatDilacak direalisasikan oleh Mobil, Motor, Minibus, dan Pegawai!\\n");

        DapatDilacak[] daftarPelacak = new DapatDilacak[] {
                mobilAvanza,
                motorNmax,
                minibusHiace,
                pegawaiSiti // Lintas hierarki (Pegawai adalah turunan Person, bukan Kendaraan!)
        };

        for (int i = 0; i < daftarPelacak.length; i++) {
            DapatDilacak item = daftarPelacak[i];
            System.out.println(String.format("  * Pelacak [%d] Lokasi     : %s", (i + 1), item.getLokasi()));
            System.out.println(String.format("               Status GPS : %s", item.getStatusGPS()));
            System.out.println(String.format("               Ping Res   : %s", item.kirimSinyalPingTelematika()));
        }

        System.out.println("\\n  Memperbarui lokasi objek secara dinamis via Interface:");
        daftarPelacak[0].perbaruiLokasi("-7.0100, 113.8700", "Pelabuhan Kalianget Sumenep");
        daftarPelacak[3].perbaruiLokasi("-7.0120, 113.8680", "Pos Layanan Pelabuhan Kalianget");

        System.out.println("\\n  >>> Pengujian Interface Perawatan pada Seluruh Kendaraan:");
        Perawatan[] armadaPerawatan = new Perawatan[] { mobilAvanza, motorNmax, minibusHiace };
        for (Perawatan armada : armadaPerawatan) {
            System.out.println("  * Kelayakan Operasional: " + (armada.cekKelayakanOperasional() ? "LAYAK JALAN" : "PERLU SERVIS"));
            System.out.println("    " + armada.getJadwalServisBerikutnya());
        }
        System.out.println();

        // =========================================================================
        // FASE 5: HETEROGENEOUS POLYMORPHIC COLLECTIONS (ARRAY & ARRAYLIST)
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 5: HETEROGENEOUS POLYMORPHIC COLLECTIONS (ARRAY & ARRAYLIST)             |");
        System.out.println("+------------------------------------------------------------------------------+");

        List<Cetakable> daftarDokumenCetak = new ArrayList<>();
        daftarDokumenCetak.add(mobilAvanza);
        daftarDokumenCetak.add(motorNmax);
        daftarDokumenCetak.add(pelangganBudi);
        daftarDokumenCetak.add(pegawaiSiti);

        System.out.println("  Iterasi Heterogeneous List<Cetakable> (Koleksi Beragam Tipe Objek):");
        for (Cetakable dok : daftarDokumenCetak) {
            System.out.println("  -> Ringkasan: " + dok.generateRingkasan());
        }
        System.out.println();

        // =========================================================================
        // FASE 6: METHOD OVERLOADING & DEFENSIVE VALIDATION TESTING
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 6: PENGUJIAN METHOD OVERLOADING & DEFENSIVE VALIDATION                   |");
        System.out.println("+------------------------------------------------------------------------------+");

        System.out.println("  >>> [1] Overloading hitungEstimasiBiaya() pada Mobil:");
        System.out.println(String.format("      - Durasi 4 hari reguler        : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4)));
        System.out.println(String.format("      - Durasi 4 hari + Promo 20%%    : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4, 20.0)));
        System.out.println(String.format("      - Durasi 4 hari + Jasa Supir   : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4, true, 150000.0)));

        System.out.println("\\n  >>> [2] Overloading tambahDeposit() pada Pelanggan:");
        pelangganBudi.tambahDeposit(250000.0);
        pelangganBudi.tambahDeposit(500000.0, "QRIS BCA Mobile", "QRIS-20261005-9988");

        System.out.println("\\n  >>> [3] Pengujian Defensive Boundary Handling (Negative Testing):");
        try {
            mobilAvanza.hitungEstimasiBiaya(3, 75.0); // Diskon ilegal > 50%
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }

        try {
            pelangganBudi.tambahDeposit(-100000.0); // Nominal negatif
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }

        try {
            new Minibus("M 9999 ZZ", "Isuzu", "Elf Short", 2022, 800000.0,
                    "ENG-ISZ-001", 2500, "Diesel", 4, false, false, "TRAYEK-01"); // Kursi < 8
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }
        System.out.println();

        // =========================================================================
        // FASE 7: END-TO-END BUSINESS FLOW INTEGRATION & SYSTEM ORCHESTRATION
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 7: INTEGRASI ALUR BISNIS PENUH & ORKESTRASI RELASI SISTEM (P1 - P7)      |");
        System.out.println("+------------------------------------------------------------------------------+");

        // 1. Agregasi Garasi
        GarasiArmada garasiPusat = new GarasiArmada("Garasi Sentral AutoRent", "Jl. Trunojoyo Barat No. 10 Sumenep", 10);
        garasiPusat.tambahKendaraan(mobilAvanza);
        garasiPusat.tambahKendaraan(motorNmax);
        garasiPusat.tambahKendaraan(minibusHiace);

        // Pencarian Overloading pada Garasi
        System.out.println("\\n  >>> Pencarian Unit di Garasi:");
        Kendaraan hasilCariPlat = garasiPusat.cariKendaraan("M 2002 HB");
        System.out.println("  * Cari Plat 'M 2002 HB' -> Ditemukan: " + hasilCariPlat.getModel() + " (" + hasilCariPlat.getTipeKendaraan() + ")");
        List<Kendaraan> hasilCariBudget = garasiPusat.cariKendaraan(500000.0);
        System.out.println("  * Cari Budget <= Rp 500.000 -> Ditemukan " + hasilCariBudget.size() + " unit armada.");

        // 2. Transaksi Sewa (Asosiasi & Komposisi)
        System.out.println("\\n  >>> Membuat Transaksi Sewa Baru (TRX-2026-001)...");
        TransaksiSewa trx1 = new TransaksiSewa("TRX-2026-001", pelangganBudi, pegawaiSiti, mobilAvanza, 4);

        // 3. Pembayaran & Pelunasan
        System.out.println("  >>> Memproses Pembayaran Digital Transaksi Sewa...");
        trx1.prosesPembayaran(1500000.0, "Transfer Virtual Account Mandiri", "VA-8899-7766-1122");

        // 4. Pengembalian & Selesai
        System.out.println("  >>> Memproses Pengembalian Unit Armada & Penyelesaian Sewa (Pemakaian 350 Km, Tepat Waktu)...");
        trx1.selesaikanTransaksi(350, 0);

        // 5. Dependency Service (Printer & Notifikasi)
        System.out.println("\\n  >>> Eksekusi Service Dependency (KuitansiPrinter & LayananNotifikasi):");
        KuitansiPrinter printer = new KuitansiPrinter("Percetakan Digital PENS Sumenep", "IZIN-PRINT-2026-009");
        LayananNotifikasi notifikasi = new LayananNotifikasi("AutoRent Cloud SMS & WA Gateway");

        System.out.println("  Mencetak Bukti Kuitansi Transaksi:");
        printer.cetakKuitansiTransaksi(trx1);

        System.out.println("  Mencetak Kartu Member Digital via Interface Cetakable:");
        printer.cetakDokumenResmi(pelangganBudi);

        System.out.println("  Mencetak Slip Kompensasi Pegawai via Interface Cetakable:");
        printer.cetakDokumenResmi(pegawaiSiti);

        notifikasi.kirimNotifikasiSewa(pelangganBudi, "Transaksi TRX-2026-001 telah selesai. Terima kasih telah menggunakan AutoRent!");
        notifikasi.kirimNotifikasiServis(pegawaiSiti, mobilAvanza.getNomorPlat(), "Unit telah dikembalikan penyewa dengan oli tersisa " + mobilAvanza.getMesin().getIndikatorKesehatanOliPersen() + "%");
        notifikasi.kirimPeringatanGPS(mobilAvanza, "Armada telah kembali terparkir aman di Pos Garasi Utama.");
        System.out.println();

        // =========================================================================
        // FASE 8: RINGKASAN EKSEKUTIF & KETERCAPAIAN DEFINITION OF DONE SPRINT 7
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 8: RINGKASAN EKSEKUTIF & VERIFIKASI DEFINITION OF DONE (MODUL 7)         |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  1. Abstract Class Kendaraan & Person berhasil diimplementasikan.     [TERPENUHI]");
        System.out.println("  2. Abstract Methods (hitungEstimasiBiaya, tampilkanSpesifikasi, dll)  [TERPENUHI]");
        System.out.println("  3. Minimal 2 Subclass Konkret (Mobil, Motor, Minibus, Pelanggan, dsb) [TERPENUHI]");
        System.out.println("  4. Minimal 1 Interface (DapatDilacak, Perawatan, Cetakable)           [TERPENUHI]");
        System.out.println("  5. Realisasi Interface pada Minimal 2 Class Lintas Hierarki          [TERPENUHI]");
        System.out.println("  6. Pengujian 4+ Skenario Polymorphism Berhasil Sempurna               [TERPENUHI]");
        System.out.println("  7. Seluruh Fitur P1-P6 Tetap Terjaga dan Terintegrasi Utuh            [TERPENUHI]");
        System.out.println("  STATUS KETERCAPAIAN SPRINT 7 : 100% SUKSES (DEFINITION OF DONE TERCAPAI)");
        System.out.println("================================================================================");
    }

    private static void cetakHeaderUtama() {
        System.out.println("================================================================================");
        System.out.println("             AUTORENT SYSTEM - MODUL 7: ABSTRAKSI & INTERFACE                   ");
        System.out.println("       PROJECT BASED LEARNING + AGILE SPRINT FRAMEWORK (SPRINT 7)              ");
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println(" Nama Mahasiswa : Ahmad Yasar Maulana Dais                                      ");
        System.out.println(" NRP            : 3125522018                                                    ");
        System.out.println(" Program Studi  : D3 Teknik Informatika - PENS PSDKU Sumenep (2026)             ");
        System.out.println(" Dosen Pengampu : Nirwana Haidar Hari, S.Pd., M.Kom.                            ");
        System.out.println(" Topik Modul 7  : Abstract Class, Abstract Method, Interface & Polymorphism    ");
        System.out.println("================================================================================\\n");
    }
}
"""

all_files = {
    "DapatDilacak.java": dapat_dilacak_code,
    "Perawatan.java": perawatan_code,
    "Cetakable.java": cetakable_code,
    "Person.java": person_code,
    "Kendaraan.java": kendaraan_code,
    "Mobil.java": mobil_code,
    "Motor.java": motor_code,
    "Minibus.java": minibus_code,
    "Pelanggan.java": pelanggan_code,
    "Pegawai.java": pegawai_code,
    "Mesin.java": mesin_code,
    "DetailItemBiaya.java": detail_item_code,
    "GarasiArmada.java": garasi_code,
    "TransaksiSewa.java": transaksi_code,
    "KuitansiPrinter.java": kuitansi_code,
    "LayananNotifikasi.java": notifikasi_code,
    "Main.java": main_code
}

for fname, code in all_files.items():
    p1 = os.path.join(src_dir, fname)
    p2 = os.path.join(sub_src_dir, fname)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(code)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated {fname} ({len(code.splitlines())} lines)")

print("\\nAll 17 Java source files successfully generated in both src/ and P7_3125522018_Ahmad Yasar Maulana Dais/src/!")

import java.util.regex.Pattern;

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

    private static final Pattern PLAT_PATTERN = Pattern.compile("^[A-Z]{1,2}\\s[0-9]{1,4}\\s[A-Z]{1,3}$");

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

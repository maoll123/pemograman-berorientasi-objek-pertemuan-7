/**
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
        sb.append("====================================================\n");
        sb.append("           LEMBAR SPESIFIKASI SEPEDA MOTOR          \n");
        sb.append("====================================================\n");
        sb.append(String.format("Plat Nomor    : %s\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Jenis / CC    : %s | %d CC\n", jenisMotor, getMesin().getKapasitasCC()));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MOTOR [%s] %s %s - %s - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), jenisMotor, getTarifPerHari());
    }
}

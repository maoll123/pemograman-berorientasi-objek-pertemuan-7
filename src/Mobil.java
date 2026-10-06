/**
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
        sb.append("====================================================\n");
        sb.append("           LEMBAR SPESIFIKASI ARMADA MOBIL          \n");
        sb.append("====================================================\n");
        sb.append(String.format("Plat Nomor    : %s\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Kapasitas     : %d Orang | Transmisi: %s\n", kapasitasPenumpang, tipeTransmisi));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MOBIL [%s] %s %s - %d Pax - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), kapasitasPenumpang, getTarifPerHari());
    }
}

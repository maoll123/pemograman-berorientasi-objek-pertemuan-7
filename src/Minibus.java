/**
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
        sb.append("====================================================\n");
        sb.append("          LEMBAR SPESIFIKASI MINIBUS TRAVEL         \n");
        sb.append("====================================================\n");
        sb.append(String.format("Plat Nomor    : %s\n", getNomorPlat()));
        sb.append(String.format("Merk / Model  : %s %s (%d)\n", getMerk(), getModel(), getTahunProduksi()));
        sb.append(String.format("Kapasitas     : %d Kursi | Izin: %s\n", jumlahKursi, nomorIzinTrayekPariwisata));
        sb.append(String.format("Tarif Rental  : Rp %,.2f per hari\n", getTarifPerHari()));
        sb.append(String.format("Lokasi GPS    : %s\n", lokasiTerkiniGPS));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MINIBUS [%s] %s %s - %d Kursi - Rp %,.0f/hari",
                getNomorPlat(), getMerk(), getModel(), jumlahKursi, getTarifPerHari());
    }
}

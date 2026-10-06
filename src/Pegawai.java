/**
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
        sb.append("====================================================\n");
        sb.append("             SLIP KOMPENSASI & GAJI PEGAWAI         \n");
        sb.append("====================================================\n");
        sb.append(String.format("NIK / ID      : %s / %s\n", nomorIndukKaryawan, getId()));
        sb.append(String.format("Nama Pegawai  : %s\n", getNama()));
        sb.append(String.format("Jabatan       : %s\n", posisiJabatan));
        sb.append(String.format("Gaji Pokok    : Rp %,.2f\n", gajiPokok));
        sb.append(String.format("Bonus Transaksi: Rp %,.2f (%d transaksi)\n",
                jumlahTransaksiDitangani * bonusPerTransaksi, jumlahTransaksiDitangani));
        sb.append(String.format("TOTAL GAJI    : Rp %,.2f\n", hitungKompensasi()));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("PEGAWAI [%s] %s (%s) - Total Gaji: Rp %,.0f",
                nomorIndukKaryawan, getNama(), posisiJabatan, hitungKompensasi());
    }
}

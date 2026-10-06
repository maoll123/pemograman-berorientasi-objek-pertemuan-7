import java.util.ArrayList;

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
        sb.append("================================================================\n");
        sb.append("                  AUTORENT SYSTEM - RESMI                       \n");
        sb.append("               BUKTI KUITANSI TRANSAKSI SEWA                    \n");
        sb.append("================================================================\n");
        sb.append(String.format("Kode Transaksi  : %-20s Status: %s\n", kodeTransaksi, (statusLunas ? "LUNAS" : "BELUM LUNAS")));
        sb.append(String.format("Pelanggan       : %s (ID: %s | Member: %s)\n",
                pelanggan.getNama(), pelanggan.getId(), pelanggan.getKategoriMember()));
        sb.append(String.format("Petugas CS      : %s (NIK: %s)\n",
                pegawaiPetugas.getNama(), pegawaiPetugas.getNomorIndukKaryawan()));
        sb.append(String.format("Unit Armada     : %s [%s] - %s\n",
                kendaraanDisewa.getModel(), kendaraanDisewa.getNomorPlat(), kendaraanDisewa.getTipeKendaraan()));
        sb.append(String.format("Durasi Sewa     : %d Hari\n", durasiHari));
        sb.append("----------------------------------------------------------------\n");
        sb.append("RINCIAN BIAYA :\n");
        for (DetailItemBiaya item : rincianBiaya) {
            sb.append(item.formatItemBiaya()).append("\n");
        }
        sb.append("----------------------------------------------------------------\n");
        sb.append(String.format("TOTAL TAGIHAN   : Rp %,15.2f\n", totalBiayaSewa));
        sb.append(String.format("TOTAL DIBAYAR   : Rp %,15.2f\n", nominalDibayar));
        sb.append(String.format("STATUS SELESAI  : %s\n", (statusSelesai ? "SELESAI / UNIT KEMBALI" : "AKTIF DALAM MASA SEWA")));
        sb.append("================================================================\n");
        sb.append("    Terima kasih telah mempercayakan perjalanan Anda bersama    \n");
        sb.append("                     AutoRent PENS Sumenep                      \n");
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

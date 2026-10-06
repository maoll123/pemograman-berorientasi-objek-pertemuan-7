import java.util.regex.Pattern;

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
        sb.append("====================================================\n");
        sb.append("             KARTU MEMBER DIGITAL AUTORENT          \n");
        sb.append("====================================================\n");
        sb.append(String.format("ID Member     : %s\n", getId()));
        sb.append(String.format("Nama Lengkap  : %s\n", getNama()));
        sb.append(String.format("Tingkat Member: %s (Hak Diskon: %.0f%%)\n", kategoriMember, getDiskonMemberPersen()));
        sb.append(String.format("Saldo Deposit : Rp %,.2f\n", saldoDeposit));
        sb.append(String.format("Kontak        : %s\n", getNomorTelepon()));
        sb.append("====================================================");
        return sb.toString();
    }

    @Override
    public String generateRingkasan() {
        return String.format("MEMBER [%s] %s (%s) - Saldo: Rp %,.0f",
                getId(), getNama(), kategoriMember, saldoDeposit);
    }
}

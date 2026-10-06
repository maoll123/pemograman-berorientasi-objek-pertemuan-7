import java.util.regex.Pattern;

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

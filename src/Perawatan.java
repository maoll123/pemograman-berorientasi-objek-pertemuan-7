/**
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

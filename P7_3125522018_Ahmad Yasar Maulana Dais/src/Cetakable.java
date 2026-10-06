/**
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

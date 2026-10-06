/**
 * Class KuitansiPrinter (Service Utility Dependency & Interface Consumer)
 * 
 * Bertanggung jawab mencetak kuitansi transaksi dan mencetak entitas apa pun
 * yang merealisasikan interface Cetakable (Interface-Based Polymorphic Printing).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class KuitansiPrinter {
    private String namaPercetakan;
    private String nomorIzin;

    public KuitansiPrinter(String namaPercetakan, String nomorIzin) {
        this.namaPercetakan = namaPercetakan;
        this.nomorIzin = nomorIzin;
    }

    public void cetakKuitansiTransaksi(TransaksiSewa transaksi) {
        if (transaksi == null) {
            System.out.println("  [ERROR] Objek transaksi sewa tidak valid!");
            return;
        }
        System.out.println(transaksi.formatCetakDokumen());
    }

    /**
     * Membuktikan pemanggilan polimorfisme berbasis interface Cetakable.
     * Dapat mencetak TransaksiSewa, Pelanggan (Kartu Member), Pegawai (Slip Gaji),
     * maupun Kendaraan (Lembar Spesifikasi).
     * 
     * @param dokumen Objek implementor interface Cetakable
     */
    public void cetakDokumenResmi(Cetakable dokumen) {
        if (dokumen == null) {
            System.out.println("  [ERROR] Dokumen cetakable tidak boleh null!");
            return;
        }
        System.out.println(String.format("  [PRINTER UTILITY: %s (Izin: %s)]", namaPercetakan, nomorIzin));
        System.out.println(dokumen.formatCetakDokumen());
        System.out.println();
    }
}

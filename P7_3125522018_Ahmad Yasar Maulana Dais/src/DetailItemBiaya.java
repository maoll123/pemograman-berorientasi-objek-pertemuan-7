/**
 * Class DetailItemBiaya (Komponen Komposisi Transaksi)
 * 
 * Merepresentasikan baris rincian komponen biaya dalam invoice / kuitansi transaksi.
 * Memiliki relasi Composition dengan TransaksiSewa.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class DetailItemBiaya {
    private String namaItem;
    private int jumlahQty;
    private double hargaSatuan;
    private double subtotalBiaya;

    public DetailItemBiaya(String namaItem, int jumlahQty, double hargaSatuan) {
        if (namaItem == null || namaItem.trim().isEmpty()) {
            throw new IllegalArgumentException("Nama item biaya tidak boleh kosong.");
        }
        if (jumlahQty <= 0) {
            throw new IllegalArgumentException("Kuantitas item biaya minimal 1.");
        }

        this.namaItem = namaItem.trim();
        this.jumlahQty = jumlahQty;
        this.hargaSatuan = hargaSatuan;
        this.subtotalBiaya = jumlahQty * hargaSatuan;
    }

    public String getNamaItem() {
        return namaItem;
    }

    public int getJumlahQty() {
        return jumlahQty;
    }

    public double getHargaSatuan() {
        return hargaSatuan;
    }

    public double getSubtotalBiaya() {
        return subtotalBiaya;
    }

    public String formatItemBiaya() {
        if (subtotalBiaya < 0) {
            return String.format("  - %-30s x %-2d @ -Rp %,10.2f = -Rp %,11.2f",
                    namaItem, jumlahQty, Math.abs(hargaSatuan), Math.abs(subtotalBiaya));
        }
        return String.format("  - %-30s x %-2d @ Rp %,11.2f = Rp %,12.2f",
                namaItem, jumlahQty, hargaSatuan, subtotalBiaya);
    }
}

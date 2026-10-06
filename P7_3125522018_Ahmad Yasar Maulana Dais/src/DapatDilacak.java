/**
 * Interface DapatDilacak
 * 
 * Mendefinisikan kontrak perilaku telematika dan pelacakan posisi GPS IoT untuk seluruh
 * entitas armada maupun petugas operasional di ekosistem AutoRent System.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public interface DapatDilacak {

    /**
     * Mengambil informasi nama area atau lokasi terkini objek.
     * 
     * @return String representasi lokasi
     */
    String getLokasi();

    /**
     * Memperbarui titik koordinat dan nama area lokasi objek.
     * 
     * @param koordinatBaru format koordinat GPS (contoh: "-7.0051, 113.8604")
     * @param namaArea nama wilayah atau pos pantau
     */
    void perbaruiLokasi(String koordinatBaru, String namaArea);

    /**
     * Mengecek status operasional modul GPS telematika.
     * 
     * @return String status konektivitas GPS
     */
    String getStatusGPS();

    /**
     * Default method (fitur modern Java 8+) untuk mengirimkan sinyal ping telematika standar.
     * Menunjukkan bahwa interface modern dapat memiliki implementasi default tanpa merusak implementor.
     * 
     * @return status pengiriman sinyal ping telematika
     */
    default String kirimSinyalPingTelematika() {
        return "Ping IoT GPS berhasil dikirimkan ke server AutoRent Telematics Central Gateway.";
    }
}

/**
 * Class LayananNotifikasi (Service Gateway Dependency)
 * 
 * Bertanggung jawab mengirimkan notifikasi multi-kanal (SMS, WhatsApp, Email)
 * kepada entitas Person secara polimorfis, serta mengirimkan telemetry alert ke objek DapatDilacak.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class LayananNotifikasi {
    private String namaProviderGateway;

    public LayananNotifikasi(String namaProviderGateway) {
        this.namaProviderGateway = namaProviderGateway;
    }

    public void kirimNotifikasiSewa(Person penerima, String pesan) {
        if (penerima == null) return;
        System.out.println(String.format("  [NOTIFIKASI GATEWAY - %s] Dikirim ke %s (%s - %s) -> \"%s\"",
                namaProviderGateway, penerima.getNama(), penerima.getNomorTelepon(), penerima.getEmail(), pesan));
    }

    public void kirimNotifikasiServis(Person penanggungJawab, String platKendaraan, String statusServis) {
        if (penanggungJawab == null) return;
        System.out.println(String.format("  [MAINTENANCE ALERT] Ke Staf %s [%s] -> Armada %s : %s",
                penanggungJawab.getNama(), penanggungJawab.getNomorTelepon(), platKendaraan, statusServis));
    }

    public void kirimPeringatanGPS(DapatDilacak target, String pesanPeringatan) {
        if (target == null) return;
        System.out.println(String.format("  [GPS TELEMATICS ALERT via %s] Lokasi: %s | Peringatan: %s",
                namaProviderGateway, target.getLokasi(), pesanPeringatan));
    }
}

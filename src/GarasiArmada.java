import java.util.ArrayList;
import java.util.List;

/**
 * Class GarasiArmada (Agregasi Polimorfis Pool Kendaraan)
 * 
 * Mengelola koleksi heterogen armada kendaraan sewa berbasis tipe abstraksi Kendaraan.
 * Mengimplementasikan method overloading untuk pencarian armada yang fleksibel
 * serta eksekusi polimorfisme massal untuk pemeliharaan (Perawatan) dan telematika (DapatDilacak).
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class GarasiArmada {
    private String namaGarasi;
    private String lokasiGarasi;
    private int kapasitasMaksimal;
    private ArrayList<Kendaraan> daftarArmada; // Agregasi Polimorfis

    public GarasiArmada(String namaGarasi, String lokasiGarasi, int kapasitasMaksimal) {
        if (namaGarasi == null || namaGarasi.trim().isEmpty()) {
            throw new IllegalArgumentException("Nama garasi tidak boleh kosong.");
        }
        if (lokasiGarasi == null || lokasiGarasi.trim().isEmpty()) {
            throw new IllegalArgumentException("Lokasi garasi tidak boleh kosong.");
        }
        if (kapasitasMaksimal <= 0) {
            throw new IllegalArgumentException("Kapasitas maksimal garasi harus positif.");
        }

        this.namaGarasi = namaGarasi.trim();
        this.lokasiGarasi = lokasiGarasi.trim();
        this.kapasitasMaksimal = kapasitasMaksimal;
        this.daftarArmada = new ArrayList<>();
    }

    public String getNamaGarasi() {
        return namaGarasi;
    }

    public String getLokasiGarasi() {
        return lokasiGarasi;
    }

    public int getKapasitasMaksimal() {
        return kapasitasMaksimal;
    }

    public ArrayList<Kendaraan> getDaftarArmada() {
        return daftarArmada;
    }

    public int getJumlahArmadaTersimpan() {
        return daftarArmada.size();
    }

    public void tambahKendaraan(Kendaraan kendaraan) {
        if (kendaraan == null) {
            throw new IllegalArgumentException("Objek kendaraan tidak boleh null.");
        }
        if (daftarArmada.size() >= kapasitasMaksimal) {
            throw new IllegalStateException("Garasi penuh! Tidak dapat menampung unit armada baru.");
        }
        for (Kendaraan k : daftarArmada) {
            if (k.getNomorPlat().equalsIgnoreCase(kendaraan.getNomorPlat())) {
                throw new IllegalArgumentException("Kendaraan dengan plat " + kendaraan.getNomorPlat() + " sudah terdaftar di garasi ini.");
            }
        }
        this.daftarArmada.add(kendaraan);
        System.out.println(String.format("  [GARASI ARMADA] Berhasil menambahkan %s [%s] ke %s.",
                kendaraan.getTipeKendaraan(), kendaraan.getNomorPlat(), this.namaGarasi));
    }

    public boolean hapusKendaraan(String nomorPlat) {
        if (nomorPlat == null) return false;
        return daftarArmada.removeIf(k -> k.getNomorPlat().equalsIgnoreCase(nomorPlat.trim()));
    }

    // --- Dynamic Binding / Polymorphic Display ---

    public void tampilkanSeluruhArmada() {
        System.out.println(String.format("\n  === DAFTAR POOL ARMADA [%s - %s] (%d/%d Unit) ===",
                namaGarasi, lokasiGarasi, daftarArmada.size(), kapasitasMaksimal));
        if (daftarArmada.isEmpty()) {
            System.out.println("  (Garasi masih kosong)");
            return;
        }
        for (int i = 0; i < daftarArmada.size(); i++) {
            Kendaraan k = daftarArmada.get(i);
            System.out.println(String.format("  [%d] Tipe: %s", (i + 1), k.getTipeKendaraan()));
            k.tampilkanSpesifikasi(); // Dynamic Method Dispatch
        }
    }

    // --- Method Overloading Pencarian Armada ---

    public Kendaraan cariKendaraan(String nomorPlat) {
        if (nomorPlat == null || nomorPlat.trim().isEmpty()) {
            throw new IllegalArgumentException("Nomor plat pencarian tidak boleh kosong.");
        }
        for (Kendaraan k : daftarArmada) {
            if (k.getNomorPlat().equalsIgnoreCase(nomorPlat.trim())) {
                return k;
            }
        }
        return null;
    }

    public List<Kendaraan> cariKendaraan(String merk, String model) {
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.getMerk().equalsIgnoreCase(merk.trim()) && k.getModel().equalsIgnoreCase(model.trim())) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    public List<Kendaraan> cariKendaraan(double maxTarifPerHari) {
        if (maxTarifPerHari <= 0) {
            throw new IllegalArgumentException("Batas tarif pencarian harus positif.");
        }
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.getTarifPerHari() <= maxTarifPerHari) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    public List<Kendaraan> cariKendaraan(boolean statusTersedia) {
        List<Kendaraan> hasil = new ArrayList<>();
        for (Kendaraan k : daftarArmada) {
            if (k.isStatusTersedia() == statusTersedia) {
                hasil.add(k);
            }
        }
        return hasil;
    }

    // --- Interface Polymorphism Batch Processing ---

    /**
     * Menjalankan prosedur servis massal memanfaatkan interface Perawatan.
     */
    public void lakukanServisMasal() {
        System.out.println(String.format("\n  === PROGRAM SERVIS PREVENTIF MASSAL GARASI [%s] ===", namaGarasi));
        int unitDiservis = 0;
        for (Kendaraan k : daftarArmada) {
            if (k instanceof Perawatan) {
                Perawatan p = (Perawatan) k;
                if (!p.cekKelayakanOperasional() || k.getMesin().getIndikatorKesehatanOliPersen() < 80) {
                    System.out.println(String.format("  -> Memproses Pemeliharaan Unit: %s [%s]", k.getMerk(), k.getNomorPlat()));
                    p.lakukanServis(); // Interface Dynamic Dispatch
                    unitDiservis++;
                }
            }
        }
        System.out.println(String.format("  [HASIL] Selesai melakukan servis preventif pada %d unit armada.\n", unitDiservis));
    }

    /**
     * Memantau posisi seluruh armada memanfaatkan interface DapatDilacak.
     */
    public void pantauSeluruhPelacakGPS() {
        System.out.println(String.format("\n  === MONITORING FLEET TELEMATICS GPS [%s] ===", namaGarasi));
        for (Kendaraan k : daftarArmada) {
            if (k instanceof DapatDilacak) {
                DapatDilacak pelacak = (DapatDilacak) k;
                System.out.println(String.format("  • [%s] %-15s : %s",
                        k.getNomorPlat(), k.getModel(), pelacak.getLokasi()));
            }
        }
    }

    public double hitungTotalNilaiArmada() {
        double total = 0;
        for (Kendaraan k : daftarArmada) {
            total += (k.getTarifPerHari() * 30.0); // Estimasi valuasi kapasitas sewa bulanan
        }
        return total;
    }
}

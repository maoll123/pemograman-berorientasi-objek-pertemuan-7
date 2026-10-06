/**
 * Class Mesin (Komponen Komposisi Kendaraan)
 * 
 * Merepresentasikan spesifikasi mekanikal dan status kesehatan mesin internal.
 * Memiliki relasi keterikatan siklus hidup yang kuat (Composition) dengan Kendaraan.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Mesin {
    private String nomorRangkaMesin;
    private int kapasitasCC;
    private String tipeBahanBakar;
    private boolean statusMesinMenyala;
    private int indikatorKesehatanOliPersen;

    public Mesin(String nomorRangkaMesin, int kapasitasCC, String tipeBahanBakar) {
        if (nomorRangkaMesin == null || nomorRangkaMesin.trim().isEmpty()) {
            throw new IllegalArgumentException("Nomor rangka mesin tidak boleh kosong.");
        }
        if (kapasitasCC < 50 || kapasitasCC > 10000) {
            throw new IllegalArgumentException("Kapasitas CC mesin tidak valid (50 - 10000 CC). Input: " + kapasitasCC);
        }
        if (tipeBahanBakar == null || tipeBahanBakar.trim().isEmpty()) {
            throw new IllegalArgumentException("Tipe bahan bakar tidak boleh kosong.");
        }

        this.nomorRangkaMesin = nomorRangkaMesin.trim().toUpperCase();
        this.kapasitasCC = kapasitasCC;
        this.tipeBahanBakar = tipeBahanBakar.trim();
        this.statusMesinMenyala = false;
        this.indikatorKesehatanOliPersen = 100;
    }

    public String getNomorRangkaMesin() {
        return nomorRangkaMesin;
    }

    public int getKapasitasCC() {
        return kapasitasCC;
    }

    public String getTipeBahanBakar() {
        return tipeBahanBakar;
    }

    public boolean isStatusMesinMenyala() {
        return statusMesinMenyala;
    }

    public int getIndikatorKesehatanOliPersen() {
        return indikatorKesehatanOliPersen;
    }

    public void nyalakanMesin() {
        this.statusMesinMenyala = true;
    }

    public void matikanMesin() {
        this.statusMesinMenyala = false;
    }

    public void gantiOliMesin() {
        this.indikatorKesehatanOliPersen = 100;
    }

    public void kurangiKesehatanOli(int km) {
        int penurunan = km / 100;
        this.indikatorKesehatanOliPersen = Math.max(5, this.indikatorKesehatanOliPersen - penurunan);
    }

    public String cekStatusMesin() {
        return String.format("Mesin %s (%d CC %s) | Status: %s | Kondisi Oli: %d%%",
                nomorRangkaMesin, kapasitasCC, tipeBahanBakar,
                (statusMesinMenyala ? "MENYALA" : "STANDBY"), indikatorKesehatanOliPersen);
    }
}

import java.util.ArrayList;
import java.util.List;

/**
 * Driver & Test Suite Utama (Main.java)
 * 
 * Menguji dan mendemonstrasikan secara komprehensif seluruh capaian pembelajaran Modul 7:
 * 1. Audit & Pembuktian Larangan Instansiasi Abstract Class (Kendaraan & Person).
 * 2. Instansiasi Sukses Subclass Konkret (Mobil, Motor, Minibus, Pelanggan, Pegawai).
 * 3. Dynamic Method Dispatch via Superclass Abstract Reference (Abstract Method Polymorphism).
 * 4. Interface Polymorphism (DapatDilacak, Perawatan, Cetakable) lintas hierarki.
 * 5. Heterogeneous Collection Processing (Array & ArrayList polimorfis superclass & interface).
 * 6. Method Overloading & Defensive Programming Verification.
 * 7. End-to-End Business Integration (Agregasi Garasi, Transaksi, Komposisi Mesin, Dependency).
 * 8. Evaluasi Definition of Done & Sprint 7 Completion.
 * 
 * @author Ahmad Yasar Maulana Dais (3125522018)
 * @version 7.0 - Modul 7 Abstraction & Interface
 */
public class Main {

    public static void main(String[] args) {
        cetakHeaderUtama();

        // =========================================================================
        // FASE 1: AUDIT & PEMBUKTIAN LARANGAN INSTANSIASI ABSTRACT CLASS
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 1: AUDIT & PEMBUKTIAN LARANGAN INSTANSIASI ABSTRACT CLASS               |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Pada Modul 7, superclass Kendaraan dan Person dideklarasikan sebagai 'abstract'.");
        System.out.println("  Artinya, kode berikut TIDAK BOLEH dikompilasi oleh Java Compiler:");
        System.out.println("    // Kendaraan k = new Kendaraan(...); // COMPILE ERROR: Kendaraan is abstract");
        System.out.println("    // Person p = new Person(...);       // COMPILE ERROR: Person is abstract");
        System.out.println("  [VERIFIKASI DESAIN] Abstraction menjamin entitas umum tidak dapat diinstansiasi langsung.");
        System.out.println("  Hanya subclass konkrit yang dapat diinstansiasi di Heap Memory.\n");

        // =========================================================================
        // FASE 2: INSTANSIASI OBJEK SUBCLASS KONKRET
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 2: INSTANSIASI SUBCLASS KONKRET & VALIDASI KONSTRUKTOR DEFENSIVE        |");
        System.out.println("+------------------------------------------------------------------------------+");

        // Subclass Kendaraan
        Mobil mobilAvanza = new Mobil("M 1001 HA", "Toyota", "Avanza Veloz", 2023, 400000.0,
                "ENG-TOY-AVZ-001", 1500, "Bensin Pertamax", "Automatic", 7, true);

        Motor motorNmax = new Motor("M 2002 HB", "Yamaha", "NMAX 155 Connected", 2024, 150000.0,
                "ENG-YAM-NMX-002", 155, "Bensin Pertamax", "Matic", 2, true);

        Minibus minibusHiace = new Minibus("M 3003 HC", "Toyota", "HiAce Premio Luxury", 2023, 1100000.0,
                "ENG-TOY-HIC-003", 2800, "Diesel Dexlite", 14, true, true, "TRAYEK-PARIWISATA-JATIM-9988");

        // Subclass Person
        Pelanggan pelangganBudi = new Pelanggan("PLG-001", "Budi Pratama", "081234567890",
                "Jl. Trunojoyo No. 45, Sumenep", "budi.pratama@gmail.com",
                "3529012345670001", 500000.0, "Gold");

        Pegawai pegawaiSiti = new Pegawai("PGW-101", "Siti Aminah", "081987654321",
                "Jl. KH. Agus Salim No. 12, Sumenep", "siti.aminah@autorent.com",
                "NIK-2026-004", "Front-Office CS & Fleet Officer", 3500000.0, 50000.0);

        System.out.println("  [OK] Berhasil menginstansiasi objek Mobil    : " + mobilAvanza.getModel() + " [" + mobilAvanza.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Motor    : " + motorNmax.getModel() + " [" + motorNmax.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Minibus  : " + minibusHiace.getModel() + " [" + minibusHiace.getNomorPlat() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Pelanggan: " + pelangganBudi.getNama() + " [" + pelangganBudi.getId() + "]");
        System.out.println("  [OK] Berhasil menginstansiasi objek Pegawai  : " + pegawaiSiti.getNama() + " [" + pegawaiSiti.getNomorIndukKaryawan() + "]\n");

        // =========================================================================
        // FASE 3: POLYMORPHISM VIA SUPERCLASS ABSTRACT REFERENCE (DYNAMIC METHOD DISPATCH)
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 3: PENGUJIAN POLYMORPHISM VIA SUPERCLASS ABSTRACT REFERENCE             |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Memanggil abstract method melalui reference Superclass Abstract (Upcasting):\n");

        // Polymorphic reference Kendaraan
        Kendaraan refK1 = mobilAvanza;
        Kendaraan refK2 = motorNmax;
        Kendaraan refK3 = minibusHiace;

        System.out.println("  >>> [1] Pemanggilan refK1.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Mobil):");
        refK1.tampilkanSpesifikasi();

        System.out.println("  >>> [2] Pemanggilan refK2.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Motor):");
        refK2.tampilkanSpesifikasi();

        System.out.println("  >>> [3] Pemanggilan refK3.tampilkanSpesifikasi() (Tipe Ref: Kendaraan, Objek: Minibus):");
        refK3.tampilkanSpesifikasi();

        System.out.println("  >>> [4] Pemanggilan Abstract Method hitungEstimasiBiaya(5 hari) secara Polimorfis:");
        System.out.println(String.format("      * Estimasi Mobil 5 Hari   : Rp %,.2f (Diskon Durasi 5%%)", refK1.hitungEstimasiBiaya(5)));
        System.out.println(String.format("      * Estimasi Motor 5 Hari   : Rp %,.2f (Diskon Hemat 6%%)", refK2.hitungEstimasiBiaya(5)));
        System.out.println(String.format("      * Estimasi Minibus 5 Hari : Rp %,.2f (Termasuk Surcharge Komersial)", refK3.hitungEstimasiBiaya(5)));

        System.out.println("\n  >>> [5] Pemanggilan Abstract Method Person via Polymorphic Reference:");
        Person refP1 = pelangganBudi;
        Person refP2 = pegawaiSiti;

        System.out.println("  [Profil via Person Ref 1]");
        refP1.tampilkanProfil();
        System.out.println("  [Profil via Person Ref 2]");
        refP2.tampilkanProfil();
        System.out.println();

        // =========================================================================
        // FASE 4: INTERFACE POLYMORPHISM LINTAS HIERARKI KELAS
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 4: PENGUJIAN INTERFACE POLYMORPHISM (LINTAS HIERARKI CLASS)             |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  Interface DapatDilacak direalisasikan oleh Mobil, Motor, Minibus, dan Pegawai!\n");

        DapatDilacak[] daftarPelacak = new DapatDilacak[] {
                mobilAvanza,
                motorNmax,
                minibusHiace,
                pegawaiSiti // Lintas hierarki (Pegawai adalah turunan Person, bukan Kendaraan!)
        };

        for (int i = 0; i < daftarPelacak.length; i++) {
            DapatDilacak item = daftarPelacak[i];
            System.out.println(String.format("  * Pelacak [%d] Lokasi     : %s", (i + 1), item.getLokasi()));
            System.out.println(String.format("               Status GPS : %s", item.getStatusGPS()));
            System.out.println(String.format("               Ping Res   : %s", item.kirimSinyalPingTelematika()));
        }

        System.out.println("\n  Memperbarui lokasi objek secara dinamis via Interface:");
        daftarPelacak[0].perbaruiLokasi("-7.0100, 113.8700", "Pelabuhan Kalianget Sumenep");
        daftarPelacak[3].perbaruiLokasi("-7.0120, 113.8680", "Pos Layanan Pelabuhan Kalianget");

        System.out.println("\n  >>> Pengujian Interface Perawatan pada Seluruh Kendaraan:");
        Perawatan[] armadaPerawatan = new Perawatan[] { mobilAvanza, motorNmax, minibusHiace };
        for (Perawatan armada : armadaPerawatan) {
            System.out.println("  * Kelayakan Operasional: " + (armada.cekKelayakanOperasional() ? "LAYAK JALAN" : "PERLU SERVIS"));
            System.out.println("    " + armada.getJadwalServisBerikutnya());
        }
        System.out.println();

        // =========================================================================
        // FASE 5: HETEROGENEOUS POLYMORPHIC COLLECTIONS (ARRAY & ARRAYLIST)
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 5: HETEROGENEOUS POLYMORPHIC COLLECTIONS (ARRAY & ARRAYLIST)             |");
        System.out.println("+------------------------------------------------------------------------------+");

        List<Cetakable> daftarDokumenCetak = new ArrayList<>();
        daftarDokumenCetak.add(mobilAvanza);
        daftarDokumenCetak.add(motorNmax);
        daftarDokumenCetak.add(pelangganBudi);
        daftarDokumenCetak.add(pegawaiSiti);

        System.out.println("  Iterasi Heterogeneous List<Cetakable> (Koleksi Beragam Tipe Objek):");
        for (Cetakable dok : daftarDokumenCetak) {
            System.out.println("  -> Ringkasan: " + dok.generateRingkasan());
        }
        System.out.println();

        // =========================================================================
        // FASE 6: METHOD OVERLOADING & DEFENSIVE VALIDATION TESTING
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 6: PENGUJIAN METHOD OVERLOADING & DEFENSIVE VALIDATION                   |");
        System.out.println("+------------------------------------------------------------------------------+");

        System.out.println("  >>> [1] Overloading hitungEstimasiBiaya() pada Mobil:");
        System.out.println(String.format("      - Durasi 4 hari reguler        : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4)));
        System.out.println(String.format("      - Durasi 4 hari + Promo 20%%    : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4, 20.0)));
        System.out.println(String.format("      - Durasi 4 hari + Jasa Supir   : Rp %,.2f", mobilAvanza.hitungEstimasiBiaya(4, true, 150000.0)));

        System.out.println("\n  >>> [2] Overloading tambahDeposit() pada Pelanggan:");
        pelangganBudi.tambahDeposit(250000.0);
        pelangganBudi.tambahDeposit(500000.0, "QRIS BCA Mobile", "QRIS-20261005-9988");

        System.out.println("\n  >>> [3] Pengujian Defensive Boundary Handling (Negative Testing):");
        try {
            mobilAvanza.hitungEstimasiBiaya(3, 75.0); // Diskon ilegal > 50%
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }

        try {
            pelangganBudi.tambahDeposit(-100000.0); // Nominal negatif
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }

        try {
            new Minibus("M 9999 ZZ", "Isuzu", "Elf Short", 2022, 800000.0,
                    "ENG-ISZ-001", 2500, "Diesel", 4, false, false, "TRAYEK-01"); // Kursi < 8
        } catch (IllegalArgumentException e) {
            System.out.println("  [TANGKAP VALIDASI] " + e.getMessage());
        }
        System.out.println();

        // =========================================================================
        // FASE 7: END-TO-END BUSINESS FLOW INTEGRATION & SYSTEM ORCHESTRATION
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 7: INTEGRASI ALUR BISNIS PENUH & ORKESTRASI RELASI SISTEM (P1 - P7)      |");
        System.out.println("+------------------------------------------------------------------------------+");

        // 1. Agregasi Garasi
        GarasiArmada garasiPusat = new GarasiArmada("Garasi Sentral AutoRent", "Jl. Trunojoyo Barat No. 10 Sumenep", 10);
        garasiPusat.tambahKendaraan(mobilAvanza);
        garasiPusat.tambahKendaraan(motorNmax);
        garasiPusat.tambahKendaraan(minibusHiace);

        // Pencarian Overloading pada Garasi
        System.out.println("\n  >>> Pencarian Unit di Garasi:");
        Kendaraan hasilCariPlat = garasiPusat.cariKendaraan("M 2002 HB");
        System.out.println("  * Cari Plat 'M 2002 HB' -> Ditemukan: " + hasilCariPlat.getModel() + " (" + hasilCariPlat.getTipeKendaraan() + ")");
        List<Kendaraan> hasilCariBudget = garasiPusat.cariKendaraan(500000.0);
        System.out.println("  * Cari Budget <= Rp 500.000 -> Ditemukan " + hasilCariBudget.size() + " unit armada.");

        // 2. Transaksi Sewa (Asosiasi & Komposisi)
        System.out.println("\n  >>> Membuat Transaksi Sewa Baru (TRX-2026-001)...");
        TransaksiSewa trx1 = new TransaksiSewa("TRX-2026-001", pelangganBudi, pegawaiSiti, mobilAvanza, 4);

        // 3. Pembayaran & Pelunasan
        System.out.println("  >>> Memproses Pembayaran Digital Transaksi Sewa...");
        trx1.prosesPembayaran(1500000.0, "Transfer Virtual Account Mandiri", "VA-8899-7766-1122");

        // 4. Pengembalian & Selesai
        System.out.println("  >>> Memproses Pengembalian Unit Armada & Penyelesaian Sewa (Pemakaian 350 Km, Tepat Waktu)...");
        trx1.selesaikanTransaksi(350, 0);

        // 5. Dependency Service (Printer & Notifikasi)
        System.out.println("\n  >>> Eksekusi Service Dependency (KuitansiPrinter & LayananNotifikasi):");
        KuitansiPrinter printer = new KuitansiPrinter("Percetakan Digital PENS Sumenep", "IZIN-PRINT-2026-009");
        LayananNotifikasi notifikasi = new LayananNotifikasi("AutoRent Cloud SMS & WA Gateway");

        System.out.println("  Mencetak Bukti Kuitansi Transaksi:");
        printer.cetakKuitansiTransaksi(trx1);

        System.out.println("  Mencetak Kartu Member Digital via Interface Cetakable:");
        printer.cetakDokumenResmi(pelangganBudi);

        System.out.println("  Mencetak Slip Kompensasi Pegawai via Interface Cetakable:");
        printer.cetakDokumenResmi(pegawaiSiti);

        notifikasi.kirimNotifikasiSewa(pelangganBudi, "Transaksi TRX-2026-001 telah selesai. Terima kasih telah menggunakan AutoRent!");
        notifikasi.kirimNotifikasiServis(pegawaiSiti, mobilAvanza.getNomorPlat(), "Unit telah dikembalikan penyewa dengan oli tersisa " + mobilAvanza.getMesin().getIndikatorKesehatanOliPersen() + "%");
        notifikasi.kirimPeringatanGPS(mobilAvanza, "Armada telah kembali terparkir aman di Pos Garasi Utama.");
        System.out.println();

        // =========================================================================
        // FASE 8: RINGKASAN EKSEKUTIF & KETERCAPAIAN DEFINITION OF DONE SPRINT 7
        // =========================================================================
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("| FASE 8: RINGKASAN EKSEKUTIF & VERIFIKASI DEFINITION OF DONE (MODUL 7)         |");
        System.out.println("+------------------------------------------------------------------------------+");
        System.out.println("  1. Abstract Class Kendaraan & Person berhasil diimplementasikan.     [TERPENUHI]");
        System.out.println("  2. Abstract Methods (hitungEstimasiBiaya, tampilkanSpesifikasi, dll)  [TERPENUHI]");
        System.out.println("  3. Minimal 2 Subclass Konkret (Mobil, Motor, Minibus, Pelanggan, dsb) [TERPENUHI]");
        System.out.println("  4. Minimal 1 Interface (DapatDilacak, Perawatan, Cetakable)           [TERPENUHI]");
        System.out.println("  5. Realisasi Interface pada Minimal 2 Class Lintas Hierarki          [TERPENUHI]");
        System.out.println("  6. Pengujian 4+ Skenario Polymorphism Berhasil Sempurna               [TERPENUHI]");
        System.out.println("  7. Seluruh Fitur P1-P6 Tetap Terjaga dan Terintegrasi Utuh            [TERPENUHI]");
        System.out.println("  STATUS KETERCAPAIAN SPRINT 7 : 100% SUKSES (DEFINITION OF DONE TERCAPAI)");
        System.out.println("================================================================================");
    }

    private static void cetakHeaderUtama() {
        System.out.println("================================================================================");
        System.out.println("             AUTORENT SYSTEM - MODUL 7: ABSTRAKSI & INTERFACE                   ");
        System.out.println("       PROJECT BASED LEARNING + AGILE SPRINT FRAMEWORK (SPRINT 7)              ");
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println(" Nama Mahasiswa : Ahmad Yasar Maulana Dais                                      ");
        System.out.println(" NRP            : 3125522018                                                    ");
        System.out.println(" Program Studi  : D3 Teknik Informatika - PENS PSDKU Sumenep (2026)             ");
        System.out.println(" Dosen Pengampu : Nirwana Haidar Hari, S.Pd., M.Kom.                            ");
        System.out.println(" Topik Modul 7  : Abstract Class, Abstract Method, Interface & Polymorphism    ");
        System.out.println("================================================================================\n");
    }
}

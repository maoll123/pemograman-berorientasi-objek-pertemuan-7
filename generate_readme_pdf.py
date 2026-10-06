import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

sys.stdout.reconfigure(encoding='utf-8')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#003366"))
        
        # Header (Only on pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 11 * 72 - 36, "AutoRent System — Sprint 7: Abstraction & Interface | Ahmad Yasar M. D. (3125522018)")
            self.setStrokeColor(colors.HexColor("#003366"))
            self.setLineWidth(0.5)
            self.line(54, 11 * 72 - 40, 8.5 * 72 - 54, 11 * 72 - 40)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#666666"))
        self.drawString(54, 32, "Praktikum PBO 2026 — PENS PSDKU Sumenep | Modul 7: Abstract Class & Interface")
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(8.5 * 72 - 54, 32, page_text)
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 42, 8.5 * 72 - 54, 42)
        
        self.restoreState()

def build_readme_pdf():
    pdf_path = os.path.join("P7_3125522018_Ahmad Yasar Maulana Dais", "README.pdf")
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=44,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        alignment=1, # Center
        textColor=colors.HexColor('#003366')
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        alignment=1,
        textColor=colors.HexColor('#005599')
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        spaceBefore=5,
        spaceAfter=3,
        textColor=colors.HexColor('#003366')
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#222222')
    )

    body_bold = ParagraphStyle(
        'BodyDarkBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.2,
        textColor=colors.HexColor('#222222')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#003366')
    )

    story = []

    # =========================================================================
    # HALAMAN 1: NAMA PROYEK, SPRINT GOAL, SPRINT BACKLOG, & AUDIT DESAIN P6
    # =========================================================================
    story.append(Paragraph("MODUL 7 — ABSTRACT CLASS, ABSTRACT METHOD, DAN INTERFACE", title_style))
    story.append(Paragraph("DOKUMEN RESMI SPRINT ARTIFACT & RINGKASAN PRAKTIKUM (README)", subtitle_style))
    story.append(Spacer(1, 4))

    # Info Mahasiswa Box
    mhs_data = [
        [Paragraph("<b>Proyek</b>: AutoRent System (Sprint 7)", table_cell_style),
         Paragraph("<b>Nama / NRP</b>: Ahmad Yasar Maulana Dais / 3125522018", table_cell_style)],
        [Paragraph("<b>Mata Kuliah</b>: Praktikum PBO (2026)", table_cell_style),
         Paragraph("<b>Dosen</b>: Nirwana Haidar Hari, S.Pd., M.Kom.", table_cell_style)]
    ]
    t_mhs = Table(mhs_data, colWidths=[240, 290])
    t_mhs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F4F8')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D8E0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_mhs)
    story.append(Spacer(1, 4))

    # Sprint Goal Callout
    sg_text = (
        "<b>📌 Sprint Goal Sprint 7:</b> Mengembangkan desain proyek P6 dengan menerapkan abstract class "
        "(Kendaraan, Person) dan interface (DapatDilacak, Perawatan, Cetakable) sehingga struktur class lebih jelas, "
        "mencegah instansiasi objek konseptual secara langsung, perilaku objek memiliki kontrak yang konsisten, "
        "dan seluruh fitur P1-P6 tetap berjalan 100% tanpa regresi."
    )
    t_sg = Table([[Paragraph(sg_text, body_style)]], colWidths=[530])
    t_sg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF3FA')),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor('#005599')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sg)
    story.append(Spacer(1, 4))

    # 1. Sprint Backlog
    story.append(Paragraph("1. Sprint Backlog P7 (7/7 Selesai - 100%)", h1_style))
    sb_data = [
        [Paragraph("ID", table_header_style), Paragraph("Aktivitas Sprint Backlog", table_header_style),
         Paragraph("Deliverable / Output", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("SB-01", table_cell_bold), Paragraph("Audit hierarchy dan behavior proyek P6", table_cell_style), Paragraph("Matriks identifikasi abstract class & interface", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-02", table_cell_bold), Paragraph("Menentukan kandidat abstract class", table_cell_style), Paragraph("Kendaraan dan Person didefinisikan abstract", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-03", table_cell_bold), Paragraph("Menentukan abstract method wajib", table_cell_style), Paragraph("hitungEstimasiBiaya(), tampilkanSpesifikasi(), dll", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-04", table_cell_bold), Paragraph("Menentukan kandidat interface sistem", table_cell_style), Paragraph("DapatDilacak, Perawatan, Cetakable", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-05", table_cell_bold), Paragraph("Memperbarui UML class diagram", table_cell_style), Paragraph("UML Modul 7 (Generalization & Realization)", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-06", table_cell_bold), Paragraph("Mengimplementasikan abstract class & interface", table_cell_style), Paragraph("17 Source file Java di src/ (0 error kompilasi)", table_cell_style), Paragraph("DONE", table_cell_bold)],
        [Paragraph("SB-07", table_cell_bold), Paragraph("Menguji polymorphism dan program", table_cell_style), Paragraph("Main.java (8 Fase Pengujian Sukses 100%)", table_cell_style), Paragraph("DONE", table_cell_bold)]
    ]
    t_sb = Table(sb_data, colWidths=[35, 175, 260, 60])
    t_sb.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_sb)
    story.append(Spacer(1, 4))

    # 2. Tabel Audit Desain P6
    story.append(Paragraph("2. Bagian A — Tabel Audit Desain P6 (Refactoring Abstraction & Interface)", h1_style))
    audit_data = [
        [Paragraph("Class / Behavior", table_header_style), Paragraph("Kondisi P6", table_header_style),
         Paragraph("Rencana P7", table_header_style), Paragraph("Alasan Perubahan Desain Arsitektural", table_header_style)],
        [Paragraph("Kendaraan", table_cell_bold), Paragraph("Class biasa (Concrete)", table_cell_style), Paragraph("Abstract class", table_cell_bold), Paragraph("Hanya konsep umum armada. Tidak boleh di-new langsung karena armada riil selalu Mobil, Motor, Minibus.", table_cell_style)],
        [Paragraph("Person", table_cell_bold), Paragraph("Class biasa (Concrete)", table_cell_style), Paragraph("Abstract class", table_cell_bold), Paragraph("Hanya kerangka identitas manusia. User sistem selalu berwujud Pelanggan atau Pegawai.", table_cell_style)],
        [Paragraph("hitungEstimasiBiaya()", table_cell_bold), Paragraph("Method biasa", table_cell_style), Paragraph("Abstract method", table_cell_bold), Paragraph("Tiap armada memiliki formula kalkulasi tarif, diskon durasi, dan surcharge unik.", table_cell_style)],
        [Paragraph("tampilkanSpesifikasi()", table_cell_bold), Paragraph("Method biasa", table_cell_style), Paragraph("Abstract method", table_cell_bold), Paragraph("Tiap armada menyajikan atribut unik (Mobil: AC/transmisi, Motor: bagasi helm, Minibus: izin trayek).", table_cell_style)],
        [Paragraph("tampilkanProfil()", table_cell_bold), Paragraph("Method biasa pada Person", table_cell_style), Paragraph("Abstract method", table_cell_bold), Paragraph("Pelanggan menyajikan saldo & diskon member, Pegawai menyajikan NIK, jabatan & total gaji.", table_cell_style)],
        [Paragraph("DapatDilacak", table_cell_bold), Paragraph("Belum ada", table_cell_style), Paragraph("Interface", table_cell_bold), Paragraph("Kontrak telematika GPS IoT yang dapat diterapkan pada Kendaraan dan Pegawai (lintas hierarki).", table_cell_style)],
        [Paragraph("Perawatan & Cetakable", table_cell_bold), Paragraph("Belum ada", table_cell_style), Paragraph("Interface", table_cell_bold), Paragraph("Standarisasi pemeliharaan unit armada serta standarisasi format cetak kuitansi, kartu & slip gaji.", table_cell_style)]
    ]
    t_aud = Table(audit_data, colWidths=[95, 80, 80, 275])
    t_aud.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_aud)

    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 2: CLASS DIAGRAM TERBARU, ABSTRACT CLASS, ABSTRACT METHOD, & INTERFACE
    # =========================================================================
    story.append(Paragraph("HALAMAN 2: ARSITEKTUR UML CLASS DIAGRAM, ABSTRACT CLASS & INTERFACE", title_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. UML Class Diagram Arsitektur Modul 7 (Generalization & Realization)", h1_style))
    
    uml_box = (
        "+---------------------------------------------------------------------------------------+\n"
        "|                 <<abstract>> Kendaraan                <<abstract>> Person             |\n"
        "| - noPlat, merk, model, tarif, mesin (◆ Mesin)       - id, nama, telp, email           |\n"
        "| + <<abstract>> hitungEstimasiBiaya(durasi): double  + <<abstract>> tampilkanProfil()  |\n"
        "| + <<abstract>> tampilkanSpesifikasi(): void         + <<abstract>> hitungKompensasi() |\n"
        "+---------------------------------------------------------------------------------------+\n"
        "          △ (extends)                                             △ (extends)            \n"
        "    ┌─────┴──────────────────┐                               ┌────┴─────────────────┐    \n"
        "  Mobil    Motor    Minibus  │                             Pelanggan    Pegawai     │    \n"
        "    │        │         │     │                                 │           │        │    \n"
        "    ┆        ┆         ┆ (implements)                          ┆           ┆(implements) \n"
        "    └────────┼─────────┼─────┴──────────┐                      ┆           │        │    \n"
        "             ▼                          ▼                      ▼           ▼        │    \n"
        "  <<interface>> DapatDilacak   <<interface>> Perawatan   <<interface>> Cetakable <──┘    \n"
        "  + getLokasi(): String        + lakukanServis(): void   + formatCetakDokumen(): String  \n"
        "  + perbaruiLokasi(k, area)    + cekKelayakan(): boolean + generateRingkasan(): String   \n"
        "  + getStatusGPS(): String     + getJadwalServis(): Str                                  \n"
        "+---------------------------------------------------------------------------------------+\n"
        "| Relasi Tambahan: GarasiArmada (◇ Agregasi Kendaraan) | TransaksiSewa (Asosiasi Person/|\n"
        "| Kendaraan & ◆ DetailItemBiaya & implements Cetakable) | KuitansiPrinter ..> Cetakable  |\n"
        "+---------------------------------------------------------------------------------------+"
    )
    p_uml = Preformatted(uml_box, ParagraphStyle('CodePre', fontName='Courier', fontSize=6.5, leading=7.5, textColor=colors.HexColor('#002244')))
    t_up = Table([[p_uml]], colWidths=[530])
    t_up.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F4F6F9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_up)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. Rincian Implementasi Abstract Class & Abstract Method", h1_style))
    abs_impl_data = [
        [Paragraph("Komponen Abstraksi", table_header_style), Paragraph("Daftar Anggota & Signature", table_header_style), Paragraph("Peran & Implementasi pada Subclass", table_header_style)],
        [Paragraph("<b><<abstract>> Kendaraan</b>", table_cell_style),
         Paragraph("• <i>Atribut</i>: noPlat, merk, model, tarifPerHari, mesin<br/>"
                   "• <i>Konstruktor</i>: Kendaraan(...) + Chaining<br/>"
                   "• <b>abstract double hitungEstimasiBiaya(int)</b><br/>"
                   "• <b>abstract void tampilkanSpesifikasi()</b><br/>"
                   "• <b>abstract String getTipeKendaraan()</b><br/>"
                   "• <i>Overload</i>: hitungEstimasiBiaya(durasi, diskon)", table_cell_style),
         Paragraph("• <b>Mobil</b>: Diskon > 7 hari (10%), > 3 hari (5%). Transmisi & AC.<br/>"
                   "• <b>Motor</b>: Diskon > 5 hari (12%), > 2 hari (6%). Helm & Jas Hujan.<br/>"
                   "• <b>Minibus</b>: Diskon paket rombongan (8%) + Surcharge harian komersial Rp 50.000. Kursi 8-30 & Izin Dishub.", table_cell_style)],
        [Paragraph("<b><<abstract>> Person</b>", table_cell_style),
         Paragraph("• <i>Atribut</i>: id, nama, nomorTelepon, alamat, email<br/>"
                   "• <b>abstract void tampilkanProfil()</b><br/>"
                   "• <b>abstract String getDeskripsiPeran()</b><br/>"
                   "• <b>abstract double hitungKompensasi()</b>", table_cell_style),
         Paragraph("• <b>Pelanggan</b>: Nomor KTP, Saldo deposit, tingkatan Member (Gold/Platinum), reward cashback loyalti.<br/>"
                   "• <b>Pegawai</b>: NIK, Posisi jabatan, Gaji Pokok + Bonus transaksi.", table_cell_style)]
    ]
    t_abs = Table(abs_impl_data, colWidths=[110, 210, 210])
    t_abs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_abs)
    story.append(Spacer(1, 4))

    story.append(Paragraph("3. Rincian Interface Sistem & Alasan Perubahan Desain", h1_style))
    if_impl_data = [
        [Paragraph("Interface", table_header_style), Paragraph("Method Kontrak", table_header_style),
         Paragraph("Class Implementor", table_header_style), Paragraph("Justifikasi & Alasan Desain", table_header_style)],
        [Paragraph("<b>DapatDilacak</b>", table_cell_bold),
         Paragraph("• getLokasi(): String<br/>• perbaruiLokasi(k, area)<br/>• getStatusGPS(): String<br/>• default pingTelematika()", table_cell_style),
         Paragraph("Mobil, Motor, Minibus, <b>Pegawai</b> (Lintas Hierarki)", table_cell_style),
         Paragraph("Menyediakan kontrak telematika IoT GPS yang seragam untuk memantau armada sewa dan kurir/driver lapangan.", table_cell_style)],
        [Paragraph("<b>Perawatan</b>", table_cell_bold),
         Paragraph("• lakukanServis(): void<br/>• cekKelayakan(): boolean<br/>• getJadwalServis(): String", table_cell_style),
         Paragraph("Mobil, Motor, Minibus", table_cell_style),
         Paragraph("Menstandarkan SOP servis berkala dan uji kelaikan jalan raya bagi armada garasi rental.", table_cell_style)],
        [Paragraph("<b>Cetakable</b>", table_cell_bold),
         Paragraph("• formatCetakDokumen()<br/>• generateRingkasan()", table_cell_style),
         Paragraph("TransaksiSewa, Pelanggan, Pegawai, Mobil, Motor, Minibus", table_cell_style),
         Paragraph("Mendukung Interface Dependency Injection pada KuitansiPrinter untuk mencetak dokumen apa pun.", table_cell_style)]
    ]
    t_if = Table(if_impl_data, colWidths=[70, 150, 120, 190])
    t_if.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_if)

    story.append(PageBreak())

    # =========================================================================
    # HALAMAN 3: LOG RUNNING, TABEL PENGUJIAN, SPRINT REVIEW & SPRINT RETROSPECTIVE
    # =========================================================================
    story.append(Paragraph("HALAMAN 3: PENGUJIAN POLYMORPHISM, SPRINT REVIEW & RETROSPECTIVE", title_style))
    story.append(Spacer(1, 4))

    # 1. Log Eksekusi Konsol
    story.append(Paragraph("1. Cuplikan Hasil Eksekusi Terminal Java (Main.java)", h1_style))
    log_sample = (
        "[FASE 1] Kendaraan & Person berstatus 'abstract' -> Mencegah instansiasi langsung (Compile Check PASSED)\n"
        "[FASE 2] 5 Subclass konkret (Mobil, Motor, Minibus, Pelanggan, Pegawai) berhasil diinstansiasi 100%.\n"
        "[FASE 3] Dynamic Method Dispatch via Superclass Reference: refK1(Mobil: Rp 1.900.000), refK2(Motor: Rp 705.000), refK3(Minibus: Rp 5.750.000)\n"
        "[FASE 4] Interface Polymorphism DapatDilacak[]: Mobil terpantau di Pelabuhan Kalianget, Pegawai di Pos Layanan Kalianget.\n"
        "[FASE 5] Heterogeneous List<Cetakable>: 4 entitas beda hierarki berhasil digenerate ringkasannya secara polimorfis.\n"
        "[FASE 6] Overloading & Defensive Boundary: Diskon >50%, Top-up negatif, Minibus kursi <8 berhasil ditangkap 100%.\n"
        "[FASE 7] End-to-End Business Flow: Transaksi TRX-2026-001 Lunas via VA Mandiri (Rp 1.403.000), Kuitansi Resmi Tercetak via Printer.\n"
        "[FASE 8] Definition of Done: 15/15 Kriteria Terpenuhi (100% SUKSES)."
    )
    p_log = Preformatted(log_sample, ParagraphStyle('LogPre', fontName='Courier', fontSize=6.2, leading=7.5, textColor=colors.HexColor('#D4D4D4')))
    t_log = Table([[p_log]], colWidths=[530])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E1E1E')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#333333')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_log)
    story.append(Spacer(1, 4))

    # 2. Tabel Pengujian
    story.append(Paragraph("2. Matriks Pengujian Polymorphism (Modul 7 Bagian F)", h1_style))
    uj_data = [
        [Paragraph("No", table_header_style), Paragraph("Skenario Pengujian", table_header_style),
         Paragraph("Hasil yang Diharapkan", table_header_style), Paragraph("Hasil Aktual", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("1", table_cell_bold), Paragraph("Audit Larangan Instansiasi Abstract Class", table_cell_style), Paragraph("Instansiasi new Kendaraan() dicegah", table_cell_style), Paragraph("Compiler error saat new class abstrak", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("2", table_cell_bold), Paragraph("Instansiasi 5 Subclass Konkret", table_cell_style), Paragraph("Objek subclass berhasil dialokasi di Heap", table_cell_style), Paragraph("5 Objek konkret terbuat sempurna", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("3", table_cell_bold), Paragraph("Abstract Method via Superclass Ref", table_cell_style), Paragraph("Dynamic method dispatch ke subclass", table_cell_style), Paragraph("Kalkulasi tarif spesifik Mobil/Motor/Bus", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("4", table_cell_bold), Paragraph("Method via Interface Reference", table_cell_style), Paragraph("Interface polymorphism lintas hierarki", table_cell_style), Paragraph("GPS Mobil & Pegawai terupdate akurat", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("5", table_cell_bold), Paragraph("Heterogeneous Collection Iteration", table_cell_style), Paragraph("Setiap objek menjalankan formatnya sendiri", table_cell_style), Paragraph("List<Cetakable> mencetak ringkasan", table_cell_style), Paragraph("PASSED", table_cell_bold)]
    ]
    t_uj = Table(uj_data, colWidths=[20, 160, 160, 140, 50])
    t_uj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_uj)
    story.append(Spacer(1, 4))

    # 3. Sprint Review & Retrospective Side-by-Side / Compact
    story.append(Paragraph("3. Sprint Review & Sprint Retrospective Evaluasi", h1_style))
    
    rev_summary = (
        "<b>Checklist Sprint Review (7/7 Terverifikasi):</b><br/>"
        "✔ Abstract class berhasil dibuat (Kendaraan & Person)<br/>"
        "✔ Abstract method diimplementasikan konsisten di seluruh subclass<br/>"
        "✔ 5 Subclass konkret (Mobil, Motor, Minibus, Pelanggan, Pegawai) aktif<br/>"
        "✔ 3 Interface (DapatDilacak, Perawatan, Cetakable) berhasil direalisasikan<br/>"
        "✔ Class diagram konsisten & sesuai dengan kode sumber<br/>"
        "✔ Pengujian polymorphism berhasil pada superclass & interface<br/>"
        "✔ Seluruh fitur proyek sebelumnya (P1-P6) tetap berjalan normal (Zero Regression)"
    )
    
    retro_summary = (
        "<b>Sprint Retrospective (Refleksi Iterasi 7):</b><br/>"
        "• <i>What Went Well?</i> Abstraction berhasil mengeliminasi instansiasi ilegal entitas umum. Multi-interface realization memungkinkan telematika GPS lintas hierarki secara modular.<br/>"
        "• <i>What Went Wrong?</i> Penyesuaian antarmuka Cetakable memerlukan standarisasi format teks yang fleksibel untuk kuitansi, kartu member, dan slip gaji.<br/>"
        "• <i>Improvement Next Sprint:</i> Menyiapkan penguasaan menyeluruh P1-P7 untuk Evaluasi UTS Praktikum P8 serta perancangan antarmuka GUI / Database pada P9."
    )

    t_eval = Table([
        [Paragraph(rev_summary, table_cell_style), Paragraph(retro_summary, table_cell_style)]
    ], colWidths=[260, 270])
    t_eval.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F0F8F0')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#FDFBF7')),
        ('BOX', (0,0), (0,0), 0.5, colors.HexColor('#006600')),
        ('BOX', (1,0), (1,0), 0.5, colors.HexColor('#CC8800')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_eval)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated 3-page README.pdf: {pdf_path}")

if __name__ == "__main__":
    build_readme_pdf()

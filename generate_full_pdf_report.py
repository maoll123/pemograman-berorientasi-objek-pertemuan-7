import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Preformatted, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

sys.stdout.reconfigure(encoding='utf-8')

class FullNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(FullNumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(FullNumberedCanvas, self).showPage()
        super(FullNumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#003366"))
        
        # Header (Only on pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 11 * 72 - 32, "Laporan Praktikum PBO — Modul 7: Abstract Class & Interface | Ahmad Yasar M. D. (3125522018)")
            self.setStrokeColor(colors.HexColor("#003366"))
            self.setLineWidth(0.5)
            self.line(40, 11 * 72 - 36, 8.5 * 72 - 40, 11 * 72 - 36)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#666666"))
        self.drawString(40, 26, "D3 Teknik Informatika - PENS PSDKU Sumenep (2026) | AutoRent System (Sprint 7)")
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(8.5 * 72 - 40, 26, page_text)
        self.setStrokeColor(colors.HexColor("#D0D0D0"))
        self.setLineWidth(0.5)
        self.line(40, 36, 8.5 * 72 - 40, 36)
        
        self.restoreState()

def build_full_pdf_report():
    pdf_path = "Laporan_Praktikum_PBO_Modul_7_AutoRent.pdf"

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=44,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        alignment=1,
        textColor=colors.HexColor('#003366')
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#005599')
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14,
        spaceBefore=10,
        spaceAfter=4,
        textColor=colors.HexColor('#003366'),
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        spaceBefore=7,
        spaceAfter=3,
        textColor=colors.HexColor('#005599'),
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#222222')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#003366')
    )

    code_title_style = ParagraphStyle(
        'CodeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=colors.HexColor('#003366'),
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )

    story = []

    # Title Banner
    story.append(Paragraph("LAPORAN PRAKTIKUM PEMROGRAMAN BERORIENTASI OBYEK", title_style))
    story.append(Paragraph("MODUL 7: ABSTRACT CLASS, ABSTRACT METHOD, DAN INTERFACE", subtitle_style))
    story.append(Paragraph("PROJECT BASED LEARNING + AGILE SPRINT FRAMEWORK (SPRINT 7)", ParagraphStyle('SubSub', parent=subtitle_style, fontSize=9, textColor=colors.HexColor('#555555'))))
    story.append(Spacer(1, 6))

    # Info Table
    info_data = [
        [Paragraph("Informasi Akademik", table_header_style), Paragraph("Keterangan Terperinci", table_header_style)],
        [Paragraph("<b>Mata Kuliah</b>", table_cell_style), Paragraph("Praktikum Pemrograman Berorientasi Obyek (PBO)", table_cell_style)],
        [Paragraph("<b>Dosen Pengampu</b>", table_cell_style), Paragraph("Nirwana Haidar Hari, S.Pd., M.Kom.", table_cell_style)],
        [Paragraph("<b>Nama Mahasiswa / NRP</b>", table_cell_style), Paragraph("Ahmad Yasar Maulana Dais / 3125522018", table_cell_style)],
        [Paragraph("<b>Program Studi & Kampus</b>", table_cell_style), Paragraph("D3 Teknik Informatika - PENS PSDKU Sumenep (2026)", table_cell_style)],
        [Paragraph("<b>Nama Proyek & Modul</b>", table_cell_style), Paragraph("AutoRent System – Sprint 7: Abstraction, Abstract Method, Interface & Polymorphism", table_cell_style)]
    ]
    t_info = Table(info_data, colWidths=[180, 350])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D8E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 8))

    # BAB I
    story.append(Paragraph("BAB I: TUJUAN PRAKTIKUM & FONDASI AGILE SPRINT (SPRINT 7)", h1_style))
    story.append(Paragraph("1.1 Tujuan Praktikum (Capaian Pembelajaran Modul 7)", h2_style))
    story.append(Paragraph(
        "Berdasarkan Buku Panduan Resmi Modul 7 Praktikum Pemrograman Berorientasi Obyek (PBO) Politeknik Elektronika Negeri Surabaya (PENS) PSDKU Sumenep, capaian pembelajaran yang wajib dikuasai dan dibuktikan pada praktikum ini adalah:<br/>"
        "a. Mampu membedakan secara fundamental karakteristik dan tujuan perancangan antara class biasa (concrete class), abstract class, dan interface.<br/>"
        "b. Mampu membuat dan mendeklarasikan abstract class yang memiliki konstruktor, atribut umum, method konkret, dan abstract method.<br/>"
        "c. Mampu mengimplementasikan abstract method secara konsisten dan adaptif pada seluruh subclass konkret (Mobil, Motor, Minibus, Pelanggan, Pegawai).<br/>"
        "d. Mampu membuat antarmuka (interface) dan menerapkannya pada class menggunakan keyword implements, termasuk pemanfaatan default method Java modern.<br/>"
        "e. Mampu membuktikan dan mengoperasikan mekanisme Dynamic Polymorphism melalui Superclass Abstract Reference dan Interface Reference lintas hierarki pewarisan.<br/>"
        "f. Mampu melakukan refactoring fungsional terhadap proyek hasil Pertemuan 6 (AutoRent System) berdasarkan prinsip Abstraction tanpa merusak struktur relasi objek sebelumnya.<br/>"
        "g. Mampu melaksanakan Sprint Review dan Sprint Retrospective secara profesional sebagai bagian dari kerangka kerja pengembangan perangkat lunak Agile Scrum.",
        body_style
    ))

    story.append(Paragraph("1.2 Review P6 dan Jembatan Arsitektural Menuju P7", h2_style))
    story.append(Paragraph(
        "Pada praktikum Pertemuan 6 (P6), proyek AutoRent System telah berhasil direfaktor dengan menerapkan konsep Dynamic Polymorphism, Method Overriding, Method Overloading, dan Dynamic Binding. Hierarki class telah terspesialisasi menjadi Superclass Kendaraan (dengan Subclass Mobil, Motor, Minibus) dan Superclass Person (dengan Subclass Pelanggan dan Pegawai), di samping mempertahankan seluruh relasi objek P4 seperti Komposisi (Mesin dan DetailItemBiaya), Agregasi (GarasiArmada), Asosiasi (TransaksiSewa), serta Dependency (KuitansiPrinter dan LayananNotifikasi).<br/><br/>"
        "Meskipun demikian, evaluasi desain arsitektural pada P6 menunjukkan adanya celah perancangan yang krusial: Superclass Kendaraan dan Person pada P6 masih berupa concrete class (class biasa). Hal ini memungkinkan terjadinya instansiasi objek langsung seperti new Kendaraan(...) atau new Person(...). Di dunia nyata bisnis rental armada, tidak pernah ada 'kendaraan tanpa wujud konkrit' yang beroperasi di jalan raya, maupun 'manusia tanpa peran spesifik' dalam sistem. Seluruh armada riil selalu berwujud Mobil, Motor, atau Minibus, dan seluruh manusia selalu berperan sebagai Pelanggan atau Pegawai.<br/><br/>"
        "Sesuai instruksi resmi Modul 7, mahasiswa TIDAK membuat proyek baru dari nol, melainkan melanjutkan dan menyempurnakan proyek AutoRent System hasil P6. Fokus utama Sprint 7 adalah melakukan evolusi arsitektural menuju tahapan Abstraction: mentransformasikan superclass konseptual menjadi Abstract Class murni, mengubah method bervariasi menjadi Abstract Method wajib, serta mengekstrak antarmuka kontrak perilaku umum (Interface DapatDilacak, Perawatan, Cetakable) guna mewujudkan arsitektur yang decoupled, modular, dan standar industri.",
        body_style
    ))

    story.append(Paragraph("1.3 Agile Sprint Framework (Sprint Goal & Sprint Backlog Modul 7)", h2_style))
    sg_call = (
        "<b>📌 Sprint Goal Sprint 7:</b> Mengembangkan desain proyek P6 dengan menerapkan abstract class dan interface yang sesuai "
        "sehingga struktur class lebih jelas, perilaku object memiliki kontrak yang konsisten, mencegah instansiasi entitas umum secara langsung, "
        "mendukung multiple interface realization lintas hierarki, dan program tetap dapat dijalankan secara terintegrasi 100%."
    )
    t_sg_call = Table([[Paragraph(sg_call, body_style)]], colWidths=[530])
    t_sg_call.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF3FA')),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor('#005599')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sg_call)
    story.append(Spacer(1, 4))

    # Sprint Backlog Table
    sb_data = [
        [Paragraph("ID Backlog", table_header_style), Paragraph("Deskripsi Aktivitas Sprint Backlog", table_header_style),
         Paragraph("Target Deliverable", table_header_style), Paragraph("Status Akhir", table_header_style)],
        [Paragraph("SB-01", table_cell_bold), Paragraph("Audit hierarchy dan behavior proyek P6", table_cell_style), Paragraph("Matriks Audit Abstraksi & Celah Desain", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-02", table_cell_bold), Paragraph("Menentukan kandidat abstract class", table_cell_style), Paragraph("Spesifikasi Abstract Class Kendaraan & Person", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-03", table_cell_bold), Paragraph("Menentukan abstract method wajib", table_cell_style), Paragraph("Daftar Abstract Method pada Kendaraan & Person", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-04", table_cell_bold), Paragraph("Menentukan kandidat interface sistem", table_cell_style), Paragraph("Definisi DapatDilacak, Perawatan, Cetakable", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-05", table_cell_bold), Paragraph("Memperbarui UML Class Diagram", table_cell_style), Paragraph("UML Diagram Modul 7 (Generalization & Realization)", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-06", table_cell_bold), Paragraph("Mengimplementasikan abstract class dan interface", table_cell_style), Paragraph("17 File Source Code Java (src/) Terintegrasi", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)],
        [Paragraph("SB-07", table_cell_bold), Paragraph("Menguji polymorphism dan program", table_cell_style), Paragraph("Test Suite Main.java (8 Fase Pengujian Sukses)", table_cell_style), Paragraph("DONE (100%)", table_cell_bold)]
    ]
    t_sb = Table(sb_data, colWidths=[45, 175, 230, 80])
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

    story.append(Paragraph("1.4 Bagian A – Audit Desain P6 (Refactoring Abstraction & Interface)", h2_style))
    audit_data = [
        [Paragraph("Class / Behavior", table_header_style), Paragraph("Kondisi P6", table_header_style),
         Paragraph("Rencana P7", table_header_style), Paragraph("Alasan Perubahan Desain Arsitektural", table_header_style)],
        [Paragraph("Kendaraan", table_cell_bold), Paragraph("Class Biasa (Concrete)", table_cell_style), Paragraph("Abstract Class", table_cell_bold), Paragraph("Hanya konsep umum armada. Tidak boleh di-new langsung karena armada riil selalu Mobil, Motor, Minibus.", table_cell_style)],
        [Paragraph("Person", table_cell_bold), Paragraph("Class Biasa (Concrete)", table_cell_style), Paragraph("Abstract Class", table_cell_bold), Paragraph("Hanya kerangka data identitas manusia. Pengguna sistem selalu berwujud Pelanggan atau Pegawai.", table_cell_style)],
        [Paragraph("hitungEstimasiBiaya()", table_cell_bold), Paragraph("Method Biasa", table_cell_style), Paragraph("Abstract Method", table_cell_bold), Paragraph("Setiap armada memiliki formula kalkulasi tarif, diskon durasi, dan surcharge operasional yang berbeda.", table_cell_style)],
        [Paragraph("tampilkanSpesifikasi()", table_cell_bold), Paragraph("Method Biasa", table_cell_style), Paragraph("Abstract Method", table_cell_bold), Paragraph("Setiap armada menyajikan spesifikasi unik (Mobil: AC/transmisi, Motor: bagasi helm, Minibus: izin trayek).", table_cell_style)],
        [Paragraph("tampilkanProfil() & hitungKompensasi()", table_cell_bold), Paragraph("Method Biasa pada Person", table_cell_style), Paragraph("Abstract Method", table_cell_bold), Paragraph("Pelanggan menyajikan saldo & diskon member, Pegawai menyajikan NIK, jabatan, dan slip total gaji.", table_cell_style)],
        [Paragraph("DapatDilacak", table_cell_bold), Paragraph("Belum Ada", table_cell_style), Paragraph("Interface", table_cell_bold), Paragraph("Mendefinisikan kontrak telematika GPS IoT yang diterapkan pada Kendaraan dan Pegawai (lintas hierarki).", table_cell_style)],
        [Paragraph("Perawatan & Cetakable", table_cell_bold), Paragraph("Belum Ada", table_cell_style), Paragraph("Interface", table_cell_bold), Paragraph("Standarisasi pemeliharaan unit armada serta standarisasi format cetak dokumen resmi (kuitansi, kartu, slip gaji).", table_cell_style)]
    ]
    t_aud = Table(audit_data, colWidths=[90, 80, 80, 280])
    t_aud.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_aud)
    story.append(Spacer(1, 8))

    # BAB II
    story.append(Paragraph("BAB II: KAJIAN TEORI & PERANCANGAN ARSITEKTUR ABSTRAKSI & INTERFACE", h1_style))
    story.append(Paragraph("2.1 Konsep Abstraksi & Abstract Class", h2_style))
    story.append(Paragraph(
        "Abstraksi (Abstraction) adalah pilar OOP yang berfokus pada penyajian esensi fungsionalitas suatu objek dengan menyembunyikan kompleksitas detail implementasi internal. Abstract Class berfungsi sebagai kerangka dasar konsep umum yang tidak dapat diinstansiasi secara langsung menggunakan kata kunci 'new', namun dapat memiliki atribut, konstruktor (yang dipanggil melalui constructor chaining super(...)), method konkret, serta abstract method.",
        body_style
    ))

    story.append(Paragraph("2.2 Konsep & Karakteristik Abstract Method", h2_style))
    story.append(Paragraph(
        "Abstract Method adalah method yang hanya memiliki deklarasi signature tanpa tubuh implementasi (body), diakhiri dengan titik koma (;). Seluruh subclass konkret diwajibkan meng-override seluruh abstract method yang diwarisinya dari abstract class. Hal ini menjamin bahwa seluruh objek turunan memiliki antarmuka pemanggilan yang konsisten namun mengeksekusi logika bisnis yang terspesialisasi (Dynamic Method Dispatch).",
        body_style
    ))

    story.append(Paragraph("2.3 Konsep Interface & Multiple Realization", h2_style))
    story.append(Paragraph(
        "Interface adalah kontrak perilaku murni yang mendefinisikan apa yang harus dapat dilakukan oleh suatu class (relasi 'can-do'). Berbeda dengan pewarisan class yang bersifat tunggal (single inheritance), Java mendukung Multiple Interface Realization di mana satu class dapat mengimplementasikan banyak interface sekaligus menggunakan kata kunci 'implements'. Interface juga mendukung fitur Java 8+ seperti default method dan static method.",
        body_style
    ))

    story.append(Paragraph("2.4 Matriks Perbandingan: Concrete Class vs Abstract Class vs Interface", h2_style))
    matriks_data = [
        [Paragraph("Dimensi Pembanding", table_header_style), Paragraph("Concrete Class", table_header_style), Paragraph("Abstract Class", table_header_style), Paragraph("Interface", table_header_style)],
        [Paragraph("Tujuan Utama", table_cell_bold), Paragraph("Entitas nyata siap pakai", table_cell_style), Paragraph("Konsep umum & berbagi logika", table_cell_style), Paragraph("Kontrak perilaku murni", table_cell_style)],
        [Paragraph("Instansiasi (new)", table_cell_bold), Paragraph("Bisa di-new langsung", table_cell_style), Paragraph("TIDAK BISA di-new", table_cell_style), Paragraph("TIDAK BISA di-new", table_cell_style)],
        [Paragraph("Keyword", table_cell_bold), Paragraph("class & extends", table_cell_style), Paragraph("abstract class & extends", table_cell_style), Paragraph("interface & implements", table_cell_style)],
        [Paragraph("Atribut Instance", table_cell_bold), Paragraph("Bebas (semua modifier)", table_cell_style), Paragraph("Bebas (mendukung state)", table_cell_style), Paragraph("Hanya public static final", table_cell_style)],
        [Paragraph("Konstruktor", table_cell_bold), Paragraph("Memiliki konstruktor", table_cell_style), Paragraph("Memiliki konstruktor (super)", table_cell_style), Paragraph("TIDAK memiliki konstruktor", table_cell_style)],
        [Paragraph("Implementasi Method", table_cell_bold), Paragraph("Wajib semua konkret", table_cell_style), Paragraph("Konkret & Abstract method", table_cell_style), Paragraph("Deklarasi (atau default/static)", table_cell_style)],
        [Paragraph("Dukungan Pewarisan", table_cell_bold), Paragraph("Single inheritance", table_cell_style), Paragraph("Single inheritance", table_cell_style), Paragraph("Multiple realization", table_cell_style)]
    ]
    t_mat = Table(matriks_data, colWidths=[90, 140, 150, 150])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_mat)
    story.append(Spacer(1, 4))

    story.append(Paragraph("2.5 Hubungan Abstraksi dengan Polymorphism", h2_style))
    story.append(Paragraph(
        "Abstraksi dan Polymorphism adalah dua sisi mata uang yang saling melengkapi. Variabel referensi bertipe Abstract Superclass (seperti Kendaraan k = new Mobil(...)) atau bertipe Interface (seperti DapatDilacak p = new Pegawai(...)) memungkinkan penulisan kode program yang sangat fleksibel, modular, dan extensible. Pemanggilan method pada polymorphic reference secara dinamis diarahkan oleh JVM ke method milik objek aktual di heap memory (Dynamic Binding).",
        body_style
    ))

    story.append(Paragraph("2.6 Pembaruan UML Class Diagram (Modul 7 Architecture)", h2_style))
    uml_full = (
        "+---------------------------------------------------------------------------------------------------------+\n"
        "|                             📌 UML CLASS DIAGRAM MODUL 7 ARSITEKTUR LENGKAP                             |\n"
        "+---------------------------------------------------------------------------------------------------------+\n"
        "|                      <<abstract>> Kendaraan                                <<abstract>> Person          |\n"
        "| - noPlat: String, merk: String, model: String, tarif: double             - id, nama, telp, email, alamat|\n"
        "| - mesin: Mesin (◆ Komposisi)                                             + <<abs>> tampilkanProfil()    |\n"
        "| + <<abstract>> hitungEstimasiBiaya(durasi: int): double                  + <<abs>> hitungKompensasi()   |\n"
        "| + <<abstract>> tampilkanSpesifikasi(): void                              + <<abs>> getDeskripsiPeran()  |\n"
        "+---------------------------------------------------------------------------------------------------------+\n"
        "             △ (Generalization)                                                       △ (Generalization)   \n"
        "    ┌────────┼────────────────────────┐                                     ┌─────────┴─────────┐         \n"
        "  Mobil    Motor                   Minibus                               Pelanggan           Pegawai      \n"
        "    │        │                        │                                      │                  │         \n"
        "    ┆        ┆ (Realization)          ┆                                      ┆                  ┆         \n"
        "    └────────┼────────────────────────┼───────────────┐                      ┆                  │         \n"
        "             ▼                        ▼               │                      ▼                  ▼         \n"
        "  <<interface>> DapatDilacak   <<interface>> Perawatan│            <<interface>> Cetakable <────┘         \n"
        "  + getLokasi(): String        + lakukanServis()      │            + formatCetakDokumen(): String         \n"
        "  + perbaruiLokasi(k, area)    + cekKelayakan()       │            + generateRingkasan(): String          \n"
        "  + getStatusGPS(): String     + getJadwalServis()    │                                                   \n"
        "+-----------------------------------------------------+---------------------------------------------------+\n"
        "| GarasiArmada (◇ Agregasi Kendaraan) | TransaksiSewa (Asosiasi Person/Kendaraan, ◆ DetailItem, Cetakable)|\n"
        "| KuitansiPrinter (Service Dependency ..> Cetakable)  | LayananNotifikasi (Gateway Alert ..> Person/Pelacak)|\n"
        "+---------------------------------------------------------------------------------------------------------+"
    )
    p_uf = Preformatted(uml_full, ParagraphStyle('FullUml', fontName='Courier', fontSize=6.5, leading=7.5, textColor=colors.HexColor('#002244')))
    t_uf = Table([[p_uf]], colWidths=[530])
    t_uf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F4F6F9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_uf)
    story.append(Spacer(1, 8))

    # BAB III
    story.append(Paragraph("BAB III: IMPLEMENTASI KODE PROGRAM JAVA (SRC)", h1_style))
    story.append(Paragraph("3.1 Arsitektur Hierarki Source Code", h2_style))
    story.append(Paragraph(
        "Seluruh implementasi Java Modul 7 disusun dalam 17 file sumber yang bersih, teruji, bebas warning/error, dan terdokumentasi javadoc lengkap. Di bawah ini disajikan kode sumber lengkap masing-masing file:",
        body_style
    ))

    src_files = [
        ("DapatDilacak.java", "Interface Kontrak Telematika & GPS Tracking IoT"),
        ("Perawatan.java", "Interface Standarisasi Pemeliharaan & Uji Kelayakan Armada"),
        ("Cetakable.java", "Interface Standarisasi Format Dokumen Resmi (Kuitansi/Kartu/Slip)"),
        ("Person.java", "Abstract Superclass Abstraksi Entitas Manusia"),
        ("Kendaraan.java", "Abstract Superclass Abstraksi Armada Kendaraan Rental"),
        ("Mobil.java", "Subclass Konkret Mobil Penumpang"),
        ("Motor.java", "Subclass Konkret Sepeda Motor"),
        ("Minibus.java", "Subclass Konkret Minibus Travel"),
        ("Pelanggan.java", "Subclass Konkret Pelanggan Rental"),
        ("Pegawai.java", "Subclass Konkret Pegawai Operasional"),
        ("Mesin.java", "Komponen Komposisi Mesin Internal Kendaraan"),
        ("DetailItemBiaya.java", "Komponen Komposisi Baris Rincian Biaya Transaksi"),
        ("GarasiArmada.java", "Agregasi Polimorfis Pool Armada & Batch Interface Processing"),
        ("TransaksiSewa.java", "Sentral Orkestrasi Relasi Transaksi (implements Cetakable)"),
        ("KuitansiPrinter.java", "Service Utility Pencetakan Berbasis Interface Cetakable"),
        ("LayananNotifikasi.java", "Service Gateway Notifikasi Multi-Kanal & Telemetry"),
        ("Main.java", "Test Suite Utama & Driver Verifikasi 8 Fase Pengujian Modul 7")
    ]

    for fname, desc in src_files:
        fpath = os.path.join("src", fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as fp:
                code_text = fp.read()
        else:
            code_text = "// File not found"

        story.append(Paragraph(f"📄 File: {fname} — {desc}", code_title_style))
        p_c = Preformatted(code_text, ParagraphStyle('CodeBox', fontName='Courier', fontSize=6.5, leading=7.5, textColor=colors.HexColor('#222222'), backColor=colors.HexColor('#F8FAFD'), borderPadding=4, borderWidth=0.5, borderColor=colors.HexColor('#D0D8E0'), spaceAfter=4))
        story.append(p_c)
        story.append(Spacer(1, 4))

    # BAB IV
    story.append(Paragraph("BAB IV: PENGUJIAN SISTEM, TABEL PENGUJIAN POLYMORPHISM & LOG EKSEKUSI", h1_style))
    story.append(Paragraph("4.1 Skenario Pengujian Komprehensif (8 Fase)", h2_style))
    story.append(Paragraph(
        "Pengujian sistem dilakukan melalui 8 fase terstruktur di dalam Main.java untuk memastikan pemenuhan 100% kriteria Modul 7 Bagian F tanpa adanya regresi fitur P1–P6.",
        body_style
    ))

    story.append(Paragraph("4.2 Matriks & Tabel Pengujian Polymorphism", h2_style))
    uji_data = [
        [Paragraph("No", table_header_style), Paragraph("Skenario Pengujian", table_header_style),
         Paragraph("Eksekusi Kode / Input", table_header_style), Paragraph("Hasil yang Diharapkan", table_header_style),
         Paragraph("Hasil Aktual", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("1", table_cell_bold), Paragraph("Audit Larangan Instansiasi Abstract Class", table_cell_style), Paragraph("new Kendaraan(...), new Person(...)", table_cell_style), Paragraph("Compiler menolak pembuatan objek", table_cell_style), Paragraph("Terbukti dicegah compiler", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("2", table_cell_bold), Paragraph("Instansiasi Subclass Konkret", table_cell_style), Paragraph("5 Subclass konkret (Mobil, Motor, Bus, Plg, Pgw)", table_cell_style), Paragraph("Objek berhasil dibuat di Heap", table_cell_style), Paragraph("5 Objek konkret terbuat sempurna", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("3", table_cell_bold), Paragraph("Abstract Method via Superclass Ref", table_cell_style), Paragraph("Kendaraan refK = mobil; refK.tampilkanSpesifikasi();", table_cell_style), Paragraph("Dynamic method dispatch ke subclass", table_cell_style), Paragraph("Tereksekusi sesuai subclass konkrit", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("4", table_cell_bold), Paragraph("Method via Reference Interface", table_cell_style), Paragraph("DapatDilacak p = pegawai; p.getLokasi();", table_cell_style), Paragraph("Interface polymorphism lintas hierarki", table_cell_style), Paragraph("Lokasi GPS terupdate akurat", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("5", table_cell_bold), Paragraph("Heterogeneous Collection Iteration", table_cell_style), Paragraph("List<Cetakable> daftar = ...; generateRingkasan();", table_cell_style), Paragraph("Setiap objek mengeksekusi format sendiri", table_cell_style), Paragraph("4 Entitas beda tipe tercetak rapi", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("6", table_cell_bold), Paragraph("Method Overloading & Defensive Test", table_cell_style), Paragraph("hitungEstimasiBiaya(4, 20.0); tambahDeposit(-1000);", table_cell_style), Paragraph("Overloading sukses; validasi defensif aktif", table_cell_style), Paragraph("IllegalArgumentException tertangkap", table_cell_style), Paragraph("PASSED", table_cell_bold)],
        [Paragraph("7", table_cell_bold), Paragraph("End-to-End Flow & Service Dependency", table_cell_style), Paragraph("TransaksiSewa -> Bayar VA -> Selesai -> Printer", table_cell_style), Paragraph("Kuitansi resmi tercetak via interface Cetakable", table_cell_style), Paragraph("Kuitansi, kartu member & slip tercetak", table_cell_style), Paragraph("PASSED", table_cell_bold)]
    ]
    t_uj = Table(uji_data, colWidths=[20, 110, 110, 130, 110, 50])
    t_uj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_uj)
    story.append(Spacer(1, 6))

    story.append(Paragraph("4.3 Log Output Eksekusi Terminal Java Konsol Lengkap", h2_style))
    if os.path.exists("execution_log_p7.txt"):
        with open("execution_log_p7.txt", "r", encoding="utf-8") as fp:
            log_str = fp.read()
    else:
        log_str = "[Log not available]"

    p_log_full = Preformatted(log_str, ParagraphStyle('LogBox', fontName='Courier', fontSize=6.0, leading=7.2, textColor=colors.HexColor('#D4D4D4'), backColor=colors.HexColor('#1E1E1E'), borderPadding=4, borderWidth=0.5, borderColor=colors.HexColor('#333333'), spaceAfter=4))
    story.append(p_log_full)
    story.append(Spacer(1, 6))

    story.append(Paragraph("4.4 Analisis & Pembahasan Mendalam", h2_style))
    story.append(Paragraph(
        "Hasil pengujian membuktikan bahwa seluruh sasaran arsitektural Modul 7 tercapai sempurna. Abstract class Kendaraan dan Person berhasil mencegah instansiasi objek tanpa wujud konkrit. Dynamic method dispatch pada abstract method mengeksekusi logika spesifik Mobil, Motor, dan Minibus secara otonom. Interface realization membuktikan fleksibilitas tinggi di mana entitas armada dan pegawai lapangan dapat dikelola dalam satu koleksi telematika GPS terpadu (cross-hierarchy polymorphism). Seluruh fitur relasi P1–P6 tetap berfungsi 100% tanpa regresi.",
        body_style
    ))

    # BAB V
    story.append(Paragraph("BAB V: SPRINT EVALUATION, DEFINITION OF DONE & PENUTUP", h1_style))
    story.append(Paragraph("5.1 Sprint Review (7/7 Item Terverifikasi)", h2_style))
    rev_data = [
        [Paragraph("Item Evaluasi Sprint Review", table_header_style), Paragraph("Status Hasil Verifikasi", table_header_style)],
        [Paragraph("Abstract class berhasil dibuat (Kendaraan dan Person)", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Abstract method diimplementasikan subclass secara konsisten", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Minimal 2 subclass dapat digunakan (Mobil, Motor, Minibus, Pelanggan, Pegawai)", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Interface berhasil diimplementasikan (DapatDilacak, Perawatan, Cetakable)", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Class diagram sesuai dengan struktur kode sumber Java", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Pengujian polymorphism berhasil pada superclass & interface", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("Fitur proyek sebelumnya (P1–P6) tetap berjalan normal tanpa regresi", table_cell_style), Paragraph("VERIFIED (100% Selesai)", table_cell_bold)],
        [Paragraph("<b>Ringkasan Keterverifikasian Sprint Review</b>", table_cell_bold), Paragraph("<b>7 / 7 ITEM TERVERIFIKASI (100%)</b>", table_cell_bold)]
    ]
    t_rev = Table(rev_data, colWidths=[380, 150])
    t_rev.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_rev)
    story.append(Spacer(1, 4))

    story.append(Paragraph("5.2 Sprint Retrospective", h2_style))
    retro_text = (
        "<b>• What Went Well?</b> Penerapan Abstraction mengeliminasi anomali instansiasi entitas umum. Realisasi interface DapatDilacak, Perawatan, dan Cetakable menghasilkan arsitektur yang sangat modular dan siap pakai.<br/>"
        "<b>• What Went Wrong?</b> Penentuan batas tanggung jawab antara abstract method di Superclass vs Interface memerlukan perancangan yang cermat.<br/>"
        "<b>• Improvement for Next Sprint (P8 UTS / P9):</b> Menyiapkan integrasi materi P1-P7 untuk UTS Praktikum P8 serta persiapan modul GUI dan persistensi database pada P9."
    )
    t_retro = Table([[Paragraph(retro_text, body_style)]], colWidths=[530])
    t_retro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FDFBF7')),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor('#CC8800')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_retro)
    story.append(Spacer(1, 4))

    story.append(Paragraph("5.3 Checklist Definition of Done (15/15 Kriteria Terpenuhi)", h2_style))
    dod_items = [
        ("1", "Menggunakan proyek hasil P6 sebagai basis refactoring", "TERPENUHI (100%)"),
        ("2", "Audit desain dan alasan penggunaan abstraksi tersedia", "TERPENUHI (100%)"),
        ("3", "Minimal 1 abstract class yang relevan dibuat (Kendaraan & Person)", "TERPENUHI (100%)"),
        ("4", "Minimal 1 abstract method dibuat (hitungEstimasi, tampilkanSpesifikasi, dll)", "TERPENUHI (100%)"),
        ("5", "Minimal 2 subclass konkret mengimplementasikan abstract method (5 Subclass)", "TERPENUHI (100%)"),
        ("6", "Minimal 1 interface dibuat (DapatDilacak, Perawatan, Cetakable)", "TERPENUHI (100%)"),
        ("7", "Minimal 2 class mengimplementasikan interface yang relevan", "TERPENUHI (100%)"),
        ("8", "Polymorphism melalui superclass dan interface dapat dibuktikan", "TERPENUHI (100%)"),
        ("9", "Class diagram diperbarui dan konsisten dengan struktur kode", "TERPENUHI (100%)"),
        ("10", "Program berhasil dikompilasi (0 error) dan dijalankan", "TERPENUHI (100%)"),
        ("11", "Minimal 4 skenario pengujian tersedia (8 Fase Pengujian Selesai)", "TERPENUHI (100%)"),
        ("12", "Fitur proyek sebelumnya (P1–P6) tetap berjalan normal", "TERPENUHI (100%)"),
        ("13", "Sprint Backlog diperbarui lengkap (SB-01 s/d SB-07)", "TERPENUHI (100%)"),
        ("14", "Sprint Review tersedia (7/7 item terverifikasi)", "TERPENUHI (100%)"),
        ("15", "Sprint Retrospective tersedia lengkap", "TERPENUHI (100%)")
    ]
    t_dod = Table([[Paragraph("No", table_header_style), Paragraph("Butir Persyaratan Definition of Done Modul 7", table_header_style), Paragraph("Status Ketercapaian", table_header_style)]] +
                  [[Paragraph(no_str, table_cell_bold), Paragraph(req_str, table_cell_style), Paragraph(st_str, table_cell_bold)] for no_str, req_str, st_str in dod_items],
                  colWidths=[30, 370, 130])
    t_dod.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#003366')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E0E0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_dod)
    story.append(Spacer(1, 4))

    story.append(Paragraph("5.4 Target Pertemuan Berikutnya (P8 — UTS Praktikum PBO)", h2_style))
    story.append(Paragraph(
        "Hasil implementasi Modul 7 ini menjadi baseline project dalam menghadapi Evaluasi Tengah Semester (P8 — UTS Praktikum). Seluruh materi terintegrasi P1 hingga P7 akan dievaluasi melalui demonstrasi sistem dan klarifikasi kode.",
        body_style
    ))

    story.append(Paragraph("5.5 Kesimpulan Akhir", h2_style))
    story.append(Paragraph(
        "Praktikum Pemrograman Berorientasi Obyek Modul 7 (Abstract Class, Abstract Method, dan Interface) pada proyek AutoRent System telah berhasil diselesaikan dengan hasil sempurna (100% Definition of Done tercapai).",
        body_style
    ))

    doc.build(story, canvasmaker=FullNumberedCanvas)
    print(f"Successfully generated Full PDF report: {pdf_path}")

if __name__ == "__main__":
    build_full_pdf_report()

import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import random

# =======================================================
# 1. DATABASE SYSTEM (Sistem Pengumpul Riwayat Anonim)
# =======================================================
def inisialisasi_db():
    conn = sqlite3.connect("mental_health_v4.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS riwayat_stres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            waktu TEXT,
            skor INTEGER,
            status TEXT,
            lokasi_rujukan TEXT,
            mood TEXT,
            curhatan TEXT
        )
    """)
    conn.commit()
    conn.close()

def simpan_anonim(skor, status, lokasi, mood, curhatan):
    conn = sqlite3.connect("mental_health_v4.db")
    cursor = conn.cursor()
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO riwayat_stres (waktu, skor, status, lokasi_rujukan, mood, curhatan) VALUES (?, ?, ?, ?, ?, ?)",
        (waktu_sekarang, skor, status, lokasi, mood, curhatan)
    )
    conn.commit()
    conn.close()

# =======================================================
# 2. ANTARMUKA APLIKASI WEB PREMIUM INTERAKTIF
# =======================================================
inisialisasi_db()
st.set_page_config(page_title="CareMental Semarang", page_icon="🧠", layout="centered")

st.title("🧠 CareMental Web App (Lifestyle & Motivation Edition)")
st.write("Platform kesehatan mental mandiri anonim terintegrasi dengan faskes Kota Semarang dan panduan pola hidup sehat.")

# 🌟 UNIK 1: RUANG MOTIVASI & SEMANGAT HIDUP (KUTIPAN ACAK HANGAT)
st.markdown("---")
st.subheader("✨ Ruang Energi Positif & Semangat Hidup")
st.write("Butuh suntikan semangat untuk menjalani hari ini? Klik tombol di bawah ini:")

kumpulan_motivasi = [
    "🌟 *Ingatlah bahwa lelahmu hari ini adalah bagian dari perjuangan hebatmu. Istirahatlah sejenak, tapi jangan pernah menyerah. Kamu jauh lebih kuat dari apa yang kamu pikirkan!*",
    "❤️ *Tidak apa-apa jika hari ini berjalan melambat atau tidak sesuai rencana. Yang terpenting adalah kamu sudah bertahan dengan sangat luar biasa sampai detik ini.*",
    "🌻 *Kamu berharga, ceritamu penting, dan kehadiranmu di dunia ini membawa arti. Esok adalah hari baru dengan harapan-harapan baru yang menantimu.*",
    "🌈 *Badai pasti berlalu, begitu juga dengan rasa cemasmu saat ini. Tarik napas dalam-dalam, hembuskan perlahan. Sesuatu yang indah sedang dipersiapkan untukmu.*",
    "💪 *Jangan membandingkan bab awal hidupmu dengan bab kejayaan orang lain. Jalani jalamu dengan senyuman, karena setiap orang punya garis waktu suksesnya masing-masing.*"
]

if st.button("🔮 Dapatkan Kata Motivasi Hari Ini"):
    st.info(random.choice(kumpulan_motivasi))

# 🌟 UNIK 2: PAPAN TIPS POLA KEHIDUPAN SEHAT BIAR TERHINDAR DARI STRES
st.markdown("---")
st.subheader("📋 Panduan Pola Hidup Sehat Anti-Stres")
st.write("Terapkan kebiasaan mikro harian ini secara konsisten agar kesehatan mental dan fisikmu tetap seimbang:")

tab1, tab2, tab3 = st.tabs(["💤 Pola Istirahat", "🍎 Pola Nutrisi", "🧘 Pola Pikiran"])

with tab1:
    st.markdown("""
    *   **Aturan Jam Tidur:** Usahakan tidur 7-8 jam setiap malam dan buat jadwal tidur yang konsisten (jam tidur dan bangun yang sama).
    *   **Detoks Digital:** Matikan atau jauhkan HP dan laptop minimal 30 menit sebelum menutup mata untuk mencegah radiasi layar mengganggu hormon tidur.
    *   **Ritual Tenang:** Lakukan peregangan badan ringan atau mendengarkan instrumen musik lembut sebelum tidur.
    """)

with tab2:
    st.markdown("""
    *   **Hidrasi Cukup:** Minum air putih minimal 2 liter (8 gelas) sehari. Kekurangan cairan ringan bisa memicu rasa pusing dan kecemasan.
    *   **Kurangi Kafein Berlebih:** Hindari konsumsi kopi atau minuman berenergi di sore dan malam hari karena bisa memicu detak jantung cepat yang menyerupai gejala panik.
    *   **Makanan Bernutrisi:** Perbanyak konsumsi makanan buah segar, sayuran hijau, dan kacang-kacangan yang membantu merangsang hormon kebahagiaan (*serotonin*).
    """)

with tab3:
    st.markdown("""
    *   **Aturan 20-20-20:** Setiap menatap layar laptop/HP selama 20 menit, palingkan mata untuk menatap objek sejauh 20 kaki (6 meter) selama 20 detik untuk mengistirahatkan saraf mata.
    *   **Jurnal Ekspresif:** Luapkan keluh kesahmu dalam bentuk tulisan atau curhatan (seperti kolom di bawah ini) agar pikiran negatif tidak menumpuk di kepala.
    *   **Koneksi Sosial:** Luangkan waktu minimal seminggu sekali untuk mengobrol santai atau jalan-jalan dengan teman dekat atau keluarga dekatmu.
    """)

# Tombol Bantuan Darurat SOS (Dari Minggu 4)
st.markdown("---")
st.error("🚨 **BUTUH BANTUAN DARURAT SEGERA?**")
col_sos1, col_sos2 = st.columns(2)
with col_sos1:
    st.link_button("☎️ Hubungi Hotline Kemenkes 119", "tel:119", use_container_width=True)
with col_sos2:
    st.link_button("🏥 Hubungi RSJD Dr. Amino Semarang", "tel:0246722565", use_container_width=True)

# Fitur Mood Tracker & Jurnal Curhat
st.markdown("---")
st.subheader("📝 Jurnal Curhat & Mood Tracker")
pilih_mood = st.selectbox(
    "Bagaimana perasaanmu saat ini?",
    ["😊 Bahagia / Stabil", "😐 Biasa Saja", "😢 Sedih / Kecewa", "😡 Marah / Kesal", "😰 Cemas / Takut"]
)
teks_curhat = st.text_area(
    "Tuliskan ceritamu hari ini (Opsional):", 
    placeholder="Ketik apa saja... Identitas nama Anda tetap tersembunyi."
)

# Komponen Kuesioner
st.markdown("---")
st.subheader("📋 Kuesioner Singkat Beban Pikiran")
q1 = st.radio(
    "1. Seberapa sering Anda merasa cemas berlebihan minggu ini?",
    ["Jarang / Tidak Pernah", "Kadang-Kadang", "Sangat Sering"]
)
q2 = st.radio(
    "2. Apakah stres mengganggu pola tidur atau pola makan Anda?",
    ["Tidak Berdampak", "Sedikit Terganggu", "Sangat Mengganggu"]
)

skor_q1 = 0 if q1 == "Jarang / Tidak Pernah" else 1 if q1 == "Kadang-Kadang" else 2
skor_q2 = 0 if q2 == "Tidak Berdampak" else 1 if q2 == "Sedikit Terganggu" else 2

if st.button("Kirim & Cek Skor", type="primary"):
    skor_total = skor_q1 + skor_q2
    
    if skor_total <= 1:
        status = "Rendah"
        lokasi_rujukan = "Edukasi Mandiri & Layanan RDRM (Rumah Duta Revolusi Mental) Jl. Simongan Raya"
        st.success(f"Skor Anda: {skor_total} — Kondisi Anda Cukup Stabil 😊")
        st.info(f"📍 **Rekomendasi**: Kondisi Anda baik. Anda bisa memanfaatkan layanan konseling gratis di **RDRM Semarang (Jl. Simongan Raya No. 49)**.")
    elif skor_total <= 3:
        status = "Sedang"
        lokasi_rujukan = "Puskesmas Pandanaran (Jl. Pandanaran No.79) / Layanan Psikologi Kampus"
        st.warning(f"Skor Anda: {skor_total} — Anda Mengalami Stres Ringan/Sedang 😐")
        st.info(f"📍 **Rekomendasi Lokasi**: Anda bisa berkonsultasi ke **Puskesmas Pandanaran (Jl. Pandanaran No.79)**.")
    else:
        status = "Tinggi"
        lokasi_rujukan = "RSJD Dr. Amino Gondohutomo (Jl. Brigjen Sudiarto No.347) / RSUP Dr. Kariadi"
        st.error(f"Skor Anda: {skor_total} — Tingkat Stres Tinggi! 🚨")
        st.info(f"📍 **Rekomendasi Penanganan**: Sangat disarankan berkonsultasi dengan profesional di **RSJD Dr. Amino Gondohutomo Pedurungan** atau Klinik Psikiatri **RSUP Dr. Kariadi**.")
    
    simpan_anonim(skor_total, status, lokasi_rujukan, pilih_mood, teks_curhat)
    st.toast("Data jurnal dan kuesioner berhasil terkirim secara anonim!", icon="✅")

# =======================================================
# 3. DASHBOARD MONITOR DATABASE PENGELOLA
# =======================================================
st.markdown("---")
st.subheader("📊 Panel Pantau Pengelola (Data Masuk, Lokasi & Grafik Analisis)")

conn = sqlite3.connect("mental_health_v4.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM riwayat_stres ORDER BY id DESC")
data_database = cursor.fetchall()
conn.close()

if data_database:
    jumlah_status = {"Rendah": 0, "Sedang": 0, "Tinggi": 0}
    format_tabel = []
    
    for row in data_database:
        status_item = row
        if status_item in jumlah_status:
            jumlah_status[status_item] += 1
            
        format_tabel.append({
            "ID Samaran": f"User-{row}",
            "Waktu Pengisian": row,
            "Skor Hasil": row,
            "Status Tingkat Stres": row,
            "Rekomendasi Lokasi Semarang": row,
            "Mood Terpilih": row,
            "Isi Curahan Hati": row
        })
    
    df_pie = pd.DataFrame({
        "Status": list(jumlah_status.keys()),
        "Jumlah": list(jumlah_status.values())
    })
    st.scatter_chart(df_pie, x="Status", y="Jumlah", size="Jumlah", color="Status")
    st.table(format_tabel)
else:
    st.info("Belum ada data kuesioner yang diisi.")

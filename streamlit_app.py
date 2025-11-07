import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 🔧 CONFIGURASI DASAR
# ======================
st.set_page_config(
    page_title="Predict 2025",
    page_icon="📊",
    layout="wide"
)

# ======================
# 🎨 HEADER & SIDEBAR
# ======================
st.sidebar.title("⚙️ Navigasi")
menu = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Analisis Data", "Prediksi"])

st.sidebar.markdown("---")
st.sidebar.info("Dibuat oleh **Anas Naufal** 🚀\n\nTerhubung langsung ke GitHub dan Streamlit Cloud.")

st.title("📈 Predict 2025 Dashboard")
st.markdown("Selamat datang di aplikasi **Streamlit Predict 2025** — tempat analisis dan prediksi data kamu.")

# ======================
# ⚡ OPTIMASI LOAD DATA
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv("predict2025.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ File `predict2025.csv` tidak ditemukan. Pastikan file ada di folder yang sama dengan `streamlit_app.py`.")
    st.stop()

# ======================
# 📊 HALAMAN: BERANDA
# ======================
if menu == "Beranda":
    st.subheader("📘 Tentang Aplikasi")
    st.write("""
    Aplikasi ini dibuat menggunakan **Streamlit** untuk menganalisis dan memprediksi data tahun 2025.
    
    Kamu bisa berpindah ke tab **Analisis Data** untuk melihat visualisasi, atau ke tab **Prediksi** untuk simulasi hasil prediksi.
    """)

    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)

# ======================
# 🔍 HALAMAN: ANALISIS DATA
# ======================
elif menu == "Analisis Data":
    st.subheader("📊 Eksplorasi & Analisis Data")

    st.write("Berikut contoh data dari file yang digunakan:")
    st.dataframe(df.head())

    st.markdown("---")
    st.write("**Statistik Deskriptif:**")
    st.write(df.describe())

    # Contoh visualisasi sederhana
    st.markdown("### Visualisasi Contoh")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        col = st.selectbox("Pilih kolom untuk visualisasi:", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        ax.set_title(f"Distribusi {col}")
        st.pyplot(fig)
    else:
        st.warning("Tidak ada kolom numerik yang bisa divisualisasikan.")

# ======================
# 🤖 HALAMAN: PREDIKSI
# ======================
elif menu == "Prediksi":
    st.subheader("🤖 Simulasi Prediksi")

    st.write("Masukkan parameter prediksi kamu di bawah ini:")
    col1, col2 = st.columns(2)
    with col1:
        nilai_a = st.number_input("Nilai A", min_value=0.0, value=10.0)
        nilai_b = st.number_input("Nilai B", min_value=0.0, value=5.0)
    with col2:
        faktor = st.slider("Faktor Pengali (%)", 0, 200, 100)

    hasil = (nilai_a + nilai_b) * (faktor / 100)
    st.success(f"📈 Hasil prediksi: **{hasil:.2f}**")

    st.caption("Simulasi ini hanya contoh perhitungan sederhana.")

# ======================
# ✅ FOOTER
# ======================
st.markdown("---")
st.markdown("🌐 **Predict 2025** | Dibangun dengan ❤️ oleh Anas Naufal menggunakan [Streamlit](https://streamlit.io)")

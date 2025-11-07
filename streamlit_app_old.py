# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Load data ---
df = pd.read_csv("predict2025.csv")
df['previous_year_rating'] = df['previous_year_rating'].fillna(df['previous_year_rating'].median())

# --- Feature engineering ---
df['performance_score'] = (
    df['previous_year_rating'] * 0.5 +
    df['avg_training_score'] * 0.4 +
    df['awards_won?'] * 10
)

# --- Business Rules ---
eligible = df[
    (df['previous_year_rating'] >= 4) &
    (df['avg_training_score'] >= 80) &
    (df['length_of_service'] >= 3)
]
dept_perf = (
    df.groupby('department')[['previous_year_rating', 'avg_training_score']]
    .mean()
    .reset_index()
)
dept_perf['overall_score'] = dept_perf['previous_year_rating'] * 0.6 + dept_perf['avg_training_score'] * 0.4

# --- Streamlit layout ---
st.set_page_config(page_title="Employee Performance Dashboard 2025", layout="wide")

st.title("📊 Employee Performance Dashboard 2025")
st.markdown("Analisis berbasis framework **CRISP-DM** untuk menentukan karyawan dan departemen terbaik tahun 2025.")

# Tabs
tab1, tab2, tab3 = st.tabs(["🏅 Top Karyawan", "🏢 Top Department", "📈 Statistik"])

with tab1:
    st.subheader("Top 10 Karyawan Paling Berprestasi")
    top10 = df.sort_values(by="performance_score", ascending=False).head(10)
    st.dataframe(top10[['employee_id','department','previous_year_rating','awards_won?','avg_training_score','performance_score']])

    fig, ax = plt.subplots(figsize=(8,5))
    ax.barh(top10['employee_id'].astype(str), top10['performance_score'], color='royalblue')
    ax.invert_yaxis()
    ax.set_xlabel("Performance Score")
    ax.set_ylabel("Employee ID")
    ax.set_title("Top 10 Karyawan Paling Berprestasi 2025")
    st.pyplot(fig)

with tab2:
    st.subheader("Top 5 Department Paling Berprestasi")
    top5 = dept_perf.sort_values(by="overall_score", ascending=False).head(5)
    st.dataframe(top5)

    fig2, ax2 = plt.subplots(figsize=(8,5))
    ax2.bar(top5['department'], top5['overall_score'], color='mediumseagreen')
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Overall Performance Score")
    ax2.set_title("Top 5 Department 2025")
    st.pyplot(fig2)

with tab3:
    st.subheader("Karyawan Layak Naik Jabatan & Bonus")
    st.write(f"Jumlah karyawan layak naik jabatan & bonus: **{len(eligible)} orang**")
    st.dataframe(eligible[['employee_id','department','previous_year_rating','avg_training_score','length_of_service']].head(20))
    st.markdown("Kriteria: Rating ≥ 4, Skor Pelatihan ≥ 80, Lama Kerja ≥ 3 tahun.")

st.success("✅ Dashboard berhasil dijalankan — Data siap untuk diintegrasikan ke sistem HR!")


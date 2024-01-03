import streamlit as st
import pandas as pd
import numpy as np


# Data gejala penyakit
data_gejala = pd.DataFrame({
    "Gejala": ["Demam", "Batuk", "Pilek", "Sakit kepala", "Nyeri otot", "Sakit tenggorokan", "Diare", "Muntah", "Sakit perut"],
    "Penyakit": ["Demam berdarah", "Flu", "Alergi", "Sakit kepala migrain", "Infeksi saluran pernapasan atas", "Radang tenggorokan", "Diare nonspesifik", "Muntah-muntah", "Gastritis"]
})

# Data pengobatan penyakit
data_pengobatan = pd.DataFrame({
    "Penyakit": ["Demam berdarah", "Flu", "Alergi", "Sakit kepala migrain", "Infeksi saluran pernapasan atas", "Radang tenggorokan", "Diare nonspesifik", "Muntah-muntah", "Gastritis"],
    "Pengobatan": ["Istirahat, minum banyak cairan, dan konsumsi obat penurun panas", "Istirahat, minum banyak cairan, dan konsumsi obat antivirus", "Hindari pemicu alergi, konsumsi obat antihistamin", "Istirahat, konsumsi obat pereda nyeri, dan konsumsi obat antimigrain", "Istirahat, minum banyak cairan, dan konsumsi obat antivirus", "Istirahat, minum banyak cairan, dan konsumsi obat antiinflamasi", "Istirahat, minum banyak cairan, dan konsumsi obat antidiare", "Istirahat, minum banyak cairan, dan konsumsi obat antimuntah", "Istirahat, konsumsi obat antiinflamasi, dan konsumsi obat prokinetik"]
})

def tampilkan_hasil_diagnosis(gejala):
    # Cari penyakit yang kemungkinan sesuai dengan gejala yang dimasukkan
    penyakit_kemungkinan = data_gejala[data_gejala["Gejala"].isin(gejala.split(", "))]

    # Jika tidak ada penyakit yang kemungkinan sesuai, tampilkan pesan tidak ditemukan
    if len(penyakit_kemungkinan) == 0:
        st.write("Penyakit tidak ditemukan")
        return

    # Ambil nama penyakit dari hasil pencarian
    nama_penyakit = penyakit_kemungkinan["Penyakit"].iloc[0]

    # Cari pengobatan untuk penyakit yang sesuai
    pengobatan = data_pengobatan[data_pengobatan["Penyakit"] == nama_penyakit]["Pengobatan"].iloc[0]

    # Tampilkan hasil diagnosis
    st.write("Hasil diagnosis:")
    st.write("Penyakit:", nama_penyakit)
    st.write("Pengobatan:", pengobatan)

def main():
    # Tampilkan judul
    st.title("Medical Diagnosis")

    # Input gejala
    gejala = st.text_input("Masukkan gejala yang Anda alami (pisahkan dengan koma):")

    # Tampilkan hasil diagnosis
    tampilkan_hasil_diagnosis(gejala)

if __name__ == "__main__":
    main()

# Decision Tree untuk Pengambilan Keputusan Proyek

Proyek ini menggunakan **Decision Tree** untuk membantu pengambilan keputusan dalam menentukan apakah sebuah proyek harus dilanjutkan atau ditunda berdasarkan karakteristik tertentu seperti anggaran, waktu, risiko, skala proyek, dan dampak lingkungan.

## Tabel Isi

- [Pendahuluan](#pendahuluan)
- [Fitur Utama](#fitur-utama)
- [Instalasi](#instalasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Contoh Visualisasi](#contoh-visualisasi)
- [Struktur Data](#struktur-data)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Pendahuluan

Pengambilan keputusan yang tepat sangat penting dalam manajemen proyek, terutama saat harus memilih apakah suatu proyek harus dilanjutkan atau ditunda. Model **Decision Tree** ini menawarkan solusi yang sederhana dan efektif untuk masalah tersebut, dengan menggunakan beberapa variabel kunci yang sering menjadi pertimbangan dalam keputusan proyek.

## Fitur Utama

- **Model Prediksi**: Menggunakan model Decision Tree untuk memprediksi apakah proyek sebaiknya dilanjutkan atau ditunda.
- **Visualisasi Keputusan**: Menyediakan visualisasi pohon keputusan dan permukaan keputusan untuk membantu memahami bagaimana model mencapai keputusannya.
- **Prediksi Input Baru**: Mampu menerima data proyek baru dan memberikan keputusan langsung.

## Instalasi

1. **Clone repositori ini** ke direktori lokal Anda:

    ```bash
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

2. **Instal dependensi** yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan kode** untuk melihat hasilnya:

    ```bash
    python decision_tree.py
    ```

## Cara Penggunaan

Setelah Anda menjalankan skrip, model akan:

1. Membangun **Decision Tree** berdasarkan data proyek yang telah ditentukan.
2. Menampilkan **visualisasi** pohon keputusan untuk memberikan gambaran tentang bagaimana model mengambil keputusan.
3. Melakukan **prediksi** untuk proyek baru berdasarkan input yang diberikan.
4. Menampilkan hasil prediksi dan memberikan rekomendasi apakah proyek tersebut sebaiknya dilanjutkan atau ditunda.

## Contoh Visualisasi

Berikut adalah contoh visualisasi yang dihasilkan oleh model:

1. **Pohon Keputusan**: Memberikan gambaran struktur keputusan yang diambil oleh model.

    ![Decision Tree](path_to_decision_tree_image.png)

2. **Permukaan Keputusan**: Menampilkan bagaimana model membagi ruang keputusan berdasarkan dua fitur pertama (Anggaran dan Waktu).

    ![Decision Surface](path_to_decision_surface_image.png)

## Struktur Data

- **Fitur Proyek**:
    - Anggaran (juta)
    - Waktu (bulan)
    - Risiko (0 = rendah, 1 = tinggi)
    - Skala Proyek (0 = kecil, 1 = menengah, 2 = besar)
    - Dampak Lingkungan (0 = rendah, 1 = sedang, 2 = tinggi)

- **Output Keputusan**:
    - 0 = Proyek Ditunda
    - 1 = Proyek Dilanjutkan

## Kontribusi

Kontribusi selalu diterima dengan tangan terbuka! Silakan buka _issue_ atau kirim _pull request_ untuk perubahan atau fitur yang ingin Anda tambahkan.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

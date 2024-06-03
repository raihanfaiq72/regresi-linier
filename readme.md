# Analisis Regresi Linear Ganda dan Korelasi antara Variabel

## Deskripsi
Kode ini bertujuan untuk melakukan analisis regresi linear ganda dan menghitung koefisien korelasi antara variabel-variabel yang diberikan. Analisis dilakukan menggunakan data omset kotor (x1), omset bersih (x2), dan cup terjual (y) selama periode waktu tertentu.

## Langkah-langkah Analisis
1. **Preprocessing Data**
   - Data omset kotor, omset bersih, dan cup terjual dimasukkan ke dalam array numpy.
   
2. **Regresi Linear Ganda**
   - Kolom 1 ditambahkan ke dalam data omset kotor (x1) untuk perhitungan konstanta (intercept).
   - Koefisien regresi dihitung menggunakan metode Ordinary Least Squares (OLS).
   - Prediksi nilai cup terjual (y_pred) dibuat berdasarkan model regresi yang dihasilkan.
   
3. **Diagram Kartesian Hasil Regresi**
   - Diagram kartesian digunakan untuk memvisualisasikan hasil prediksi terhadap data observasi.
   - Scatter plot menampilkan data observasi dan hasil prediksi, sementara garis merah menunjukkan garis identitas.
   
4. **Koefisien Regresi**
   - Koefisien regresi, yaitu intercept (β0), koefisien untuk omset kotor (β1), dan koefisien untuk omset bersih (β2), ditampilkan.

5. **Koefisien Korelasi**
   - Koefisien korelasi antara cup terjual (y) dan omset kotor (x1), omset bersih (x2), serta antara omset kotor (x1) dan omset bersih (x2) dihitung dan ditampilkan.

6. **Scatterplot Antara Variabel**
   - Tiga scatterplot digunakan untuk memvisualisasikan hubungan antara variabel:
     - Cup Terjual (y) vs Omset Kotor (x1)
     - Cup Terjual (y) vs Omset Bersih (x2)
     - Omset Kotor (x1) vs Omset Bersih (x2)

## Cara Penggunaan
1. Pastikan Anda telah menginstal library numpy dan matplotlib.
2. Jalankan kode pada lingkungan Python yang sesuai.
3. Amati hasil analisis regresi linear ganda dan koefisien korelasi antara variabel.

## Kontributor
- Muhammad Faiq Raiha
- Galen Kumara Anwar
- Ahmad Husni Mubarok Yasin
- Umi khalsum

import numpy as np
import matplotlib.pyplot as plt

# Data
x1 = np.array([342500, 389000, 342000, 278000, 288000, 232000, 321000, 366000, 278000, 316000, 421000, 404000, 422000, 287000, 377000, 402000, 387000, 287000, 245000, 342000, 344000, 289000, 350000, 243000, 323000, 313000, 322000, 367000, 400000, 256000, 504000])  # Omset Kotor
x2 = np.array([148000, 179000, 125000, 104000, 109000, 67000, 117000, 136000, 102000, 112000, 134000, 182000, 202000, 98000, 173000, 289000, 218000, 108000, 77000, 135000, 223000, 146000, 163000, 89000, 132000, 105000, 165000, 188000, 121000, 147000, 203000])  # Omset Bersih
y = np.array([155, 198, 178, 148, 189, 156, 177, 190, 145, 169, 232, 202, 243, 153, 172, 230, 214, 171, 127, 186, 183, 166, 186, 142, 165, 191, 165, 196, 200, 123, 223])  # Cup Terjual

# Menambahkan kolom 1 ke x untuk perhitungan konstanta (intercept)
X = np.column_stack((np.ones(len(x1)), x1, x2))

# Menghitung koefisien regresi
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# Membuat prediksi
y_pred = X @ beta

# Membuat diagram kartesian
plt.figure(figsize=(10, 6))

# Plot data observasi
plt.scatter(y, y_pred)
plt.plot([min(y), max(y)], [min(y), max(y)], '--', color='red')  # Garis identitas
plt.title('Regresi Linear Ganda: Hasil Prediksi thdp Data Observasi')
plt.xlabel('Data Observasi')
plt.ylabel('Hasil Prediksi')
plt.grid(True)
plt.show()

# Menampilkan koefisien regresi
print("Koefisien regresi:")
print("Intercept (β0):", beta[0])
print("Koefisien untuk omset kotor (β1):", beta[1])
print("Koefisien untuk omset bersih (β2):", beta[2])


#hasil faiq
# Hitung koefisien korelasi antara Y dan X1
corr_y_x1 = np.corrcoef(y, x1)[0, 1]
print("Koefisien Korelasi antara Y dan X1:", corr_y_x1)

# Hitung koefisien korelasi antara Y dan X2
corr_y_x2 = np.corrcoef(y, x2)[0, 1]
print("Koefisien Korelasi antara Y dan X2:", corr_y_x2)

# Hitung koefisien korelasi antara X1 dan X2
corr_x1_x2 = np.corrcoef(x1, x2)[0, 1]
print("Koefisien Korelasi antara X1 dan X2:", corr_x1_x2)

plt.figure(figsize=(15, 5))

# plot untuk antara Y dan X1
plt.subplot(1, 3, 1)
plt.scatter(x1, y)
plt.title('plot untuk Y thdp X1')
plt.xlabel('Omset Kotor (X1)')
plt.ylabel('Cup Terjual (Y)')

# plot untuk antara Y dan X2
plt.subplot(1, 3, 2)
plt.scatter(x2, y)
plt.title('plot untuk Y thdp X2')
plt.xlabel('Omset Bersih (X2)')
plt.ylabel('Cup Terjual (Y)')

# plot untuk antara X1 dan X2
plt.subplot(1, 3, 3)
plt.scatter(x1, x2)
plt.title('plot untuk X1 thdp X2')
plt.xlabel('Omset Kotor (X1)')
plt.ylabel('Omset Bersih (X2)')

plt.tight_layout()
plt.show()
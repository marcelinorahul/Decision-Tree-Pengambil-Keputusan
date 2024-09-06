# Import library yang diperlukan untuk membuat model dan visualisasi
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

# Definisikan data contoh fiktif
# Setiap angka dalam X mewakili karakteristik proyek:
# Anggaran, Waktu, Risiko, Skala Proyek, Dampak Lingkungan
X = [
    [500, 6, 0, 0, 0],   # Data proyek 1
    [600, 12, 1, 2, 2],  # Data proyek 2
    [700, 8, 0, 1, 1],   # Data proyek 3
    [400, 10, 1, 0, 1],  # Data proyek 4
    [550, 7, 0, 2, 2],   # Data proyek 5
    [650, 9, 1, 1, 0],   # Data proyek 6
    [750, 5, 0, 2, 0],   # Data proyek 7
    [300, 11, 1, 1, 2],  # Data proyek 8
]

# Y adalah hasil keputusan untuk setiap proyek:
# 1 = Proyek dilanjutkan, 0 = Proyek ditunda
Y = [1, 0, 1, 0, 0, 1, 1, 0]

# Label untuk setiap kolom fitur (karakteristik proyek)
features = ["Anggaran (juta)", "Waktu (bulan)", "Risiko", "Skala Proyek", "Dampak Lingkungan"]
# Nama kelas yang digunakan untuk hasil keputusan
class_names = ["Tunda", "Lanjutkan"]

# Membuat model Decision Tree (Pohon Keputusan)
# Menggunakan kriteria 'gini' untuk membagi data dan kedalaman maksimal 4
model = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
# Melatih model menggunakan data X dan Y
model = model.fit(X, Y)

# Visualisasi pohon keputusan untuk membantu memahami bagaimana keputusan dibuat
plt.figure(figsize=(20,10))
tree.plot_tree(model, feature_names=features, class_names=class_names, filled=True, rounded=True)
plt.show()

# Prediksi keputusan berdasarkan data proyek baru
input_data = [[580, 10, 1, 1, 1]]  # Contoh data proyek baru
prediksi = model.predict(input_data)

# Menampilkan hasil keputusan yang mudah dipahami
if prediksi == 1:
    keputusan = "Proyek bisa dilanjutkan."
else:
    keputusan = "Proyek sebaiknya ditunda."

print(f"Hasil keputusan: {keputusan}")

# Fungsi untuk menampilkan visualisasi permukaan keputusan (untuk dua fitur pertama)
def plot_decision_surface(clf, X, y, feature_names):
    # Pastikan hanya menggunakan dua fitur pertama untuk visualisasi
    if X.shape[1] != 2:
        raise ValueError("Fitur input untuk plot_decision_surface harus 2 dimensi.")

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    # Membuat data input baru dengan 5 fitur, 
    # menggunakan nilai rata-rata untuk fitur yang tidak divisualisasikan
    mean_values = np.mean(X, axis=0)[2:] # Rata-rata untuk fitur 3, 4, dan 5
    
    # Membuat array 2D untuk mean_values agar kompatibel dengan xx.ravel()
    mean_values_2d = np.tile(mean_values, (xx.ravel().shape[0], 1))
    
    input_data = np.c_[xx.ravel(), yy.ravel(), mean_values_2d]
    
    # Memprediksi hasil keputusan
    Z = clf.predict(input_data)
    Z = Z.reshape(xx.shape)

    # Visualisasi hasil prediksi dalam bentuk kontur warna
    plt.figure(figsize=(12,8))
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=100, edgecolor='k', cmap=plt.cm.RdYlBu)
    plt.title("Visualisasi Permukaan Keputusan")
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.show()

# Konversi data untuk visualisasi (menggunakan dua fitur pertama: Anggaran dan Waktu)
X_vis = np.array(X)[:, [0, 1]]  # Hanya menggunakan Anggaran dan Waktu
plot_decision_surface(model, X_vis, np.array(Y), features[:2])

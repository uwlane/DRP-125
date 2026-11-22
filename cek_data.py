import pandas as pd

# 1. Memuat dataset dari file CSV
df = pd.read_csv("Coffe_sales.csv")

# Melihat jumlah baris dan kolom dalam data & 5 baris pertama
print("1. UKURAN & RINGKASAN DATA")
print("Ukuran data (baris, kolom):", df.shape)
print("\n5 Data Teratas:")
print(df.head())


print("\n2. CEK KESEHATAN DATA")

# Mengecek informasi tipe data dan jumlah baris non-null tiap kolom
df.info()

# Menghitung jumlah nilai yang kosong (missing values) di setiap kolom
print("\nJumlah Data Kosong (Missing Value):")
print(df.isna().sum())

# Mengecek apakah ada baris data yang duplikat persis secara keseluruhan
print("\nJumlah Baris Duplikat:", df.duplicated().sum())

# Melihat sampel kolom Time sebelum dibersihkan
print("\nSampel Kolom Time (Sebelum dibersihkan):")
print(df["Time"].head())

print("\n3. PROSES PEMBERSIHAN DATA & CEK KATEGORI")

# Membersihkan spasi berlebih di awal/akhir nama kopi agar tidak bikin kategori ganda
df["coffee_name"] = df["coffee_name"].str.strip()
print("Distribusi Nama Kopi (coffee_name):")
print(df["coffee_name"].value_counts())

# Membersihkan format kolom Time (membuang milidetik)
df["Time"] = pd.to_datetime(df["Time"], format="mixed").dt.strftime("%H:%M:%S")
print("\nKolom Time setelah dibersihkan (tanpa milidetik):")
print(df[["Time", "hour_of_day"]].head())

# Mengecek isi kategori teks lainnya 
cat_cols = ["cash_type", "Time_of_Day", "Weekday", "Month_name"]
for col in cat_cols:
    print(f"\nDistribusi kategori untuk kolom: {col}")
    print(df[col].value_counts(dropna=False))


print("\n4. CEK KOLOM ANGKA (JAM & HARGA)")

# Melihat ringkasan statistik deskriptif (min, max, mean, dll) untuk data angka
print(df[["hour_of_day", "money"]].describe())

# Mengecek batas jam transaksi terkecil dan terbesar
print("\nJam terkecil:", df["hour_of_day"].min(), "| Jam terbesar:", df["hour_of_day"].max())

# Mengecek apakah ada jam transaksi yang tidak wajar di luar rentang 0-23
invalid_hours = ((df["hour_of_day"] < 0) | (df["hour_of_day"] > 23)).sum()
print("Jumlah jam di luar rentang 0-23:", invalid_hours)

# Mengecek apakah ada harga/uang yang bernilai 0 atau negatif (anomali harga)
invalid_money = (df["money"] <= 0).sum()
print("Jumlah transaksi dengan harga <= 0:", invalid_money)

# Menampilkan 5 transaksi dengan harga termurah untuk cek kewajaran
print("\n5 Transaksi Termurah:")
print(df.sort_values(by="money").head())

# Menampilkan 5 transaksi dengan harga termahal untuk cek apakah ada salah ketik/outlier ekstrem
print("\n5 Transaksi Termahal:")
print(df.sort_values(by="money", ascending=False).head())


print("\n5. CEK KONSISTENSI WAKTU & HARI")

# Memeriksa apakah pembagian waktu (Time_of_Day) sudah sesuai dengan jam transaksinya (hour_of_day)
print("Tabel Silang (Crosstab) Jam vs Waktu (Time_of_Day):")
print(pd.crosstab(df["hour_of_day"], df["Time_of_Day"]))

# Memeriksa apakah urutan angka hari (Weekdaysort) cocok dengan nama harinya (Weekday)
print("\nTabel Silang (Crosstab) Urutan Hari vs Nama Hari:")
print(pd.crosstab(df["Weekdaysort"], df["Weekday"]))

# Memeriksa apakah urutan angka bulan (Monthsort) cocok dengan nama bulannya (Month_name)
print("\nTabel Silang (Crosstab) Urutan Bulan vs Nama Bulan:")
print(pd.crosstab(df["Monthsort"], df["Month_name"]))

print("\n--- SEMUA PENGECEKAN SELESAI ---")

# Menyimpan dataframe yang sudah bersih ke file CSV baru agar perubahannya tidak hilang
df.to_csv("Coffe_sales_bersih.csv", index=False)
print("File baru yang sudah bersih berhasil disimpan dengan nama: 'Coffe_sales_bersih.csv'")
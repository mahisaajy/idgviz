import os
import pandas as pd

def convert_all_xlsx_to_csv(folder_path):
    """
    Convert all .xlsx files in a folder to .csv files.

    Parameters:
        folder_path (str): Path to the folder containing .xlsx files.
    """
    try:
        # Memastikan folder ada
        if not os.path.exists(folder_path):
            print(f"Folder tidak ditemukan: {folder_path}")
            return

        # Mendapatkan semua file dengan ekstensi .xlsx di folder
        xlsx_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

        if not xlsx_files:
            print(f"Tidak ada file .xlsx di folder: {folder_path}")
            return

        # Membuat folder untuk menyimpan hasil jika belum ada
        output_folder = os.path.join(folder_path, "converted_csv")
        os.makedirs(output_folder, exist_ok=True)

        # Mengonversi setiap file .xlsx menjadi .csv
        for xlsx_file in xlsx_files:
            xlsx_path = os.path.join(folder_path, xlsx_file)
            csv_file = os.path.splitext(xlsx_file)[0] + ".csv"
            csv_path = os.path.join(output_folder, csv_file)

            # Membaca dan mengonversi file
            df = pd.read_excel(xlsx_path)
            df.to_csv(csv_path, index=False)
            print(f"Berhasil mengonversi: {xlsx_path} -> {csv_path}")

        print(f"Semua file .xlsx telah dikonversi ke folder: {output_folder}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
folder_path = "draft"  # Ganti dengan path folder Anda
convert_all_xlsx_to_csv(folder_path)

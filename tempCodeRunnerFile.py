import tkinter as tk
from tkinter import font

# Fungsi untuk menampilkan hasil prediksi
def show_prediction():
    # Menampilkan hasil prediksi dengan warna dan font yang menarik
    result_label.config(text="Hasil Prediksi: Teknologi Informasi", fg="#007acc")

# Inisialisasi window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.config(bg="#1f1f2e")  # Background utama yang lebih gelap untuk efek modern

# Custom font untuk judul
title_font = font.Font(family="Helvetica", size=18, weight="bold")
input_font = font.Font(family="Arial", size=10)

# Label judul
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=title_font, bg="#007acc", fg="white", pady=10)
title_label.pack(fill="x", padx=20, pady=(20, 10))

# Frame untuk menampung input nilai mata pelajaran
input_frame = tk.Frame(root, bg="#1f1f2e")
input_frame.pack(pady=20)

# Label dan Entry untuk nilai mata pelajaran
entries = []
for i in range(1, 11):
    subject_label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i}:", font=input_font, bg="#1f1f2e", fg="white")
    subject_label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(input_frame, width=15, font=input_font, bg="#2f2f3e", fg="white", insertbackground="white")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Frame untuk tombol dan hasil prediksi
bottom_frame = tk.Frame(root, bg="#1f1f2e")
bottom_frame.pack(pady=20)

# Button untuk hasil prediksi dengan gaya modern
predict_button = tk.Button(
    bottom_frame, text="Hasil Prediksi", font=("Arial", 12, "bold"), bg="#007acc", fg="white",
    activebackground="#005f99", activeforeground="white", command=show_prediction, relief="flat", padx=20, pady=5
)
predict_button.pack(pady=10)

# Label untuk hasil prediksi dengan font dan warna lebih modern
result_label = tk.Label(bottom_frame, text="Hasil Prediksi: ", font=("Arial", 12), bg="#1f1f2e", fg="#a9a9b3")
result_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()

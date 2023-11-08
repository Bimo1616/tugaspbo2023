import tkinter as tk

def hitung_bmi():
    berat_badan = float(entry_berat.get())
    tinggi = float(entry_tinggi.get())
    bmi = berat_badan / (tinggi ** 2)
    label_hasil.config(text=f"BMI Anda adalah: {bmi:.2f}")
    if bmi < 18.5:
        label_kategori.config(text="Kategori BMI Anda: Kurus")
    elif 18.5 <= bmi < 24.9:
        label_kategori.config(text="Kategori BMI Anda: Normal")
    elif 25 <= bmi < 29.9:
        label_kategori.config(text="Kategori BMI Anda: Gemuk")
    else:
        label_kategori.config(text="Kategori BMI Anda: Obesitas")

# Membuat jendela utama
window = tk.Tk()
window.title("Kalkulator BMI")

# Membuat label dan input untuk berat badan
label_berat = tk.Label(window, text="Berat Badan (kg):")
label_berat.pack()
entry_berat = tk.Entry(window)
entry_berat.pack()

# Membuat label dan input untuk tinggi
label_tinggi = tk.Label(window, text="Tinggi (m):")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Membuat tombol "Hitung BMI"
tombol_hitung = tk.Button(window, text="Hitung BMI", command=hitung_bmi)
tombol_hitung.pack()

# Membuat label untuk hasil dan kategori BMI
label_hasil = tk.Label(window, text="")
label_hasil.pack()
label_kategori = tk.Label(window, text="")
label_kategori.pack()

# Menjalankan aplikasi
window.mainloop()
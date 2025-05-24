import tkinter as tk
from tkinter import messagebox
from fuzzy_logic import compute_outputs

def run_gui():
    root = tk.Tk()
    root.title("Smart Room Climate Controller")
    root.geometry("400x450")

    labels = ['Oda Sıcaklığı (°C)', 'Nem (%)', 'CO2 (ppm)', 'İnsan Sayısı', 'Dış Sıcaklık (°C)']
    entries = []

    for idx, label in enumerate(labels):
        tk.Label(root, text=label).pack(pady=(10 if idx == 0 else 5, 0))
        entry = tk.Entry(root)
        entry.pack()
        entries.append(entry)

    result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
    result_label.pack(pady=20)

    def on_submit():
        try:
            values = [float(e.get()) for e in entries]
            heat, fan = compute_outputs(*values)
            result_label.config(text=f"Isıtma Düzeyi: {heat:.2f}%
Fan Hızı: {fan:.2f}%")
        except Exception as e:
            messagebox.showerror("Hata", f"Girdi hatası: {e}")

    tk.Button(root, text="Hesapla", command=on_submit).pack(pady=10)

    root.mainloop()

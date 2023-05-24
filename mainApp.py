from tkinter import *
from tkinter import ttk
import tkinter as tk
from daftarHarga import Harga

window = tk.Tk()
window.title('FAST PRINT')
window.resizable(0,0)

# Fungsi menengahkan frame di jendela
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

# Mengatur ukuran jendela dan menengahkannya di tengah layar
window_width = 600
window_height = 400
center_window(window, window_width, window_height)

frame = tk.Frame(window)
frame.pack()

# Menengahkan label judul di atas frame
title_label = tk.Label(text="FAST PRINT", font=("Arial", 24))
title_label.pack(pady=10)

# Input Print Hitam Putih
labelBlackWhite = Label(
    window,
    text="Print Hitam Putih\t",
    font=("Arial", 10)
)
labelBlackWhite.place(x=30, y=60)

intBlackWhite = IntVar()
entryBlackWhite = Entry(
    window,
    textvariable=intBlackWhite,
    font=("Arial", 10)
)
entryBlackWhite.place(x=30, y=90, width=40, height=20)

lembarBlackWhite = Label(
    window,
    text="Lembar\t",
    font=("Arial", 10)
)
lembarBlackWhite.place(x=75, y=90)

ukuranBlackWhite = StringVar(value="Pilih")
comboboxBlacWhite = ttk.Combobox(
    window,
    font=("Arial", 7),
    textvariable=ukuranBlackWhite,
    state="readonly"
)
comboboxBlacWhite.place(x=30, y=120, width=45)
comboboxBlacWhite["values"]=("A3", "A4", "F4")

ukBlackWhite = Label (
    window,
    text="Ukuran Kertas",
    font=("Arial", 10)
)
ukBlackWhite.place(x=75, y=120)

# Input Print Berwarna
labelWarna = Label(
    window,
    text="Print Berwarna\t",
    font=("Arial", 10)
)
labelWarna.place(x=30, y=150)

intWarna = IntVar()
entryWarna = Entry(
    window,
    textvariable=intWarna,
    font=("Arial", 10)
)
entryWarna.place(x=30, y=175, width=40, height=20)

lembarWarna = Label(
    window,
    text="Lembar\t",
    font=("Arial", 10)
)
lembarWarna.place(x=75, y=175)

ukuranWarna = StringVar(value="Pilih")
comboboxWarna = ttk.Combobox(
    window,
    font=("Arial",  7),
    textvariable=ukuranWarna,
    state="readonly"
)
comboboxWarna.place(x=30, y=205, width=45)
comboboxWarna["values"]=("A3", "A4", "F4")

ukWarna = Label (
    window,
    text="Ukuran Kertas",
    font=("Arial", 10)
)
ukWarna.place(x=75, y=205)

# Input Fotocopy
labelCopy = Label(
    window,
    text="Foto Copy\t",
    font=("Arial", 10)
)
labelCopy.place(x=250, y=60)

intCopy = IntVar()
entryCopy = Entry(
    window,
    textvariable=intCopy,
    font=("Arial", 10)
)
entryCopy.place(x=250, y=90, width=40, height=20)

lembarCopy = Label(
    window,
    text="Lembar\t",
    font=("Arial", 10)
)
lembarCopy.place(x=295, y=90)

ukuranCopy = StringVar(value="Pilih")
comboboxCopy = ttk.Combobox(
    window,
    font=("Arial",  7),
    textvariable=ukuranCopy,
    state="readonly"
)
comboboxCopy.place(x=250, y=120, width=45)
comboboxCopy["values"]=("A3", "A4", "F4")

ukCopy = Label (
    window,
    text="Ukuran Kertas",
    font=("Arial", 9)
)
ukCopy.place(x=295, y=120)

# Hitung Total Bayar
def hitung_harga():
    lembar_blackWhite = intBlackWhite.get()
    ukuran_blackWhite = ukuranBlackWhite.get()
    lembar_warna = intWarna.get()
    ukuran_warna = ukuranWarna.get()
    lembar_copy = intCopy.get()
    ukuran_copy = ukuranCopy.get()

    total_bayar = (
        Harga.get_harga_print_hitam_putih(ukuran_blackWhite) * lembar_blackWhite +
        Harga.get_harga_print_berwarna(ukuran_warna) * lembar_warna +
        Harga.get_harga_fotocopy(ukuran_copy) * lembar_copy
    )

    print ("Total Bayar = Rp",total_bayar)

# Button Hitung Total Bayar
buttonHitung = Button(
    window,
    text="Hitung Harga",
    font=("Arial", 10),
    command=hitung_harga
)
buttonHitung.place(x=250, y=200, width=120, height=30)


window.mainloop()

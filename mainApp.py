from tkinter import *
from tkinter import ttk
import tkinter as tk
from daftarHarga import Harga

window = tk.Tk()
window.title('FAST PRINT')
window.resizable(0, 0)


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

#label judul
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
comboboxBlackWhite = ttk.Combobox(
    window,
    font=("Arial", 7),
    textvariable=ukuranBlackWhite,
    state="readonly"
)
comboboxBlackWhite.place(x=30, y=120, width=45)
comboboxBlackWhite["values"] = ("A3", "A4", "F4")

ukBlackWhite = Label(
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
    font=("Arial", 7),
    textvariable=ukuranWarna,
    state="readonly"
)
comboboxWarna.place(x=30, y=205, width=45)
comboboxWarna["values"] = ("A3", "A4", "F4")

ukWarna = Label(
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
labelCopy.place(x=230, y=60)

intCopy = IntVar()
entryCopy = Entry(
    window,
    textvariable=intCopy,
    font=("Arial", 10)
)
entryCopy.place(x=230, y=90, width=40, height=20)

lembarCopy = Label(
    window,
    text="Lembar\t",
    font=("Arial", 10)
)
lembarCopy.place(x=275, y=90)

ukuranCopy = StringVar(value="Pilih")
comboboxCopy = ttk.Combobox(
    window,
    font=("Arial", 7),
    textvariable=ukuranCopy,
    state="readonly"
)
comboboxCopy.place(x=230, y=120, width=45)
comboboxCopy["values"] = ("A3", "A4", "F4")

ukCopy = Label(
    window,
    text="Ukuran Kertas",
    font=("Arial", 9)
)
ukCopy.place(x=275, y=120)


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

    intHargaTotal.set(total_bayar)
    print("Total Bayar = Rp", total_bayar)


# Button Hitung Total Bayar
buttonHitung = Button(
    window,
    text="Hitung Harga",
    font=("Arial", 10),
    command=hitung_harga
)
buttonHitung.place(x=230, y=200, width=120, height=30)

# List Daftar Harga
price_list_frame = tk.Frame(window)
price_list_frame.place(x=420, y=40)

price_list_label = tk.Label(price_list_frame, text="Daftar Harga", font=("Arial", 12, "bold"))
price_list_label.pack(pady=5)

price_list = Listbox(price_list_frame, font=("Arial", 10))
price_list.pack(fill=BOTH, expand=True)

price_list.insert(END, "Harga Print Hitam Putih:")
price_list.insert(END, f"A3: Rp {Harga.get_harga_print_hitam_putih('A3')}")
price_list.insert(END, f"A4: Rp {Harga.get_harga_print_hitam_putih('A4')}")
price_list.insert(END, f"F4: Rp {Harga.get_harga_print_hitam_putih('F4')}")
price_list.insert(END, "")
price_list.insert(END, "Harga Print Berwarna:")
price_list.insert(END, f"A3: Rp {Harga.get_harga_print_berwarna('A3')}")
price_list.insert(END, f"A4: Rp {Harga.get_harga_print_berwarna('A4')}")
price_list.insert(END, f"F4: Rp {Harga.get_harga_print_berwarna('F4')}")
price_list.insert(END, "")
price_list.insert(END, "Harga Fotocopy:")
price_list.insert(END, f"A3: Rp {Harga.get_harga_fotocopy('A3')}")
price_list.insert(END, f"A4: Rp {Harga.get_harga_fotocopy('A4')}")
price_list.insert(END, f"F4: Rp {Harga.get_harga_fotocopy('F4')}")

#Output Harga Total
labelHargaTotal = Label(
    window,
    text="Harga Total\t",
    font=("Arial", 10)
)
labelHargaTotal.place(x=30, y=270)

intHargaTotal = IntVar()
OuputHargaTotal = Entry(
    window,
    textvariable=intHargaTotal,
    font=("Arial", 10)
)
OuputHargaTotal.place(x=40, y=300, width=60, height=20)

window.mainloop()
